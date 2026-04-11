---
title: CT Abdomen Pelvis with Contrast
slug: ct-abdomen-pelvis-with-contrast
category: abdomen
protocol_type: contrast-enhanced
last_updated: '2026-01-02'
author: ''
synonyms: []
clinical_indications:
- Abdominal pain
- Oncology staging
- Infection source
- Post-operative complications
position: Supine with arms raised
npo: NPO 4 hours for solids
premedication: 'Oral contrast: 900 mL Readi-Cat 2 over 90 minutes. Last cup 30 min
  before scan'
contrast:
  agent: Isovue 370
  volume: 1.5 mL/kg
  flow_rate: 3 mL/s
  duration: 40s
  timing: Empiric Delay (70s)
tech_params:
  kv: '120'
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: 1.0-1.375
series:
- name: Portal Venous Phase
  start: Diaphragm
  end: Lesser trochanters
  delay: 70 sec
  thickness: 0.625 mm
  notes: Standard portal venous timing
- name: Renal Delay
  start: 1-2cm above kidneys
  end: 1-2cm below kidneys
  delay: 300 sec
  thickness: 0.625 mm
  notes: Renal Delay series
recons:
- plane: Axial
  acquisition: Portal venous
  fov: Abdomen
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Primary diagnostic series
- plane: Axial
  acquisition: Renal Delay
  fov: Abdomen
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Renal Delay series
- plane: Coronal
  acquisition: Portal venous
  fov: Full AP
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Coronal reformats for overview
- plane: Sagittal
  acquisition: Portal venous
  fov: Full AP
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Sagittal reformats for bowel loops
notes:
  tech: Ensure adequate oral contrast opacification. Scan from diaphragm through pubic
    symphysis. 70 second delay typical
  nursing: 20-22G IV required. Verify patent IV. Oral contrast 250-500mL water before
    scan.
  rad: Systematic review of all solid organs. Check for free fluid/air. Assess bowel
    enhancement pattern
  tips: Arms raised completely. Remove all metal objects from scan range
  additional_recons: Thin slice 1mm for 3D if mass identified
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history. Pre-medicate if prior reaction
---

# CT Abdomen Pelvis with Contrast

**Last Updated:** 2026-01-02  
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Portal Venous Phase | Contrast (70 sec delay) | Diaphragm to Pubic symphysis |
        | Renal Delay | Contrast (300 sec delay) | 1-2cm above and below kidneys |

    === "Clinical Indications"

        - Abdominal pain
        - Oncology staging
        - Infection source
        - Post-operative complications

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours for solids
    - **Pre-Medication:**
        - Oral contrast: 900 mL Readi-Cat 2 over 90 minutes. Last cup 30 min before scan

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 3 mL/s |
        | Duration | 40s |
        | Timing Method | Empiric Delay (70s) |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Ensure adequate oral contrast opacification. Scan from diaphragm through pubic symphysis. 70 second delay typical
        - Additional Recons: Thin slice 1mm for 3D if mass identified

    === "Nursing Notes"

        - 20-22G IV required. Verify patent IV. Oral contrast 250-500mL water before scan.

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history. Pre-medicate if prior reaction

    === "Radiologist Notes"

        - Systematic review of all solid organs. Check for free fluid/air. Assess bowel enhancement pattern

    === "Tips & Tricks"

        - Arms raised completely. Remove all metal objects from scan range

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Diaphragm | Pubic symphysis | N/A | N/A | AP and lateral |
    | Portal Venous Phase | Diaphragm | Lesser trochanters | 70 sec | 0.625 mm | Standard portal venous timing |
    | Renal Delay | 1-2cm above kidneys | 1-2cm below kidneys | 300 sec | 0.625 mm | Renal Delay series |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.375 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Portal venous | Abdomen | 3 mm/3 mm | Standard | 3 | Primary diagnostic series |
    | Axial | Renal Delay | Abdomen | 3 mm/3 mm | Standard | 3 | Renal Delay series |
    | Coronal | Portal venous | Full AP | 3 mm/3 mm | Standard | 3 | Coronal reformats for overview |
    | Sagittal | Portal venous | Full AP | 3 mm/3 mm | Standard | 3 | Sagittal reformats for bowel loops |
