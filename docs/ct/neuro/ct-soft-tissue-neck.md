---
title: CT Soft Tissue Neck
slug: ct-soft-tissue-neck
category: neuro
protocol_type: contrast-enhanced
last_updated: '2024-01-15'
author: Dr. Thompson
synonyms: []
clinical_indications:
- Neck mass
- Deep neck infection
- Abscess
- Airway assessment
- Lymphadenopathy
position: Supine head-first
npo: NPO 2 hours
premedication: ''
contrast:
  agent: Omnipaque 350
  volume: 100 mL
  flow_rate: 3 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 200-250)
  rotation_time: 0.5s
  pitch: '1'
series:
- name: Contrast Neck
  start: Skull base
  end: Thoracic inlet
  delay: 60-70 sec
  thickness: 1-2 mm
  notes: Venous phase
recons:
- plane: Axial
  acquisition: Neck
  fov: Neck
  thickness_increment: 2.5 mm/2 mm
  kernel: Standard
  ir_strength: '3'
  notes: Soft tissue neck
- plane: Coronal
  acquisition: Neck
  fov: Neck
  thickness_increment: 3 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Coronal neck spaces
- plane: Sagittal
  acquisition: Neck
  fov: Midline
  thickness_increment: 3 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Airway and retropharyngeal
notes:
  tech: Skull base to thoracic inlet. 60-70 sec delay for venous phase. Arms down.
    Minimize swallowing. May need NC if calcium assessment
  nursing: 18-20G IV. Coach no swallowing during scan
  rad: Assess neck spaces. Retropharyngeal. Parapharyngeal. Masticator. Parotid. Submandibular.
    Thyroid. Lymph nodes. Abscess vs phlegmon
  tips: Arms down. Minimize swallowing. Quiet breathing
  additional_recons: Assess all neck spaces. Measure lymph nodes. Airway diameter
    if concern
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# CT Soft Tissue Neck

**Last Updated:** 2024-01-15  
**Author:** Dr. Thompson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Contrast Neck | Contrast (60-70 sec delay) | Skull base to Thoracic inlet |

    === "Clinical Indications"

        - Neck mass
        - Deep neck infection
        - Abscess
        - Airway assessment
        - Lymphadenopathy

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first
    - **NPO Status:** NPO 2 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 100 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Skull base to thoracic inlet. 60-70 sec delay for venous phase. Arms down. Minimize swallowing. May need NC if calcium assessment
        - Additional Recons: Assess all neck spaces. Measure lymph nodes. Airway diameter if concern

    === "Nursing Notes"

        - 18-20G IV. Coach no swallowing during scan

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Assess neck spaces. Retropharyngeal. Parapharyngeal. Masticator. Parotid. Submandibular. Thyroid. Lymph nodes. Abscess vs phlegmon

    === "Tips & Tricks"

        - Arms down. Minimize swallowing. Quiet breathing

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Skull base | Thoracic inlet | N/A | N/A | Lateral |
    | Contrast Neck | Skull base | Thoracic inlet | 60-70 sec | 1-2 mm | Venous phase |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Neck | Neck | 2.5 mm/2 mm | Standard | 3 | Soft tissue neck |
    | Coronal | Neck | Neck | 3 mm/2.5 mm | Standard | 3 | Coronal neck spaces |
    | Sagittal | Neck | Midline | 3 mm/2.5 mm | Standard | 3 | Airway and retropharyngeal |
