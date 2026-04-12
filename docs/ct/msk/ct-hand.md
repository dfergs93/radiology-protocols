---
title: CT Hand
slug: ct-hand
category: msk
protocol_type: musculoskeletal
last_updated: '2024-01-15'
author: Dr. Chen
synonyms: []
clinical_indications:
- Hand fracture
- Scaphoid fracture
- Metacarpal fracture
- Foreign body
- Pre-operative planning
position: Prone with hand extended (superman position) or supine with arm at side
npo: N/A
premedication: ''
contrast:
  agent: None typically. Contrast if infection
  volume: 'If contrast: 50 mL'
  flow_rate: 2 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 150-200)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: CT Hand
  start: Distal radius/ulna
  end: Fingertips
  delay: N/A or 60s if contrast
  thickness: 0.625 mm
  notes: Submillimeter
recons:
- plane: Axial
  acquisition: Hand
  fov: Hand
  thickness_increment: 1 mm/0.75 mm
  kernel: Bone
  ir_strength: N/A
  notes: Thin axial
- plane: Coronal
  acquisition: Hand
  fov: Hand
  thickness_increment: 1 mm/0.75 mm
  kernel: Bone
  ir_strength: N/A
  notes: Coronal hand
- plane: Sagittal
  acquisition: Hand
  fov: Hand
  thickness_increment: 1 mm/0.75 mm
  kernel: Bone
  ir_strength: N/A
  notes: Sagittal hand
- plane: Oblique sagittal
  acquisition: Hand
  fov: Scaphoid
  thickness_increment: 1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Scaphoid long axis
notes:
  tech: Distal radius/ulna through fingertips. Submillimeter. Position hand flat.
    Bilateral scout for comparison
  nursing: No IV unless infection suspected
  rad: Carpal fractures (scaphoid navicular lunate). Metacarpals. Phalanges. CMC joints.
    Foreign bodies
  tips: Superman position preferred. Submillimeter for scaphoid
  additional_recons: Scaphoid-specific views. 3D if complex. Document foreign body
    location
safety:
  renal: N/A or eGFR > 30
  allergy: N/A or check allergy
---

# CT Hand

**Last Updated:** 2024-01-15  
**Author:** Dr. Chen

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Hand | Contrast (N/A or 60s if contrast delay) | Distal radius/ulna to Fingertips |

    === "Clinical Indications"

        - Hand fracture
        - Scaphoid fracture
        - Metacarpal fracture
        - Foreign body
        - Pre-operative planning

-   __2. Patient Prep__

    ---

    - **Position:** Prone with hand extended (superman position) or supine with arm at side
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection |
        | Volume | If contrast: 50 mL |
        | Flow Rate | 2 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Distal radius/ulna through fingertips. Submillimeter. Position hand flat. Bilateral scout for comparison
        - Additional Recons: Scaphoid-specific views. 3D if complex. Document foreign body location

    === "Nursing Notes"

        - No IV unless infection suspected

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Carpal fractures (scaphoid navicular lunate). Metacarpals. Phalanges. CMC joints. Foreign bodies

    === "Tips & Tricks"

        - Superman position preferred. Submillimeter for scaphoid

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Distal radius/ulna | Fingertips | N/A | N/A | AP and lateral |
    | CT Hand | Distal radius/ulna | Fingertips | N/A or 60s if contrast | 0.625 mm | Submillimeter |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Hand | Hand | 1 mm/0.75 mm | Bone | N/A | Thin axial |
    | Coronal | Hand | Hand | 1 mm/0.75 mm | Bone | N/A | Coronal hand |
    | Sagittal | Hand | Hand | 1 mm/0.75 mm | Bone | N/A | Sagittal hand |
    | Oblique sagittal | Hand | Scaphoid | 1 mm | Bone | N/A | Scaphoid long axis |
