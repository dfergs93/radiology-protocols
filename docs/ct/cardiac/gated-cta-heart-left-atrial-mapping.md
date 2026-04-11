---
title: Gated CTA Heart Left Atrial Mapping
slug: gated-cta-heart-left-atrial-mapping
category: cardiac
protocol_type: cardiac gated
last_updated: '2024-01-15'
author: Dr. Kim
synonyms: []
clinical_indications:
- Pre-ablation planning
- Atrial fibrillation
- Pulmonary vein anatomy
position: Supine feet-first
npo: NPO 2-4 hours
premedication: HR < 65 preferred. Premedication not required.
contrast:
  agent: Isovue 370
  volume: 1.1 mL/kg
  flow_rate: 5 mL/s
  duration: 15 sec
  timing: Bolus Tracking
  roi: Left Atrium
  trigger: 200 HU
tech_params:
  kv: '100'
  mas: Auto ECG modulation
  rotation_time: 0.28s
  pitch: 0.2-0.24
series:
- name: Gated CTA
  start: Pulmonary veins
  end: Below LA
  delay: Bolus tracked
  thickness: 0.5 mm
  notes: Retrospective - thin slices critical
- name: Delayed CTA
  start: Pulmonary veins
  end: Below LA
  delay: 40s
  thickness: 0.5 mm
  notes: Retrospective - thin slices critical
recons:
- plane: Axial
  acquisition: Gated CTA
  fov: LA/PV
  thickness_increment: 0.5 mm/0.5 mm
  kernel: Cardiac
  ir_strength: '3'
  notes: Primary PV anatomy
- plane: Coronal
  acquisition: Gated CTA
  fov: LA/PV
  thickness_increment: 0.75 mm
  kernel: Cardiac
  ir_strength: '3'
  notes: PV ostia en face
- plane: Sagittal
  acquisition: Gated CTA
  fov: LA/PV
  thickness_increment: 0.75 mm
  kernel: Cardiac
  ir_strength: '3'
  notes: Lateral PV views
- plane: Axial
  acquisition: Delayed CTA
  fov: LA/PV
  thickness_increment: 0.5 mm/0.5 mm
  kernel: Cardiac
  ir_strength: '3'
  notes: Left Atrial Appendage Thrombus
notes:
  tech: Retrospective gating. Focus on left atrium and pulmonary veins. Thin slices
    critical. Extended coverage for all PV ostia
  nursing: 20G IV
  rad: Map pulmonary vein anatomy (number ostia diameters). Left atrial appendage
    morphology. Esophageal position. LA size
  tips: Thin slices essential. Complete PV coverage. Document variants
  additional_recons: 3D LA reconstruction. PV ostia measurements (diameter area).
    LAA morphology. Esophageal position
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# Gated CTA Heart Left Atrial Mapping

**Last Updated:** 2024-01-15  
**Author:** Dr. Kim

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Flash CTA | Arterial | Carina to Below Heart |
        | Delayed | Delayed (30s)| Carina to Mid Heart |

    === "Clinical Indications"

        - Pre-ablation planning
        - Atrial fibrillation
        - Pulmonary vein anatomy

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet-first
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:**
        - HR < 65 preferred. Premedication not required.

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.1 mL/kg |
        | Flow Rate | 5 mL/s |
        | Duration | 15 sec |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Left Atrium |
        | Trigger (HU) | 200 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Retrospective gating. Focus on left atrium and pulmonary veins. Thin slices critical. Extended coverage for all PV ostia
        - Additional Recons: 3D LA reconstruction. PV ostia measurements (diameter area). LAA morphology. Esophageal position

    === "Nursing Notes"

        - 20G IV

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Map pulmonary vein anatomy (number ostia diameters). Left atrial appendage morphology. Esophageal position. LA size

    === "Tips & Tricks"

        - Thin slices essential. Complete PV coverage. Document variants

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Top of chest | Below heart | N/A | N/A | AP lateral |
    | Gated CTA | Pulmonary veins | Below LA | Bolus tracked | 0.5 mm | Retrospective - thin slices critical |
    | Delayed CTA | Pulmonary veins | Below LA | 40s | 0.5 mm | Retrospective - thin slices critical |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto ECG modulation |
    | Rotation Time | 0.28s |
    | Pitch | 0.2-0.24 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated CTA | LA/PV | 0.5 mm/0.5 mm | Cardiac | 3 | Primary PV anatomy |
    | Coronal | Gated CTA | LA/PV | 0.75 mm | Cardiac | 3 | PV ostia en face |
    | Sagittal | Gated CTA | LA/PV | 0.75 mm | Cardiac | 3 | Lateral PV views |
    | Axial | Delayed CTA | LA/PV | 0.5 mm/0.5 mm | Cardiac | 3 | Left Atrial Appendage Thrombus |
