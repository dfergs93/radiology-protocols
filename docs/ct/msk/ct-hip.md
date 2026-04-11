---
title: CT Hip
slug: ct-hip
category: msk
protocol_type: musculoskeletal
last_updated: '2024-01-15'
author: Dr. Anderson
synonyms: []
clinical_indications:
- Hip fracture
- Acetabular fracture
- Femoral neck
- Pre-operative planning
- FAI assessment
position: Supine
npo: N/A
premedication: ''
contrast:
  agent: None typically. Contrast if infection/mass
  volume: 'If contrast: 100 mL'
  flow_rate: 2-3 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 250)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: CT Pelvis/Hips
  start: Iliac crests
  end: Proximal femurs
  delay: N/A or 60s if contrast
  thickness: 0.625 mm
  notes: Submillimeter for 3D
recons:
- plane: Axial
  acquisition: Hips
  fov: Pelvis/hips
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: N/A
  notes: Axial bone
- plane: Coronal
  acquisition: Hips
  fov: Pelvis/hips
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: N/A
  notes: Coronal hips
- plane: Sagittal
  acquisition: Hips
  fov: Each hip
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: N/A
  notes: Sagittal hips
- plane: Judet views
  acquisition: Hips
  fov: Acetabulum
  thickness_increment: 2 mm oblique
  kernel: Bone
  ir_strength: N/A
  notes: Obturator and iliac obliques
notes:
  tech: Iliac crests through proximal femurs. Bilateral for comparison. Submillimeter
    for 3D acetabular reconstructions
  nursing: No IV unless contrast indicated
  rad: Femoral neck fractures. Acetabular fractures (Judet/Letournel). Hip dislocation.
    FAI morphology. AVN
  tips: Bilateral coverage. Submillimeter for acetabular 3D
  additional_recons: 3D pelvis. Judet oblique views. Letournel classification. FAI
    measurements (alpha angle)
safety:
  renal: N/A or eGFR > 30
  allergy: N/A or check allergy
---

# CT Hip

**Last Updated:** 2024-01-15  
**Author:** Dr. Anderson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Pelvis/Hips | Contrast (N/A or 60s if contrast delay) | Iliac crests to Proximal femurs |

    === "Clinical Indications"

        - Hip fracture
        - Acetabular fracture
        - Femoral neck
        - Pre-operative planning
        - FAI assessment

-   __2. Patient Prep__

    ---

    - **Position:** Supine
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection/mass |
        | Volume | If contrast: 100 mL |
        | Flow Rate | 2-3 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Iliac crests through proximal femurs. Bilateral for comparison. Submillimeter for 3D acetabular reconstructions
        - Additional Recons: 3D pelvis. Judet oblique views. Letournel classification. FAI measurements (alpha angle)

    === "Nursing Notes"

        - No IV unless contrast indicated

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Femoral neck fractures. Acetabular fractures (Judet/Letournel). Hip dislocation. FAI morphology. AVN

    === "Tips & Tricks"

        - Bilateral coverage. Submillimeter for acetabular 3D

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Iliac crests | Proximal femurs | N/A | N/A | AP |
    | CT Pelvis/Hips | Iliac crests | Proximal femurs | N/A or 60s if contrast | 0.625 mm | Submillimeter for 3D |

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
    | Axial | Hips | Pelvis/hips | 2 mm/2 mm | Bone | N/A | Axial bone |
    | Coronal | Hips | Pelvis/hips | 2 mm/2 mm | Bone | N/A | Coronal hips |
    | Sagittal | Hips | Each hip | 2 mm/2 mm | Bone | N/A | Sagittal hips |
    | Judet views | Hips | Acetabulum | 2 mm oblique | Bone | N/A | Obturator and iliac obliques |
