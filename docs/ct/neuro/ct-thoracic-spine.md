---
title: CT Thoracic Spine
slug: ct-thoracic-spine
category: neuro
protocol_type: spine
last_updated: '2024-01-15'
author: Dr. White
synonyms: []
clinical_indications:
- Thoracic spine trauma
- Compression fracture
- Back pain
- Tumor
- Infection
position: Supine
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
- name: T-spine Helical
  start: C7
  end: L1
  delay: N/A or 60s if contrast
  thickness: 0.625-1 mm
  notes: Submillimeter
recons:
- plane: Axial
  acquisition: T-spine
  fov: T-spine
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: '3'
  notes: Bone and soft tissue
- plane: Sagittal
  acquisition: T-spine
  fov: T-spine
  thickness_increment: 2 mm/1.5 mm
  kernel: Bone
  ir_strength: '3'
  notes: Midline and parasagittal
- plane: Coronal
  acquisition: T-spine
  fov: T-spine
  thickness_increment: 2.5 mm/2 mm
  kernel: Bone
  ir_strength: '3'
  notes: Coronal overview
notes:
  tech: C7 to L1. Submillimeter helical. Sagittal and coronal reformats. Arms up if
    possible
  nursing: No IV unless contrast indicated. Arms up to reduce artifact
  rad: Alignment. Compression fractures. Pedicles. Spinal canal. Disc spaces. Paraspinal
    soft tissues
  tips: Arms up reduces artifact. Bone algorithm
  additional_recons: ''
safety:
  renal: N/A or verify eGFR
  allergy: N/A or check allergy
---

# CT Thoracic Spine

**Last Updated:** 2024-01-15  
**Author:** Dr. White

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | T-spine Helical | Contrast (N/A or 60s if contrast delay) | C7 to L1 |

    === "Clinical Indications"

        - Thoracic spine trauma
        - Compression fracture
        - Back pain
        - Tumor
        - Infection

-   __2. Patient Prep__

    ---

    - **Position:** Supine
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

        - C7 to L1. Submillimeter helical. Sagittal and coronal reformats. Arms up if possible

    === "Nursing Notes"

        - No IV unless contrast indicated. Arms up to reduce artifact

        !!! warning "Safety First"
            - **Renal Function:** N/A or verify eGFR
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Alignment. Compression fractures. Pedicles. Spinal canal. Disc spaces. Paraspinal soft tissues

    === "Tips & Tricks"

        - Arms up reduces artifact. Bone algorithm

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | C7 | L1 | N/A | N/A | AP and lateral |
    | T-spine Helical | C7 | L1 | N/A or 60s if contrast | 0.625-1 mm | Submillimeter |

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
    | Axial | T-spine | T-spine | 2 mm/2 mm | Bone | 3 | Bone and soft tissue |
    | Sagittal | T-spine | T-spine | 2 mm/1.5 mm | Bone | 3 | Midline and parasagittal |
    | Coronal | T-spine | T-spine | 2.5 mm/2 mm | Bone | 3 | Coronal overview |

Category: Neuro

Protocol Type: Spine
