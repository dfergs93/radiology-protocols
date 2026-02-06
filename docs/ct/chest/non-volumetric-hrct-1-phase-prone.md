# Non-Volumetric HRCT 1 Phase Prone

**Last Updated:** 2024-01-15  
**Author:** Dr. Martinez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | HRCT Prone | Contrast (Full inspiration delay) | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Dependent atelectasis vs fibrosis
        - Posterior lung assessment
        - ILD with gravity-dependent changes

-   __2. Patient Prep__

    ---

    - **Position:** Prone with arms extended forward
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Single INSPIRATION. PRONE position. Non-volumetric (1-2cm intervals). Distinguish atelectasis from fibrosis

    === "Nursing Notes"

        - Position patient prone safely. Cushion support. Breath hold coaching

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Differentiate dependent atelectasis from true fibrosis. Posterior lung better aerated prone

    === "Tips & Tricks"

        - Safe prone positioning. Compare to supine if available

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Non-Volumetric HRCT 1 Phase Prone Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout Prone | Lung apices | Costophrenic angles | N/A | N/A | Lateral |
    | HRCT Prone | Lung apices | Costophrenic angles | Full inspiration | 1 mm at 1-2cm intervals | Sequential prone |

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
    | Axial | HRCT prone | Chest | 1 mm display | Lung | 3 | Prone images |
    | Coronal | HRCT prone | Chest | 2 mm | Lung | 3 | Coronal prone |
    | Compare | Supine vs prone | Posterior lungs | 1 mm | Lung | 3 | Dependent changes |


### Additional Reconstructions

Compare prone to supine to differentiate atelectasis from fibrosis

Category: Chest

Protocol Type: Chest/Pulmonary
