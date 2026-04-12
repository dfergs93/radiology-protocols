---
title: Gated CTA TAVR
slug: gated-cta-tavr
category: cardiac
protocol_type: cardiac gated
last_updated: '2024-01-15'
author: Dr. Davis
synonyms: []
clinical_indications:
- Pre-TAVR planning
- Aortic stenosis valve replacement planning
position: Supine with arms raised
npo: NPO 4 hours
premedication: HR < 65 target. Premedication not required.
contrast:
  agent: Isovue 370
  volume: 1.6 mL/kg
  flow_rate: 4 mL/s
  duration: 22s
  timing: Bolus Tracking
  roi: Ascending aorta
  trigger: 180 HU
tech_params:
  kv: '100'
  mas: Auto ECG chest / High mAs AP
  rotation_time: 0.28 / 0.5s
  pitch: 0.2-0.24 / 1.2-1.5
series:
- name: Gated CTA Chest
  start: Thoracic inlet
  end: Diaphragm
  delay: Bolus tracked
  thickness: 0.5 mm
  notes: Retrospective gating for valve
- name: Flash CTA AP
  start: Diaphragm
  end: Femoral heads
  delay: Immediate
  thickness: 0.625 mm
  notes: Iliofemoral access planning
recons:
- plane: Axial
  acquisition: Gated chest
  fov: Heart
  thickness_increment: 0.5 mm/0.5 mm
  kernel: Cardiac
  ir_strength: '3'
  notes: Aortic valve and root measurements
- plane: Axial
  acquisition: Flash AP
  fov: AP
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Access vessel assessment
- plane: Double oblique
  acquisition: Gated chest
  fov: Aortic valve
  thickness_increment: 0.5 mm
  kernel: Cardiac
  ir_strength: '3'
  notes: En face aortic annulus for sizing
- plane: 3D VR
  acquisition: Flash AP
  fov: Iliofemoral
  thickness_increment: 1.5 mm source
  kernel: Vascular
  ir_strength: '3'
  notes: 3D access planning
notes:
  tech: Gated CHEST retrospective + Flash AP. Gated for valve measurements. AP for
    access planning. TAVR post-processing required
  nursing: 20G IV antecubital
  rad: Measure aortic annulus (3 diameters). Coronary heights. Access vessels (iliofemoral).
    Valve calcium. Comprehensive TAVR measurements
  tips: TAVR-specific measurements protocol. Thin slices critical
  additional_recons: 'TAVR measurements: annulus area perimeter diameters. Coronary
    heights. Sinus of Valsalva. STJ. Ascending aorta. Access vessels'
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# Gated CTA TAVR

**Last Updated:** 2024-01-15  
**Author:** Dr. Davis

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Gated CTA Chest | Arterial (bolus tracked) | Thoracic inlet to Diaphragm |
        | Flash CTA AP | Contrast (Immediate delay) | Diaphragm to Femoral heads |

    === "Clinical Indications"

        - Pre-TAVR planning
        - Aortic stenosis valve replacement planning

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
        | Volume | 1.6 mL/kg |
        | Flow Rate | 4 mL/s |
        | Duration | 22s |
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

        - Gated CHEST retrospective + Flash AP. Gated for valve measurements. AP for access planning. TAVR post-processing required
        - Additional Recons: TAVR measurements: annulus area perimeter diameters. Coronary heights. Sinus of Valsalva. STJ. Ascending aorta. Access vessels

    === "Nursing Notes"

        - 20G IV antecubital

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Measure aortic annulus (3 diameters). Coronary heights. Access vessels (iliofemoral). Valve calcium. Comprehensive TAVR measurements

    === "Tips & Tricks"

        - TAVR-specific measurements protocol. Thin slices critical

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Thoracic inlet | Femoral heads | N/A | N/A | AP lateral full |
    | Gated CTA Chest | Thoracic inlet | Diaphragm | Bolus tracked | 0.5 mm | Retrospective gating for valve |
    | Flash CTA AP | Diaphragm | Femoral heads | Immediate | 0.625 mm | Iliofemoral access planning |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated chest | Heart | 0.5 mm/0.5 mm | Cardiac | 3 | Aortic valve and root measurements |
    | Axial | Flash AP | AP | 2 mm/2 mm | Vascular | 3 | Access vessel assessment |
    | Double oblique | Gated chest | Aortic valve | 0.5 mm | Cardiac | 3 | En face aortic annulus for sizing |
    | 3D VR | Flash AP | Iliofemoral | 1.5 mm source | Vascular | 3 | 3D access planning |
