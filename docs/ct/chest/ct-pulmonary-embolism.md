---
title: CT Pulmonary Embolism
slug: ct-pulmonary-embolism
category: chest
protocol_type: contrast-enhanced
last_updated: '2026-01-01'
author: ''
synonyms: []
clinical_indications:
- Suspected pulmonary embolism
- Acute dyspnea
- Chest pain with elevated D-dimer
position: Supine feet-first with arms raised
npo: NPO 2 hours recommended
premedication: None required
contrast:
  agent: Isovue 370
  volume: 1.3 mL/kg
  flow_rate: 5 mL/s
  duration: 15 - 20s
  timing: Bolus Tracking
  roi: Main Pulmonary Artery
  trigger: 100 HU
tech_params:
  kv: '100'
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: 1.0-1.2
series:
- name: Pulmonary Angiogram
  start: Lung apices
  end: Adrenal glands
  delay: Bolus tracked
  thickness: 0.625 mm
  notes: Caudocranial direction from diaphragm to apices
recons:
- plane: Axial
  acquisition: Angiogram
  fov: Chest
  thickness_increment: 1.25 mm/1.25 mm
  kernel: Standard
  ir_strength: '3'
  notes: Mediastinal window for PE assessment
- plane: Axial
  acquisition: Angiogram
  fov: Chest
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Lung
  ir_strength: '3'
  notes: Lung window for parenchymal assessment
- plane: Coronal
  acquisition: Angiogram
  fov: Chest
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Overview of pulmonary vasculature
- plane: Sagittal
  acquisition: Angiogram
  fov: Chest
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Optional for clinical correlation
notes:
  tech: Caudocranial scan direction. Coach breath hold. ROI in main PA at level of
    bifurcation
  nursing: 20G or larger IV in antecubital preferred. Verify good flow before injection
  rad: Assess RV/LV ratio. Look for signs of right heart strain. Check for DVT in
    leg veins if imaged
  tips: Arms fully raised to reduce beam hardening
  additional_recons: MIP reconstructions of pulmonary arteries
safety:
  renal: Verify eGFR > 30
  allergy: Check iodine allergy history and prior reactions
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
        | Pulmonary Angiogram | Arterial (bolus tracked) | Lung apices to Costophrenic Angles |

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
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.3 mL/kg |
        | Flow Rate | 5 mL/s |
        | Duration | 15 - 20s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Main Pulmonary Artery |
        | Trigger (HU) | 100 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Caudocranial scan direction. Coach breath hold. ROI in main PA at level of bifurcation
        - Additional Recons: MIP reconstructions of pulmonary arteries

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
    | Scout/Topogram | Lung apices | Adrenal glands | N/A | N/A | AP and lateral |
    | Pulmonary Angiogram | Lung apices | Adrenal glands | Bolus tracked | 0.625 mm | Caudocranial direction from diaphragm to apices |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angiogram | Chest | 1.25 mm/1.25 mm | Standard | 3 | Mediastinal window for PE assessment |
    | Axial | Angiogram | Chest | 2.5 mm/2.5 mm | Lung | 3 | Lung window for parenchymal assessment |
    | Coronal | Angiogram | Chest | 3 mm/3 mm | Standard | 3 | Overview of pulmonary vasculature |
    | Sagittal | Angiogram | Chest | 3 mm/3 mm | Standard | 3 | Optional for clinical correlation |
