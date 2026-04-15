---
title: Non-Contrast CT Head
slug: non-contrast-ct-head
category: neuro
protocol_type: neuroradiology
last_updated: '2026-01-03'
author: 
synonyms: []
clinical_indications:
- Acute stroke protocol
- Head trauma
- Headache - worst of life
- Altered mental status
position: Supine head-first
npo: N/A
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: '120'
  mas: Auto (reference 300)
  rotation_time: 1s
  pitch: '0.5'
series:
- name: Non-Contrast Head
  start: Vertex
  end: Foramen magnum
  delay: N/A
  thickness: 5 mm
  notes: Angle parallel to hard palate
recons:
- plane: Axial
  acquisition: Non-contrast
  fov: Brain
  thickness_increment: 5 mm/5 mm
  kernel: Brain
  ir_strength: '3'
  notes: Primary diagnostic - brain window
- plane: Axial
  acquisition: Non-contrast
  fov: Brain
  thickness_increment: 5 mm/5 mm
  kernel: Bone
  ir_strength: N/A
  notes: Bone window for fractures
- plane: Coronal
  acquisition: Non-contrast
  fov: Brain
  thickness_increment: 3 mm/3 mm
  kernel: Brain
  ir_strength: '3'
  notes: Optional - for skull base evaluation
- plane: Sagittal
  acquisition: Non-contrast
  fov: Brain
  thickness_increment: 3 mm/3 mm
  kernel: Brain
  ir_strength: '3'
  notes: Optional - for midline structures
notes:
  tech: Minimize patient motion. Gantry angle parallel to skull base to reduce orbital
    dose. Ensure head straight
  nursing: No IV required. Explain importance of staying still
  rad: Look for hyperdense MCA sign. Assess grey-white differentiation. Check for
    hemorrhage and mass effect
  tips: Remove dentures and hearing aids. Secure head in holder
  additional_recons: Thin slice 1.25mm if subtle fracture suspected
safety:
  renal: N/A
  allergy: N/A
---

# Non-Contrast CT Head

**Last Updated:** 2026-01-03  
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast Head | Non-contrast | Vertex to Foramen magnum |

    === "Clinical Indications"

        - Acute stroke protocol
        - Head trauma
        - Headache - worst of life
        - Altered mental status

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Minimize patient motion. Gantry angle parallel to skull base to reduce orbital dose. Ensure head straight
        - Additional Recons: Thin slice 1.25mm if subtle fracture suspected

    === "Nursing Notes"

        - No IV required. Explain importance of staying still

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Look for hyperdense MCA sign. Assess grey-white differentiation. Check for hemorrhage and mass effect

    === "Tips & Tricks"

        - Remove dentures and hearing aids. Secure head in holder

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Vertex | C1 | N/A | N/A | Lateral scout |
    | Non-Contrast Head | Vertex | Foramen magnum | N/A | 5 mm | Angle parallel to hard palate |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Non-contrast | Brain | 5 mm/5 mm | Brain | 3 | Primary diagnostic - brain window |
    | Axial | Non-contrast | Brain | 5 mm/5 mm | Bone | N/A | Bone window for fractures |
    | Coronal | Non-contrast | Brain | 3 mm/3 mm | Brain | 3 | Optional - for skull base evaluation |
    | Sagittal | Non-contrast | Brain | 3 mm/3 mm | Brain | 3 | Optional - for midline structures |
