---
title: CT Ankle
slug: ct-ankle
category: msk
protocol_type: musculoskeletal
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Ankle fracture
- Ligament injury
- Pilon fracture
- Pre-operative planning
- Hardware assessment
position: Supine feet first
npo: N/A
premedication: ''
contrast:
  agent: None typically. Contrast if infection/mass
  volume: 'If contrast: 75 mL'
  flow_rate: 2-3 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: CT Ankle
  start: Distal tib/fib
  end: Hindfoot
  delay: N/A or 60s if contrast
  thickness: 0.625 mm
  notes: Submillimeter
recons:
- plane: Axial
  acquisition: Ankle
  fov: Ankle
  thickness_increment: 1 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Bone algorithm
- plane: Coronal
  acquisition: Ankle
  fov: Ankle
  thickness_increment: 1.5 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Coronal ankle
- plane: Sagittal
  acquisition: Ankle
  fov: Ankle
  thickness_increment: 1.5 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Sagittal ankle
- plane: 3D surface
  acquisition: Ankle
  fov: Bones
  thickness_increment: 0.625 mm source
  kernel: Bone
  ir_strength: N/A
  notes: 3D for complex fractures
notes:
  tech: Include distal tibia/fibula through hindfoot. Submillimeter for 3D. Bilateral
    scout for positioning. May scan bilateral for comparison
  nursing: No IV unless contrast needed
  rad: Malleolar fractures. Tibial plafond. Talus. Calcaneus. Syndesmosis. Ligaments
    on contrast
  tips: Bilateral scout for symmetry. Submillimeter for 3D
  additional_recons: 3D reconstruction for surgical planning. Document fracture fragments
safety:
  renal: N/A or eGFR > 30
  allergy: N/A or check allergy
---

# CT Ankle

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Ankle | Contrast (N/A or 60s if contrast delay) | Distal tib/fib to Hindfoot |

    === "Clinical Indications"

        - Ankle fracture
        - Ligament injury
        - Pilon fracture
        - Pre-operative planning
        - Hardware assessment

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet first
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection/mass |
        | Volume | If contrast: 75 mL |
        | Flow Rate | 2-3 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Include distal tibia/fibula through hindfoot. Submillimeter for 3D. Bilateral scout for positioning. May scan bilateral for comparison
        - Additional Recons: 3D reconstruction for surgical planning. Document fracture fragments

    === "Nursing Notes"

        - No IV unless contrast needed

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Malleolar fractures. Tibial plafond. Talus. Calcaneus. Syndesmosis. Ligaments on contrast

    === "Tips & Tricks"

        - Bilateral scout for symmetry. Submillimeter for 3D

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout Bilateral | Bilateral ankles | Feet | N/A | N/A | AP for positioning |
    | CT Ankle | Distal tib/fib | Hindfoot | N/A or 60s if contrast | 0.625 mm | Submillimeter |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Ankle | Ankle | 1 mm/1 mm | Bone | N/A | Bone algorithm |
    | Coronal | Ankle | Ankle | 1.5 mm/1 mm | Bone | N/A | Coronal ankle |
    | Sagittal | Ankle | Ankle | 1.5 mm/1 mm | Bone | N/A | Sagittal ankle |
    | 3D surface | Ankle | Bones | 0.625 mm source | Bone | N/A | 3D for complex fractures |
