---
title: Non-Volumetric HRCT 1 Respiratory Phase
slug: non-volumetric-hrct-1-respiratory-phase
category: chest
protocol_type: chest/pulmonary
last_updated: '2024-01-15'
author: Dr. Chen
synonyms: []
clinical_indications:
- HRCT follow-up
- Known ILD monitoring
- Bronchiectasis assessment
position: Supine with arms raised
npo: N/A
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: '120'
  mas: Reduced (100-150 reference)
  rotation_time: Sequentials
  pitch: N/A
series:
- name: HRCT Inspiration
  start: Lung apices
  end: Costophrenic angles
  delay: Full inspiration
  thickness: 1 mm at 1-2cm intervals
  notes: Sequential slices
recons:
- plane: Axial
  acquisition: HRCT
  fov: Chest
  thickness_increment: 1 mm display
  kernel: Lung
  ir_strength: '3'
  notes: HRCT images
- plane: Coronal
  acquisition: HRCT
  fov: Chest
  thickness_increment: 2 mm
  kernel: Lung
  ir_strength: '3'
  notes: Coronal overview
- plane: Targeted
  acquisition: HRCT
  fov: Area of interest
  thickness_increment: 1 mm
  kernel: Lung
  ir_strength: '3'
  notes: Focus on abnormality
notes:
  tech: Single INSPIRATION phase. Non-volumetric (1-2cm intervals). Lower dose for
    follow-up
  nursing: No IV. Single inspiration breath hold
  rad: Follow ILD changes. Bronchiectasis. Lower radiation than volumetric
  tips: Non-volumetric reduces dose. Good for follow-up
  additional_recons: Target slices through abnormality. Compare to prior
safety:
  renal: N/A
  allergy: N/A
---

# Non-Volumetric HRCT 1 Respiratory Phase

**Last Updated:** 2024-01-15  
**Author:** Dr. Chen

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | HRCT Inspiration | Non-Contrast (Full inspiration delay) | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - HRCT follow-up
        - Known ILD monitoring
        - Bronchiectasis assessment

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

        - Single INSPIRATION phase. Non-volumetric (1-2cm intervals). Lower dose for follow-up
        - Additional Recons: Target slices through abnormality. Compare to prior

    === "Nursing Notes"

        - No IV. Single inspiration breath hold

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Follow ILD changes. Bronchiectasis. Lower radiation than volumetric

    === "Tips & Tricks"

        - Non-volumetric reduces dose. Good for follow-up

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | AP |
    | HRCT Inspiration | Lung apices | Costophrenic angles | Full inspiration | 1 mm at 1-2cm intervals | Sequential slices |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Reduced (100-150 reference) |
    | Rotation Time | Sequentials |
    | Pitch | N/A |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | HRCT | Chest | 1 mm display | Lung | 3 | HRCT images |
    | Coronal | HRCT | Chest | 2 mm | Lung | 3 | Coronal overview |
    | Targeted | HRCT | Area of interest | 1 mm | Lung | 3 | Focus on abnormality |
