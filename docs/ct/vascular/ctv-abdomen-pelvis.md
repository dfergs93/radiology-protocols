# CTV Abdomen Pelvis

**Last Updated:** 2024-01-15  
**Author:** Dr. Chen

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTV Venous Phase | Contrast (180 sec delay) | Diaphragm to Proximal femur |

    === "Clinical Indications"

        - Deep vein thrombosis
        - May-Thurner syndrome
        - IVC filter placement planning
        - Venous malformation

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history
    
    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:** 
      Oral contrast optional


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 125 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Scan at 180 seconds for venous phase. Slower injection rate OK for venous imaging. Scan from diaphragm to femoral veins

    === "Nursing Notes"

        - 18-20G IV

    === "Radiologist Notes"
        - Assess IVC iliac femoral veins for thrombosis. Look for compression (May-Thurner). Measure vessel caliber for filter sizing

    === "Tips & Tricks"

        - Arms raised. May add leg veins if DVT suspected

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CTV Abdomen Pelvis Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (125 mL)    :active, contrast, 00:00, 41s
      Saline (50mL)          :active, saline, after contrast, 16s
      section Portal Venous Phase
      CTV Venous Phase    :done, scan1, 03:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Diaphragm | Proximal femur | N/A | N/A | AP |
    | CTV Venous Phase | Diaphragm | Proximal femur | 180 sec | 0.625 mm | Extended delay for venous opacification |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.375 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Venous | Full AP | 2.5 mm/2.5 mm | Standard | 3 | Assess for filling defects |
    | Coronal | Venous | Full AP | 3 mm/3 mm | Standard | 3 | MIP of venous system |
    | Sagittal | Venous | Full AP | 3 mm/3 mm | Standard | 3 | IVC and iliac veins |
    | 3D VR | Venous | Full AP | 2 mm source | Standard | 3 | 3D venous anatomy |


### Additional Reconstructions

MIP venograms. 3D VR of venous system

Category: Vascular

Protocol Type: Vascular
