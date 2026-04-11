---
title: CTV Head
slug: ctv-head
category: neuro
protocol_type: vascular
last_updated: '2024-01-15'
author: Dr. Rodriguez
synonyms: []
clinical_indications:
- Venous sinus thrombosis
- Dural sinus thrombosis
- Intracranial hypertension
- Venous malformation
position: Supine head-first
npo: NPO 2 hours
premedication: ''
contrast:
  agent: Omnipaque 350
  volume: 75-100 mL
  flow_rate: 3-4 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 250)
  rotation_time: 0.5-0.6s
  pitch: Helical
series:
- name: NC Head
  start: Vertex
  end: Foramen magnum
  delay: N/A
  thickness: 5 mm
  notes: Baseline
- name: CTV Head
  start: Skull base
  end: Vertex
  delay: 60-90 sec delay
  thickness: 0.625-1 mm
  notes: Venous phase
recons:
- plane: Axial
  acquisition: CTV
  fov: Head
  thickness_increment: 1 mm/1 mm
  kernel: Brain
  ir_strength: '3'
  notes: Venous sinuses
- plane: MIP
  acquisition: CTV
  fov: Sinuses
  thickness_increment: Thick slab
  kernel: Brain
  ir_strength: N/A
  notes: Venogram overview
- plane: 3D VR
  acquisition: CTV
  fov: Venous system
  thickness_increment: 1 mm source
  kernel: Brain
  ir_strength: N/A
  notes: 3D venogram
- plane: Sagittal
  acquisition: CTV
  fov: Midline
  thickness_increment: 1.5 mm
  kernel: Brain
  ir_strength: '3'
  notes: Sagittal sinus
notes:
  tech: NC Head then delayed venous CTV (60-90 sec). Skull base to vertex. Assess
    venous sinuses
  nursing: 18-20G IV
  rad: 'NC: hemorrhage. CTV: filling defects in sinuses. Venous thrombosis. Cortical
    vein thrombosis'
  tips: Delayed timing 60-90 sec. Look for filling defects
  additional_recons: 3D VR venogram. MIP maximum intensity projection. Document filling
    defects
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# CTV Head

**Last Updated:** 2024-01-15  
**Author:** Dr. Rodriguez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Head | Non-contrast | Vertex to Foramen magnum |
        | CTV Head | Contrast (60-90 sec delay delay) | Skull base to Vertex |

    === "Clinical Indications"

        - Venous sinus thrombosis
        - Dural sinus thrombosis
        - Intracranial hypertension
        - Venous malformation

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first
    - **NPO Status:** NPO 2 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 75-100 mL |
        | Flow Rate | 3-4 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - NC Head then delayed venous CTV (60-90 sec). Skull base to vertex. Assess venous sinuses
        - Additional Recons: 3D VR venogram. MIP maximum intensity projection. Document filling defects

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
    | Scout | Vertex | C1 | N/A | N/A | Lateral |
    | NC Head | Vertex | Foramen magnum | N/A | 5 mm | Baseline |
    | CTV Head | Skull base | Vertex | 60-90 sec delay | 0.625-1 mm | Venous phase |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5-0.6s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTV | Head | 1 mm/1 mm | Brain | 3 | Venous sinuses |
    | MIP | CTV | Sinuses | Thick slab | Brain | N/A | Venogram overview |
    | 3D VR | CTV | Venous system | 1 mm source | Brain | N/A | 3D venogram |
    | Sagittal | CTV | Midline | 1.5 mm | Brain | 3 | Sagittal sinus |
