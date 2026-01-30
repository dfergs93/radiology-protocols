# CT Chest Abdomen Pelvis with Contrast

**Last Updated:** 2024-01-15  
**Author:** Dr. Smith

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Scout/Topogram | Non-contrast | Thoracic inlet to Pubic symphysis |
        | Portal Venous Phase | Contrast (70 sec delay) | Lung bases or diaphragm to Pubic symphysis |

    === "Clinical Indications"

        - Oncology staging
        - Infection source
        - Abdominal pain
        - Trauma

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history
    
    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours solids. Clear liquids OK up to 2 hours
    - **Pre-Medication:** 
      Oral contrast: 250-500 mL neutral (Volumen or water). Give 60-90 min before scan


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 3-4 mL/s |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30. High volume protocol



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Single phase portal venous. Oral contrast for bowel opacification. 40 second injection. 70 second scan delay from start of injection

    === "Nursing Notes"

        - 18-20G IV. Adequate oral contrast intake. Verify renal function

    === "Radiologist Notes"
        - Portal venous phase optimal for solid organ and bowel assessment. Systematic review all organs

    === "Tips & Tricks"

        - Arms fully raised. Neutral oral contrast preferred over positive

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Chest Abdomen Pelvis with Contrast Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.5 mL/kg)    :active, contrast, 00:00, 30s
      Saline (50mL)          :active, saline, after contrast, 14s
      section Portal Venous Phase
      Portal Venous Phase    :done, scan2, 01:10, 25s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Thoracic inlet | Pubic symphysis | N/A | N/A | AP and lateral |
    | Portal Venous Phase | Lung bases or diaphragm | Pubic symphysis | 70 sec | 0.625 mm | Single portal venous phase |

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
    | Axial | Portal venous | Chest | 2.5 mm/2.5 mm | Standard | 3 | Chest diagnostic |
    | Axial | Portal venous | Abdomen | 2.5 mm/2.5 mm | Standard | 3 | Abdomen diagnostic |
    | Axial | Portal venous | Pelvis | 3 mm/3 mm | Standard | 3 | Pelvis diagnostic |
    | Coronal | Portal venous | Full CAP | 3 mm/3 mm | Standard | 3 | Coronal overview |


### Additional Reconstructions

Sagittal reformats optional

Category: Abdomen

Protocol Type: Contrast-Enhanced
