---
title: Pregnant Trauma CT AP
slug: pregnant-trauma-ct-ap
category: trauma
protocol_type: trauma
last_updated: '2024-01-15'
author: Dr. Anderson
synonyms: []
clinical_indications:
- Pregnant trauma patient
- Multi-trauma pregnancy
- Maternal injury assessment
position: Supine with left lateral tilt if possible
npo: None - trauma
premedication: ''
contrast:
  agent: Omnipaque 350
  volume: 125 mL
  flow_rate: 3 mL/s
tech_params:
  kv: '100'
  mas: Reduced mAs if possible
  rotation_time: 0.5s
  pitch: '1.375'
series:
- name: Portal Venous AP
  start: Diaphragm
  end: Pubic symphysis
  delay: 70 sec
  thickness: 2.5 mm
  notes: Single phase minimize radiation
recons:
- plane: Axial
  acquisition: Portal venous
  fov: AP
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Maternal organs
- plane: Coronal
  acquisition: Portal venous
  fov: AP
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Overview
- plane: Sagittal
  acquisition: Portal venous
  fov: Pelvis
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Uterus and placenta
notes:
  tech: Portal venous phase 70s. SINGLE PHASE to minimize fetal radiation. Shield
    uterus if injury distant. Document weeks gestation
  nursing: Pregnancy documented. Fetal heart tones if equipment available. Shield
    if possible
  rad: Assess maternal injuries. Minimize fetal radiation exposure. Document placental
    injury if visible
  tips: Document gestational age. Shield fetus if possible. Minimize radiation
  additional_recons: ''
safety:
  renal: Check if known
  allergy: Trauma indication documented
---

# Pregnant Trauma CT AP

**Last Updated:** 2024-01-15  
**Author:** Dr. Anderson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Portal Venous AP | Contrast (70 sec delay) | Diaphragm to Pubic symphysis |

    === "Clinical Indications"

        - Pregnant trauma patient
        - Multi-trauma pregnancy
        - Maternal injury assessment

-   __2. Patient Prep__

    ---

    - **Position:** Supine with left lateral tilt if possible
    - **NPO Status:** None - trauma
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 125 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Portal venous phase 70s. SINGLE PHASE to minimize fetal radiation. Shield uterus if injury distant. Document weeks gestation

    === "Nursing Notes"

        - Pregnancy documented. Fetal heart tones if equipment available. Shield if possible

        !!! warning "Safety First"
            - **Renal Function:** Check if known
            - **Allergy:** Trauma indication documented

    === "Radiologist Notes"

        - Assess maternal injuries. Minimize fetal radiation exposure. Document placental injury if visible

    === "Tips & Tricks"

        - Document gestational age. Shield fetus if possible. Minimize radiation

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Pubic symphysis | N/A | N/A | Low dose scout |
    | Portal Venous AP | Diaphragm | Pubic symphysis | 70 sec | 2.5 mm | Single phase minimize radiation |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Reduced mAs if possible |
    | Rotation Time | 0.5s |
    | Pitch | 1.375 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Portal venous | AP | 2.5 mm/2.5 mm | Standard | 3 | Maternal organs |
    | Coronal | Portal venous | AP | 3 mm/3 mm | Standard | 3 | Overview |
    | Sagittal | Portal venous | Pelvis | 3 mm/3 mm | Standard | 3 | Uterus and placenta |
