"""render_protocol.py — shared module for generating protocol Markdown documents.

Public API
----------
render_document(fm: dict) -> str
    Takes a YAML front matter dict and returns a complete Markdown document string
    (YAML front matter block + rendered body).
"""

from __future__ import annotations

import yaml


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _yaml_block(fm: dict) -> str:
    """Serialise *fm* to a fenced YAML front matter block."""
    return '---\n' + yaml.dump(fm, default_flow_style=False, allow_unicode=True) + '---\n'


def _is_no_contrast(agent: str) -> bool:
    """Return True when the agent value indicates no contrast."""
    return agent.strip().upper() in ('N/A', 'NONE', '')


def _contrast_section(contrast: dict) -> str:
    """Render the IV contrast card content."""
    agent = contrast.get('agent', '')
    if _is_no_contrast(agent):
        return (
            '    !!! info "No Intravenous Contrast"\n'
            '    This protocol does not require IV contrast administration.\n'
        )

    lines = [
        '    === "Injection Parameters"\n',
        '\n',
        '        | Parameter | Value |\n',
        '        |-----------|-------|\n',
        f'        | Agent | {agent} |\n',
        f'        | Volume | {contrast.get("volume", "")} |\n',
        f'        | Flow Rate | {contrast.get("flow_rate", "")} |\n',
        f'        | Duration | {contrast.get("duration", "")} |\n',
        f'        | Timing Method | {contrast.get("timing", "")} |\n',
        f'        | ROI Placement | {contrast.get("roi", "")} |\n',
        f'        | Trigger (HU) | {contrast.get("trigger", "")} |\n',
        '\n',
        '    === "Lab Requirements"\n',
        '        Use full dose if GFR > 30\n',
        '        !!! warning "If GFR < 30"\n',
        r'            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)' + '\n',
    ]
    return ''.join(lines)


def _premedication_bullets(premedication: str) -> str:
    """Return indented bullet lines for the premedication field."""
    if not premedication or not premedication.strip():
        return '        - None required\n'
    items = [item.strip() for item in premedication.split('|') if item.strip()]
    if not items:
        return '        - None required\n'
    return ''.join(f'        - {item}\n' for item in items)


def _indications_bullets(indications: list) -> str:
    if not indications:
        return '        - None\n'
    return ''.join(f'        - {ind}\n' for ind in indications)


def _series_acquisition_summary(series: list) -> str:
    """Render the compact series summary table inside Clinical Summary card."""
    rows = ''
    for s in series:
        rows += f'        | {s.get("name","")} | {s.get("delay","")} | {s.get("start","")} → {s.get("end","")} |\n'
    return rows


def _series_full_table(series: list) -> str:
    rows = ''
    for s in series:
        rows += (
            f'    | {s.get("name","")} | {s.get("start","")} | {s.get("end","")} '
            f'| {s.get("delay","")} | {s.get("thickness","")} | {s.get("notes","")} |\n'
        )
    return rows


def _recons_table(recons: list) -> str:
    rows = ''
    for r in recons:
        rows += (
            f'    | {r.get("plane","")} | {r.get("acquisition","")} | {r.get("fov","")} '
            f'| {r.get("thickness_increment","")} | {r.get("kernel","")} '
            f'| {r.get("ir_strength","")} | {r.get("notes","")} |\n'
        )
    return rows


# ---------------------------------------------------------------------------
# Public function
# ---------------------------------------------------------------------------

def render_document(fm: dict) -> str:
    """Return a complete Markdown document for *fm*.

    Parameters
    ----------
    fm : dict
        Parsed YAML front matter dict (see module docstring for expected keys).

    Returns
    -------
    str
        Full document: YAML front matter block followed by the rendered body.
    """
    title = fm.get('title', '')
    last_updated = fm.get('last_updated', '')
    author = fm.get('author', '')
    position = fm.get('position', '')
    npo = fm.get('npo', '')
    premedication = fm.get('premedication', '')
    contrast = fm.get('contrast', {})
    series = fm.get('series', [])
    recons = fm.get('recons', [])
    notes = fm.get('notes', {})
    safety = fm.get('safety', {})
    clinical_indications = fm.get('clinical_indications', [])

    body = f"""
# {title}

**Last Updated:** {last_updated}
**Author:** {author}

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
{_series_acquisition_summary(series)}
    === "Clinical Indications"

{_indications_bullets(clinical_indications)}
-   __2. Patient Prep__

    ---

    - **Position:** {position}
    - **NPO Status:** {npo}
    - **Pre-Medication:**
{_premedication_bullets(premedication)}
-   __3. IV Contrast & Injection__

    ---
{_contrast_section(contrast)}
-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - {notes.get('tech', '')}

    === "Nursing Notes"

        - {notes.get('nursing', '')}

        !!! warning "Safety First"
            - **Renal Function:** {safety.get('renal', '')}
            - **Allergy:** {safety.get('allergy', '')}

    === "Radiologist Notes"

        - {notes.get('rad', '')}

    === "Tips & Tricks"

        - {notes.get('tips', '')}

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
{_series_full_table(series)}
=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
{_recons_table(recons)}"""

    return _yaml_block(fm) + body
