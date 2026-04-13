---
author: ''
category: vascular
clinical_indications:
- Suspected pulmonary embolism
- Acute dyspnea
- Chest pain with elevated D-dimer
contrast:
  agent: Isovue 370
  duration: 15 - 20s
  flow_rate: 5 mL/s
  roi: Main Pulmonary Artery
  timing: Bolus Tracking
  trigger: 100 HU
  volume: 1.3 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: MIP reconstructions of pulmonary arteries
  nursing: 20G or larger IV in antecubital preferred. Verify good flow before injection
  rad: Assess RV/LV ratio. Look for signs of right heart strain. Check for DVT in
    leg veins if imaged
  tech: Caudocranial scan direction. Coach breath hold. ROI in main PA at level of
    bifurcation
  tips: Arms fully raised to reduce beam hardening
npo: NPO 2 hours recommended
position: Supine feet-first with arms raised
premedication: None required
protocol_type: contrast-enhanced
recons:
- acquisition: Angiogram
  fov: Chest
  ir_strength: '3'
  kernel: Standard
  notes: Mediastinal window for PE assessment
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Angiogram
  fov: Chest
  ir_strength: '3'
  kernel: Lung
  notes: Lung window for parenchymal assessment
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Angiogram
  fov: Chest
  ir_strength: '3'
  kernel: Standard
  notes: Overview of pulmonary vasculature
  plane: Coronal
  thickness_increment: 3 mm/3 mm
- acquisition: Angiogram
  fov: Chest
  ir_strength: '3'
  kernel: Standard
  notes: Optional for clinical correlation
  plane: Sagittal
  thickness_increment: 3 mm/3 mm
safety:
  allergy: Check iodine allergy history and prior reactions
  renal: Verify eGFR > 30
series:
- delay: Bolus tracked
  end: Adrenal glands
  name: Pulmonary Angiogram
  notes: Caudocranial direction from diaphragm to apices
  start: Lung apices
  thickness: 0.625 mm
slug: ct-pulmonary-embolism
synonyms: []
tech_params:
  kv: '100'
  mas: Auto (reference 200)
  pitch: 1.0-1.2
  rotation_time: 0.5s
title: CT Pulmonary Embolism
---

# CT Pulmonary Embolism

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Pulmonary Angiogram | Bolus tracked | Lung apices → Adrenal glands |

    === "Clinical Indications"

        - Suspected pulmonary embolism
        - Acute dyspnea
        - Chest pain with elevated D-dimer

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet-first with arms raised
    - **NPO Status:** NPO 2 hours recommended
    - **Pre-Medication:**
        - None required

-   __3. IV Contrast & Injection__

    ---
    === "Injection Parameters"

        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.3 mL/kg |
        | Flow Rate | 5 mL/s |
        | Duration | 15 - 20s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Main Pulmonary Artery |
        | Trigger (HU) | 100 HU |

    === "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Caudocranial scan direction. Coach breath hold. ROI in main PA at level of bifurcation

    === "Nursing Notes"

        - 20G or larger IV in antecubital preferred. Verify good flow before injection

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check iodine allergy history and prior reactions

    === "Radiologist Notes"

        - Assess RV/LV ratio. Look for signs of right heart strain. Check for DVT in leg veins if imaged

    === "Tips & Tricks"

        - Arms fully raised to reduce beam hardening

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Pulmonary Angiogram | Lung apices | Adrenal glands | Bolus tracked | 0.625 mm | Caudocranial direction from diaphragm to apices |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angiogram | Chest | 1.25 mm/1.25 mm | Standard | 3 | Mediastinal window for PE assessment |
    | Axial | Angiogram | Chest | 2.5 mm/2.5 mm | Lung | 3 | Lung window for parenchymal assessment |
    | Coronal | Angiogram | Chest | 3 mm/3 mm | Standard | 3 | Overview of pulmonary vasculature |
    | Sagittal | Angiogram | Chest | 3 mm/3 mm | Standard | 3 | Optional for clinical correlation |
