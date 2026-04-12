---
title: CT Adrenal Mass Protocol
slug: ct-adrenal-mass-protocol
category: abdomen
protocol_type: contrast-enhanced
last_updated: '2024-01-15'
author: Dr. Thompson
synonyms: []
clinical_indications:
- Adrenal mass characterization
- Adenoma vs metastasis
- Incidentaloma workup
position: Supine with arms raised
npo: NPO 4 hours
premedication: ''
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
  pitch: '1'
series:
- name: Non-Contrast
  start: Diaphragm
  end: Kidneys
  delay: N/A
  thickness: 2.5 mm
  notes: Measure absolute HU in mass
- name: Portal Venous
  start: Diaphragm
  end: Kidneys
  delay: 70 sec
  thickness: 2.5 mm
  notes: Enhanced HU measurement
- name: 15 Minute Delay
  start: Diaphragm
  end: Kidneys
  delay: 900 sec
  thickness: 2.5 mm
  notes: Delayed HU for washout calculation
recons:
- plane: Axial
  acquisition: All phases
  fov: Adrenals
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: ROI measurements in mass
- plane: Axial
  acquisition: All phases
  fov: Adrenals
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Compare enhancement
- plane: Coronal
  acquisition: Portal venous
  fov: Adrenals
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Anatomic overview
notes:
  tech: 'THREE phases: 1) Non-contrast for absolute HU 2) Portal venous 70s 3) 15
    MINUTE delayed for washout. All phases cover adrenals'
  nursing: 20-22G IV. Patient must wait 15 min for delayed phase
  rad: 'NC: lipid-rich adenoma < 10 HU. Portal venous: enhancement. 15 min delay:
    calculate washout (adenoma shows washout)'
  tips: Patient wait time 15 min. Measure HU carefully with ROI in same location
  additional_recons: 'Calculate absolute washout: (Enhanced HU - Delayed HU)/(Enhanced
    HU - NC HU) x 100. >60% suggests adenoma. Measure HU in all phases'
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history. Explain 15 min delay
---

# CT Adrenal Mass Protocol

**Last Updated:** 2024-01-15  
**Author:** Dr. Thompson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast | Non-contrast | Diaphragm to Kidneys |
        | Portal Venous | Contrast (70 sec delay) | Diaphragm to Kidneys |
        | 15 Minute Delay | Contrast (900 sec delay) | Diaphragm to Kidneys |

    === "Clinical Indications"

        - Adrenal mass characterization
        - Adenoma vs metastasis
        - Incidentaloma workup

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    

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

        - THREE phases: 1) Non-contrast for absolute HU 2) Portal venous 70s 3) 15 MINUTE delayed for washout. All phases cover adrenals
        - Additional Recons: Calculate absolute washout: (Enhanced HU - Delayed HU)/(Enhanced HU - NC HU) x 100. >60% suggests adenoma. Measure HU in all phases

    === "Nursing Notes"

        - 20-22G IV. Patient must wait 15 min for delayed phase

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history. Explain 15 min delay

    === "Radiologist Notes"

        - NC: lipid-rich adenoma < 10 HU. Portal venous: enhancement. 15 min delay: calculate washout (adenoma shows washout)

    === "Tips & Tricks"

        - Patient wait time 15 min. Measure HU carefully with ROI in same location

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Kidneys | N/A | N/A | AP |
    | Non-Contrast | Diaphragm | Kidneys | N/A | 2.5 mm | Measure absolute HU in mass |
    | Portal Venous | Diaphragm | Kidneys | 70 sec | 2.5 mm | Enhanced HU measurement |
    | 15 Minute Delay | Diaphragm | Kidneys | 900 sec | 2.5 mm | Delayed HU for washout calculation |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | All phases | Adrenals | 2.5 mm/2.5 mm | Standard | 3 | ROI measurements in mass |
    | Axial | All phases | Adrenals | 2.5 mm/2.5 mm | Standard | 3 | Compare enhancement |
    | Coronal | Portal venous | Adrenals | 3 mm/3 mm | Standard | 3 | Anatomic overview |
