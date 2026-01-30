# CTA Chest

**Last Updated:** 2024-01-15  
**Author:** Dr. Johnson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Scout/Topogram | Non-contrast | Lung apices to Adrenal glands |
        | CTA Arterial Chest | Arterial (bolus tracked) | Lung apices to Adrenal glands |

    === "Clinical Indications"

        - Thoracic aortic aneurysm
        - Aortic dissection
        - Great vessel evaluation

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history
    
    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 2 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 100 mL |
        | Flow Rate | 4 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta or main PA |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Choose ROI based on indication - ascending aorta for aortic pathology or main PA for PE

    === "Nursing Notes"

        - 20G IV minimum

    === "Radiologist Notes"
        - Assess aorta and great vessels. Measure aneurysm if present. Look for dissection flap

    === "Tips & Tricks"

        - Arms fully raised

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CTA Chest Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (100 mL)    :active, contrast, 00:00, 25s
      Saline (50mL)          :active, saline, after contrast, 12s
      section Arterial Phase
      CTA Arterial Chest    :crit, scan2, 00:25, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Lung apices | Adrenal glands | N/A | N/A | AP and lateral |
    | CTA Arterial Chest | Lung apices | Adrenal glands | Bolus tracked | 0.625 mm | Caudocranial direction |

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
    | Axial | Arterial | Chest | 1.25 mm/1.25 mm | Vascular | 3 | Primary diagnostic series |
    | Axial | Arterial | Chest | 2.5 mm/2.5 mm | Lung | 3 | Lung window for parenchyma |
    | Coronal | Arterial | Chest | 2.5 mm/2.5 mm | Vascular | 3 | MIP coronal great vessels |
    | Sagittal | Arterial | Chest | 2.5 mm/2.5 mm | Vascular | 3 | MIP sagittal aortic arch |


### Additional Reconstructions

3D VR of thoracic vasculature

Category: Vascular

Protocol Type: Vascular
