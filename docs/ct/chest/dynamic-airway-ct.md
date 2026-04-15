---
author: None
category: chest
clinical_indications:
- Tracheobronchomalacia
- Expiratory central airway collapse
- EDAC
contrast:
  agent: N/A
  duration: ''
  flow_rate: ''
  roi: ''
  timing: ''
  trigger: ''
  volume: ''
last_updated: '2026-01-01'
notes:
  additional_recons: Measure tracheal AP diameter inspiration vs expiration. Calculate
    collapse percentage. 3D airway
  nursing: No IV. Coach dynamic breathing. May need forced expiration
  rad: Measure tracheal collapse percentage. >50% collapse suggests tracheomalacia.
    Assess bronchi
  tech: 'TWO acquisitions: 1) INSPIRATION carina to carina+10cm 2) MID-EXPIRATION
    same level. Airway reconstructions required'
  tips: Coach forced expiration. Exact same level both phases
npo: N/A
position: Supine with arms raised
premedication: ''
protocol_type: non-contrast
recons:
- acquisition: Both phases
  fov: Airway
  ir_strength: '3'
  kernel: Lung
  notes: Axial airway
  plane: Axial
  thickness_increment: 1-2 mm/1 mm
- acquisition: Both phases
  fov: Airway
  ir_strength: '3'
  kernel: Lung
  notes: Coronal airway
  plane: Coronal
  thickness_increment: 1.5 mm
- acquisition: Both phases
  fov: Airway
  ir_strength: '3'
  kernel: Lung
  notes: Sagittal airway
  plane: Sagittal
  thickness_increment: 1.5 mm
- acquisition: Both phases
  fov: Airway
  ir_strength: N/A
  kernel: Lung
  notes: 3D airway reconstruction
  plane: 3D VR
  thickness_increment: 0.625-1 mm source
safety:
  allergy: N/A
  renal: N/A
series:
- delay: Full inspiration
  end: Carina+10cm
  name: Inspiration
  notes: Thin for 3D
  start: Thoracic inlet
  thickness: 0.625-1 mm
- delay: Forced mid-expiration
  end: Carina+10cm
  name: Mid-Expiration
  notes: Same level as inspiration
  start: Thoracic inlet
  thickness: 0.625-1 mm
slug: dynamic-airway-ct
synonyms: []
tech_params:
  kv: '120'
  mas: Auto (reference 200)
  pitch: Helical
  rotation_time: 0.5s
title: Dynamic Airway CT
---

# Dynamic Airway CT

**Last Updated:** 2026-01-01
**Author:** None

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Inspiration | Full inspiration | Thoracic inlet → Carina+10cm |
        | Mid-Expiration | Forced mid-expiration | Thoracic inlet → Carina+10cm |

    === "Clinical Indications"

        - Tracheobronchomalacia
        - Expiratory central airway collapse
        - EDAC

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** N/A
    - **Pre-Medication:**
        - None required

-   __3. IV Contrast & Injection__

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO acquisitions: 1) INSPIRATION carina to carina+10cm 2) MID-EXPIRATION same level. Airway reconstructions required

    === "Nursing Notes"

        - No IV. Coach dynamic breathing. May need forced expiration

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Measure tracheal collapse percentage. >50% collapse suggests tracheomalacia. Assess bronchi

    === "Tips & Tricks"

        - Coach forced expiration. Exact same level both phases

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Inspiration | Thoracic inlet | Carina+10cm | Full inspiration | 0.625-1 mm | Thin for 3D |
    | Mid-Expiration | Thoracic inlet | Carina+10cm | Forced mid-expiration | 0.625-1 mm | Same level as inspiration |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Both phases | Airway | 1-2 mm/1 mm | Lung | 3 | Axial airway |
    | Coronal | Both phases | Airway | 1.5 mm | Lung | 3 | Coronal airway |
    | Sagittal | Both phases | Airway | 1.5 mm | Lung | 3 | Sagittal airway |
    | 3D VR | Both phases | Airway | 0.625-1 mm source | Lung | N/A | 3D airway reconstruction |
