# Quantitative Lung Density CT

**Last Updated:** 2024-01-15  
**Author:** Dr. Patel

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Volumetric Inspiration | Contrast (Full inspiration (TLC) delay) | Lung apices to Costophrenic angles |
        | Volumetric Expiration | Contrast (Full expiration (RV) delay) | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Emphysema quantification
        - COPD assessment
        - Alpha-1 antitrypsin deficiency
        - Pre-LVRS

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

        - TWO VOLUMETRIC acquisitions: 1) Full INSPIRATION 2) FULL EXPIRATION (complete exhalation). Contiguous thin slices. Quantitative software

    === "Nursing Notes"

        - No IV. Coach complete inspiration and complete expiration

    === "Radiologist Notes"
        - Quantify emphysema (% lung <-950 HU inspiration). Air trapping (% lung <-856 HU expiration). Emphysema distribution

    === "Tips & Tricks"

        - Complete exhalation critical for RV. Volumetric contiguous

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Quantitative Lung Density CT Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | AP lateral |
    | Volumetric Inspiration | Lung apices | Costophrenic angles | Full inspiration (TLC) | 0.625-1 mm | Contiguous for quantification |
    | Volumetric Expiration | Lung apices | Costophrenic angles | Full expiration (RV) | 0.625-1 mm | Contiguous complete exhalation |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 150-200) |
    | Rotation Time | 0.5s |
    | Pitch | 1 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Inspiration | Chest | 1 mm/1 mm | Lung | 3 | Quantitative inspiration |
    | Axial | Expiration | Chest | 1 mm/1 mm | Lung | 3 | Quantitative expiration |
    | Density map | Inspiration | Lungs | Color coded | Lung | N/A | Emphysema distribution map |
    | Density map | Expiration | Lungs | Color coded | Lung | N/A | Air trapping map |


### Additional Reconstructions

Quantitative emphysema analysis. Report % lung <-950 HU. Air trapping metrics. Upper/lower lobe distribution

Category: Chest

Protocol Type: Chest/Pulmonary
