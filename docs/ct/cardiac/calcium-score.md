# Calcium Score

**Last Updated:** 2024-01-15  
**Author:** Dr. Smith

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Calcium Score | Contrast (Prospective 75% delay) | Carina to Below heart |

    === "Clinical Indications"

        - Cardiovascular risk assessment
        - Chest pain low-intermediate risk
        - Asymptomatic screening

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A
        - **Allergy:** N/A
    
    - **Position:** Supine feet-first
    - **NPO Status:** NPO not required
    - **Pre-Medication:** 
      HR control not needed for calcium score


-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Prospective ECG gating. 3mm slices. Cover entire heart. 75% R-R interval typical. Ensure ECG leads well connected

    === "Nursing Notes"

        - No IV needed. Apply ECG leads carefully. Explain breath hold

    === "Radiologist Notes"
        - Calculate Agatston score. Report percentile for age/sex. Document coronary calcification distribution

    === "Tips & Tricks"

        - Good ECG tracing essential. Patient breath hold coaching

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Calcium Score Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Top of chest | Diaphragm | N/A | N/A | AP and lateral |
    | Calcium Score | Carina | Below heart | Prospective 75% | 3 mm | Sequential axial gated acquisition |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (low dose) |
    | Rotation Time | 0.28-0.35s |
    | Pitch | Sequential |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Calcium score | Heart | 3 mm/3 mm | Standard | 3 | For Agatston score calculation |
    | Axial | Calcium score | Heart | 3 mm/3 mm | Standard | 3 | Duplicate for quality control |
    | Curved MPR | Calcium score | Coronaries | 3 mm | Standard | 3 | Optional vessel-specific views |


### Additional Reconstructions

Agatston score calculation. Percentile reporting

Category: Cardiac

Protocol Type: Non-Contrast
