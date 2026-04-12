---
title: CT Knee
slug: ct-knee
category: msk
protocol_type: musculoskeletal
last_updated: '2024-01-15'
author: Dr. Thompson
synonyms: []
clinical_indications:
- Knee fracture
- Tibial plateau
- Patellar fracture
- Pre-operative planning
- Hardware evaluation
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
- name: CT Knee
  start: Distal femur
  end: Proximal tib/fib
  delay: N/A or 60s if contrast
  thickness: 0.625 mm
  notes: Submillimeter
recons:
- plane: Axial
  acquisition: Knee
  fov: Knee
  thickness_increment: 1.5 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Bone algorithm
- plane: Coronal
  acquisition: Knee
  fov: Knee
  thickness_increment: 1.5 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Coronal knee
- plane: Sagittal
  acquisition: Knee
  fov: Knee
  thickness_increment: 1.5 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Sagittal knee
- plane: 3D surface
  acquisition: Knee
  fov: Bones
  thickness_increment: 0.625 mm source
  kernel: Bone
  ir_strength: N/A
  notes: 3D for surgical planning
notes:
  tech: Distal femur through proximal tibia/fibula. Submillimeter. Extended FOV for
    alignment. Bilateral scout
  nursing: No IV unless contrast indicated
  rad: Tibial plateau fractures (Schatzker). Femoral condyles. Patella. Fibula. Cruciate
    ligaments on contrast. Menisci
  tips: Bilateral scout for alignment assessment
  additional_recons: Schatzker classification if tibial plateau. Measure alignment.
    3D reconstruction
safety:
  renal: N/A or eGFR > 30
  allergy: N/A or check allergy
---

# CT Knee

**Last Updated:** 2024-01-15  
**Author:** Dr. Thompson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Knee | Contrast (N/A or 60s if contrast delay) | Distal femur to Proximal tib/fib |

    === "Clinical Indications"

        - Knee fracture
        - Tibial plateau
        - Patellar fracture
        - Pre-operative planning
        - Hardware evaluation

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

        - Distal femur through proximal tibia/fibula. Submillimeter. Extended FOV for alignment. Bilateral scout
        - Additional Recons: Schatzker classification if tibial plateau. Measure alignment. 3D reconstruction

    === "Nursing Notes"

        - No IV unless contrast indicated

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Tibial plateau fractures (Schatzker). Femoral condyles. Patella. Fibula. Cruciate ligaments on contrast. Menisci

    === "Tips & Tricks"

        - Bilateral scout for alignment assessment

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout Bilateral | Bilateral knees | Extended | N/A | N/A | AP for alignment |
    | CT Knee | Distal femur | Proximal tib/fib | N/A or 60s if contrast | 0.625 mm | Submillimeter |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Knee | Knee | 1.5 mm/1 mm | Bone | N/A | Bone algorithm |
    | Coronal | Knee | Knee | 1.5 mm/1 mm | Bone | N/A | Coronal knee |
    | Sagittal | Knee | Knee | 1.5 mm/1 mm | Bone | N/A | Sagittal knee |
    | 3D surface | Knee | Bones | 0.625 mm source | Bone | N/A | 3D for surgical planning |
