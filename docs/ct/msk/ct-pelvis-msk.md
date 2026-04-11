---
title: CT Pelvis MSK
slug: ct-pelvis-msk
category: msk
protocol_type: contrast-enhanced
last_updated: '2024-01-15'
author: Dr. Kim
synonyms: []
clinical_indications:
- Pelvic fracture
- Sacral fracture
- SI joint
- Pelvic ring injury
- Pre-operative planning
position: Supine
npo: N/A
premedication: ''
contrast:
  agent: None typically. Contrast if infection
  volume: 'If contrast: 100 mL'
  flow_rate: 2-3 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 250)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: CT Pelvis
  start: Iliac crests
  end: Proximal femurs
  delay: N/A or 60s if contrast
  thickness: 0.625 mm
  notes: Submillimeter for 3D
recons:
- plane: Axial
  acquisition: Pelvis
  fov: Pelvis
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: N/A
  notes: Axial bone
- plane: Coronal
  acquisition: Pelvis
  fov: Pelvis
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: N/A
  notes: Coronal pelvis
- plane: Sagittal
  acquisition: Pelvis
  fov: Pelvis
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: N/A
  notes: Sagittal sacrum
- plane: Inlet/Outlet
  acquisition: Pelvis
  fov: Pelvic ring
  thickness_increment: 2-3 mm oblique
  kernel: Bone
  ir_strength: N/A
  notes: Pelvic ring views
notes:
  tech: Iliac crests to proximal femurs. Submillimeter for 3D. Assess pelvic ring
    integrity. Inlet and outlet views
  nursing: No IV unless contrast indicated
  rad: Pelvic ring fractures (Young-Burgess). Sacral fractures (Denis). Acetabulum.
    SI joints. Symphysis pubis
  tips: Submillimeter for 3D pelvic reconstruction
  additional_recons: 3D pelvis. Inlet and outlet views. Young-Burgess classification.
    Measure displacement
safety:
  renal: N/A or eGFR > 30
  allergy: N/A or check allergy
---

# CT Pelvis MSK

**Last Updated:** 2024-01-15  
**Author:** Dr. Kim

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Pelvis | Contrast (N/A or 60s if contrast delay) | Iliac crests to Proximal femurs |

    === "Clinical Indications"

        - Pelvic fracture
        - Sacral fracture
        - SI joint
        - Pelvic ring injury
        - Pre-operative planning

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

        - Iliac crests to proximal femurs. Submillimeter for 3D. Assess pelvic ring integrity. Inlet and outlet views

    === "Nursing Notes"

        - No IV unless contrast indicated

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Pelvic ring fractures (Young-Burgess). Sacral fractures (Denis). Acetabulum. SI joints. Symphysis pubis

    === "Tips & Tricks"

        - Submillimeter for 3D pelvic reconstruction

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Iliac crests | Proximal femurs | N/A | N/A | AP |
    | CT Pelvis | Iliac crests | Proximal femurs | N/A or 60s if contrast | 0.625 mm | Submillimeter for 3D |

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
    | Axial | Pelvis | Pelvis | 2 mm/2 mm | Bone | N/A | Axial bone |
    | Coronal | Pelvis | Pelvis | 2 mm/2 mm | Bone | N/A | Coronal pelvis |
    | Sagittal | Pelvis | Pelvis | 2 mm/2 mm | Bone | N/A | Sagittal sacrum |
    | Inlet/Outlet | Pelvis | Pelvic ring | 2-3 mm oblique | Bone | N/A | Pelvic ring views |

### Additional Reconstructions

3D pelvis. Inlet and outlet views. Young-Burgess classification. Measure displacement

Category: Msk

Protocol Type: Contrast-Enhanced
