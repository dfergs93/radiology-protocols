---
author: None
category: vascular
clinical_indications:
- Active GI bleeding
- Hematemesis
- Melena with hemodynamic instability
- Hematochezia
contrast:
  agent: Isovue 370
  duration: 20s
  flow_rate: 4-5 mL/s
  roi: Abdominal aorta
  timing: 'Triple phase: Arterial + Portal Venous + Delayed'
  trigger: 150 HU
  volume: 1.5 mL/kg
last_updated: '2026-01-05'
notes:
  additional_recons: MIP of all three phases side-by-side for comparison
  nursing: Large bore IV 18-20G essential. Verify with saline test
  rad: Look for arterial extravasation (early) and pooling (delayed). Note location
    and potential source vessel
  tech: High flow rate critical for arterial phase. Scan arterial at 25 sec then portal
    at 70 sec then delayed at 90-180 sec. Look for active extravasation
  tips: Arms raised to avoid artifacts. Fast table speed to cover area quickly in
    arterial phase
npo: NPO if possible (emergent study)
position: Supine with arms raised
premedication: ''
protocol_type: vascular
recons:
- acquisition: Non-contrast
  fov: Full AP
  ir_strength: '3'
  kernel: Standard
  notes: Look for intrinsic hyperdensities
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Arterial
  fov: Full AP
  ir_strength: '3'
  kernel: Standard
  notes: Look for arterial blush/extravasation
  plane: Axial
  thickness_increment: 0.75 mm/0.75 mm
- acquisition: Delayed
  fov: Full AP
  ir_strength: '3'
  kernel: Standard
  notes: Look for contrast pooling in bowel
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: All phases
  fov: Full AP
  ir_strength: '3'
  kernel: Standard
  notes: MIP to track extravasation
  plane: Coronal
  thickness_increment: 3 mm/3 mm
safety:
  allergy: Document allergy history. Emergency indication overrides mild allergy
  renal: eGFR > 30 preferred but can proceed emergently
series:
- delay: Non-contrast
  end: Pubic symphysis
  name: Non-contrast
  notes: ''
  start: Diaphragm
  thickness: 0.625 mm
- delay: 25 sec
  end: Pubic symphysis
  name: Arterial Phase
  notes: High flow rate 5 mL/s critical
  start: Diaphragm
  thickness: 0.625 mm
- delay: 90 sec
  end: Pubic symphysis
  name: Delayed Phase
  notes: Extended delay to see pooling of contrast
  start: Diaphragm
  thickness: 0.625 mm
slug: cta-for-gi-bleed
synonyms: []
tech_params:
  kv: 100-120
  mas: Auto (reference 300)
  pitch: '1.375'
  rotation_time: 0.5s
title: CTA for GI Bleed
---

# CTA for GI Bleed

**Last Updated:** 2026-01-05
**Author:** None

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | Non-contrast | Diaphragm → Pubic symphysis |
        | Arterial Phase | 25 sec | Diaphragm → Pubic symphysis |
        | Delayed Phase | 90 sec | Diaphragm → Pubic symphysis |

    === "Clinical Indications"

        - Active GI bleeding
        - Hematemesis
        - Melena with hemodynamic instability
        - Hematochezia

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO if possible (emergent study)
    - **Pre-Medication:**
        - None required

-   __3. IV Contrast & Injection__

    ---
    === "Injection Parameters"

        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Duration | 20s |
        | Timing Method | Triple phase: Arterial + Portal Venous + Delayed |
        | ROI Placement | Abdominal aorta |
        | Trigger (HU) | 150 HU |

    === "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - High flow rate critical for arterial phase. Scan arterial at 25 sec then portal at 70 sec then delayed at 90-180 sec. Look for active extravasation

    === "Nursing Notes"

        - Large bore IV 18-20G essential. Verify with saline test

        !!! warning "Safety First"
            - **Renal Function:** eGFR > 30 preferred but can proceed emergently
            - **Allergy:** Document allergy history. Emergency indication overrides mild allergy

    === "Radiologist Notes"

        - Look for arterial extravasation (early) and pooling (delayed). Note location and potential source vessel

    === "Tips & Tricks"

        - Arms raised to avoid artifacts. Fast table speed to cover area quickly in arterial phase

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Non-contrast | Diaphragm | Pubic symphysis | Non-contrast | 0.625 mm |  |
    | Arterial Phase | Diaphragm | Pubic symphysis | 25 sec | 0.625 mm | High flow rate 5 mL/s critical |
    | Delayed Phase | Diaphragm | Pubic symphysis | 90 sec | 0.625 mm | Extended delay to see pooling of contrast |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Non-contrast | Full AP | 1 mm/1 mm | Standard | 3 | Look for intrinsic hyperdensities |
    | Axial | Arterial | Full AP | 0.75 mm/0.75 mm | Standard | 3 | Look for arterial blush/extravasation |
    | Axial | Delayed | Full AP | 1 mm/1 mm | Standard | 3 | Look for contrast pooling in bowel |
    | Coronal | All phases | Full AP | 3 mm/3 mm | Standard | 3 | MIP to track extravasation |
