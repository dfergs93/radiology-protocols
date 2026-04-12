---
title: CTA Pelvis Prostate Artery Embolization
slug: cta-pelvis-prostate-artery-embolization
category: vascular
protocol_type: vascular
last_updated: '2024-01-15'
author: Dr. Jackson
synonyms: []
clinical_indications:
- Pre-procedural planning for prostate artery embolization
- Benign prostatic hyperplasia
position: Supine with arms raised
npo: NPO 2-4 hours
premedication: ''
contrast:
  agent: Isovue 370
  volume: 1.2 mL/kg
  flow_rate: 3-4 mL/s
  duration: 18-22s
  timing: Bolus Tracking
  roi: Common iliac artery
  trigger: 150 HU
tech_params:
  kv: '100'
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: '0.9'
series:
- name: CTA Arterial
  start: Iliac crest
  end: Lesser trochanters
  delay: Bolus tracked
  thickness: 0.625 mm
  notes: Focus on internal iliac branches
recons:
- plane: Axial
  acquisition: Arterial
  fov: Pelvis
  thickness_increment: 1 mm/1 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Identify prostate artery origins
- plane: Coronal
  acquisition: Arterial
  fov: Pelvis
  thickness_increment: 1.5 mm/1.5 mm
  kernel: Vascular
  ir_strength: '3'
  notes: MIP of iliac vessels
- plane: Sagittal
  acquisition: Arterial
  fov: Pelvis
  thickness_increment: 1.5 mm/1.5 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Lateral view pelvic vessels
- plane: 3D VR
  acquisition: Arterial
  fov: Pelvis
  thickness_increment: 0.75 mm source
  kernel: Vascular
  ir_strength: '3'
  notes: 3D roadmap for interventional radiologist
notes:
  tech: Scan from L3 to proximal femur. Arterial phase essential. Focus on internal
    iliac branches and prostate supply
  nursing: 18-20G IV | Chcek BP for nitroglycerin administration, check for contraindications
  rad: Identify prostate artery origins (usually anterior division of internal iliac).
    Map anatomy for IR. Note variants and anastomoses
  tips: Full bladder helpful for prostate visualization. Coordinate with IR before
    scan
  additional_recons: 3D VR with prostate vessels highlighted. Curved MPR of internal
    iliac branches. Measure vessel diameters
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# CTA Pelvis Prostate Artery Embolization

**Last Updated:** 2024-01-15  
**Author:** Dr. Jackson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Arterial | Arterial (bolus tracked) | Iliac crest to Lesser trochanters |

    === "Clinical Indications"

        - Pre-procedural planning for prostate artery embolization
        - Benign prostatic hyperplasia

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 2-4 hours
    - **Pre-medication:** 
        - Nitroglycerin 0.8 mg SL if systolic BP > 110
        - Nitroglycerin 0.4 mg SL if systolic BP > 100
    
-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.2 mL/kg |
        | Flow Rate | 3-4 mL/s |
        | Duration | 18-22s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Common iliac artery |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Scan from L3 to proximal femur. Arterial phase essential. Focus on internal iliac branches and prostate supply
        - Additional Recons: 3D VR with prostate vessels highlighted. Curved MPR of internal iliac branches. Measure vessel diameters

    === "Nursing Notes"

        - 18-20G IV
        - Chcek BP for nitroglycerin administration, check for contraindications

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Identify prostate artery origins (usually anterior division of internal iliac). Map anatomy for IR. Note variants and anastomoses

    === "Tips & Tricks"

        - Full bladder helpful for prostate visualization. Coordinate with IR before scan

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Iliac crest | Lesser trochanters | N/A | N/A | AP pelvis |
    | CTA Arterial | Iliac crest | Lesser trochanters | Bolus tracked | 0.625 mm | Focus on internal iliac branches |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Pelvis | 1 mm/1 mm | Vascular | 3 | Identify prostate artery origins |
    | Coronal | Arterial | Pelvis | 1.5 mm/1.5 mm | Vascular | 3 | MIP of iliac vessels |
    | Sagittal | Arterial | Pelvis | 1.5 mm/1.5 mm | Vascular | 3 | Lateral view pelvic vessels |
    | 3D VR | Arterial | Pelvis | 0.75 mm source | Vascular | 3 | 3D roadmap for interventional radiologist |
