---
title: Volumetric HRCT 2 Respiratory Phases
slug: volumetric-hrct-2-respiratory-phases
category: chest
protocol_type: chest/pulmonary
last_updated: '2024-01-15'
author: Dr. White
synonyms: []
clinical_indications:
- Interstitial lung disease without prone imaging
- ILD diagnosis
- Diffuse lung disease
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
  delay: Full inspiration
  thickness: 1 mm
  notes: Contiguous 1mm slices
- name: Limited Expiration
  start: Carina
  end: Costophrenic angles
  delay: Full expiration
  thickness: 1 mm
  notes: Limited coverage expiration
recons:
- plane: Axial
  acquisition: Inspiration
  fov: Chest
  thickness_increment: 1 mm/1 mm
  kernel: Lung
  ir_strength: '3'
  notes: Thin slice ILD assessment
- plane: Axial
  acquisition: Expiration
  fov: Lower lungs
  thickness_increment: 1 mm/1 mm
  kernel: Lung
  ir_strength: '3'
  notes: Air trapping assessment
- plane: Coronal
  acquisition: Inspiration
  fov: Chest
  thickness_increment: 1.5 mm
  kernel: Lung
  ir_strength: '3'
  notes: ILD distribution
- plane: Sagittal
  acquisition: Inspiration
  fov: Chest
  thickness_increment: 2 mm
  kernel: Lung
  ir_strength: '3'
  notes: Craniocaudal distribution
notes:
  tech: 'TWO acquisitions: 1) Full INSPIRATION 2) Limited EXPIRATION (carina to bases).
    Volumetric (contiguous thin slice). Coach breathing'
  nursing: No IV. Careful breath hold coaching. Inspiration and expiration
  rad: ILD pattern recognition. Honeycombing. Ground glass. Reticular. Mosaic attenuation
    on expiration
  tips: Volumetric contiguous slices. Coach breathing carefully
  additional_recons: Thin slice for ILD detail. Compare inspiration vs expiration.
    Quantitative analysis if available
safety:
  renal: N/A
  allergy: N/A
---

# Volumetric HRCT 2 Respiratory Phases

**Last Updated:** 2024-01-15  
**Author:** Dr. White

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Volumetric Inspiration | Contrast (Full inspiration delay) | Lung apices to Costophrenic angles |
        | Limited Expiration | Contrast (Full expiration delay) | Carina to Costophrenic angles |

    === "Clinical Indications"

        - Interstitial lung disease without prone imaging
        - ILD diagnosis
        - Diffuse lung disease

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

        - TWO acquisitions: 1) Full INSPIRATION 2) Limited EXPIRATION (carina to bases). Volumetric (contiguous thin slice). Coach breathing
        - Additional Recons: Thin slice for ILD detail. Compare inspiration vs expiration. Quantitative analysis if available

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
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | AP lateral |
    | Volumetric Inspiration | Lung apices | Costophrenic angles | Full inspiration | 1 mm | Contiguous 1mm slices |
    | Limited Expiration | Carina | Costophrenic angles | Full expiration | 1 mm | Limited coverage expiration |

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
    | Axial | Inspiration | Chest | 1 mm/1 mm | Lung | 3 | Thin slice ILD assessment |
    | Axial | Expiration | Lower lungs | 1 mm/1 mm | Lung | 3 | Air trapping assessment |
    | Coronal | Inspiration | Chest | 1.5 mm | Lung | 3 | ILD distribution |
    | Sagittal | Inspiration | Chest | 2 mm | Lung | 3 | Craniocaudal distribution |
