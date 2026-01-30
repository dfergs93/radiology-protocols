# Non-Volumetric HRCT 3 Respiratory Phases

**Last Updated:** 2024-01-15  
**Author:** Dr. Hayes

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Inspiration | Contrast (Full inspiration delay) | Lung apices to Costophrenic angles |
        | Mid-Expiration | Contrast (Mid-expiration delay) | Lung apices to Costophrenic angles |
        | Full Expiration | Contrast (Full expiration delay) | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Air trapping assessment
        - Small airways disease
        - Constrictive bronchiolitis
        - Hypersensitivity pneumonitis

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A
        - **Allergy:** N/A
    
    - **Position:** Supine with arms raised
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - THREE acquisitions: 1) INSPIRATION 2) MID-EXPIRATION 3) FULL EXPIRATION. Non-volumetric (1-2cm intervals). Lower dose than volumetric

    === "Nursing Notes"

        - No IV. Coach three breathing phases carefully

    === "Radiologist Notes"
        - Mosaic attenuation. Air trapping. Small airways disease. Compare three phases

    === "Tips & Tricks"

        - Coach three distinct breath holds. Non-volumetric lower dose

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Non-Volumetric HRCT 3 Respiratory Phases Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | AP |
    | Inspiration | Lung apices | Costophrenic angles | Full inspiration | 1 mm axial at 1-2cm intervals | Sequential non-volumetric |
    | Mid-Expiration | Lung apices | Costophrenic angles | Mid-expiration | 1 mm at intervals | Sequential |
    | Full Expiration | Lung apices | Costophrenic angles | Full expiration | 1 mm at intervals | Sequential |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Reduced (100-150 reference) |
    | Rotation Time | Sequentials |
    | Pitch | N/A |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | All phases | Chest | 1 mm display | Lung | 3 | Compare three phases |
    | Coronal reformat | Inspiration | Chest | 2 mm | Lung | 3 | Inspiration overview |
    | Mosaic MIP | All phases | Lungs | 5 mm | Lung | N/A | Air trapping visualization |


### Additional Reconstructions

Side-by-side comparison of three phases. Quantify air trapping

Category: Chest

Protocol Type: Chest/Pulmonary
