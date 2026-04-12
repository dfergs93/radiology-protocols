---
title: Non-Volumetric HRCT 1 Phase Prone
slug: non-volumetric-hrct-1-phase-prone
category: chest
protocol_type: chest/pulmonary
last_updated: '2024-01-15'
author: Dr. Martinez
synonyms: []
clinical_indications:
- Dependent atelectasis vs fibrosis
- Posterior lung assessment
- ILD with gravity-dependent changes
position: Prone with arms extended forward
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
- name: HRCT Prone
  start: Lung apices
  end: Costophrenic angles
  delay: Full inspiration
  thickness: 1 mm at 1-2cm intervals
  notes: Sequential prone
recons:
- plane: Axial
  acquisition: HRCT prone
  fov: Chest
  thickness_increment: 1 mm display
  kernel: Lung
  ir_strength: '3'
  notes: Prone images
- plane: Coronal
  acquisition: HRCT prone
  fov: Chest
  thickness_increment: 2 mm
  kernel: Lung
  ir_strength: '3'
  notes: Coronal prone
- plane: Compare
  acquisition: Supine vs prone
  fov: Posterior lungs
  thickness_increment: 1 mm
  kernel: Lung
  ir_strength: '3'
  notes: Dependent changes
notes:
  tech: Single INSPIRATION. PRONE position. Non-volumetric (1-2cm intervals). Distinguish
    atelectasis from fibrosis
  nursing: Position patient prone safely. Cushion support. Breath hold coaching
  rad: Differentiate dependent atelectasis from true fibrosis. Posterior lung better
    aerated prone
  tips: Safe prone positioning. Compare to supine if available
  additional_recons: Compare prone to supine to differentiate atelectasis from fibrosis
safety:
  renal: N/A
  allergy: N/A
---

# Non-Volumetric HRCT 1 Phase Prone

**Last Updated:** 2024-01-15  
**Author:** Dr. Martinez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | HRCT Prone | Contrast (Full inspiration delay) | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Dependent atelectasis vs fibrosis
        - Posterior lung assessment
        - ILD with gravity-dependent changes

-   __2. Patient Prep__

    ---

    - **Position:** Prone with arms extended forward
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Single INSPIRATION. PRONE position. Non-volumetric (1-2cm intervals). Distinguish atelectasis from fibrosis
        - Additional Recons: Compare prone to supine to differentiate atelectasis from fibrosis

    === "Nursing Notes"

        - Position patient prone safely. Cushion support. Breath hold coaching

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Differentiate dependent atelectasis from true fibrosis. Posterior lung better aerated prone

    === "Tips & Tricks"

        - Safe prone positioning. Compare to supine if available

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout Prone | Lung apices | Costophrenic angles | N/A | N/A | Lateral |
    | HRCT Prone | Lung apices | Costophrenic angles | Full inspiration | 1 mm at 1-2cm intervals | Sequential prone |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | HRCT prone | Chest | 1 mm display | Lung | 3 | Prone images |
    | Coronal | HRCT prone | Chest | 2 mm | Lung | 3 | Coronal prone |
    | Compare | Supine vs prone | Posterior lungs | 1 mm | Lung | 3 | Dependent changes |
