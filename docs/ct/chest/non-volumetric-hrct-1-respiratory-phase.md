# Non-Volumetric HRCT 1 Respiratory Phase

**Last Updated:** 2024-01-15  
**Author:** Dr. Chen

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | HRCT Inspiration | Contrast (Full inspiration delay) | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - HRCT follow-up
        - Known ILD monitoring
        - Bronchiectasis assessment

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Single INSPIRATION phase. Non-volumetric (1-2cm intervals). Lower dose for follow-up

    === "Nursing Notes"

        - No IV. Single inspiration breath hold

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Follow ILD changes. Bronchiectasis. Lower radiation than volumetric

    === "Tips & Tricks"

        - Non-volumetric reduces dose. Good for follow-up

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Non-Volumetric HRCT 1 Respiratory Phase Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | AP |
    | HRCT Inspiration | Lung apices | Costophrenic angles | Full inspiration | 1 mm at 1-2cm intervals | Sequential slices |

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
    | Axial | HRCT | Chest | 1 mm display | Lung | 3 | HRCT images |
    | Coronal | HRCT | Chest | 2 mm | Lung | 3 | Coronal overview |
    | Targeted | HRCT | Area of interest | 1 mm | Lung | 3 | Focus on abnormality |


### Additional Reconstructions

Target slices through abnormality. Compare to prior

Category: Chest

Protocol Type: Chest/Pulmonary
