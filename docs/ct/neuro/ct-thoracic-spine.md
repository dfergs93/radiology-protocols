# CT Thoracic Spine

**Last Updated:** 2024-01-15  
**Author:** Dr. White

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | T-spine Helical | Contrast (N/A or 60s if contrast delay) | C7 to L1 |

    === "Clinical Indications"

        - Thoracic spine trauma
        - Compression fracture
        - Back pain
        - Tumor
        - Infection

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A or verify eGFR
        - **Allergy:** N/A or check allergy
    
    - **Position:** Supine
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection/tumor |
        | Volume | If contrast: 100 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        
        NC typical. Contrast for infection tumor mets



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - C7 to L1. Submillimeter helical. Sagittal and coronal reformats. Arms up if possible

    === "Nursing Notes"

        - No IV unless contrast indicated. Arms up to reduce artifact

    === "Radiologist Notes"
        - Alignment. Compression fractures. Pedicles. Spinal canal. Disc spaces. Paraspinal soft tissues

    === "Tips & Tricks"

        - Arms up reduces artifact. Bone algorithm

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Thoracic Spine Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 100 mL)    :active, contrast, 00:00, 33s
      Saline (50mL)          :active, saline, after contrast, 16s
      section Scan Phase 2
      T-spine Helical    :done, scan2, 01:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | C7 | L1 | N/A | N/A | AP and lateral |
    | T-spine Helical | C7 | L1 | N/A or 60s if contrast | 0.625-1 mm | Submillimeter |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | T-spine | T-spine | 2 mm/2 mm | Bone | 3 | Bone and soft tissue |
    | Sagittal | T-spine | T-spine | 2 mm/1.5 mm | Bone | 3 | Midline and parasagittal |
    | Coronal | T-spine | T-spine | 2.5 mm/2 mm | Bone | 3 | Coronal overview |


Category: Neuro

Protocol Type: Spine
