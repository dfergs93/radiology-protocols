---
author: None
category: chest
clinical_indications:
- Interstitial lung disease without prone imaging
- ILD diagnosis
- Diffuse lung disease
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
  additional_recons: Thin slice for ILD detail. Compare inspiration vs expiration.
    Quantitative analysis if available
  nursing: No IV. Careful breath hold coaching. Inspiration and expiration
  rad: ILD pattern recognition. Honeycombing. Ground glass. Reticular. Mosaic attenuation
    on expiration
  tech: 'TWO acquisitions: 1) Full INSPIRATION 2) EXPIRATION  Volumetric (contiguous
    thin slice). Coach breathing'
  tips: Volumetric contiguous slices. Coach breathing carefully
npo: N/A
position: Supine with arms raised
premedication: ''
protocol_type: chest/pulmonary
recons:
- acquisition: Inspiration
  fov: Chest
  ir_strength: '3'
  kernel: Lung
  notes: Thin slice ILD assessment
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Expiration
  fov: Lower lungs
  ir_strength: '3'
  kernel: Lung
  notes: Air trapping assessment
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Inspiration
  fov: Chest
  ir_strength: '3'
  kernel: Lung
  notes: ILD distribution
  plane: Coronal
  thickness_increment: 1.5 mm
- acquisition: Inspiration
  fov: Chest
  ir_strength: '3'
  kernel: Lung
  notes: Craniocaudal distribution
  plane: Sagittal
  thickness_increment: 2 mm
safety:
  allergy: N/A
  renal: N/A
series:
- delay: Full inspiration
  end: Costophrenic angles
  name: Volumetric Inspiration
  notes: Contiguous 1mm slices
  start: Lung apices
  thickness: 1 mm
- delay: Full expiration
  end: Costophrenic angles
  name: Expiration
  notes: Limited coverage expiration
  start: Lung apices
  thickness: 1 mm
slug: volumetric-hrct-2-respiratory-phases
synonyms: []
tech_params:
  kv: '120'
  mas: Auto (reference 150-200)
  pitch: '1'
  rotation_time: 0.5s
title: Volumetric HRCT 2 Respiratory Phases
---

# Volumetric HRCT 2 Respiratory Phases

**Last Updated:** 2026-01-01
**Author:** None

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Volumetric Inspiration | Full inspiration | Lung apices → Costophrenic angles |
        | Expiration | Full expiration | Lung apices → Costophrenic angles |

    === "Clinical Indications"

        - Interstitial lung disease without prone imaging
        - ILD diagnosis
        - Diffuse lung disease

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

        - TWO acquisitions: 1) Full INSPIRATION 2) EXPIRATION  Volumetric (contiguous thin slice). Coach breathing

    === "Nursing Notes"

        - No IV. Careful breath hold coaching. Inspiration and expiration

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - ILD pattern recognition. Honeycombing. Ground glass. Reticular. Mosaic attenuation on expiration

    === "Tips & Tricks"

        - Volumetric contiguous slices. Coach breathing carefully

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Volumetric Inspiration | Lung apices | Costophrenic angles | Full inspiration | 1 mm | Contiguous 1mm slices |
    | Expiration | Lung apices | Costophrenic angles | Full expiration | 1 mm | Limited coverage expiration |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Inspiration | Chest | 1 mm/1 mm | Lung | 3 | Thin slice ILD assessment |
    | Axial | Expiration | Lower lungs | 1 mm/1 mm | Lung | 3 | Air trapping assessment |
    | Coronal | Inspiration | Chest | 1.5 mm | Lung | 3 | ILD distribution |
    | Sagittal | Inspiration | Chest | 2 mm | Lung | 3 | Craniocaudal distribution |
