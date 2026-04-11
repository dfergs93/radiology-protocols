---
title: CT Shoulder
slug: ct-shoulder
category: msk
protocol_type: musculoskeletal
last_updated: '2024-01-15'
author: Dr. Lee
synonyms: []
clinical_indications:
- Shoulder fracture
- Proximal humerus
- Glenoid
- Scapula
- Rotator cuff calcification
position: Supine with arm at side
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
- name: CT Shoulder
  start: Entire scapula
  end: Proximal humerus
  delay: N/A or 60s if contrast
  thickness: 0.625 mm
  notes: Submillimeter
recons:
- plane: Axial
  acquisition: Shoulder
  fov: Shoulder
  thickness_increment: 1.5 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Axial bone
- plane: Coronal
  acquisition: Shoulder
  fov: Shoulder
  thickness_increment: 2 mm/1.5 mm
  kernel: Bone
  ir_strength: N/A
  notes: Coronal shoulder
- plane: Sagittal
  acquisition: Shoulder
  fov: Shoulder
  thickness_increment: 2 mm/1.5 mm
  kernel: Bone
  ir_strength: N/A
  notes: Sagittal shoulder
- plane: Oblique
  acquisition: Shoulder
  fov: Glenoid
  thickness_increment: 1.5 mm
  kernel: Bone
  ir_strength: N/A
  notes: Glenoid en face
notes:
  tech: Include entire scapula and proximal humerus. Submillimeter for glenoid detail.
    Y-views for scapula
  nursing: No IV unless contrast indicated
  rad: Proximal humerus fractures (Neer). Glenoid fractures. Scapular fractures. AC
    joint. Rotator cuff calcifications
  tips: Include entire scapula. Submillimeter for glenoid
  additional_recons: 3D reconstruction. Neer classification if proximal humerus. Glenoid
    version measurements
safety:
  renal: N/A or eGFR > 30
  allergy: N/A or check allergy
---

# CT Shoulder

**Last Updated:** 2024-01-15  
**Author:** Dr. Lee

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Shoulder | Contrast (N/A or 60s if contrast delay) | Entire scapula to Proximal humerus |

    === "Clinical Indications"

        - Shoulder fracture
        - Proximal humerus
        - Glenoid
        - Scapula
        - Rotator cuff calcification

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arm at side
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

        - Include entire scapula and proximal humerus. Submillimeter for glenoid detail. Y-views for scapula
        - Additional Recons: 3D reconstruction. Neer classification if proximal humerus. Glenoid version measurements

    === "Nursing Notes"

        - No IV unless contrast indicated

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Proximal humerus fractures (Neer). Glenoid fractures. Scapular fractures. AC joint. Rotator cuff calcifications

    === "Tips & Tricks"

        - Include entire scapula. Submillimeter for glenoid

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Include scapula | Proximal humerus | N/A | N/A | AP and Y-view |
    | CT Shoulder | Entire scapula | Proximal humerus | N/A or 60s if contrast | 0.625 mm | Submillimeter |

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
    | Axial | Shoulder | Shoulder | 1.5 mm/1 mm | Bone | N/A | Axial bone |
    | Coronal | Shoulder | Shoulder | 2 mm/1.5 mm | Bone | N/A | Coronal shoulder |
    | Sagittal | Shoulder | Shoulder | 2 mm/1.5 mm | Bone | N/A | Sagittal shoulder |
    | Oblique | Shoulder | Glenoid | 1.5 mm | Bone | N/A | Glenoid en face |
