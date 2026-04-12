---
title: Trauma CTA Chest with PV CT AP
slug: trauma-cta-chest-with-pv-ct-ap
category: trauma
protocol_type: vascular
last_updated: '2024-01-15'
author: Dr. Lee
synonyms: []
clinical_indications:
- Blunt thoracic trauma
- Aortic injury
- Great vessel injury
- Multi-trauma
position: Supine with arms raised
npo: None - trauma
premedication: ''
contrast:
  agent: Omnipaque 350
  volume: 125 mL
  flow_rate: 4 mL/s
  timing: 'Dual phase: CTA Chest arterial + Portal venous AP'
  roi: Descending aorta
  trigger: 150 HU
tech_params:
  kv: 100-120
  mas: Auto (reference 250)
  rotation_time: 0.5s
  pitch: 1.0-1.2
series:
- name: CTA Chest
  start: Lung apices
  end: Diaphragm
  delay: Bolus tracked
  thickness: 0.625 mm
  notes: Arterial phase
- name: Portal Venous AP
  start: Diaphragm
  end: Pubic symphysis
  delay: 70 sec from start
  thickness: 0.625 mm
  notes: Portal venous phase
recons:
- plane: Axial
  acquisition: CTA chest
  fov: Chest
  thickness_increment: 1.25 mm/1.25 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Aorta and great vessels
- plane: Axial
  acquisition: PV AP
  fov: Abdomen/Pelvis
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Solid organs
- plane: Coronal
  acquisition: CTA chest
  fov: Chest
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Aorta overview
- plane: Sagittal
  acquisition: CTA chest
  fov: Aorta
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Sagittal aorta
notes:
  tech: 'TWO acquisitions: 1) CTA CHEST arterial (bolus track) 2) Portal venous ABDOMEN/PELVIS
    70s. Chest arterial for aorta/vessels'
  nursing: Large bore IV 18-20G. Verify flow
  rad: 'Chest arterial: aortic injury (intimal flap pseudoaneurysm). AP portal venous:
    solid organ injury'
  tips: Trauma indication. Fast scan. Good IV essential
  additional_recons: 3D aorta and great vessels. Curved MPR aorta. Grade aortic injury
safety:
  renal: eGFR > 30 if known
  allergy: Trauma indication
---

# Trauma CTA Chest with PV CT AP

**Last Updated:** 2024-01-15  
**Author:** Dr. Lee

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Chest | Arterial (bolus tracked) | Lung apices to Diaphragm |
        | Portal Venous AP | Contrast (70 sec from start delay) | Diaphragm to Pubic symphysis |

    === "Clinical Indications"

        - Blunt thoracic trauma
        - Aortic injury
        - Great vessel injury
        - Multi-trauma

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** None - trauma
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 125 mL |
        | Flow Rate | 4 mL/s |
        | Timing Method | Dual phase: CTA Chest arterial + Portal venous AP |
        | ROI Placement | Descending aorta |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO acquisitions: 1) CTA CHEST arterial (bolus track) 2) Portal venous ABDOMEN/PELVIS 70s. Chest arterial for aorta/vessels
        - Additional Recons: 3D aorta and great vessels. Curved MPR aorta. Grade aortic injury

    === "Nursing Notes"

        - Large bore IV 18-20G. Verify flow

        !!! warning "Safety First"
            - **Renal Function:** eGFR > 30 if known
            - **Allergy:** Trauma indication

    === "Radiologist Notes"

        - Chest arterial: aortic injury (intimal flap pseudoaneurysm). AP portal venous: solid organ injury

    === "Tips & Tricks"

        - Trauma indication. Fast scan. Good IV essential

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Pubic symphysis | N/A | N/A | AP full |
    | CTA Chest | Lung apices | Diaphragm | Bolus tracked | 0.625 mm | Arterial phase |
    | Portal Venous AP | Diaphragm | Pubic symphysis | 70 sec from start | 0.625 mm | Portal venous phase |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTA chest | Chest | 1.25 mm/1.25 mm | Vascular | 3 | Aorta and great vessels |
    | Axial | PV AP | Abdomen/Pelvis | 2.5 mm/2.5 mm | Standard | 3 | Solid organs |
    | Coronal | CTA chest | Chest | 2 mm/2 mm | Vascular | 3 | Aorta overview |
    | Sagittal | CTA chest | Aorta | 2 mm/2 mm | Vascular | 3 | Sagittal aorta |
