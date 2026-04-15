---
author: 
category: neuro
clinical_indications:
- Venous sinus thrombosis
- Dural sinus thrombosis
- Intracranial hypertension
- Venous malformation
contrast:
  agent: Isovue 370
  duration: 15-20s
  flow_rate: 3-4 mL/s
  roi: ''
  timing: Fixed Delay
  trigger: ''
  volume: 75-100 mL
last_updated: '2026-01-01'
notes:
  additional_recons: 3D VR venogram. MIP maximum intensity projection. Document filling
    defects
  nursing: 18-20G IV
  rad: 'NC: hemorrhage. CTV: filling defects in sinuses. Venous thrombosis. Cortical
    vein thrombosis'
  tech: NC Head then delayed venous CTV (60-90 sec). Skull base to vertex. Assess
    venous sinuses
  tips: Delayed timing 60-90 sec. Look for filling defects
npo: NPO 2 hours
position: Supine head-first
premedication: ''
protocol_type: vascular
recons:
- acquisition: CTV
  fov: Head
  ir_strength: '3'
  kernel: Brain
  notes: Venous sinuses
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: CTV
  fov: Sinuses
  ir_strength: N/A
  kernel: Brain
  notes: Venogram overview
  plane: MIP
  thickness_increment: Thick slab
- acquisition: CTV
  fov: Venous system
  ir_strength: N/A
  kernel: Brain
  notes: 3D venogram
  plane: 3D VR
  thickness_increment: 1 mm source
- acquisition: CTV
  fov: Midline
  ir_strength: '3'
  kernel: Brain
  notes: Sagittal sinus
  plane: Sagittal
  thickness_increment: 1.5 mm
safety:
  allergy: Check allergy history
  renal: Verify eGFR > 30
series:
- delay: N/A
  end: Foramen magnum
  name: NC Head
  notes: Baseline
  start: Vertex
  thickness: 5 mm
- delay: 60-90 sec delay
  end: Vertex
  name: CTV Head
  notes: Venous phase
  start: Skull base
  thickness: 0.625-1 mm
slug: ctv-head
synonyms: []
tech_params:
  kv: '120'
  mas: Auto (reference 250)
  pitch: Helical
  rotation_time: 0.5-0.6s
title: CTV Head
---

# CTV Head

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Head | N/A | Vertex → Foramen magnum |
        | CTV Head | 60-90 sec delay | Skull base → Vertex |

    === "Clinical Indications"

        - Venous sinus thrombosis
        - Dural sinus thrombosis
        - Intracranial hypertension
        - Venous malformation

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first
    - **NPO Status:** NPO 2 hours
    - **Pre-Medication:**
        - None required

-   __3. IV Contrast & Injection__

    ---
    === "Injection Parameters"

        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 75-100 mL |
        | Flow Rate | 3-4 mL/s |
        | Duration | 15-20s |
        | Timing Method | Fixed Delay |
        | ROI Placement |  |
        | Trigger (HU) |  |

    === "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - NC Head then delayed venous CTV (60-90 sec). Skull base to vertex. Assess venous sinuses

    === "Nursing Notes"

        - 18-20G IV

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - NC: hemorrhage. CTV: filling defects in sinuses. Venous thrombosis. Cortical vein thrombosis

    === "Tips & Tricks"

        - Delayed timing 60-90 sec. Look for filling defects

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | NC Head | Vertex | Foramen magnum | N/A | 5 mm | Baseline |
    | CTV Head | Skull base | Vertex | 60-90 sec delay | 0.625-1 mm | Venous phase |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTV | Head | 1 mm/1 mm | Brain | 3 | Venous sinuses |
    | MIP | CTV | Sinuses | Thick slab | Brain | N/A | Venogram overview |
    | 3D VR | CTV | Venous system | 1 mm source | Brain | N/A | 3D venogram |
    | Sagittal | CTV | Midline | 1.5 mm | Brain | 3 | Sagittal sinus |
