---
title: CT Upper Extremity
slug: ct-upper-extremity
category: msk
protocol_type: contrast-enhanced
last_updated: '2024-01-15'
author: Dr. White
synonyms: []
clinical_indications:
- Upper extremity fracture
- Humerus
- Radius/ulna
- Forearm
- Elbow injury
position: Supine with arm positioned
npo: N/A
premedication: ''
contrast:
  agent: None typically. Contrast if infection
  volume: 'If contrast: 75 mL'
  flow_rate: 2-3 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: CT Upper Extremity
  start: Proximal to injury
  end: Distal to injury
  delay: N/A or 60s if contrast
  thickness: 0.625-1 mm
  notes: Submillimeter
recons:
- plane: Axial
  acquisition: Upper extremity
  fov: Region
  thickness_increment: 1-2 mm/1-2 mm
  kernel: Bone
  ir_strength: N/A
  notes: Bone windows
- plane: Coronal
  acquisition: Upper extremity
  fov: Region
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: N/A
  notes: Coronal
- plane: Sagittal
  acquisition: Upper extremity
  fov: Region
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: N/A
  notes: Sagittal
- plane: 3D surface
  acquisition: Upper extremity
  fov: Bones
  thickness_increment: 0.625 mm source
  kernel: Bone
  ir_strength: N/A
  notes: 3D if complex
notes:
  tech: 'FOV based on region: shoulder to hand. Submillimeter for fracture detail.
    Position for comfort and coverage'
  nursing: No IV unless contrast needed
  rad: Fractures. Alignment. Intra-articular extension. Comminution. Soft tissue injury
    on contrast
  tips: Position for patient comfort and diagnostic quality
  additional_recons: Document fracture location alignment. Soft tissue windows if
    contrast
safety:
  renal: N/A or eGFR > 30
  allergy: N/A or check allergy
---

# CT Upper Extremity

**Last Updated:** 2024-01-15  
**Author:** Dr. White

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Upper Extremity | Contrast (N/A or 60s if contrast delay) | Proximal to injury to Distal to injury |

    === "Clinical Indications"

        - Upper extremity fracture
        - Humerus
        - Radius/ulna
        - Forearm
        - Elbow injury

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arm positioned
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection |
        | Volume | If contrast: 75 mL |
        | Flow Rate | 2-3 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - FOV based on region: shoulder to hand. Submillimeter for fracture detail. Position for comfort and coverage
        - Additional Recons: Document fracture location alignment. Soft tissue windows if contrast

    === "Nursing Notes"

        - No IV unless contrast needed

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Fractures. Alignment. Intra-articular extension. Comminution. Soft tissue injury on contrast

    === "Tips & Tricks"

        - Position for patient comfort and diagnostic quality

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Region specific | Extended | N/A | N/A | AP and lateral |
    | CT Upper Extremity | Proximal to injury | Distal to injury | N/A or 60s if contrast | 0.625-1 mm | Submillimeter |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Upper extremity | Region | 1-2 mm/1-2 mm | Bone | N/A | Bone windows |
    | Coronal | Upper extremity | Region | 2 mm/2 mm | Bone | N/A | Coronal |
    | Sagittal | Upper extremity | Region | 2 mm/2 mm | Bone | N/A | Sagittal |
    | 3D surface | Upper extremity | Bones | 0.625 mm source | Bone | N/A | 3D if complex |
