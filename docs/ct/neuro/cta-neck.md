---
title: CTA Neck
slug: cta-neck
category: neuro
protocol_type: vascular
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Carotid stenosis
- Vertebral artery dissection
- Neck vessel assessment
- Pre-CEA planning
position: Supine head-first
npo: NPO 2 hours
premedication: ''
contrast:
  agent: Omnipaque 350
  volume: 90-100 mL
  flow_rate: 4-5 mL/s
  timing: Bolus Tracking
  roi: Aortic arch
  trigger: 150 HU
tech_params:
  kv: 100-120
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: '0.9'
series:
- name: CTA Neck
  start: Aortic arch
  end: Skull base
  delay: Bolus tracked
  thickness: 0.625 mm
  notes: Caudocranial
recons:
- plane: Axial
  acquisition: CTA
  fov: Neck
  thickness_increment: 1 mm/1 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Source images
- plane: Coronal
  acquisition: CTA
  fov: Neck
  thickness_increment: 1.5 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Vessel overview
- plane: Sagittal
  acquisition: CTA
  fov: Carotids
  thickness_increment: 1.5 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Vertebral arteries
- plane: Curved MPR
  acquisition: CTA
  fov: Carotid bifurcations
  thickness_increment: 1 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Stenosis measurement
notes:
  tech: Aortic arch to skull base. Bolus tracking in arch. Submillimeter. Minimize
    swallowing during scan
  nursing: 20G IV antecubital preferred
  rad: Assess carotid bifurcations. Stenosis grading. Vertebral arteries. Dissection.
    Plaque morphology
  tips: Minimize swallowing. Submillimeter acquisition
  additional_recons: Curved MPR both carotid bifurcations. Measure stenosis (NASCET).
    3D VR. MIP
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# CTA Neck

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Neck | Arterial (bolus tracked) | Aortic arch to Skull base |

    === "Clinical Indications"

        - Carotid stenosis
        - Vertebral artery dissection
        - Neck vessel assessment
        - Pre-CEA planning

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
        | Volume | 90-100 mL |
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

        - Aortic arch to skull base. Bolus tracking in arch. Submillimeter. Minimize swallowing during scan
        - Additional Recons: Curved MPR both carotid bifurcations. Measure stenosis (NASCET). 3D VR. MIP

    === "Nursing Notes"

        - 20G IV antecubital preferred

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Assess carotid bifurcations. Stenosis grading. Vertebral arteries. Dissection. Plaque morphology

    === "Tips & Tricks"

        - Minimize swallowing. Submillimeter acquisition

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Aortic arch | Skull base | N/A | N/A | AP lateral |
    | CTA Neck | Aortic arch | Skull base | Bolus tracked | 0.625 mm | Caudocranial |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTA | Neck | 1 mm/1 mm | Vascular | 3 | Source images |
    | Coronal | CTA | Neck | 1.5 mm | Vascular | 3 | Vessel overview |
    | Sagittal | CTA | Carotids | 1.5 mm | Vascular | 3 | Vertebral arteries |
    | Curved MPR | CTA | Carotid bifurcations | 1 mm | Vascular | 3 | Stenosis measurement |
