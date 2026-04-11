---
title: CT Chest Abdomen Pelvis with Contrast
slug: ct-chest-abdomen-pelvis-with-contrast
category: abdomen
protocol_type: contrast-enhanced
last_updated: '2024-01-15'
author: Dr. Smith
synonyms: []
clinical_indications:
- Oncology staging
- Infection source
- Abdominal pain
position: Supine with arms raised
npo: NPO 4 hours solids. Clear liquids OK up to 2 hours
premedication: 'Oral contrast: 250-500 mL neutral (Volumen or water). Give 60-90 min
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
  start: Lung bases or diaphragm
  end: Pubic symphysis
  delay: 70 sec
  thickness: 0.625 mm
  notes: Single portal venous phase
- name: Renal Delay
  start: 1-2cm above kidneys
  end: 1-2cm below kidneys
  delay: 300 sec
  thickness: 0.625 mm
  notes: Renal Delay series
recons:
- plane: Axial
  acquisition: Portal venous
  fov: CAP
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Chest diagnostic
- plane: Axial
  acquisition: Renal Delay
  fov: Abdomen
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Renal diagnostic
- plane: Coronal
  acquisition: Portal venous
  fov: Full CAP
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Coronal overview
notes:
  tech: Single phase portal venous. 40 second injection. 70 second scan delay from
    start of injection
  nursing: 20-22G IV. Verify renal function
  rad: Portal venous phase optimal for solid organ and bowel assessment. Systematic
    review all organs
  tips: Arms fully raised. Neutral oral contrast preferred over positive
  additional_recons: Sagittal reformats optional
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# CT Chest Abdomen Pelvis with Contrast

**Last Updated:** 2024-01-15  
**Author:** Dr. Smith

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Portal Venous Phase | Contrast (70 sec delay) | Lung bases or diaphragm to Pubic symphysis |
        | Renal Delay | 1-2cm above and below kidneys | 300 sec | 0.625 mm | Renal Delay series |

    === "Clinical Indications"

        - Oncology staging
        - Infection source
        - Abdominal pain

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours solids. Clear liquids OK up to 2 hours
    - **Pre-Medication:**
        - Oral contrast: 250-500 mL neutral (Volumen or water). Give 60-90 min before scan

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

        - Single phase portal venous. 40 second injection. 70 second scan delay from start of injection
        - Additional Recons: Sagittal reformats optional

    === "Nursing Notes"

        - 20-22G IV. Verify renal function

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Portal venous phase optimal for solid organ and bowel assessment. Systematic review all organs

    === "Tips & Tricks"

        - Arms fully raised. Neutral oral contrast preferred over positive

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Thoracic inlet | Pubic symphysis | N/A | N/A | AP and lateral |
    | Portal Venous Phase | Lung bases or diaphragm | Pubic symphysis | 70 sec | 0.625 mm | Single portal venous phase |
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
    | Axial | Portal venous | CAP | 2.5 mm/2.5 mm | Standard | 3 | Chest diagnostic |
    | Axial | Renal Delay | Abdomen | 2.5 mm/2.5 mm | Standard | 3 | Renal diagnostic |
    | Coronal | Portal venous | Full CAP | 3 mm/3 mm | Standard | 3 | Coronal overview |
