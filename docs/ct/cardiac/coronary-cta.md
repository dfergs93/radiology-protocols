---
author: ''
category: cardiac
clinical_indications:
- Intermediate chest pain
- Suspected infarct
- Coronary artery dissection or aneurysm
- Anomalous coronary artery
- Stent patency
contrast:
  agent: Isovue 370
  duration: 20s
  flow_rate: 4-5 mL/s
  roi: Ascending aorta
  timing: Bolus Tracking
  trigger: 200 HU
  volume: 1.1 mL/kg
last_updated: '2026-02-02'
notes:
  additional_recons: Curved MPR of all coronaries.
  nursing: 20G IV minimum. Check for metoprolol or nitroglycerin contraindications.
    Nitro is priority over metoprolol if BP is borderline.
  rad: Calculate Agatston score. Give CAD-RADS score. Check function look for potential
    focal wall motion abnormalities
  tech: Non-valsalva breathing technique, cardiac breathing instruction. Put in study
    notes if patient unable to follow breathing instructions. | If high HR variability,
    can trigger by millisecond (200ms - 450 ms pulse range). Revolution CT is better
    for Afib. | Target End diastole if HR < 65bpm. Target End systole if HR > 86bpm.
    Target End diastole to End systole if HR 66 - 75 bpm
  tips: Full chest coverage essential. Extended FOV. Low pitch for retrospective gating
npo: NPO 2-4 hours
position: Supine feet-first
premedication: HR < 60 target. | Metoprolol 5mg IV increments up to 15mg. Metoprolol
  contraindications include sBP < 100, 2nd/3rd degree heart block, and inhaler dependent
  asthma. | Nitroglycerin 0.4mg SL 5 minutes before scan. Nitroglycerin contraindications
  include sBP < 100, PDE5 inhibitors within 48 hrs, severe aortic stenosis.
protocol_type: vascular
recons:
- acquisition: Calcium score
  fov: Heart
  ir_strength: '3'
  kernel: Standard
  notes: For Agatston score calculation
  plane: Axial
  thickness_increment: 3 mm/3 mm
- acquisition: Calcium score
  fov: Chest
  ir_strength: '3'
  kernel: Lung
  notes: Lung FOV for Extracardiac findings
  plane: Axial
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Gated CTA
  fov: Heart
  ir_strength: '3'
  kernel: Cardiac
  notes: Native coronary assessment
  plane: Axial
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: Gated CTA
  fov: Heart
  ir_strength: '3'
  kernel: Cardiac
  notes: MPRs by 3D lab
  plane: 3D VR
  thickness_increment: 0.5 mm source
safety:
  allergy: Check allergy history
  renal: Verify eGFR > 30
series:
- delay: N/A
  end: Below heart
  name: Calcium Score
  notes: Calcium score
  start: Carina
  thickness: 3 mm
- delay: Bolus tracked
  end: 2cm below heart apex
  name: Gated CTA
  notes: Retrospective gating
  start: 2cm above LAD
  thickness: 0.5-0.625 mm
slug: coronary-cta
synonyms: []
tech_params:
  kv: 100-120
  mas: Auto ECG modulation
  pitch: 0.2-0.24
  rotation_time: 0.28s
title: Coronary CTA
---

# Coronary CTA

**Last Updated:** 2026-02-02
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Calcium Score | N/A | Carina → Below heart |
        | Gated CTA | Bolus tracked | 2cm above LAD → 2cm below heart apex |

    === "Clinical Indications"

        - Intermediate chest pain
        - Suspected infarct
        - Coronary artery dissection or aneurysm
        - Anomalous coronary artery
        - Stent patency

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet-first
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:**
        - HR < 60 target.
        - Metoprolol 5mg IV increments up to 15mg. Metoprolol contraindications include sBP < 100, 2nd/3rd degree heart block, and inhaler dependent asthma.
        - Nitroglycerin 0.4mg SL 5 minutes before scan. Nitroglycerin contraindications include sBP < 100, PDE5 inhibitors within 48 hrs, severe aortic stenosis.

-   __3. IV Contrast & Injection__

    ---
    === "Injection Parameters"

        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.1 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Duration | 20s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 200 HU |

    === "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Non-valsalva breathing technique, cardiac breathing instruction. Put in study notes if patient unable to follow breathing instructions. | If high HR variability, can trigger by millisecond (200ms - 450 ms pulse range). Revolution CT is better for Afib. | Target End diastole if HR < 65bpm. Target End systole if HR > 86bpm. Target End diastole to End systole if HR 66 - 75 bpm

    === "Nursing Notes"

        - 20G IV minimum. Check for metoprolol or nitroglycerin contraindications. Nitro is priority over metoprolol if BP is borderline.

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Calculate Agatston score. Give CAD-RADS score. Check function look for potential focal wall motion abnormalities

    === "Tips & Tricks"

        - Full chest coverage essential. Extended FOV. Low pitch for retrospective gating

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Calcium Score | Carina | Below heart | N/A | 3 mm | Calcium score |
    | Gated CTA | 2cm above LAD | 2cm below heart apex | Bolus tracked | 0.5-0.625 mm | Retrospective gating |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Calcium score | Heart | 3 mm/3 mm | Standard | 3 | For Agatston score calculation |
    | Axial | Calcium score | Chest | 1.5 mm/1.5 mm | Lung | 3 | Lung FOV for Extracardiac findings |
    | Axial | Gated CTA | Heart | 0.625 mm/0.625 mm | Cardiac | 3 | Native coronary assessment |
    | 3D VR | Gated CTA | Heart | 0.5 mm source | Cardiac | 3 | MPRs by 3D lab |
