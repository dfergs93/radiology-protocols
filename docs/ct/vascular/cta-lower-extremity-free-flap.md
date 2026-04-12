---
title: CTA Lower Extremity Free Flap
slug: cta-lower-extremity-free-flap
category: vascular
protocol_type: vascular
last_updated: '2024-01-15'
author: Dr. Kim
synonyms: []
clinical_indications:
- Pre-operative planning for free flap harvest (fibula ALT anterolateral thigh)
position: Supine with legs extended
npo: NPO 2-4 hours
premedication: ''
contrast:
  agent: Isovue 370
  volume: 1.5 mL/kg
  flow_rate: 4-5 mL/s
  duration: 25s
  timing: Bolus Tracking
  roi: Femoral artery
  trigger: 150 HU
tech_params:
  kv: '100'
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: '0.9'
series:
- name: CTA Arterial
  start: Mid-Thigh
  end: Toes
  delay: Bolus tracked
  thickness: 0.625 mm
  notes: Bilateral for comparison and variants
- name: CTA Delayed
  start: Mid-Thigh
  end: Toes
  delay: 60s
  thickness: 0.625 mm
  notes: Bilateral for comparison and variants
recons:
- plane: Axial
  acquisition: Arterial
  fov: Thighs/Legs
  thickness_increment: 1 mm/1 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Thin slice for perforator identification
- plane: Coronal
  acquisition: Arterial
  fov: Full legs
  thickness_increment: 1.5 mm/1.5 mm
  kernel: Vascular
  ir_strength: '3'
  notes: MIP to show perforator course
- plane: Sagittal
  acquisition: Arterial
  fov: Full legs
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Lateral perforator views
notes:
  tech: Scan from iliac crest to ankle. Focus on perforators in region of interest.
    Arterial phase critical for mapping
  nursing: 18-20G IV
  rad: Map perforator vessels. Measure vessel caliber and length. Identify dominant
    pedicle. Note anatomic variants
  tips: Legs straight and not rotated. Mark skin over region of interest if possible
  additional_recons: Curved MPR of main vessels. Measure perforator locations from
    bony landmarks
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# CTA Lower Extremity Free Flap

**Last Updated:** 2024-01-15  
**Author:** Dr. Kim

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Arterial | Arterial (bolus tracked) | Mid-thigh to Toes |
        | Delay | Delayed (60s) | Mid-thigh to Toes |

    === "Clinical Indications"

        - Pre-operative planning for free flap harvest (fibula ALT anterolateral thigh)

-   __2. Patient Prep__

    ---

    - **Position:** Supine with legs extended
    - **NPO Status:** NPO 2-4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Duration | 25s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Femoral artery |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Scan from iliac crest to ankle. Focus on perforators in region of interest. Arterial phase critical for mapping
        - Additional Recons: Curved MPR of main vessels. Measure perforator locations from bony landmarks

    === "Nursing Notes"

        - 18-20G IV

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Map perforator vessels. Measure vessel caliber and length. Identify dominant pedicle. Note anatomic variants

    === "Tips & Tricks"

        - Legs straight and not rotated. Mark skin over region of interest if possible

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Mid-Thigh | Toes | N/A | N/A | AP both legs for comparison |
    | CTA Arterial | Mid-Thigh | Toes | Bolus tracked | 0.625 mm | Bilateral for comparison and variants |
    | CTA Delayed | Mid-Thigh | Toes | 60s | 0.625 mm | Bilateral for comparison and variants |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Thighs/Legs | 1 mm/1 mm | Vascular | 3 | Thin slice for perforator identification |
    | Coronal | Arterial | Full legs | 1.5 mm/1.5 mm | Vascular | 3 | MIP to show perforator course |
    | Sagittal | Arterial | Full legs | 2 mm/2 mm | Vascular | 3 | Lateral perforator views |
