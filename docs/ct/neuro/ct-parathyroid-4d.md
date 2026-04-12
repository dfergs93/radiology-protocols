---
title: CT Parathyroid 4D
slug: ct-parathyroid-4d
category: neuro
protocol_type: contrast-enhanced
last_updated: '2024-01-15'
author: Dr. Kim
synonyms: []
clinical_indications:
- Hyperparathyroidism
- Parathyroid adenoma localization
- Pre-operative parathyroid planning
position: Supine head-first with arms down
npo: NPO 4 hours
premedication: ''
contrast:
  agent: Omnipaque 350
  volume: 75-100 mL
  flow_rate: 4 mL/s
  timing: 4D multi-phase
  roi: Carotid artery
  trigger: 150 HU
tech_params:
  kv: '120'
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: '1'
series:
- name: Non-Contrast
  start: Skull base
  end: Carina
  delay: N/A
  thickness: 2.5 mm
  notes: Baseline
- name: Arterial Phase
  start: Skull base
  end: Carina
  delay: 25 sec
  thickness: 2 mm
  notes: Parathyroid enhancement
- name: Venous Phase
  start: Skull base
  end: Carina
  delay: 55 sec
  thickness: 2 mm
  notes: Thyroid enhancement
- name: Delayed Phase
  start: Skull base
  end: Carina
  delay: 90 sec
  thickness: 2.5 mm
  notes: Washout phase
recons:
- plane: Axial
  acquisition: All phases
  fov: Neck
  thickness_increment: 2 mm/2 mm
  kernel: Standard
  ir_strength: '3'
  notes: Compare all four phases
- plane: Axial
  acquisition: Arterial
  fov: Neck
  thickness_increment: 2 mm/2 mm
  kernel: Standard
  ir_strength: '3'
  notes: Peak parathyroid enhancement
- plane: Subtraction
  acquisition: Arterial - NC
  fov: Neck
  thickness_increment: 2 mm
  kernel: Standard
  ir_strength: '3'
  notes: Enhance parathyroid conspicuity
- plane: Coronal
  acquisition: Arterial
  fov: Neck
  thickness_increment: 2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Ectopic adenoma search
notes:
  tech: 'FOUR phases: 1) NC 2) Arterial 25s 3) Venous 55s 4) Delayed/washout 90s.
    Skull base to mediastinum. Parathyroid enhances early washes out'
  nursing: 18-20G IV. High flow rate for arterial
  rad: 'NC: baseline. Arterial: parathyroid lights up. Venous: thyroid enhances. Delayed:
    parathyroid washes out faster than thyroid'
  tips: Four phase critical. Look for early enhancement and washout
  additional_recons: Subtraction images. Compare all phases. Document location for
    surgeon. Measure size
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# CT Parathyroid 4D

**Last Updated:** 2024-01-15  
**Author:** Dr. Kim

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast | Non-contrast | Skull base to Carina |
        | Arterial Phase | Contrast (25 sec delay) | Skull base to Carina |
        | Venous Phase | Contrast (55 sec delay) | Skull base to Carina |
        | Delayed Phase | Contrast (90 sec delay) | Skull base to Carina |

    === "Clinical Indications"

        - Hyperparathyroidism
        - Parathyroid adenoma localization
        - Pre-operative parathyroid planning

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first with arms down
    - **NPO Status:** NPO 4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 75-100 mL |
        | Flow Rate | 4 mL/s |
        | Timing Method | 4D multi-phase |
        | ROI Placement | Carotid artery |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - FOUR phases: 1) NC 2) Arterial 25s 3) Venous 55s 4) Delayed/washout 90s. Skull base to mediastinum. Parathyroid enhances early washes out
        - Additional Recons: Subtraction images. Compare all phases. Document location for surgeon. Measure size

    === "Nursing Notes"

        - 18-20G IV. High flow rate for arterial

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - NC: baseline. Arterial: parathyroid lights up. Venous: thyroid enhances. Delayed: parathyroid washes out faster than thyroid

    === "Tips & Tricks"

        - Four phase critical. Look for early enhancement and washout

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Skull base | Carina | N/A | N/A | AP lateral |
    | Non-Contrast | Skull base | Carina | N/A | 2.5 mm | Baseline |
    | Arterial Phase | Skull base | Carina | 25 sec | 2 mm | Parathyroid enhancement |
    | Venous Phase | Skull base | Carina | 55 sec | 2 mm | Thyroid enhancement |
    | Delayed Phase | Skull base | Carina | 90 sec | 2.5 mm | Washout phase |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | All phases | Neck | 2 mm/2 mm | Standard | 3 | Compare all four phases |
    | Axial | Arterial | Neck | 2 mm/2 mm | Standard | 3 | Peak parathyroid enhancement |
    | Subtraction | Arterial - NC | Neck | 2 mm | Standard | 3 | Enhance parathyroid conspicuity |
    | Coronal | Arterial | Neck | 2.5 mm | Standard | 3 | Ectopic adenoma search |
