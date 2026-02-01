# CT Cervical Spine

**Last Updated:** 2024-01-15  
**Author:** Dr. Rodriguez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | C-spine Helical | Contrast (N/A or 60s if contrast delay) | Skull base to T1 |

    === "Clinical Indications"

        - Cervical spine trauma
        - Degenerative disease
        - Neck pain
        - Radiculopathy
        - Myelopathy

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A or verify eGFR
        - **Allergy:** N/A or check allergy
    
    - **Position:** Supine head-first
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
        
        NC typical. Contrast for infection tumor or post-op



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Skull base to T1. Submillimeter helical. Sagittal and coronal reformats required. Bone algorithm

    === "Nursing Notes"

        - No IV unless contrast needed. Cervical precautions if trauma

    === "Radiologist Notes"
        - Alignment. Fractures. Disc spaces. Neural foramina. Spinal canal. Facet joints. Degenerative changes

    === "Tips & Tricks"

        - Minimize motion. C-collar if trauma

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Cervical Spine Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 100 mL)    :active, contrast, 00:00, 33s
      Saline (50mL)          :active, saline, after contrast, 16s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Skull base | T1 | N/A | N/A | AP and lateral |
    | C-spine Helical | Skull base | T1 | N/A or 60s if contrast | 0.625 mm | Submillimeter acquisition |

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
    | Axial | C-spine | C-spine | 2 mm/2 mm | Bone | 3 | Bone and soft tissue |
    | Sagittal | C-spine | C-spine | 2 mm/1.5 mm | Bone | 3 | Midline and parasagittal |
    | Coronal | C-spine | C-spine | 2 mm/2 mm | Bone | 3 | Coronal alignment |
    | Oblique sagittal | C-spine | Neural foramina | 2 mm | Bone | 3 | Foraminal narrowing |


### Additional Reconstructions

Sagittal and coronal bone reconstructions. Oblique for foramina

Category: Neuro

Protocol Type: Spine
