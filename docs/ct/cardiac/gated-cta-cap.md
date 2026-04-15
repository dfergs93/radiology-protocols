---
title: Gated CTA CAP
slug: gated-cta-cap
category: cardiac
protocol_type: cardiac gated
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Aortic dissection
- Aortic aneurysm with cardiac involvement
- Combined cardiac and aortic pathology
position: Supine with arms raised
npo: NPO 2-4 hours
premedication: HR < 65 target. Premedication not required.
contrast:
  agent: Isovue 370
  volume: 1.6 mL/kg
  flow_rate: 4 mL/s
  duration: 20-24s
  timing: Bolus Tracking
  roi: Ascending aorta
  trigger: 180 HU
tech_params:
  kv: '100'
  mas: Auto ECG chest / High mAs AP
  rotation_time: 0.28 chest / 0.5 APs
  pitch: 0.2-0.24 chest / 1.2-1.5 AP
series:
- name: Flash Non-contrast
  start: Thoracic inlet
  end: Pubic symphysis
  delay: N/A
  thickness: 0.625 mm
  notes: Non-contrast
- name: Gated CTA Chest
  start: Thoracic inlet
  end: Diaphragm
  delay: Bolus tracked
  thickness: 0.5-0.625 mm
  notes: Retrospective gating chest
- name: Flash CTA AP
  start: Diaphragm
  end: Pubic symphysis
  delay: Immediate after chest
  thickness: 0.625 mm
  notes: High pitch helical - no gating
- name: Stent Delay (optional)
  start: Top of Stent
  end: Bottom of Stent
  delay: 40 sec
  thickness: 0.625 mm
  notes: Stent coverage
recons:
- plane: Axial
  acquisition: Gated chest
  fov: Chest
  thickness_increment: 0.75 mm/0.75 mm
  kernel: Cardiac
  ir_strength: '3'
  notes: Aortic root and valve
- plane: Axial
  acquisition: Flash AP
  fov: Abdomen/Pelvis
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Abdominal aorta and branches
- plane: Coronal
  acquisition: Both
  fov: Full CAP
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Vascular
  ir_strength: '3'
  notes: MIP full aorta
- plane: Sagittal
  acquisition: Both
  fov: Full CAP
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Curved MPR entire aorta
notes:
  tech: 'TWO acquisitions: 1) Gated retrospective CHEST 2) Flash helical ABDOMEN/PELVIS.
    Chest gated for aortic root. AP flash arterial'
  nursing: 20G IV minimum
  rad: 'Gated chest: assess aortic root valve coronaries. Flash AP: assess aorta and
    branches. Combined cardiac and vascular'
  tips: Arms up. Careful timing between gated and flash acquisitions
  additional_recons: Curved MPR full aorta. Aortic valve reformats. 3D VR
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# Gated CTA CAP

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Flash Non-contrast | Non-contrast | Thoracic inlet to Pubic symphysis |
        | Gated CTA Chest | Arterial (bolus tracked) | Thoracic inlet to Diaphragm |
        | Flash CTA AP | Contrast (Immediate after chest delay) | Diaphragm to Pubic symphysis |
        | Stent delay (optional) | Contrast (40 sec delay) | Stent coverage |

    === "Clinical Indications"

        - Aortic dissection
        - Aortic aneurysm with cardiac involvement
        - Combined cardiac and aortic pathology

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:**
        - HR < 65 target. Premedication not required.

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.6 mL/kg |
        | Flow Rate | 4 mL/s |
        | Duration | 20-24s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 180 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO acquisitions: 1) Gated retrospective CHEST 2) Flash helical ABDOMEN/PELVIS. Chest gated for aortic root. AP flash arterial
        - Additional Recons: Curved MPR full aorta. Aortic valve reformats. 3D VR

    === "Nursing Notes"

        - 20G IV minimum

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Gated chest: assess aortic root valve coronaries. Flash AP: assess aorta and branches. Combined cardiac and vascular

    === "Tips & Tricks"

        - Arms up. Careful timing between gated and flash acquisitions

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Thoracic inlet | Pubic symphysis | N/A | N/A | Full AP lateral |
    | Flash Non-contrast | Thoracic inlet | Pubic symphysis | N/A | 0.625 mm | Non-contrast |
    | Gated CTA Chest | Thoracic inlet | Diaphragm | Bolus tracked | 0.5-0.625 mm | Retrospective gating chest |
    | Flash CTA AP | Diaphragm | Pubic symphysis | Immediate after chest | 0.625 mm | High pitch helical - no gating |
    | Stent Delay (optional) | Top of Stent | Bottom of Stent | 40 sec | 0.625 mm | Stent coverage |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated chest | Chest | 0.75 mm/0.75 mm | Cardiac | 3 | Aortic root and valve |
    | Axial | Flash AP | Abdomen/Pelvis | 2 mm/2 mm | Vascular | 3 | Abdominal aorta and branches |
    | Coronal | Both | Full CAP | 2.5 mm/2.5 mm | Vascular | 3 | MIP full aorta |
    | Sagittal | Both | Full CAP | 2.5 mm/2.5 mm | Vascular | 3 | Curved MPR entire aorta |
