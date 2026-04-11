---
title: Trauma Lower Extremity Runoff CTA
slug: trauma-lower-extremity-runoff-cta
category: trauma
protocol_type: vascular
last_updated: '2024-01-15'
author: Dr. Williams
synonyms: []
clinical_indications:
- Extremity vascular injury
- Penetrating trauma
- Fracture with vascular concern
- Pulseless extremity
position: Supine legs extended
npo: None - trauma
premedication: ''
contrast:
  agent: Omnipaque 350
  volume: 125 mL
  flow_rate: 4-5 mL/s
  timing: Bolus Tracking
  roi: Abdominal aorta or proximal to injury
  trigger: 150 HU
tech_params:
  kv: 100-120
  mas: Auto (reference 250)
  rotation_time: 0.5s
  pitch: 1.2-1.5
series:
- name: CTA Arterial
  start: Coverage as needed
  end: Distal to injury
  delay: Bolus tracked
  thickness: 0.625 mm
  notes: Arterial phase runoff
recons:
- plane: Axial
  acquisition: Arterial
  fov: Legs
  thickness_increment: 1.5 mm/1.5 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Assess vessels
- plane: Coronal
  acquisition: Arterial
  fov: Legs
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: MIP overview
- plane: Sagittal
  acquisition: Arterial
  fov: Injured area
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Vessel-bone relationship
- plane: 3D VR
  acquisition: Arterial
  fov: Vessels
  thickness_increment: 1 mm source
  kernel: Vascular
  ir_strength: '3'
  notes: 3D vascular anatomy
notes:
  tech: Extend coverage based on injury. Aorta to ankles if bilateral. May do unilateral
    focused study. Arterial phase
  nursing: 18-20G IV. May need proximal IV if arm injury
  rad: 'Assess arterial injury: transection pseudoaneurysm occlusion extravasation.
    Evaluate fracture relationship to vessels'
  tips: Tailor coverage to injury. Fast acquisition
  additional_recons: MIP and 3D VR. Document vascular injury. Measure vessel caliber
safety:
  renal: Check if available
  allergy: Trauma indication
---

# Trauma Lower Extremity Runoff CTA

**Last Updated:** 2024-01-15  
**Author:** Dr. Williams

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Arterial | Arterial (bolus tracked) | Coverage as needed to Distal to injury |

    === "Clinical Indications"

        - Extremity vascular injury
        - Penetrating trauma
        - Fracture with vascular concern
        - Pulseless extremity

-   __2. Patient Prep__

    ---

    - **Position:** Supine legs extended
    - **NPO Status:** None - trauma
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 125 mL |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Abdominal aorta or proximal to injury |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Extend coverage based on injury. Aorta to ankles if bilateral. May do unilateral focused study. Arterial phase
        - Additional Recons: MIP and 3D VR. Document vascular injury. Measure vessel caliber

    === "Nursing Notes"

        - 18-20G IV. May need proximal IV if arm injury

        !!! warning "Safety First"
            - **Renal Function:** Check if available
            - **Allergy:** Trauma indication

    === "Radiologist Notes"

        - Assess arterial injury: transection pseudoaneurysm occlusion extravasation. Evaluate fracture relationship to vessels

    === "Tips & Tricks"

        - Tailor coverage to injury. Fast acquisition

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Aorta or pelvis | Ankles | N/A | N/A | AP legs |
    | CTA Arterial | Coverage as needed | Distal to injury | Bolus tracked | 0.625 mm | Arterial phase runoff |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5s |
    | Pitch | 1.2-1.5 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Legs | 1.5 mm/1.5 mm | Vascular | 3 | Assess vessels |
    | Coronal | Arterial | Legs | 2 mm/2 mm | Vascular | 3 | MIP overview |
    | Sagittal | Arterial | Injured area | 2 mm/2 mm | Vascular | 3 | Vessel-bone relationship |
    | 3D VR | Arterial | Vessels | 1 mm source | Vascular | 3 | 3D vascular anatomy |
