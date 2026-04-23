---
author: None
category: cardiac
clinical_indications:
- Pre-TAVR planning
- Aortic stenosis valve replacement planning
contrast:
  agent: Isovue 370
  duration: 22s
  flow_rate: 4 mL/s
  roi: Ascending aorta
  timing: Bolus Tracking
  trigger: 180 HU
  volume: 1.6 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: 'TAVR measurements: annulus area perimeter diameters. Coronary
    heights. Sinus of Valsalva. STJ. Ascending aorta. Access vessels'
  nursing: 20G IV antecubital
  rad: Measure aortic annulus (3 diameters). Coronary heights. Access vessels (iliofemoral).
    Valve calcium. Comprehensive TAVR measurements
  tech: Gated CHEST retrospective + Flash AP. Gated for valve measurements. AP for
    access planning. TAVR post-processing required
  tips: TAVR-specific measurements protocol. Thin slices critical
npo: NPO 4 hours
position: Supine with arms raised
premedication: HR < 65 target. Premedication not required.
protocol_type: cardiac gated
recons:
- acquisition: Gated chest
  fov: Heart
  ir_strength: '3'
  kernel: Cardiac
  notes: Aortic valve and root measurements
  plane: Axial
  thickness_increment: 0.5 mm/0.5 mm
- acquisition: Flash AP
  fov: AP
  ir_strength: '3'
  kernel: Vascular
  notes: Access vessel assessment
  plane: Axial
  thickness_increment: 2 mm/2 mm
- acquisition: Gated chest
  fov: Aortic valve
  ir_strength: '3'
  kernel: Cardiac
  notes: En face aortic annulus for sizing
  plane: Double oblique
  thickness_increment: 0.5 mm
- acquisition: Flash AP
  fov: Iliofemoral
  ir_strength: '3'
  kernel: Vascular
  notes: 3D access planning
  plane: 3D VR
  thickness_increment: 1.5 mm source
safety:
  allergy: Check allergy history
  renal: Verify eGFR > 30
series:
- delay: Bolus tracked
  end: Diaphragm
  name: Gated CTA Chest
  notes: Retrospective gating for valve
  start: Thoracic inlet
  thickness: 0.5 mm
- delay: Immediate
  end: Femoral heads
  name: Flash CTA AP
  notes: Iliofemoral access planning
  start: Diaphragm
  thickness: 0.625 mm
- delay: NA
  end: Femoral Heads
  name: Noncon CAP
  notes: ''
  start: Thoracic Inlet
  thickness: 1 mm
slug: gated-cta-tavr
synonyms: []
tech_params:
  kv: '100'
  mas: Auto ECG chest / High mAs AP
  pitch: 0.2-0.24 / 1.2-1.5
  rotation_time: 0.28 / 0.5s
title: Gated CTA TAVR
---

# Gated CTA TAVR

**Last Updated:** 2026-01-01
**Author:** None

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Gated CTA Chest | Bolus tracked | Thoracic inlet → Diaphragm |
        | Flash CTA AP | Immediate | Diaphragm → Femoral heads |
        | Noncon CAP | NA | Thoracic Inlet → Femoral Heads |

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
    === "Injection Parameters"

        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.6 mL/kg |
        | Flow Rate | 4 mL/s |
        | Duration | 22s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 180 HU |

    === "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Gated CHEST retrospective + Flash AP. Gated for valve measurements. AP for access planning. TAVR post-processing required

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
    | Noncon CAP | Thoracic Inlet | Femoral Heads | NA | 1 mm |  |
    | Gated CTA Chest | Thoracic inlet | Diaphragm | Bolus tracked | 0.5 mm | Retrospective gating for valve |
    | Flash CTA AP | Diaphragm | Femoral heads | Immediate | 0.625 mm | Iliofemoral access planning |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated chest | Heart | 0.5 mm/0.5 mm | Cardiac | 3 | Aortic valve and root measurements |
    | Axial | Flash AP | AP | 2 mm/2 mm | Vascular | 3 | Access vessel assessment |
    | Double oblique | Gated chest | Aortic valve | 0.5 mm | Cardiac | 3 | En face aortic annulus for sizing |
    | 3D VR | Flash AP | Iliofemoral | 1.5 mm source | Vascular | 3 | 3D access planning |
