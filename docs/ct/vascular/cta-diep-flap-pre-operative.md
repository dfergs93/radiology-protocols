---
title: CTA DIEP Flap Pre-operative
slug: cta-diep-flap-pre-operative
category: vascular
protocol_type: vascular
last_updated: '2024-01-15'
author: Dr. Williams
synonyms: []
clinical_indications:
- Pre-operative planning for DIEP flap breast reconstruction
position: Supine with arms at sides or on chest
npo: NPO 2-4 hours
premedication: ''
contrast:
  agent: Isovue 370
  volume: 1.5 mL/kg
  flow_rate: 4-5 mL/s
  duration: 20s
  timing: Bolus Tracking
  roi: Abdominal aorta
  trigger: 150 HU
tech_params:
  kv: '100'
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: '0.9'
series:
- name: CTA Arterial
  start: Xiphoid
  end: Pubic symphysis
  delay: Bolus tracked
  thickness: 0.625 mm
  notes: Focus on abdominal wall
recons:
- plane: Axial
  acquisition: Arterial
  fov: Abdomen
  thickness_increment: 1 mm/1 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Thin slice for perforator mapping
- plane: Coronal
  acquisition: Arterial
  fov: Abdomen
  thickness_increment: 1.5 mm/1.5 mm
  kernel: Vascular
  ir_strength: '3'
  notes: MIP to show perforator course
- plane: Sagittal
  acquisition: Arterial
  fov: Abdomen
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Lateral views of perforators
- plane: 3D VR
  acquisition: Arterial
  fov: Anterior abd wall
  thickness_increment: 1 mm source
  kernel: Vascular
  ir_strength: '3'
  notes: 3D reconstruction for surgical planning
notes:
  tech: Scan from mid-liver to greater trochanters. Remove tight-fitting underwear.
    If patient can exercise, do leg lifts on table before injection.
  nursing: 18-20G IV
  rad: Map perforator locations. Measure vessel caliber. Identify dominant perforators.
    Note relationship to umbilicus. Prefer perforators below umbilicus.
  tips: Arms positioned to not obscure anterior abdominal wall
  additional_recons: 3D VR color-coded perforator map. Measure distances from umbilicus
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# CTA DIEP Flap Pre-operative

**Last Updated:** 2024-01-15  
**Author:** Dr. Williams

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Arterial | Arterial (bolus tracked) | Mid-Liver to Greater Trochanters |

    === "Clinical Indications"

        - Pre-operative planning for DIEP flap breast reconstruction

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms at sides or on chest
    - **NPO Status:** NPO 2-4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Duration | 20s |
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

        - Scan from mid-liver to greater trochanters. Remove tight-fitting underwear. If patient can exercise, do leg lifts on table before injection.
        - Additional Recons: 3D VR color-coded perforator map. Measure distances from umbilicus

    === "Nursing Notes"

        - 18-20G IV

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Map perforator locations. Measure vessel caliber. Identify dominant perforators. Note relationship to umbilicus. Prefer perforators below umbilicus. 

    === "Tips & Tricks"

        - Arms positioned to not obscure anterior abdominal wall

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Xiphoid | Pubic symphysis | N/A | N/A | AP |
    | CTA Arterial | Xiphoid | Pubic symphysis | Bolus tracked | 0.625 mm | Focus on abdominal wall |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Abdomen | 1 mm/1 mm | Vascular | 3 | Thin slice for perforator mapping |
    | Coronal | Arterial | Abdomen | 1.5 mm/1.5 mm | Vascular | 3 | MIP to show perforator course |
    | Sagittal | Arterial | Abdomen | 2 mm/2 mm | Vascular | 3 | Lateral views of perforators |
    | 3D VR | Arterial | Anterior abd wall | 1 mm source | Vascular | 3 | 3D reconstruction for surgical planning |
