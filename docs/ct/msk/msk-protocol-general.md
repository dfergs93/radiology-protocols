---
title: MSK Protocol General
slug: msk-protocol-general
category: msk
protocol_type: contrast-enhanced
last_updated: '2024-01-15'
author: Dr. Lee
synonyms: []
clinical_indications:
- Pre-operative planning
- Post-operative assessment
- Infection
- Mass
- Soft tissue tumor
- Abscess
position: Depends on body part
npo: NPO 2-4 hours if contrast
premedication: ''
contrast:
  agent: Omnipaque 350 if contrast
  volume: 100 mL if contrast
  flow_rate: 2-3 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 200-250)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: Non-contrast
  start: Region
  end: Region
  delay: N/A
  thickness: 0.625-1 mm
  notes: Baseline if done
- name: Contrast phase
  start: Region
  end: Region
  delay: 60-90 sec if done
  thickness: 0.625-1 mm
  notes: Standard if done
- name: Delayed phase
  start: Region
  end: Region
  delay: 5-10 min if done
  thickness: 1-2 mm
  notes: For infection/tumor
recons:
- plane: Axial
  acquisition: Acquisition
  fov: Region
  thickness_increment: 1-2 mm/1-2 mm
  kernel: Bone and Standard
  ir_strength: '3'
  notes: Primary images
- plane: Coronal
  acquisition: Region
  fov: Region
  thickness_increment: 2 mm/2 mm
  kernel: Bone and Standard
  ir_strength: '3'
  notes: Coronal reformats
- plane: Sagittal
  acquisition: Region
  fov: Region
  thickness_increment: 2 mm/2 mm
  kernel: Bone and Standard
  ir_strength: '3'
  notes: Sagittal reformats
- plane: 3D if needed
  acquisition: Region
  fov: Bones
  thickness_increment: 0.625-1 mm source
  kernel: Bone
  ir_strength: N/A
  notes: 3D for surgical planning
notes:
  tech: Field of view specific to region. Submillimeter if 3D needed. NC and/or contrast
    based on indication. Delayed phase (5-10 min) for infection/tumor
  nursing: IV for contrast studies. Document indication
  rad: 'NC: baseline bone soft tissue. Contrast: enhancement pattern. Delayed: washout
    or persistent enhancement. 3D for surgical planning'
  tips: Tailor protocol to clinical question. Bilateral for comparison
  additional_recons: Compare to contralateral side. Measure lesions. Bone and soft
    tissue windows
safety:
  renal: N/A or eGFR > 30
  allergy: N/A or check allergy
---

# MSK Protocol General

**Last Updated:** 2024-01-15  
**Author:** Dr. Lee

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | Non-contrast | Region to Region |
        | Contrast phase | Contrast (60-90 sec if done delay) | Region to Region |
        | Delayed phase | Contrast (5-10 min if done delay) | Region to Region |

    === "Clinical Indications"

        - Pre-operative planning
        - Post-operative assessment
        - Infection
        - Mass
        - Soft tissue tumor
        - Abscess

-   __2. Patient Prep__

    ---

    - **Position:** Depends on body part
    - **NPO Status:** NPO 2-4 hours if contrast
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 if contrast |
        | Volume | 100 mL if contrast |
        | Flow Rate | 2-3 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Field of view specific to region. Submillimeter if 3D needed. NC and/or contrast based on indication. Delayed phase (5-10 min) for infection/tumor
        - Additional Recons: Compare to contralateral side. Measure lesions. Bone and soft tissue windows

    === "Nursing Notes"

        - IV for contrast studies. Document indication

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - NC: baseline bone soft tissue. Contrast: enhancement pattern. Delayed: washout or persistent enhancement. 3D for surgical planning

    === "Tips & Tricks"

        - Tailor protocol to clinical question. Bilateral for comparison

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Region specific | Region specific | N/A | N/A | Two views |
    | Non-contrast | Region | Region | N/A | 0.625-1 mm | Baseline if done |
    | Contrast phase | Region | Region | 60-90 sec if done | 0.625-1 mm | Standard if done |
    | Delayed phase | Region | Region | 5-10 min if done | 1-2 mm | For infection/tumor |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Acquisition | Region | 1-2 mm/1-2 mm | Bone and Standard | 3 | Primary images |
    | Coronal | Region | Region | 2 mm/2 mm | Bone and Standard | 3 | Coronal reformats |
    | Sagittal | Region | Region | 2 mm/2 mm | Bone and Standard | 3 | Sagittal reformats |
    | 3D if needed | Region | Bones | 0.625-1 mm source | Bone | N/A | 3D for surgical planning |
