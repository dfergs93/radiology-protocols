---
title: Gated CTA Chest
slug: gated-cta-chest
category: cardiac
protocol_type: cardiac gated
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Thoracic aortic dissection
- Chest pain radiating to the back
- Follow up thoracic aortic aneurysm
position: Supine feet-first
npo: NPO 2-4 hours
premedication: HR < 60 target. Premedication not required.
contrast:
  agent: Isovue 370
  volume: 1.1 mL/kg
  flow_rate: 4-5 mL/s
  duration: 20s
  timing: Bolus Tracking
  roi: Ascending aorta
  trigger: 200 HU
tech_params:
  kv: '100'
  mas: Auto ECG modulation
  rotation_time: 0.28s
  pitch: 0.2-0.24
series:
- name: Non-contrast
  start: Lung apices
  end: Diaphragm
  delay: N/A
  thickness: 3 mm
  notes: Calcium score
- name: Gated CTA
  start: Lung apices
  end: Diaphragm
  delay: Bolus tracked
  thickness: 0.5-0.625 mm
  notes: Retrospective ECG gating
- name: Stent delay (optional)
  start: Start of Stent
  end: End of Stent
  delay: 40 sec
  thickness: 0.5-0.625 mm
  notes: Optional for stent assessment
recons:
- plane: Axial
  acquisition: Gated CTA
  fov: Heart
  thickness_increment: 0.75 mm/0.5 mm
  kernel: Cardiac
  ir_strength: '3'
  notes: Primary coronary assessment
- plane: Curved MPR
  acquisition: Gated CTA
  fov: Each coronary
  thickness_increment: 0.75 mm
  kernel: Cardiac
  ir_strength: '3'
  notes: Vessel-specific reconstructions
- plane: Axial
  acquisition: Non-contrast
  fov: Heart
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Calcium scoring
- plane: Short/long axis
  acquisition: Gated CTA
  fov: Heart
  thickness_increment: Multi-phase
  kernel: Cardiac
  ir_strength: '3'
  notes: Functional assessment
notes:
  tech: 'Retrospective ECG gating. Cover heart. Bolus tracking in ascending aorta.
    Optional stent protocol: add 40 sec delayed phase'
  nursing: 20G IV minimum. HR control critical. Nitro administration. Monitor BP
  rad: Assess coronaries for stenosis plaque. Evaluate anomalous anatomy. Stent patency
    if applicable. Cardiac function from multi-phase
  tips: HR control essential. Coach breathing. Gating quality check
  additional_recons: Curved MPR all coronaries. Short/long axis. Multi-phase for function.
    Calcium score
safety:
  renal: Verify eGFR > 30
  allergy: Check metoprolol contraindications
---

# Gated CTA Chest

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | Non-contrast | Lung Apices to Diaphragm |
        | Gated CTA | Arterial (bolus tracked) | Lung Apices to Diaphragm |
        | Stent delay (optional) | Contrast (40 sec delay) | Stent coverage |

    === "Clinical Indications"

        - Thoracic aortic dissection
        - Chest pain radiating to the back
        - Follow up thoracic aortic aneurysm

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet-first
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:**
        - HR < 60 target. Premedication not required.

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.1 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Duration | 20s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 200 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Retrospective ECG gating. Cover heart. Bolus tracking in ascending aorta. Optional stent protocol: add 40 sec delayed phase
        - Additional Recons: Curved MPR all coronaries. Short/long axis. Multi-phase for function. Calcium score

    === "Nursing Notes"

        - 20G IV minimum. HR control critical. Nitro administration. Monitor BP

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check metoprolol contraindications

    === "Radiologist Notes"

        - Assess coronaries for stenosis plaque. Evaluate anomalous anatomy. Stent patency if applicable. Cardiac function from multi-phase

    === "Tips & Tricks"

        - HR control essential. Coach breathing. Gating quality check

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Top of chest | Diaphragm | N/A | N/A | AP lateral |
    | Non-contrast | Lung apices | Diaphragm | N/A | 3 mm | Calcium score |
    | Gated CTA | Lung apices | Diaphragm | Bolus tracked | 0.5-0.625 mm | Retrospective ECG gating |
    | Stent delay (optional) | Start of Stent | End of Stent | 40 sec | 0.5-0.625 mm | Optional for stent assessment |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated CTA | Heart | 0.75 mm/0.5 mm | Cardiac | 3 | Primary coronary assessment |
    | Curved MPR | Gated CTA | Each coronary | 0.75 mm | Cardiac | 3 | Vessel-specific reconstructions |
    | Axial | Non-contrast | Heart | 3 mm/3 mm | Standard | 3 | Calcium scoring |
    | Short/long axis | Gated CTA | Heart | Multi-phase | Cardiac | 3 | Functional assessment |
