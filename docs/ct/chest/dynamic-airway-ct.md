---
title: Dynamic Airway CT
slug: dynamic-airway-ct
category: chest
protocol_type: non-contrast
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Tracheobronchomalacia
- Expiratory central airway collapse
- EDAC
position: Supine with arms raised
npo: N/A
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: '120'
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: Inspiration
  start: Thoracic inlet
  end: Carina+10cm
  delay: Full inspiration
  thickness: 0.625-1 mm
  notes: Thin for 3D
- name: Mid-Expiration
  start: Thoracic inlet
  end: Carina+10cm
  delay: Forced mid-expiration
  thickness: 0.625-1 mm
  notes: Same level as inspiration
- name: Cine (optional)
  start: Carina level
  end: Single slice
  delay: Continuous breathing
  thickness: Cine mode
  notes: Dynamic collapse
recons:
- plane: Axial
  acquisition: Both phases
  fov: Airway
  thickness_increment: 1-2 mm/1 mm
  kernel: Lung
  ir_strength: '3'
  notes: Axial airway
- plane: Coronal
  acquisition: Both phases
  fov: Airway
  thickness_increment: 1.5 mm
  kernel: Lung
  ir_strength: '3'
  notes: Coronal airway
- plane: Sagittal
  acquisition: Both phases
  fov: Airway
  thickness_increment: 1.5 mm
  kernel: Lung
  ir_strength: '3'
  notes: Sagittal airway
- plane: 3D VR
  acquisition: Both phases
  fov: Airway
  thickness_increment: 0.625-1 mm source
  kernel: Lung
  ir_strength: N/A
  notes: 3D airway reconstruction
notes:
  tech: 'TWO acquisitions: 1) INSPIRATION carina to carina+10cm 2) MID-EXPIRATION
    same level. Cine if available. Airway reconstructions required'
  nursing: No IV. Coach dynamic breathing. May need forced expiration
  rad: Measure tracheal collapse percentage. >50% collapse suggests tracheomalacia.
    Assess bronchi
  tips: Coach forced expiration. Exact same level both phases
  additional_recons: Measure tracheal AP diameter inspiration vs expiration. Calculate
    collapse percentage. 3D airway
safety:
  renal: N/A
  allergy: N/A
---

# Dynamic Airway CT

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Inspiration | Contrast (Full inspiration delay) | Thoracic inlet to Carina+10cm |
        | Mid-Expiration | Contrast (Forced mid-expiration delay) | Thoracic inlet to Carina+10cm |

    === "Clinical Indications"

        - Tracheobronchomalacia
        - Expiratory central airway collapse
        - EDAC

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO acquisitions: 1) INSPIRATION carina to carina+10cm 2) MID-EXPIRATION same level. Cine if available. Airway reconstructions required
        - Additional Recons: Measure tracheal AP diameter inspiration vs expiration. Calculate collapse percentage. 3D airway

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
    | Scout | Thoracic inlet | Carina+10cm | N/A | N/A | Lateral |
    | Inspiration | Thoracic inlet | Carina+10cm | Full inspiration | 0.625-1 mm | Thin for 3D |
    | Mid-Expiration | Thoracic inlet | Carina+10cm | Forced mid-expiration | 0.625-1 mm | Same level as inspiration |
    | Cine (optional) | Carina level | Single slice | Continuous breathing | Cine mode | Dynamic collapse |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Both phases | Airway | 1-2 mm/1 mm | Lung | 3 | Axial airway |
    | Coronal | Both phases | Airway | 1.5 mm | Lung | 3 | Coronal airway |
    | Sagittal | Both phases | Airway | 1.5 mm | Lung | 3 | Sagittal airway |
    | 3D VR | Both phases | Airway | 0.625-1 mm source | Lung | N/A | 3D airway reconstruction |
