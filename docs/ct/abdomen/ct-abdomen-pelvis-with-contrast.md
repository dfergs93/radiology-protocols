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
        | Portal Venous Phase | Contrast (70 sec delay) | Diaphragm to Pubic symphysis |

    === "Clinical Indications"

        - Abdominal pain
        - Oncology staging
        - Infection source
        - Post-operative complications

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours for solids
    - **Pre-Medication:**
        - Oral contrast: 900 mL Readi-Cat 2 over 90 minutes. Last cup 30 min before scan

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 125 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Ensure adequate oral contrast opacification. Scan from diaphragm through pubic symphysis. 70 second delay typical

    === "Nursing Notes"

        - 18-20G IV required. Verify patent IV. May give rectal contrast for distal colon/rectal evaluation. Oral contrast 900mL given 2 hrs before

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history. Pre-medicate if prior reaction

    === "Radiologist Notes"

        - Systematic review of all solid organs. Check for free fluid/air. Assess bowel enhancement pattern

    === "Tips & Tricks"

        - Arms raised completely. Remove all metal objects from scan range

</div>


### Protocol Details
  ```mermaid
  ---
  displayMode: compact
  config:
    theme: default
    themeCSS: " #Saline{ fill: #4ed5ff; stroke: #2094f3; } "
  ---
    gantt
      title CT Abdomen Pelvis with Contrast Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (125 mL)    :active, contrast, 00:00, 41s
      Saline          :active, saline, after contrast, 6s
      section Other
      Portal Venous Phase    :done, scan1, 01:10, 7s
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
