---
title: Quantitative Lung Density CT
slug: quantitative-lung-density-ct
category: chest
protocol_type: chest/pulmonary
last_updated: '2024-01-15'
author: Dr. Patel
synonyms: []
clinical_indications:
- Bronchiolitis Obliterans Syndrome
- Emphysema quantification
- COPD assessment
position: Supine with arms raised
npo: N/A
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: '120'
  mas: Auto (reference 150-200)
  rotation_time: 0.5s
  pitch: '1'
series:
- name: Volumetric Inspiration
  start: Lung apices
  end: Costophrenic angles
  delay: Full inspiration (TLC)
  thickness: 0.625-1 mm
  notes: Contiguous for quantification
- name: Volumetric Expiration
  start: Lung apices
  end: Costophrenic angles
  delay: Full expiration (RV)
  thickness: 0.625-1 mm
  notes: Contiguous complete exhalation
recons:
- plane: Axial
  acquisition: Inspiration
  fov: Chest
  thickness_increment: 1 mm/1 mm
  kernel: Lung
  ir_strength: '3'
  notes: Quantitative inspiration
- plane: Axial
  acquisition: Expiration
  fov: Chest
  thickness_increment: 1 mm/1 mm
  kernel: Lung
  ir_strength: '3'
  notes: Quantitative expiration
- plane: Density map
  acquisition: Inspiration
  fov: Lungs
  thickness_increment: Color coded
  kernel: Lung
  ir_strength: N/A
  notes: Emphysema distribution map
- plane: Density map
  acquisition: Expiration
  fov: Lungs
  thickness_increment: Color coded
  kernel: Lung
  ir_strength: N/A
  notes: Air trapping map
notes:
  tech: 'TWO VOLUMETRIC acquisitions: 1) Full INSPIRATION 2) FULL EXPIRATION (complete
    exhalation). Contiguous thin slices. Quantitative software'
  nursing: No IV. Coach complete inspiration and complete expiration
  rad: Quantify emphysema (% lung <-950 HU inspiration). Air trapping (% lung <-856
    HU expiration). Emphysema distribution
  tips: Complete exhalation critical for RV. Volumetric contiguous
  additional_recons: Quantitative emphysema analysis. Report % lung <-950 HU. Air
    trapping metrics. Upper/lower lobe distribution
safety:
  renal: N/A
  allergy: N/A
---

# Quantitative Lung Density CT

**Last Updated:** 2024-01-15  
**Author:** Dr. Patel

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Volumetric Inspiration | Contrast (Full inspiration (TLC) delay) | Lung apices to Costophrenic angles |
        | Volumetric Expiration | Contrast (Full expiration (RV) delay) | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Bronchiolitis Obliterans Syndrome
        - Emphysema quantification
        - COPD assessment

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

        - TWO VOLUMETRIC acquisitions: 1) Full INSPIRATION 2) FULL EXPIRATION (complete exhalation). Contiguous thin slices. Quantitative software
        - Additional Recons: Quantitative emphysema analysis. Report % lung <-950 HU. Air trapping metrics. Upper/lower lobe distribution

    === "Nursing Notes"

        - No IV. Coach complete inspiration and complete expiration

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Quantify emphysema (% lung <-950 HU inspiration). Air trapping (% lung <-856 HU expiration). Emphysema distribution

    === "Tips & Tricks"

        - Complete exhalation critical for RV. Volumetric contiguous

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | AP lateral |
    | Volumetric Inspiration | Lung apices | Costophrenic angles | Full inspiration (TLC) | 0.625-1 mm | Contiguous for quantification |
    | Volumetric Expiration | Lung apices | Costophrenic angles | Full expiration (RV) | 0.625-1 mm | Contiguous complete exhalation |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 150-200) |
    | Rotation Time | 0.5s |
    | Pitch | 1 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Inspiration | Chest | 1 mm/1 mm | Lung | 3 | Quantitative inspiration |
    | Axial | Expiration | Chest | 1 mm/1 mm | Lung | 3 | Quantitative expiration |
    | Density map | Inspiration | Lungs | Color coded | Lung | N/A | Emphysema distribution map |
    | Density map | Expiration | Lungs | Color coded | Lung | N/A | Air trapping map |
