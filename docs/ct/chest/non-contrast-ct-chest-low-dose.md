---
title: Non-Contrast CT Chest Low Dose
slug: non-contrast-ct-chest-low-dose
category: chest
protocol_type: non-contrast
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Non Contrast chest for patient's age < 60
position: Supine with arms raised
npo: N/A
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: 100-120
  mas: Low dose (40-60 reference)
  rotation_time: 0.5s
  pitch: 1.0-1.2
series:
- name: Low Dose Chest
  start: Lung apices
  end: Costophrenic angles
  delay: N/A
  thickness: 1-1.25 mm
  notes: Low dose helical
recons:
- plane: Axial
  acquisition: Chest
  fov: Chest
  thickness_increment: 1.25 mm/1.25 mm
  kernel: Lung
  ir_strength: High IR 4-5
  notes: Thin slice nodule detection
- plane: Axial
  acquisition: Chest
  fov: Chest
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Mediastinal window
- plane: Coronal
  acquisition: Chest
  fov: Chest
  thickness_increment: 2 mm/2 mm
  kernel: Lung
  ir_strength: High IR
  notes: Coronal overview
- plane: MIP
  acquisition: Chest
  fov: Lungs
  thickness_increment: 5 mm slab
  kernel: Lung
  ir_strength: N/A
  notes: Nodule detection
notes:
  tech: LOW DOSE technique. Reduced mAs 30-50% of standard. Helical acquisition. High
    IR strength
  nursing: No IV. Explain screening purpose and low radiation
  rad: Lung nodule detection. Measure nodules. Lung-RADS classification. Emphysema
    assessment
  tips: Low dose protocol. High iterative reconstruction. Nodule measurement software
  additional_recons: CAD nodule detection. Measure all nodules ≥3mm. Lung-RADS reporting
safety:
  renal: N/A
  allergy: N/A
---

# Non-Contrast CT Chest Low Dose

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Low Dose Chest | Non-contrast | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Non Contrast chest for patient's age < 60

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

        - LOW DOSE technique. Reduced mAs 30-50% of standard. Helical acquisition. High IR strength
        - Additional Recons: CAD nodule detection. Measure all nodules ≥3mm. Lung-RADS reporting

    === "Nursing Notes"

        - No IV. Explain screening purpose and low radiation

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Lung nodule detection. Measure nodules. Lung-RADS classification. Emphysema assessment

    === "Tips & Tricks"

        - Low dose protocol. High iterative reconstruction. Nodule measurement software

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | Low dose AP |
    | Low Dose Chest | Lung apices | Costophrenic angles | N/A | 1-1.25 mm | Low dose helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Chest | Chest | 1.25 mm/1.25 mm | Lung | High IR 4-5 | Thin slice nodule detection |
    | Axial | Chest | Chest | 2.5 mm/2.5 mm | Standard | 3 | Mediastinal window |
    | Coronal | Chest | Chest | 2 mm/2 mm | Lung | High IR | Coronal overview |
    | MIP | Chest | Lungs | 5 mm slab | Lung | N/A | Nodule detection |
