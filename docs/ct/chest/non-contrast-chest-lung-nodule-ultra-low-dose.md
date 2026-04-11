---
title: Non-Contrast Chest Lung Nodule Ultra Low Dose
slug: non-contrast-chest-lung-nodule-ultra-low-dose
category: chest
protocol_type: chest/pulmonary
last_updated: '2024-01-15'
author: Dr. Rodriguez
synonyms: []
clinical_indications:
- Pulmonary nodule follow-up
- Known nodule surveillance
position: Supine with arms raised
npo: N/A
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: '100'
  mas: Ultra low (20-30 reference)
  rotation_time: 0.5s
  pitch: 1.0-1.2
series:
- name: Ultra Low Dose Chest
  start: Lung apices
  end: Costophrenic angles
  delay: N/A
  thickness: 1-1.25 mm
  notes: Ultra low dose helical
recons:
- plane: Axial
  acquisition: Chest
  fov: Chest
  thickness_increment: 1.25 mm/1.25 mm
  kernel: Lung
  ir_strength: Maximum IR 5
  notes: Nodule follow-up
- plane: Axial
  acquisition: Chest
  fov: Chest
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: High IR
  notes: Mediastinal
- plane: Coronal
  acquisition: Chest
  fov: Chest
  thickness_increment: 2 mm/2 mm
  kernel: Lung
  ir_strength: Maximum IR
  notes: Coronal
notes:
  tech: ULTRA LOW DOSE 10-20% standard dose. For follow-up of KNOWN nodules only.
    Not for initial detection. Maximum IR
  nursing: No IV. Known nodule follow-up only
  rad: Follow known nodules. Compare to prior. Measure size. Not for initial detection
  tips: Ultra low dose. Maximum IR. Prior comparison essential
  additional_recons: ''
safety:
  renal: N/A
  allergy: N/A
---

# Non-Contrast Chest Lung Nodule Ultra Low Dose

**Last Updated:** 2024-01-15  
**Author:** Dr. Rodriguez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Ultra Low Dose Chest | Non-contrast | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Pulmonary nodule follow-up
        - Known nodule surveillance

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

        - ULTRA LOW DOSE 10-20% standard dose. For follow-up of KNOWN nodules only. Not for initial detection. Maximum IR

    === "Nursing Notes"

        - No IV. Known nodule follow-up only

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Follow known nodules. Compare to prior. Measure size. Not for initial detection

    === "Tips & Tricks"

        - Ultra low dose. Maximum IR. Prior comparison essential

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | Ultra low dose |
    | Ultra Low Dose Chest | Lung apices | Costophrenic angles | N/A | 1-1.25 mm | Ultra low dose helical |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Ultra low (20-30 reference) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.2 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Chest | Chest | 1.25 mm/1.25 mm | Lung | Maximum IR 5 | Nodule follow-up |
    | Axial | Chest | Chest | 2.5 mm/2.5 mm | Standard | High IR | Mediastinal |
    | Coronal | Chest | Chest | 2 mm/2 mm | Lung | Maximum IR | Coronal |

Category: Chest

Protocol Type: Chest/Pulmonary
