---
title: Non-Volumetric HRCT 3 Respiratory Phases
slug: non-volumetric-hrct-3-respiratory-phases
category: chest
protocol_type: chest/pulmonary
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Interstitial lung disease
- Air trapping assessment
- Constrictive bronchiolitis
- Hypersensitivity pneumonitis
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
- name: Inspiration
  start: Lung apices
  end: Costophrenic angles
  delay: Full inspiration
  thickness: 1 mm axial at 1-2cm intervals
  notes: Sequential non-volumetric
- name: Full Expiration
  start: Lung apices
  end: Costophrenic angles
  delay: Full expiration
  thickness: 1 mm at intervals
  notes: Sequential
- name: Prone
  start: Lung apices
  end: Costophrenic angles
  delay: Full inspiration
  thickness: 1 mm at intervals
  notes: Sequential
recons:
- plane: Axial
  acquisition: All phases
  fov: Chest
  thickness_increment: 1 mm display
  kernel: Lung
  ir_strength: '3'
  notes: Compare three phases
- plane: Coronal reformat
  acquisition: Inspiration
  fov: Chest
  thickness_increment: 2 mm
  kernel: Lung
  ir_strength: '3'
  notes: Inspiration overview
- plane: Mosaic MIP
  acquisition: All phases
  fov: Lungs
  thickness_increment: 5 mm
  kernel: Lung
  ir_strength: N/A
  notes: Air trapping visualization
notes:
  tech: 'THREE acquisitions: 1) INSPIRATION 2) MID-EXPIRATION 3) FULL EXPIRATION.
    Non-volumetric (1-2cm intervals). Lower dose than volumetric'
  nursing: No IV. Coach three breathing phases carefully
  rad: Mosaic attenuation. Air trapping. Small airways disease. Compare three phases
  tips: Coach three distinct breath holds. Non-volumetric lower dose
  additional_recons: Side-by-side comparison of three phases. Quantify air trapping
safety:
  renal: N/A
  allergy: N/A
---

# Non-Volumetric HRCT 3 Respiratory Phases

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Inspiration | Non-Contrast (Full inspiration delay) | Lung apices to Costophrenic angles |
        | Full Expiration | Non-Contrast (Full expiration delay) | Lung apices to Costophrenic angles |
        | Prone | Non-Contrast (Full inspiration delay) | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Interstitial lung disease
        - Air trapping assessment
        - Constrictive bronchiolitis
        - Hypersensitivity pneumonitis

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

        - THREE acquisitions: 1) INSPIRATION 2) MID-EXPIRATION 3) FULL EXPIRATION. Non-volumetric (1-2cm intervals). Lower dose than volumetric
        - Additional Recons: Side-by-side comparison of three phases. Quantify air trapping

    === "Nursing Notes"

        - No IV. Coach three breathing phases carefully

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Mosaic attenuation. Air trapping. Small airways disease. Compare three phases

    === "Tips & Tricks"

        - Coach three distinct breath holds. Non-volumetric lower dose

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | AP |
    | Inspiration | Lung apices | Costophrenic angles | Full inspiration | 1 mm axial at 1-2cm intervals | Sequential non-volumetric |
    | Full Expiration | Lung apices | Costophrenic angles | Full expiration | 1 mm at intervals | Sequential |
    | Prone | Lung apices | Costophrenic angles | Full inspiration | 1 mm at intervals | Sequential |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | All phases | Chest | 1 mm display | Lung | 3 | Compare three phases |
    | Coronal reformat | Inspiration | Chest | 2 mm | Lung | 3 | Inspiration overview |
    | Mosaic MIP | All phases | Lungs | 5 mm | Lung | N/A | Air trapping visualization |
