---
title: CTA Popliteal Entrapment
slug: cta-popliteal-entrapment
category: vascular
protocol_type: vascular
last_updated: '2024-01-15'
author: Dr. Thompson
synonyms: []
clinical_indications:
- Popliteal entrapment syndrome
- Exercise-induced leg pain
- Young patient with claudication
position: Supine with legs extended in neutral position
npo: NPO 2-4 hours
premedication: ''
contrast:
  agent: Isovue 370
  volume: 'Dual injection: 1.2 mL/kg + 1.2 mL/kg'
  flow_rate: 4 mL/s
  duration: 18-20s + 18-20s
  timing: Bolus Tracking
  roi: Popliteal artery
  trigger: 150 HU
tech_params:
  kv: '100'
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: '0.9'
series:
- name: CTA Neutral Position
  start: Distal femur
  end: Ankle
  delay: Bolus tracked from 1st injection
  thickness: 0.625 mm
  notes: Both legs neutral resting position
- name: CTA Delayed Neutral Position
  start: Distal femur
  end: Ankle
  delay: 40 sec delay from 1st injection
  thickness: 0.625 mm
  notes: Both legs neutral resting position
- name: CTA Plantarflexion
  start: Distal femur
  end: Ankle
  delay: Bolus tracked from 2nd injection
  thickness: 0.625 mm
  notes: Patient actively plantarflexes both feet - point toes
recons:
- plane: Axial
  acquisition: Neutral
  fov: Both legs
  thickness_increment: 1.5 mm/1.5 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Baseline popliteal artery anatomy
- plane: Axial
  acquisition: Plantarflexion
  fov: Both legs
  thickness_increment: 1.5 mm/1.5 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Assess for compression with maneuver
- plane: Coronal
  acquisition: Both phases
  fov: Both legs
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: MIP comparison neutral vs flexion
- plane: Sagittal
  acquisition: Both phases
  fov: Both legs
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Lateral view popliteal fossa
notes:
  tech: 'TWO acquisitions required: 1) Neutral position 2) Active plantarflexion.
    Both legs scanned for comparison. Coach patient on plantarflexion technique'
  nursing: 18-20G IV antecubital
  rad: Compare neutral vs plantarflexion images. Look for popliteal artery compression
    deviation or occlusion with plantarflexion. Assess muscle anatomy
  tips: Coach patient on maintaining plantarflexion during second acquisition. Use
    foot straps if needed
  additional_recons: Side-by-side comparison of neutral vs plantarflexion. 3D VR showing
    muscle-vessel relationship
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history. Explain plantarflexion maneuver to patient
---

# CTA Popliteal Entrapment

**Last Updated:** 2024-01-15  
**Author:** Dr. Thompson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Neutral Position | Arterial (bolus tracked from 1st injection) | 4cm above the knees to the toes |
        | CTA Delayed Neutral Position | Delayed Arterial (40 sec delay from 1st injection) | 4cm above the knees to the toes |
        | CTA Plantarflexion | Arterial (bolus tracked from 2nd injection) | 4cm above the knees to the toes |

    === "Clinical Indications"

        - Popliteal entrapment syndrome
        - Exercise-induced leg pain
        - Young patient with claudication

-   __2. Patient Prep__

    ---

    - **Position:** Supine with legs extended in neutral position
    - **NPO Status:** NPO 2-4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | Dual injection: 1.2 mL/kg + 1.2 mL/kg |
        | Flow Rate | 4 mL/s |
        | Duration | 18-20s + 18-20s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Popliteal artery |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO acquisitions required: 1) Neutral position 2) Active plantarflexion. Both legs scanned for comparison. Coach patient on plantarflexion technique
        - Additional Recons: Side-by-side comparison of neutral vs plantarflexion. 3D VR showing muscle-vessel relationship

    === "Nursing Notes"

        - 18-20G IV antecubital

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history. Explain plantarflexion maneuver to patient

    === "Radiologist Notes"

        - Compare neutral vs plantarflexion images. Look for popliteal artery compression deviation or occlusion with plantarflexion. Assess muscle anatomy

    === "Tips & Tricks"

        - Coach patient on maintaining plantarflexion during second acquisition. Use foot straps if needed

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Distal femur | Ankle | N/A | N/A | AP both legs |
    | CTA Neutral Position | Distal femur | Ankle | Bolus tracked from 1st injection | 0.625 mm | Both legs neutral resting position |
    | CTA Delayed Neutral Position | Distal femur | Ankle | 40 sec delay from 1st injection | 0.625 mm | Both legs neutral resting position |
    | CTA Plantarflexion | Distal femur | Ankle | Bolus tracked from 2nd injection | 0.625 mm | Patient actively plantarflexes both feet - point toes |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 0.9 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Neutral | Both legs | 1.5 mm/1.5 mm | Vascular | 3 | Baseline popliteal artery anatomy |
    | Axial | Plantarflexion | Both legs | 1.5 mm/1.5 mm | Vascular | 3 | Assess for compression with maneuver |
    | Coronal | Both phases | Both legs | 2 mm/2 mm | Vascular | 3 | MIP comparison neutral vs flexion |
    | Sagittal | Both phases | Both legs | 2 mm/2 mm | Vascular | 3 | Lateral view popliteal fossa |
