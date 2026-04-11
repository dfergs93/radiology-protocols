---
title: CTA Head
slug: cta-head
category: neuro
protocol_type: vascular
last_updated: '2024-01-15'
author: Dr. Thompson
synonyms: []
clinical_indications:
- Aneurysm screening
- Subarachnoid hemorrhage
- Vascular malformation
- Intracranial stenosis
position: Supine head-first
npo: NPO 2 hours
premedication: ''
contrast:
  agent: Omnipaque 350
  volume: 75-100 mL
  flow_rate: 4-5 mL/s
  timing: Bolus Tracking
  roi: Aortic arch or carotid
  trigger: 150 HU
tech_params:
  kv: 100-120
  mas: Auto (reference 250)
  rotation_time: 0.5-0.6s
  pitch: Helical
series:
- name: NC Head (optional)
  start: Vertex
  end: Foramen magnum
  delay: N/A
  thickness: 5 mm
  notes: Baseline if SAH
- name: CTA Head
  start: Skull base
  end: Vertex
  delay: Bolus tracked
  thickness: 0.5-0.625 mm
  notes: Submillimeter for 3D
recons:
- plane: Axial
  acquisition: CTA
  fov: Head
  thickness_increment: 0.75 mm/0.75 mm
  kernel: Brain
  ir_strength: '3'
  notes: Source images
- plane: MIP
  acquisition: CTA
  fov: Circle of Willis
  thickness_increment: Thick slab
  kernel: Brain
  ir_strength: N/A
  notes: Vessel overview
- plane: 3D VR
  acquisition: CTA
  fov: Intracranial vessels
  thickness_increment: 0.5 mm source
  kernel: Brain
  ir_strength: N/A
  notes: 3D angiogram
- plane: Curved MPR
  acquisition: CTA
  fov: Individual vessels
  thickness_increment: 0.75 mm
  kernel: Brain
  ir_strength: '3'
  notes: Vessel-specific views
notes:
  tech: NC Head optional then CTA skull base to vertex. Bolus tracking. Submillimeter
    for 3D reconstruction
  nursing: 20G IV minimum. Good bolus essential
  rad: Assess circle of Willis. Aneurysms. Stenosis. Vascular malformations. Anatomic
    variants
  tips: Minimize motion. Thin slices for small aneurysms
  additional_recons: 3D VR and MIP. Measure aneurysm if present. Assess A1 A2 dominance
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# CTA Head

**Last Updated:** 2024-01-15  
**Author:** Dr. Thompson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Head (optional) | Non-contrast | Vertex to Foramen magnum |
        | CTA Head | Arterial (bolus tracked) | Skull base to Vertex |

    === "Clinical Indications"

        - Aneurysm screening
        - Subarachnoid hemorrhage
        - Vascular malformation
        - Intracranial stenosis

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
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Aortic arch or carotid |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - NC Head optional then CTA skull base to vertex. Bolus tracking. Submillimeter for 3D reconstruction
        - Additional Recons: 3D VR and MIP. Measure aneurysm if present. Assess A1 A2 dominance

    === "Nursing Notes"

        - 20G IV minimum. Good bolus essential

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Assess circle of Willis. Aneurysms. Stenosis. Vascular malformations. Anatomic variants

    === "Tips & Tricks"

        - Minimize motion. Thin slices for small aneurysms

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Vertex | C1 | N/A | N/A | Lateral |
    | NC Head (optional) | Vertex | Foramen magnum | N/A | 5 mm | Baseline if SAH |
    | CTA Head | Skull base | Vertex | Bolus tracked | 0.5-0.625 mm | Submillimeter for 3D |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5-0.6s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTA | Head | 0.75 mm/0.75 mm | Brain | 3 | Source images |
    | MIP | CTA | Circle of Willis | Thick slab | Brain | N/A | Vessel overview |
    | 3D VR | CTA | Intracranial vessels | 0.5 mm source | Brain | N/A | 3D angiogram |
    | Curved MPR | CTA | Individual vessels | 0.75 mm | Brain | 3 | Vessel-specific views |
