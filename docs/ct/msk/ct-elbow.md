---
title: CT Elbow
slug: ct-elbow
category: msk
protocol_type: musculoskeletal
last_updated: '2024-01-15'
author: Dr. Martinez
synonyms: []
clinical_indications:
- Elbow fracture
- Radial head fracture
- Olecranon fracture
- Coronoid
- Terrible triad
position: Supine with elbow extended if possible or positioned for comfort
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
- name: CT Elbow
  start: Distal humerus
  end: Proximal radius/ulna
  delay: N/A or 60s if contrast
  thickness: 0.625 mm
  notes: Submillimeter
recons:
- plane: Axial
  acquisition: Elbow
  fov: Elbow
  thickness_increment: 1.5 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Axial bone
- plane: Coronal
  acquisition: Elbow
  fov: Elbow
  thickness_increment: 1.5 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Coronal elbow
- plane: Sagittal
  acquisition: Elbow
  fov: Elbow
  thickness_increment: 1.5 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Sagittal elbow
- plane: 3D surface
  acquisition: Elbow
  fov: Bones
  thickness_increment: 0.625 mm source
  kernel: Bone
  ir_strength: N/A
  notes: 3D for complex fractures
notes:
  tech: Distal humerus through proximal radius/ulna. Submillimeter. Position extended
    if possible. Bilateral for comparison
  nursing: No IV unless contrast needed
  rad: Distal humerus fractures. Radial head. Olecranon. Coronoid. Elbow dislocation.
    Terrible triad
  tips: Position extended if possible. Submillimeter for detail
  additional_recons: Document terrible triad if present. Radial head-capitellum alignment.
    3D reconstruction
safety:
  renal: N/A or eGFR > 30
  allergy: N/A or check allergy
---

# CT Elbow

**Last Updated:** 2024-01-15  
**Author:** Dr. Martinez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Elbow | Contrast (N/A or 60s if contrast delay) | Distal humerus to Proximal radius/ulna |

    === "Clinical Indications"

        - Elbow fracture
        - Radial head fracture
        - Olecranon fracture
        - Coronoid
        - Terrible triad

-   __2. Patient Prep__

    ---

    - **Position:** Supine with elbow extended if possible or positioned for comfort
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

        - Distal humerus through proximal radius/ulna. Submillimeter. Position extended if possible. Bilateral for comparison

    === "Nursing Notes"

        - No IV unless contrast needed

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Distal humerus fractures. Radial head. Olecranon. Coronoid. Elbow dislocation. Terrible triad

    === "Tips & Tricks"

        - Position extended if possible. Submillimeter for detail

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Distal humerus | Proximal forearm | N/A | N/A | AP lateral |
    | CT Elbow | Distal humerus | Proximal radius/ulna | N/A or 60s if contrast | 0.625 mm | Submillimeter |

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
    | Axial | Elbow | Elbow | 1.5 mm/1 mm | Bone | N/A | Axial bone |
    | Coronal | Elbow | Elbow | 1.5 mm/1 mm | Bone | N/A | Coronal elbow |
    | Sagittal | Elbow | Elbow | 1.5 mm/1 mm | Bone | N/A | Sagittal elbow |
    | 3D surface | Elbow | Bones | 0.625 mm source | Bone | N/A | 3D for complex fractures |

### Additional Reconstructions

Document terrible triad if present. Radial head-capitellum alignment. 3D reconstruction

Category: Msk

Protocol Type: Musculoskeletal
