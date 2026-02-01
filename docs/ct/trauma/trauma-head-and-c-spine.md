# Trauma Head and C-Spine

**Last Updated:** 2024-01-15  
**Author:** Dr. Smith

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Head | Non-contrast | Vertex to Foramen magnum |
        | NC C-spine | Non-contrast | Skull base to T1 |

    === "Clinical Indications"

        - Trauma head injury
        - C-spine clearance
        - Multi-trauma assessment

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A
        - **Allergy:** N/A
    
    - **Position:** Supine head-first. Cervical collar in place
    - **NPO Status:** None - trauma
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO acquisitions: 1) Head vertex to C1 2) C-spine skull base to T1. Head: 5mm axial. C-spine: 0.625mm with reformats. Minimize movement

    === "Nursing Notes"

        - Maintain cervical precautions. C-collar remains on. Document GCS

    === "Radiologist Notes"
        - Head: acute hemorrhage skull fractures. C-spine: fractures alignment ligamentous injury

    === "Tips & Tricks"

        - Keep C-collar on. Minimize patient movement

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Trauma Head and C-Spine Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout Head | Vertex | C1 | N/A | N/A | Lateral |
    | NC Head | Vertex | Foramen magnum | N/A | 5 mm | Parallel to hard palate |
    | Scout C-spine | Skull base | T1 | N/A | N/A | AP and lateral |
    | NC C-spine | Skull base | T1 | N/A | 0.625 mm | Helical submillimeter |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (300 head / 250 spine) |
    | Rotation Time | 1.0 head / 0.5 spines |
    | Pitch | 0.5 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Head | Brain | 5 mm/5 mm | Brain | 3 | Brain and bone windows |
    | Sagittal | C-spine | C-spine | 2 mm/2 mm | Bone | 3 | Midline and parasagittal |
    | Coronal | C-spine | C-spine | 2 mm/2 mm | Bone | 3 | Coronal alignment |
    | Axial | C-spine | C-spine | 2 mm/2 mm | Bone | 3 | Axial bone windows |


### Additional Reconstructions

C-spine: Sagittal and coronal bone reformats. 3D if complex fracture

Category: Trauma

Protocol Type: Trauma
