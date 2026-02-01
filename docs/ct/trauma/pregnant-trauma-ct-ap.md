# Pregnant Trauma CT AP

**Last Updated:** 2024-01-15  
**Author:** Dr. Anderson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Portal Venous AP | Contrast (70 sec delay) | Diaphragm to Pubic symphysis |

    === "Clinical Indications"

        - Pregnant trauma patient
        - Multi-trauma pregnancy
        - Maternal injury assessment

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Check if known
        - **Allergy:** Trauma indication documented
    
    - **Position:** Supine with left lateral tilt if possible
    - **NPO Status:** None - trauma
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 125 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        
        Proceed with trauma indication. Document medical necessity and gestational age



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Portal venous phase 70s. SINGLE PHASE to minimize fetal radiation. Shield uterus if injury distant. Document weeks gestation

    === "Nursing Notes"

        - Pregnancy documented. Fetal heart tones if equipment available. Shield if possible

    === "Radiologist Notes"
        - Assess maternal injuries. Minimize fetal radiation exposure. Document placental injury if visible

    === "Tips & Tricks"

        - Document gestational age. Shield fetus if possible. Minimize radiation

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Pregnant Trauma CT AP Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (125 mL)    :active, contrast, 00:00, 41s
      Saline (50mL)          :active, saline, after contrast, 16s
      section Portal Venous Phase
      Portal Venous AP    :done, scan1, 01:10, 25s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Pubic symphysis | N/A | N/A | Low dose scout |
    | Portal Venous AP | Diaphragm | Pubic symphysis | 70 sec | 2.5 mm | Single phase minimize radiation |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Reduced mAs if possible |
    | Rotation Time | 0.5s |
    | Pitch | 1.375 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Portal venous | AP | 2.5 mm/2.5 mm | Standard | 3 | Maternal organs |
    | Coronal | Portal venous | AP | 3 mm/3 mm | Standard | 3 | Overview |
    | Sagittal | Portal venous | Pelvis | 3 mm/3 mm | Standard | 3 | Uterus and placenta |


Category: Trauma

Protocol Type: Trauma
