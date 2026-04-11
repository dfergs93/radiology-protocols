---
title: CT Cervical Spine
slug: ct-cervical-spine
category: neuro
protocol_type: spine
last_updated: '2024-01-15'
author: Dr. Rodriguez
synonyms: []
clinical_indications:
- Cervical spine trauma
- Degenerative disease
- Neck pain
- Radiculopathy
- Myelopathy
position: Supine head-first
npo: N/A
premedication: ''
contrast:
  agent: None typically. Contrast if infection/tumor
  volume: 'If contrast: 100 mL'
  flow_rate: 3 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 250)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: C-spine Helical
  start: Skull base
  end: T1
  delay: N/A or 60s if contrast
  thickness: 0.625 mm
  notes: Submillimeter acquisition
recons:
- plane: Axial
  acquisition: C-spine
  fov: C-spine
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: '3'
  notes: Bone and soft tissue
- plane: Sagittal
  acquisition: C-spine
  fov: C-spine
  thickness_increment: 2 mm/1.5 mm
  kernel: Bone
  ir_strength: '3'
  notes: Midline and parasagittal
- plane: Coronal
  acquisition: C-spine
  fov: C-spine
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: '3'
  notes: Coronal alignment
- plane: Oblique sagittal
  acquisition: C-spine
  fov: Neural foramina
  thickness_increment: 2 mm
  kernel: Bone
  ir_strength: '3'
  notes: Foraminal narrowing
notes:
  tech: Skull base to T1. Submillimeter helical. Sagittal and coronal reformats required.
    Bone algorithm
  nursing: No IV unless contrast needed. Cervical precautions if trauma
  rad: Alignment. Fractures. Disc spaces. Neural foramina. Spinal canal. Facet joints.
    Degenerative changes
  tips: Minimize motion. C-collar if trauma
  additional_recons: Sagittal and coronal bone reconstructions. Oblique for foramina
safety:
  renal: N/A or verify eGFR
  allergy: N/A or check allergy
---

# CT Cervical Spine

**Last Updated:** 2024-01-15  
**Author:** Dr. Rodriguez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | C-spine Helical | Contrast (N/A or 60s if contrast delay) | Skull base to T1 |

    === "Clinical Indications"

        - Cervical spine trauma
        - Degenerative disease
        - Neck pain
        - Radiculopathy
        - Myelopathy

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection/tumor |
        | Volume | If contrast: 100 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Skull base to T1. Submillimeter helical. Sagittal and coronal reformats required. Bone algorithm
        - Additional Recons: Sagittal and coronal bone reconstructions. Oblique for foramina

    === "Nursing Notes"

        - No IV unless contrast needed. Cervical precautions if trauma

        !!! warning "Safety First"
            - **Renal Function:** N/A or verify eGFR
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Alignment. Fractures. Disc spaces. Neural foramina. Spinal canal. Facet joints. Degenerative changes

    === "Tips & Tricks"

        - Minimize motion. C-collar if trauma

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Skull base | T1 | N/A | N/A | AP and lateral |
    | C-spine Helical | Skull base | T1 | N/A or 60s if contrast | 0.625 mm | Submillimeter acquisition |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | C-spine | C-spine | 2 mm/2 mm | Bone | 3 | Bone and soft tissue |
    | Sagittal | C-spine | C-spine | 2 mm/1.5 mm | Bone | 3 | Midline and parasagittal |
    | Coronal | C-spine | C-spine | 2 mm/2 mm | Bone | 3 | Coronal alignment |
    | Oblique sagittal | C-spine | Neural foramina | 2 mm | Bone | 3 | Foraminal narrowing |
