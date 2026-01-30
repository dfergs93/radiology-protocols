# Non-Contrast CT Chest Routine

**Last Updated:** 2024-01-15  
**Author:** Dr. Thompson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Chest | Non-contrast | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Pulmonary nodule
        - Interstitial lung disease screening
        - Chest pain low risk
        - Follow-up

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

        - Standard dose helical chest. Lung apices to costophrenic angles. Routine lung and mediastinal windows

    === "Nursing Notes"

        - No IV needed. Breath hold coaching

    === "Radiologist Notes"
        - Assess lung parenchyma nodules masses. Mediastinal lymph nodes. Pleura. Incidental findings

    === "Tips & Tricks"

        - Full inspiration breath hold

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Non-Contrast CT Chest Routine Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | AP and lateral |
    | NC Chest | Lung apices | Costophrenic angles | N/A | 1-1.25 mm | Standard dose helical |

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
    | Axial | Chest | Chest | 2.5 mm/2.5 mm | Standard | 3 | Mediastinal window |
    | Axial | Chest | Chest | 2.5 mm/2.5 mm | Lung | 3 | Lung window |
    | Coronal | Chest | Chest | 3 mm/3 mm | Lung | 3 | Coronal lung |
    | Sagittal | Chest | Chest | 3 mm/3 mm | Standard | 3 | Optional mediastinum |


### Additional Reconstructions

Thin slice 1mm for nodule detection and measurement

Category: Chest

Protocol Type: Non-Contrast
