# Calcium Score

**Last Updated:** 2026-02-02  
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Calcium Score | Non-contrast | Carina to Below heart |

    === "Clinical Indications"

        - Cardiovascular risk assessment
        - Chest pain low-intermediate risk
        - Asymptomatic screening
        - Elevated HLD
        - Significant cardiovascular risk factors

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet-first
    - **NPO Status:** No caffeine day of exam
    - **Pre-Medication:**
        - HR control not needed for calcium score

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Prospective ECG gating.
        - Suspended Respiration breathing instructions.
        - For single source CT: Target End Diastole if HR < 63BPM, else target End diastole and end systole. For dual source CT: Target End diastole if HR <79, else target end systole. Ensure ECG leads well connected, Goal: <= 60 BPM, regular (+/- 5).

    === "Nursing Notes"

        - No IV needed.

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Check breathing motion on lung FOV. Calculate Agatston score. Report percentile for age/sex. Document coronary calcification distribution

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
    | Calcium Score | Carina | Below heart | N/A | 1.5 mm | Sequential axial gated acquisition |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (low dose) |
    | Rotation Time | 0.28-0.35s |
    | Pitch | 1.0-1.2 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Calcium score | Heart | 3 mm/3 mm | Standard | 3 | For Agatston score calculation |
    | Axial | Calcium score | Chest | 1.5 mm/1.5 mm | Lung | 3 | Lung FOV for Extracardiac findings |


### Additional Reconstructions

Agatston score calculation. Percentile reporting

Category: Cardiac

Protocol Type: Non-Contrast
