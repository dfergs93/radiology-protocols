---
title: Non-Contrast CT Chest Routine
slug: non-contrast-ct-chest-routine
category: chest
protocol_type: non-contrast
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Age > 60
- Chest pain low risk
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
  pitch: 1.0-1.2
series:
- name: NC Chest
  start: Lung apices
  end: Costophrenic angles
  delay: N/A
  thickness: 1-1.25 mm
  notes: Standard dose helical
recons:
- plane: Axial
  acquisition: Chest
  fov: Chest
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Mediastinal window
- plane: Axial
  acquisition: Chest
  fov: Chest
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Lung
  ir_strength: '3'
  notes: Lung window
- plane: Coronal
  acquisition: Chest
  fov: Chest
  thickness_increment: 3 mm/3 mm
  kernel: Lung
  ir_strength: '3'
  notes: Coronal lung
- plane: Sagittal
  acquisition: Chest
  fov: Chest
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Optional mediastinum
notes:
  tech: Standard dose helical chest. Lung apices to costophrenic angles. Routine lung
    and mediastinal windows
  nursing: No IV needed. Breath hold coaching
  rad: Assess lung parenchyma nodules masses. Mediastinal lymph nodes. Pleura. Incidental
    findings
  tips: Full inspiration breath hold
  additional_recons: Thin slice 1mm for nodule detection and measurement
safety:
  renal: N/A
  allergy: N/A
---

# Non-Contrast CT Chest Routine

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Chest | Non-contrast | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Age > 60
        - Chest pain low risk

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

        - Standard dose helical chest. Lung apices to costophrenic angles. Routine lung and mediastinal windows
        - Additional Recons: Thin slice 1mm for nodule detection and measurement

    === "Nursing Notes"

        - No IV needed. Breath hold coaching

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Assess lung parenchyma nodules masses. Mediastinal lymph nodes. Pleura. Incidental findings

    === "Tips & Tricks"

        - Full inspiration breath hold

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | AP and lateral |
    | NC Chest | Lung apices | Costophrenic angles | N/A | 1-1.25 mm | Standard dose helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Chest | Chest | 2.5 mm/2.5 mm | Standard | 3 | Mediastinal window |
    | Axial | Chest | Chest | 2.5 mm/2.5 mm | Lung | 3 | Lung window |
    | Coronal | Chest | Chest | 3 mm/3 mm | Lung | 3 | Coronal lung |
    | Sagittal | Chest | Chest | 3 mm/3 mm | Standard | 3 | Optional mediastinum |
