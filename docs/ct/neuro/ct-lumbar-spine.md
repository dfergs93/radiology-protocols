---
title: CT Lumbar Spine
slug: ct-lumbar-spine
category: neuro
protocol_type: spine
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Lumbar spine trauma
- Degenerative disease
- Back pain
- Radiculopathy
- Sciatica
position: Supine
npo: N/A
premedication: ''
contrast:
  agent: None typically. Contrast if infection/tumor/post-op
  volume: 'If contrast: 100 mL'
  flow_rate: 3 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 250)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: L-spine Helical
  start: T12
  end: Sacrum
  delay: N/A or 60s if contrast
  thickness: 0.625 mm
  notes: Submillimeter
recons:
- plane: Axial
  acquisition: L-spine
  fov: L-spine
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: '3'
  notes: Bone and soft tissue
- plane: Sagittal
  acquisition: L-spine
  fov: L-spine
  thickness_increment: 2 mm/1.5 mm
  kernel: Bone
  ir_strength: '3'
  notes: Midline and parasagittal
- plane: Coronal
  acquisition: L-spine
  fov: L-spine
  thickness_increment: 2.5 mm/2 mm
  kernel: Bone
  ir_strength: '3'
  notes: Coronal overview
- plane: Oblique sagittal
  acquisition: L-spine
  fov: Neural foramina
  thickness_increment: 2 mm
  kernel: Bone
  ir_strength: '3'
  notes: Foraminal assessment
notes:
  tech: T12 to sacrum. Submillimeter helical. Sagittal and coronal reformats. Oblique
    for foramina
  nursing: No IV unless contrast needed
  rad: Alignment. Fractures. Disc spaces. Spinal canal stenosis. Neural foramina.
    Facet joints. Spondylolisthesis
  tips: Bone algorithm. Sagittal and coronal reconstructions
  additional_recons: Oblique sagittal for foramina. Measure spinal canal. Grade stenosis
safety:
  renal: N/A or verify eGFR
  allergy: N/A or check allergy
---

# CT Lumbar Spine

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | L-spine Helical | Contrast (N/A or 60s if contrast delay) | T12 to Sacrum |

    === "Clinical Indications"

        - Lumbar spine trauma
        - Degenerative disease
        - Back pain
        - Radiculopathy
        - Sciatica

-   __2. Patient Prep__

    ---

    - **Position:** Supine
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection/tumor/post-op |
        | Volume | If contrast: 100 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - T12 to sacrum. Submillimeter helical. Sagittal and coronal reformats. Oblique for foramina
        - Additional Recons: Oblique sagittal for foramina. Measure spinal canal. Grade stenosis

    === "Nursing Notes"

        - No IV unless contrast needed

        !!! warning "Safety First"
            - **Renal Function:** N/A or verify eGFR
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Alignment. Fractures. Disc spaces. Spinal canal stenosis. Neural foramina. Facet joints. Spondylolisthesis

    === "Tips & Tricks"

        - Bone algorithm. Sagittal and coronal reconstructions

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | T12 | Sacrum | N/A | N/A | AP and lateral |
    | L-spine Helical | T12 | Sacrum | N/A or 60s if contrast | 0.625 mm | Submillimeter |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | L-spine | L-spine | 2 mm/2 mm | Bone | 3 | Bone and soft tissue |
    | Sagittal | L-spine | L-spine | 2 mm/1.5 mm | Bone | 3 | Midline and parasagittal |
    | Coronal | L-spine | L-spine | 2.5 mm/2 mm | Bone | 3 | Coronal overview |
    | Oblique sagittal | L-spine | Neural foramina | 2 mm | Bone | 3 | Foraminal assessment |
