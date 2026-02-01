# CT Lumbar Spine

**Last Updated:** 2024-01-15  
**Author:** Dr. Hayes

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | L-spine Helical | Contrast (N/A or 60s if contrast delay) | T12 to Sacrum |

    === "Clinical Indications"

        - Lumbar spine trauma
        - Degenerative disease
        - Back pain
        - Radiculopathy
        - Sciatica

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
        | Agent | None typically. Contrast if infection/tumor/post-op |
        | Volume | If contrast: 100 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        
        NC typical. Contrast for infection tumor or post-op with hardware



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - T12 to sacrum. Submillimeter helical. Sagittal and coronal reformats. Oblique for foramina

    === "Nursing Notes"

        - No IV unless contrast needed

    === "Radiologist Notes"
        - Alignment. Fractures. Disc spaces. Spinal canal stenosis. Neural foramina. Facet joints. Spondylolisthesis

    === "Tips & Tricks"

        - Bone algorithm. Sagittal and coronal reconstructions

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Lumbar Spine Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 100 mL)    :active, contrast, 00:00, 33s
      Saline (50mL)          :active, saline, after contrast, 16s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | T12 | Sacrum | N/A | N/A | AP and lateral |
    | L-spine Helical | T12 | Sacrum | N/A or 60s if contrast | 0.625 mm | Submillimeter |

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
    | Axial | L-spine | L-spine | 2 mm/2 mm | Bone | 3 | Bone and soft tissue |
    | Sagittal | L-spine | L-spine | 2 mm/1.5 mm | Bone | 3 | Midline and parasagittal |
    | Coronal | L-spine | L-spine | 2.5 mm/2 mm | Bone | 3 | Coronal overview |
    | Oblique sagittal | L-spine | Neural foramina | 2 mm | Bone | 3 | Foraminal assessment |


### Additional Reconstructions

Oblique sagittal for foramina. Measure spinal canal. Grade stenosis

Category: Neuro

Protocol Type: Spine
