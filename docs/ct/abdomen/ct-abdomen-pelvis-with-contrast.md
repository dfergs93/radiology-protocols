# CT Abdomen Pelvis with Contrast

**Last Updated:** 2026-01-02  
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Scout/Topogram | Non-contrast | Diaphragm to Pubic symphysis |
        | Portal Venous Phase | Contrast (70 sec delay) | Diaphragm to Pubic symphysis |

    === "Clinical Indications"

        - Abdominal pain
        - Oncology staging
        - Infection source
        - Post-operative complications

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history. Pre-medicate if prior reaction
    
    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours for solids
    - **Pre-Medication:** 
      Oral contrast: 900 mL Readi-Cat 2 over 90 minutes. Last cup 30 min before scan


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 125 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30. Consider split bolus technique if eGFR 30-45



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Ensure adequate oral contrast opacification. Scan from diaphragm through pubic symphysis. 70 second delay typical

    === "Nursing Notes"

        - 18-20G IV required. Verify patent IV. May give rectal contrast for distal colon/rectal evaluation. Oral contrast 900mL given 2 hrs before

    === "Radiologist Notes"
        - Systematic review of all solid organs. Check for free fluid/air. Assess bowel enhancement pattern

    === "Tips & Tricks"

        - Arms raised completely. Remove all metal objects from scan range

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Abdomen Pelvis with Contrast Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (125 mL)    :active, contrast, 00:00, 41s
      Saline (50mL)          :active, saline, after contrast, 16s
      section Portal Venous Phase
      Portal Venous Phase    :done, scan2, 01:10, 25s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Diaphragm | Pubic symphysis | N/A | N/A | AP and lateral |
    | Portal Venous Phase | Diaphragm | Pubic symphysis | 70 sec | 0.625 mm | Standard portal venous timing |

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
    | Axial | Portal venous | Abdomen | 3 mm/3 mm | Standard | 3 | Primary diagnostic series |
    | Axial | Portal venous | Pelvis | 3 mm/3 mm | Standard | 3 | Pelvis diagnostic series |
    | Coronal | Portal venous | Full AP | 3 mm/3 mm | Standard | 3 | Coronal reformats for overview |
    | Sagittal | Portal venous | Full AP | 3 mm/3 mm | Standard | 3 | Sagittal reformats for bowel loops |


### Additional Reconstructions

Thin slice 1mm for 3D if mass identified

Category: Abdomen

Protocol Type: Contrast-Enhanced
