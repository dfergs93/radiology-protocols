# Non-Contrast Chest Lung Nodule Ultra Low Dose

**Last Updated:** 2024-01-15  
**Author:** Dr. Rodriguez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Ultra Low Dose Chest | Non-contrast | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Pulmonary nodule follow-up
        - Known nodule surveillance
        - Post-treatment monitoring

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

        - ULTRA LOW DOSE 10-20% standard dose. For follow-up of KNOWN nodules only. Not for initial detection. Maximum IR

    === "Nursing Notes"

        - No IV. Known nodule follow-up only

    === "Radiologist Notes"
        - Follow known nodules. Compare to prior. Measure size. Not for initial detection

    === "Tips & Tricks"

        - Ultra low dose. Maximum IR. Prior comparison essential

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Non-Contrast Chest Lung Nodule Ultra Low Dose Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | Ultra low dose |
    | Ultra Low Dose Chest | Lung apices | Costophrenic angles | N/A | 1-1.25 mm | Ultra low dose helical |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Ultra low (20-30 reference) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.2 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Chest | Chest | 1.25 mm/1.25 mm | Lung | Maximum IR 5 | Nodule follow-up |
    | Axial | Chest | Chest | 2.5 mm/2.5 mm | Standard | High IR | Mediastinal |
    | Coronal | Chest | Chest | 2 mm/2 mm | Lung | Maximum IR | Coronal |


Category: Chest

Protocol Type: Chest/Pulmonary
