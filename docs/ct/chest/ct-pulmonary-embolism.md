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
        | Scout/Topogram | Non-contrast | Lung apices to Adrenal glands |
        | Pulmonary Angiogram | Arterial (bolus tracked) | Lung apices to Adrenal glands |

    === "Clinical Indications"

        - Suspected pulmonary embolism
        - Acute dyspnea
        - Chest pain with elevated D-dimer

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check iodine allergy history and prior reactions
    
    - **Position:** Supine feet-first with arms raised
    - **NPO Status:** NPO 2 hours recommended
    - **Pre-Medication:** 
      None required


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 100 mL |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Main Pulmonary Artery |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30. Reduce if eGFR 30-60



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Caudocranial scan direction. Coach breath hold. ROI in main PA at level of bifurcation

    === "Nursing Notes"

        - 20G or larger IV in antecubital preferred. Verify good flow before injection

    === "Radiologist Notes"
        - Assess RV/LV ratio. Look for signs of right heart strain. Check for DVT in leg veins if imaged

    === "Tips & Tricks"

        - Arms fully raised to reduce beam hardening

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Pulmonary Embolism Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (100 mL)    :active, contrast, 00:00, 22s
      Saline (50mL)          :active, saline, after contrast, 11s
      section Scan Phase 2
      Pulmonary Angiogram    :crit, scan2, 00:25, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Lung apices | Adrenal glands | N/A | N/A | AP and lateral |
    | Pulmonary Angiogram | Lung apices | Adrenal glands | Bolus tracked | 0.625 mm | Caudocranial direction from diaphragm to apices |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.2 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angiogram | Chest | 1.25 mm/1.25 mm | Standard | 3 | Mediastinal window for PE assessment |
    | Axial | Angiogram | Chest | 2.5 mm/2.5 mm | Lung | 3 | Lung window for parenchymal assessment |
    | Coronal | Angiogram | Chest | 3 mm/3 mm | Standard | 3 | Overview of pulmonary vasculature |
    | Sagittal | Angiogram | Chest | 3 mm/3 mm | Standard | 3 | Optional for clinical correlation |


### Additional Reconstructions

MIP reconstructions of pulmonary arteries

Category: Chest

Protocol Type: Contrast-Enhanced
