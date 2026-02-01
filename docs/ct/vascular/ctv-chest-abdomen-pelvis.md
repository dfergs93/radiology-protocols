# CTV Chest Abdomen Pelvis

**Last Updated:** 2024-01-15  
**Author:** Dr. White

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTV Venous Phase | Contrast (180 sec delay) | Thoracic inlet to Proximal femur |

    === "Clinical Indications"

        - Superior vena cava syndrome
        - Central venous occlusion
        - Tumor staging with venous involvement

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history. May need bilateral IVs
    
    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 2-4 hours
    

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

        - Scan at 180 seconds. Include SVC through femoral veins. May need arm injection for SVC assessment

    === "Nursing Notes"

        - 18-20G IV - may need bilateral arm IVs for SVC

    === "Radiologist Notes"
        - Assess SVC IVC and major tributaries. Look for thrombosis compression or tumor invasion

    === "Tips & Tricks"

        - Arms raised. For SVC consider bilateral arm injection

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CTV Chest Abdomen Pelvis Timeline
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
    | Scout/Topogram | Thoracic inlet | Proximal femur | N/A | N/A | AP full body |
    | CTV Venous Phase | Thoracic inlet | Proximal femur | 180 sec | 0.625 mm | Extended venous phase |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.2 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Venous | Chest | 2 mm/2 mm | Standard | 3 | SVC and central veins |
    | Axial | Venous | Abdomen/Pelvis | 2.5 mm/2.5 mm | Standard | 3 | IVC and tributaries |
    | Coronal | Venous | Full CAP | 3 mm/3 mm | Standard | 3 | MIP full venous system |
    | Sagittal | Venous | Full CAP | 3 mm/3 mm | Standard | 3 | Sagittal venogram |


### Additional Reconstructions

3D venogram MIP. Curved MPR of SVC and IVC

Category: Vascular

Protocol Type: Vascular
