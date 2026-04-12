---
title: CT Lower Extremity
slug: ct-lower-extremity
category: msk
protocol_type: contrast-enhanced
last_updated: '2024-01-15'
author: Dr. Rodriguez
synonyms: []
clinical_indications:
- Lower extremity fracture
- Tibia/fibula
- Femur
- Post-operative hardware assessment
position: Supine
npo: N/A
premedication: ''
contrast:
  agent: None typically. Contrast if infection
  volume: 'If contrast: 100 mL'
  flow_rate: 2-3 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 200-250)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: CT Lower Extremity
  start: Proximal to injury
  end: Distal to injury
  delay: N/A or 60s if contrast
  thickness: 0.625-1 mm
  notes: Submillimeter
recons:
- plane: Axial
  acquisition: Lower extremity
  fov: Region
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: N/A
  notes: Bone windows
- plane: Coronal
  acquisition: Lower extremity
  fov: Region
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: N/A
  notes: Coronal
- plane: Sagittal
  acquisition: Lower extremity
  fov: Region
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: N/A
  notes: Sagittal
- plane: 3D surface
  acquisition: Lower extremity
  fov: Bones
  thickness_increment: 0.625 mm source
  kernel: Bone
  ir_strength: N/A
  notes: 3D reconstruction
notes:
  tech: 'FOV based on region: hip to ankle. Submillimeter for fracture. Extended coverage
    for alignment'
  nursing: No IV unless contrast needed
  rad: Fractures. Alignment. Comminution. Intra-articular extension. Hardware position.
    Infection on contrast
  tips: Extended coverage for alignment measurements
  additional_recons: Alignment measurements. Hardware position. 3D for surgical planning
safety:
  renal: N/A or eGFR > 30
  allergy: N/A or check allergy
---

# CT Lower Extremity

**Last Updated:** 2024-01-15  
**Author:** Dr. Rodriguez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Lower Extremity | Contrast (N/A or 60s if contrast delay) | Proximal to injury to Distal to injury |

    === "Clinical Indications"

        - Lower extremity fracture
        - Tibia/fibula
        - Femur
        - Post-operative hardware assessment

-   __2. Patient Prep__

    ---

    - **Position:** Supine
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection |
        | Volume | If contrast: 100 mL |
        | Flow Rate | 2-3 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - FOV based on region: hip to ankle. Submillimeter for fracture. Extended coverage for alignment
        - Additional Recons: Alignment measurements. Hardware position. 3D for surgical planning

    === "Nursing Notes"

        - No IV unless contrast needed

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Fractures. Alignment. Comminution. Intra-articular extension. Hardware position. Infection on contrast

    === "Tips & Tricks"

        - Extended coverage for alignment measurements

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Region specific | Extended | N/A | N/A | AP and lateral |
    | CT Lower Extremity | Proximal to injury | Distal to injury | N/A or 60s if contrast | 0.625-1 mm | Submillimeter |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Lower extremity | Region | 2 mm/2 mm | Bone | N/A | Bone windows |
    | Coronal | Lower extremity | Region | 2 mm/2 mm | Bone | N/A | Coronal |
    | Sagittal | Lower extremity | Region | 2 mm/2 mm | Bone | N/A | Sagittal |
    | 3D surface | Lower extremity | Bones | 0.625 mm source | Bone | N/A | 3D reconstruction |
