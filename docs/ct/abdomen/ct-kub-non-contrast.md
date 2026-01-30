# CT KUB Non-Contrast

**Last Updated:** 2024-01-15  
**Author:** Dr. Johnson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast KUB | Non-contrast | Top of kidneys to Pubic symphysis |

    === "Clinical Indications"

        - Nephrolithiasis
        - Renal colic
        - Flank pain
        - Hematuria

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A
        - **Allergy:** N/A
    
    - **Position:** Supine with arms raised
    - **NPO Status:** None required
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - LOW DOSE protocol. Reduced mAs. Cover kidneys to pubic symphysis. Stone protocol settings

    === "Nursing Notes"

        - No IV needed. No oral contrast. Explain low radiation technique

    === "Radiologist Notes"
        - Look for stones - measure size and location. Check for hydronephrosis. Assess for alternative diagnoses

    === "Tips & Tricks"

        - Low dose protocol. Reduced mAs. Image quality adequate for stones

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT KUB Non-Contrast Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Top of kidneys | Pubic symphysis | N/A | N/A | AP scout |
    | Non-Contrast KUB | Top of kidneys | Pubic symphysis | N/A | 1-2 mm | Low dose technique |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Low dose (50-100 ref) |
    | Rotation Time | 0.5s |
    | Pitch | 1.375-1.5 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Non-contrast | KUB | 2.5 mm/2.5 mm | Standard | 3 | Stone detection |
    | Axial | Non-contrast | KUB | 2.5 mm/2.5 mm | Bone | N/A | Bone window for stones |
    | Coronal | Non-contrast | KUB | 3 mm/3 mm | Standard | 3 | Coronal stone overview |
    | MIP | Non-contrast | Kidneys/ureters | 5 mm slab | Standard | N/A | Stone localization |


### Additional Reconstructions

Thin slice 1mm for small stones. Stone size measurements

Category: Abdomen

Protocol Type: Non-Contrast
