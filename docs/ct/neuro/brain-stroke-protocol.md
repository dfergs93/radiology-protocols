---
title: Brain Stroke Protocol
slug: brain-stroke-protocol
category: neuro
protocol_type: neuroradiology
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Acute stroke
- CVA
- Neurological deficit < 24 hours
- Stroke code
position: Supine head-first
npo: None - emergency
premedication: ''
contrast:
  agent: IsoVue 370 for CTA/CTP
  volume: 100 mL
  flow_rate: 4-5 mL/s
  timing: Multi-phase stroke protocol
  roi: Multiple ROIs
  trigger: Varies
tech_params:
  kv: '120'
  mas: Auto (300 head)
  rotation_time: 1.0 / 0.5s
  pitch: '0.5'
series:
- name: NC Head
  start: Skull base
  end: Vertex
  delay: N/A
  thickness: 5 mm
  notes: STAT no contrast
- name: CTA Arch to Vertex
  start: Aortic arch
  end: Vertex
  delay: Bolus tracked aorta
  thickness: 0.625 mm
  notes: Intracranial vessels
- name: CTP (optional)
  start: Skull base
  end: Vertex
  delay: Auto-triggered
  thickness: 5 mm dynamic
  notes: Perfusion if candidate
recons:
- plane: Axial
  acquisition: NC head
  fov: Brain
  thickness_increment: 5 mm/5 mm
  kernel: Brain
  ir_strength: '3'
  notes: STAT hemorrhage detection
- plane: Axial
  acquisition: CTA Arch to Vertex
  fov: Head and Neck
  thickness_increment: 1 mm/1 mm
  kernel: Brain
  ir_strength: '3'
  notes: LVO detection
- plane: MIP
  acquisition: CTA
  fov: Circle of Willis
  thickness_increment: Thick slab
  kernel: Brain
  ir_strength: N/A
  notes: Vessel overview
- plane: CTP maps
  acquisition: CTP
  fov: Perfusion
  thickness_increment: Color maps
  kernel: N/A
  ir_strength: N/A
  notes: CBF CBV MTT Tmax maps
notes:
  tech: 'STAT protocol: 1) NC Head 2) CTA Head/Neck (aortic arch to vertex) 3) CTP
    (optional). Minimize door-to-scan time'
  nursing: No IV for NC. Large bore for CTA/CTP. STAT coordination
  rad: 'NC: hemorrhage early ischemia hyperdense vessel. CTA: LVO large vessel occlusion.
    CTP: penumbra core mismatch'
  tips: STAT protocol. Minimize delays. LVO detection critical
  additional_recons: CTA MIP and 3D. CTP perfusion maps if done. ASPECTS score. LVO
    documentation
safety:
  renal: Emergency proceed
  allergy: STAT protocol
---

# Brain Stroke Protocol

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Head | Non-contrast | Vertex to Foramen magnum |
        | CTA Arch to Vertex | Arterial (bolus tracked) | Aortic arch to Vertex |
        | CTP (optional) | Contrast (Auto-triggered delay) | Skull base to Vertex |

    === "Clinical Indications"

        - Acute stroke
        - CVA
        - Neurological deficit < 24 hours
        - Stroke code

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first
    - **NPO Status:** None - emergency
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | IsoVue 370 for CTA/CTP |
        | Volume | 100 mL |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Multi-phase stroke protocol |
        | ROI Placement | Multiple ROIs |
        | Trigger (HU) | Varies |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - STAT protocol: 1) NC Head 2) CTA Head/Neck (aortic arch to vertex) 3) CTP (optional). Minimize door-to-scan time
        - Additional Recons: CTA MIP and 3D. CTP perfusion maps if done. ASPECTS score. LVO documentation

    === "Nursing Notes"

        - No IV for NC. Large bore for CTA/CTP. STAT coordination

        !!! warning "Safety First"
            - **Renal Function:** Emergency proceed
            - **Allergy:** STAT protocol

    === "Radiologist Notes"

        - NC: hemorrhage early ischemia hyperdense vessel. CTA: LVO large vessel occlusion. CTP: penumbra core mismatch

    === "Tips & Tricks"

        - STAT protocol. Minimize delays. LVO detection critical

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Vertex | Aortic arch | N/A | N/A | STAT lateral |
    | NC Head | Skull base | Vertex | N/A | 5 mm | STAT no contrast |
    | CTA Arch to Vertex | Aortic arch | Vertex | Bolus tracked aorta | 0.625 mm | Intracranial vessels |
    | CTP (optional) | Skull base | Vertex | Auto-triggered | 5 mm dynamic | Perfusion if candidate |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | NC head | Brain | 5 mm/5 mm | Brain | 3 | STAT hemorrhage detection |
    | Axial | CTA Arch to Vertex | Head and Neck | 1 mm/1 mm | Brain | 3 | LVO detection |
    | MIP | CTA | Circle of Willis | Thick slab | Brain | N/A | Vessel overview |
    | CTP maps | CTP | Perfusion | Color maps | N/A | N/A | CBF CBV MTT Tmax maps |
