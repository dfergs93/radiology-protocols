---
title: CTA Lower Extremity Runoff for PAD
slug: cta-lower-extremity-runoff-for-pad
category: vascular
protocol_type: vascular
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Peripheral arterial disease
- Claudication
- Critical limb ischemia
- Pre-operative bypass planning
position: Supine with arms raised. Legs straight
npo: NPO 2-4 hours
premedication: ''
contrast:
  agent: Isovue 370
  volume: 1.9 mL/kg
  flow_rate: 3-4 mL/s
  duration: 35s (5s fast 5-6mL/s then 30 s slow 3-4mL/s)
  timing: Bolus Tracking
  roi: Abdominal aorta
  trigger: 150 HU
tech_params:
  kv: 100-120
  mas: Auto (reference 250)
  rotation_time: 0.5s
  pitch: 1.2-1.5
series:
- name: CTA Arterial
  start: Renal arteries
  end: Ankle
  delay: Bolus tracked
  thickness: 0.625 mm
  notes: May need slower table speed if severe PAD
- name: CTA Runoff
  start: Mid Thigh
  end: Foot
  delay: Immediately after CTA
  thickness: 0.625 mm
  notes: Runoff phase to evaluate distal vessels
recons:
- plane: Axial
  acquisition: Arterial
  fov: Pelvis/Legs
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Assess all vessel segments
- plane: Coronal
  acquisition: Arterial
  fov: Full legs
  thickness_increment: 3 mm/3 mm
  kernel: Vascular
  ir_strength: '3'
  notes: MIP full arterial tree
- plane: Sagittal
  acquisition: Arterial
  fov: Full legs
  thickness_increment: 3 mm/3 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Lateral views of vessels
- plane: 3D VR
  acquisition: Arterial
  fov: Full legs
  thickness_increment: 1.5 mm source
  kernel: Vascular
  ir_strength: '3'
  notes: 3D for surgical planning
notes:
  tech: Scan from diaphragm to toes. Tape feet together. Use automatic bolus tracking.
    Extend delay if known severe PAD. Cover tibial vessels to ankle
  nursing: 18-20G IV antecubital, flow rate up to 6 mL/s
  rad: Assess aortoiliac femoral popliteal and tibial vessels. Grade stenoses. Identify
    occlusions. Assess runoff vessels
  tips: Ensure legs are straight and not rotated. Remove shoes and metal
  additional_recons: MIP and 3D VR. Curved MPR of each arterial segment. Bone subtraction
    for vessels.
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# CTA Lower Extremity Runoff for PAD

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | Non-contrast | Diaphragm to Toes |
        | CTA Arterial | Arterial (bolus tracked) | Above the diaphragm to Toes |
        | CTA Runoff | Immediately after CTA | Knees to Toes |

    === "Clinical Indications"

        - Peripheral arterial disease
        - Claudication
        - Critical limb ischemia
        - Pre-operative bypass planning

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised. Legs straight
    - **NPO Status:** NPO 2-4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.9 mL/kg |
        | Flow Rate | 3-4 mL/s |
        | Duration | 35s (5s fast 5-6mL/s then 30 s slow 3-4mL/s) |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Abdominal aorta |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Scan from diaphragm to toes. Tape feet together. Use automatic bolus tracking. Extend delay if known severe PAD. Cover tibial vessels to ankle
        - Additional Recons: MIP and 3D VR. Curved MPR of each arterial segment. Bone subtraction for vessels.

    === "Nursing Notes"

        - 18-20G IV antecubital, flow rate up to 6 mL/s

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Assess aortoiliac femoral popliteal and tibial vessels. Grade stenoses. Identify occlusions. Assess runoff vessels

    === "Tips & Tricks"

        - Ensure legs are straight and not rotated. Remove shoes and metal

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Renal arteries | Feet | N/A | N/A | AP full legs |
    | CTA Arterial | Renal arteries | Ankle | Bolus tracked | 0.625 mm | May need slower table speed if severe PAD |
    | CTA Runoff | Mid Thigh | Foot | Immediately after CTA | 0.625 mm | Runoff phase to evaluate distal vessels |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Pelvis/Legs | 2 mm/2 mm | Vascular | 3 | Assess all vessel segments |
    | Coronal | Arterial | Full legs | 3 mm/3 mm | Vascular | 3 | MIP full arterial tree |
    | Sagittal | Arterial | Full legs | 3 mm/3 mm | Vascular | 3 | Lateral views of vessels |
    | 3D VR | Arterial | Full legs | 1.5 mm source | Vascular | 3 | 3D for surgical planning |
