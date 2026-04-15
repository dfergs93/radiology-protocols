---
title: CT Triple Phase Liver
slug: ct-triple-phase-liver
category: abdomen
protocol_type: contrast-enhanced
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Liver lesion characterization
- HCC surveillance
- Liver mass protocol
position: Supine with arms raised
npo: NPO 4 hours
premedication: None typically. Oral contrast optional
contrast:
  agent: Isovue 370
  volume: 1.5 mL/kg
  flow_rate: 4-5 mL/s
  duration: 25s
  timing: 'Triple phase: NC + Arterial + Portal Venous + Delayed'
  roi: Abdominal aorta
  trigger: 150 HU
tech_params:
  kv: '100'
  mas: Auto (reference 200-250)
  rotation_time: 0.5s
  pitch: 0.9-1.0
series:
- name: Non-Contrast
  start: Diaphragm
  end: Iliac crests
  delay: N/A
  thickness: 2.5 mm
  notes: Liver FOV
- name: Late Arterial
  start: Diaphragm
  end: Iliac crests
  delay: 30-35 sec or bolus track
  thickness: 1.25 mm
  notes: Liver FOV - hypervascular lesions
- name: Portal Venous
  start: Diaphragm
  end: Pubic symphysis
  delay: 70 sec
  thickness: 2.5 mm
  notes: Full AP FOV
- name: Delayed Phase
  start: Diaphragm
  end: Iliac crests
  delay: 300 sec
  thickness: 2.5 mm
  notes: Liver FOV - washout assessment
recons:
- plane: Axial
  acquisition: All phases
  fov: Liver
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Compare all phases
- plane: Axial
  acquisition: Portal venous
  fov: Full AP
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Full abdomen pelvis PV
- plane: Coronal
  acquisition: All phases
  fov: Liver
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Coronal comparison
- plane: Subtraction
  acquisition: Arterial - NC
  fov: Liver
  thickness_increment: 2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Enhance lesion conspicuity
notes:
  tech: 'FOUR acquisitions: 1) NC abdomen 2) Late arterial (bolus track or 30-35s)
    3) Portal venous 70s 4) Delayed 5 min. FOV: Abdomen for NC/Art/Delay. Full AP
    for PV | Injection duration is fixed at 25 s'
  nursing: 20-22G IV. High flow rate critical
  rad: 'NC: characterize lesion. Arterial: hypervascular lesions HCC. Portal: most
    liver lesions. Delayed: washout pattern'
  tips: High flow rate. Extended 5 min delay. Breath hold coaching
  additional_recons: ''
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# CT Triple Phase Liver

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast (optional) | Non-contrast | Diaphragm to Iliac crests |
        | Late Arterial | Arterial (16 sec delay) | Diaphragm to Iliac crests |
        | Portal Venous | Contrast (70 sec delay) | Diaphragm to Lesser trochanters |
        | Delayed Phase | Contrast (300 sec delay) | Diaphragm to Iliac crests |

    === "Clinical Indications"

        - Liver lesion characterization
        - HCC surveillance
        - Liver mass protocol

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    - **Pre-Medication:**
        - None typically. Oral contrast optional

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Duration | 25s |
        | Timing Method | Triple phase: NC + Arterial + Portal Venous + Delayed |
        | ROI Placement | Abdominal aorta |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - FOUR acquisitions: 1) NC abdomen 2) Late arterial (bolus track or 30-35s) 3) Portal venous 70s 4) Delayed 5 min. FOV: Abdomen for NC/Art/Delay. Full AP for PV
        - Injection duration is fixed at 25 s

    === "Nursing Notes"

        - 20-22G IV. High flow rate critical

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - NC: characterize lesion. Arterial: hypervascular lesions HCC. Portal: most liver lesions. Delayed: washout pattern

    === "Tips & Tricks"

        - High flow rate. Extended 5 min delay. Breath hold coaching

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Iliac crests | N/A | N/A | AP |
    | Non-Contrast | Diaphragm | Iliac crests | N/A | 2.5 mm | Liver FOV |
    | Late Arterial | Diaphragm | Iliac crests | 30-35 sec or bolus track | 1.25 mm | Liver FOV - hypervascular lesions |
    | Portal Venous | Diaphragm | Pubic symphysis | 70 sec | 2.5 mm | Full AP FOV |
    | Delayed Phase | Diaphragm | Iliac crests | 300 sec | 2.5 mm | Liver FOV - washout assessment |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | All phases | Liver | 2.5 mm/2.5 mm | Standard | 3 | Compare all phases |
    | Axial | Portal venous | Full AP | 2.5 mm/2.5 mm | Standard | 3 | Full abdomen pelvis PV |
    | Coronal | All phases | Liver | 3 mm/3 mm | Standard | 3 | Coronal comparison |
    | Subtraction | Arterial - NC | Liver | 2.5 mm | Standard | 3 | Enhance lesion conspicuity |
