---
title: CT Foot
slug: ct-foot
category: msk
protocol_type: musculoskeletal
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Foot fracture
- Lisfranc injury
- Tarsal fractures
- Foreign body
- Pre-operative planning
position: Supine feet first
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
- name: CT Foot
  start: Calcaneus
  end: Toes
  delay: N/A or 60s if contrast
  thickness: 0.625 mm
  notes: Submillimeter
recons:
- plane: Axial
  acquisition: Foot
  fov: Foot
  thickness_increment: 1 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Axial bone
- plane: Coronal
  acquisition: Foot
  fov: Foot
  thickness_increment: 1.5 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Coronal foot
- plane: Sagittal
  acquisition: Foot
  fov: Foot
  thickness_increment: 1.5 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Sagittal foot
- plane: Oblique
  acquisition: Foot
  fov: Lisfranc
  thickness_increment: 1.5 mm
  kernel: Bone
  ir_strength: N/A
  notes: Lisfranc joint
notes:
  tech: Calcaneus through toes. Submillimeter. Weight-bearing position if able. Bilateral
    for comparison
  nursing: No IV unless infection suspected
  rad: Calcaneus. Talus. Navicular. Cuneiforms. Metatarsals. Phalanges. Lisfranc ligament.
    Plantar fascia
  tips: Weight-bearing if possible. Bilateral comparison helpful
  additional_recons: Document Lisfranc alignment. Calcaneal angles. 3D if complex
safety:
  renal: N/A or eGFR > 30
  allergy: N/A or check allergy
---

# CT Foot

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Foot | Contrast (N/A or 60s if contrast delay) | Calcaneus to Toes |

    === "Clinical Indications"

        - Foot fracture
        - Lisfranc injury
        - Tarsal fractures
        - Foreign body
        - Pre-operative planning

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet first
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

        - Calcaneus through toes. Submillimeter. Weight-bearing position if able. Bilateral for comparison
        - Additional Recons: Document Lisfranc alignment. Calcaneal angles. 3D if complex

    === "Nursing Notes"

        - No IV unless infection suspected

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Calcaneus. Talus. Navicular. Cuneiforms. Metatarsals. Phalanges. Lisfranc ligament. Plantar fascia

    === "Tips & Tricks"

        - Weight-bearing if possible. Bilateral comparison helpful

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Calcaneus | Toes | N/A | N/A | Lateral and AP |
    | CT Foot | Calcaneus | Toes | N/A or 60s if contrast | 0.625 mm | Submillimeter |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Foot | Foot | 1 mm/1 mm | Bone | N/A | Axial bone |
    | Coronal | Foot | Foot | 1.5 mm/1 mm | Bone | N/A | Coronal foot |
    | Sagittal | Foot | Foot | 1.5 mm/1 mm | Bone | N/A | Sagittal foot |
    | Oblique | Foot | Lisfranc | 1.5 mm | Bone | N/A | Lisfranc joint |
