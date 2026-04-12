---
title: Gated CTA CAP Sternotomy Revision
slug: gated-cta-cap-sternotomy-revision
category: cardiac
protocol_type: cardiac gated
last_updated: '2024-01-15'
author: Dr. Williams
synonyms: []
clinical_indications:
- Pre-operative planning for redo sternotomy
- Retrosternal structures assessment
position: Supine with arms raised
npo: NPO 4 hours
premedication: HR < 65 target. Premedication not required.
contrast:
  agent: Isovue 370
  volume: 1.2 mL/kg
  flow_rate: 5 mL/s
  duration: 15s
  timing: Bolus Tracking
  roi: Ascending aorta
  trigger: 180 HU
tech_params:
  kv: '100'
  mas: Auto ECG chest / High mAs other
  rotation_time: 0.28 / 0.5s
  pitch: 0.2-0.24 / 1.2-1.5
series:
- name: Gated CTA Chest
  start: Thoracic inlet
  end: Diaphragm
  delay: Bolus tracked
  thickness: 0.5-0.625 mm
  notes: Retrospective gating
- name: Flash AP
  start: Diaphragm
  end: Pubic symphysis
  delay: Immediate
  thickness: 0.625 mm
  notes: Arterial phase AP
- name: Venogram Chest
  start: Thoracic inlet
  end: Diaphragm
  delay: 60 sec
  thickness: 1 mm
  notes: Retrosternal venous structures
recons:
- plane: Axial
  acquisition: Gated chest
  fov: Chest
  thickness_increment: 0.75 mm/0.75 mm
  kernel: Cardiac
  ir_strength: '3'
  notes: Cardiac and coronary anatomy
- plane: Axial
  acquisition: Venogram
  fov: Chest
  thickness_increment: 1.25 mm/1.25 mm
  kernel: Standard
  ir_strength: '3'
  notes: Critical for retrosternal structures
- plane: Coronal
  acquisition: All phases
  fov: Chest
  thickness_increment: 2 mm/2 mm
  kernel: Standard
  ir_strength: '3'
  notes: Anterior chest wall structures
- plane: 3D VR
  acquisition: Venogram
  fov: Chest
  thickness_increment: 1 mm source
  kernel: Standard
  ir_strength: '3'
  notes: 3D map retrosternal vessels for surgery
notes:
  tech: 'THREE acquisitions: 1) Gated CHEST 2) Flash AP arterial 3) CHEST venogram
    60 sec delay. Venous for retrosternal structures'
  nursing: 20G IV
  rad: 'Gated: cardiac anatomy. Arterial: systemic vessels. VENOUS: retrosternal veins
    and adherent structures critical for surgical planning'
  tips: Venous phase critical for surgical planning. Map all retrosternal structures
  additional_recons: 3D VR venogram highlighting retrosternal veins. Distance measurements
    sternum to heart
safety:
  renal: Verify eGFR > 30
  allergy: Large contrast load - verify renal function
---

# Gated CTA CAP Sternotomy Revision

**Last Updated:** 2024-01-15  
**Author:** Dr. Williams

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Gated CTA Chest | Arterial (bolus tracked) | Thoracic inlet to Diaphragm |
        | Flash AP | Contrast (Immediate delay) | Diaphragm to Pubic symphysis |
        | Venogram Chest | Contrast (60 sec delay) | Thoracic inlet to Diaphragm |

    === "Clinical Indications"

        - Pre-operative planning for redo sternotomy
        - Retrosternal structures assessment

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    - **Pre-Medication:**
        - HR < 65 target. Premedication not required.

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.2 mL/kg |
        | Flow Rate | 5 mL/s |
        | Duration | 15s |
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

        - THREE acquisitions: 1) Gated CHEST 2) Flash AP arterial 3) CHEST venogram 60 sec delay. Venous for retrosternal structures
        - Additional Recons: 3D VR venogram highlighting retrosternal veins. Distance measurements sternum to heart

    === "Nursing Notes"

        - 20G IV

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Large contrast load - verify renal function

    === "Radiologist Notes"

        - Gated: cardiac anatomy. Arterial: systemic vessels. VENOUS: retrosternal veins and adherent structures critical for surgical planning

    === "Tips & Tricks"

        - Venous phase critical for surgical planning. Map all retrosternal structures

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Thoracic inlet | Pubic symphysis | N/A | N/A | AP lateral full |
    | Gated CTA Chest | Thoracic inlet | Diaphragm | Bolus tracked | 0.5-0.625 mm | Retrospective gating |
    | Flash AP | Diaphragm | Pubic symphysis | Immediate | 0.625 mm | Arterial phase AP |
    | Venogram Chest | Thoracic inlet | Diaphragm | 60 sec | 1 mm | Retrosternal venous structures |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated chest | Chest | 0.75 mm/0.75 mm | Cardiac | 3 | Cardiac and coronary anatomy |
    | Axial | Venogram | Chest | 1.25 mm/1.25 mm | Standard | 3 | Critical for retrosternal structures |
    | Coronal | All phases | Chest | 2 mm/2 mm | Standard | 3 | Anterior chest wall structures |
    | 3D VR | Venogram | Chest | 1 mm source | Standard | 3 | 3D map retrosternal vessels for surgery |
