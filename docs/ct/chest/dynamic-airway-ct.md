# Dynamic Airway CT

**Last Updated:** 2024-01-15  
**Author:** Dr. Lee

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Inspiration | Contrast (Full inspiration delay) | Thoracic inlet to Carina+10cm |
        | Mid-Expiration | Contrast (Forced mid-expiration delay) | Thoracic inlet to Carina+10cm |
        | Cine (optional) | Contrast (Continuous breathing delay) | Carina level to Single slice |

    === "Clinical Indications"

        - Tracheomalacia
        - Bronchomalacia
        - Expiratory central airway collapse
        - EDAC

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

        - TWO acquisitions: 1) INSPIRATION carina to carina+10cm 2) MID-EXPIRATION same level. Cine if available. Airway reconstructions required

    === "Nursing Notes"

        - No IV. Coach dynamic breathing. May need forced expiration

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Measure tracheal collapse percentage. >50% collapse suggests tracheomalacia. Assess bronchi

    === "Tips & Tricks"

        - Coach forced expiration. Exact same level both phases

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Dynamic Airway CT Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Thoracic inlet | Carina+10cm | N/A | N/A | Lateral |
    | Inspiration | Thoracic inlet | Carina+10cm | Full inspiration | 0.625-1 mm | Thin for 3D |
    | Mid-Expiration | Thoracic inlet | Carina+10cm | Forced mid-expiration | 0.625-1 mm | Same level as inspiration |
    | Cine (optional) | Carina level | Single slice | Continuous breathing | Cine mode | Dynamic collapse |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Both phases | Airway | 1-2 mm/1 mm | Lung | 3 | Axial airway |
    | Coronal | Both phases | Airway | 1.5 mm | Lung | 3 | Coronal airway |
    | Sagittal | Both phases | Airway | 1.5 mm | Lung | 3 | Sagittal airway |
    | 3D VR | Both phases | Airway | 0.625-1 mm source | Lung | N/A | 3D airway reconstruction |


### Additional Reconstructions

Measure tracheal AP diameter inspiration vs expiration. Calculate collapse percentage. 3D airway

Category: Chest

Protocol Type: Non-Contrast
