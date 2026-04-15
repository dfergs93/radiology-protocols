---
title: CTA Head and Neck (Arch to Vertex)
slug: cta-head-and-neck-arch-to-vertex
category: neuro
protocol_type: vascular
last_updated: '2026-01-04'
author: 
synonyms: []
clinical_indications:
- Stroke workup
- Carotid stenosis
- Vertebral artery dissection
- Aneurysm screening
position: Supine head-first with arms at sides
npo: NPO 2 hours
premedication: None typically. Consider anxiolytic if severe claustrophobia
contrast:
  agent: Isovue 370
  volume: 80-100 mL
  flow_rate: 4-5 mL/s
  timing: Bolus Tracking
  roi: Aortic arch
  trigger: 150 HU
tech_params:
  kv: 100-120
  mas: Auto (reference 250)
  rotation_time: 0.5s
  pitch: '0.9'
series:
- name: CTA Neck
  start: Aortic arch
  end: Skull base
  delay: Bolus tracked
  thickness: 0.625 mm
  notes: Arterial phase - caudocranial
- name: CTA Head
  start: Skull base
  end: Vertex
  delay: Immediate
  thickness: 0.625 mm
  notes: Same bolus as neck - single acquisition
recons:
- plane: Axial
  acquisition: CTA
  fov: Neck
  thickness_increment: 1 mm/1 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Submillimeter for carotid assessment
- plane: Axial
  acquisition: CTA
  fov: Head
  thickness_increment: 1 mm/1 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Submillimeter for circle of Willis
- plane: Coronal
  acquisition: CTA
  fov: Neck
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: MIP for carotid overview
- plane: Sagittal
  acquisition: CTA
  fov: Full
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: MIP for vertebral arteries
notes:
  tech: Scan from aortic arch through vertex. Use bolus tracking in arch. Minimize
    dental artifact with gantry angulation
  nursing: Good antecubital IV access required - 20G minimum. Verify injection site
    for extravasation risk
  rad: Evaluate complete circle of Willis. Assess carotid bifurcations. Look for dissection.
    Check aneurysms
  tips: Remove dentures. Minimize swallowing during neck acquisition
  additional_recons: MIP and 3D VR reconstructions of vessels. Curved MPR of carotids
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history and renal function
---

# CTA Head and Neck (Arch to Vertex)

**Last Updated:** 2026-01-04  
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Neck | Arterial (bolus tracked) | Aortic arch to Skull base |
        | CTA Head | Contrast (Immediate delay) | Skull base to Vertex |

    === "Clinical Indications"

        - Stroke workup
        - Carotid stenosis
        - Vertebral artery dissection
        - Aneurysm screening

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first with arms at sides
    - **NPO Status:** NPO 2 hours
    - **Pre-Medication:**
        - None typically. Consider anxiolytic if severe claustrophobia

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 80-100 mL |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Aortic arch |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Scan from aortic arch through vertex. Use bolus tracking in arch. Minimize dental artifact with gantry angulation
        - Additional Recons: MIP and 3D VR reconstructions of vessels. Curved MPR of carotids

    === "Nursing Notes"

        - Good antecubital IV access required - 20G minimum. Verify injection site for extravasation risk

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history and renal function

    === "Radiologist Notes"

        - Evaluate complete circle of Willis. Assess carotid bifurcations. Look for dissection. Check aneurysms

    === "Tips & Tricks"

        - Remove dentures. Minimize swallowing during neck acquisition

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Aortic arch | Vertex | N/A | N/A | AP and lateral |
    | CTA Neck | Aortic arch | Skull base | Bolus tracked | 0.625 mm | Arterial phase - caudocranial |
    | CTA Head | Skull base | Vertex | Immediate | 0.625 mm | Same bolus as neck - single acquisition |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTA | Neck | 1 mm/1 mm | Vascular | 3 | Submillimeter for carotid assessment |
    | Axial | CTA | Head | 1 mm/1 mm | Vascular | 3 | Submillimeter for circle of Willis |
    | Coronal | CTA | Neck | 2 mm/2 mm | Vascular | 3 | MIP for carotid overview |
    | Sagittal | CTA | Full | 2 mm/2 mm | Vascular | 3 | MIP for vertebral arteries |
