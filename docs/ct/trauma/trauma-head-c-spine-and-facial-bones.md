# Trauma Head C-Spine and Facial Bones

**Last Updated:** 2024-01-15  
**Author:** Dr. Johnson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Head | Non-contrast | Vertex to Foramen magnum |
        | NC C-spine | Non-contrast | Skull base to T1 |
        | NC Facial Bones | Non-contrast | Frontal sinus to Mandible |

    === "Clinical Indications"

        - Facial trauma
        - Maxillofacial fractures
        - Orbital fractures with head/spine injury

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A
        - **Allergy:** N/A
    
    - **Position:** Supine head-first. C-collar on
    - **NPO Status:** None - trauma
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - THREE acquisitions: 1) Head 2) C-spine 3) Facial bones. Face: submillimeter helical for 3D. C-collar remains

    === "Nursing Notes"

        - C-collar precautions. Document mechanism of injury

    === "Radiologist Notes"
        - Head: intracranial injury. C-spine: fractures. Face: Le Fort midface orbital mandible fractures

    === "Tips & Tricks"

        - C-collar on. Remove dentures if safe

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Trauma Head C-Spine and Facial Bones Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Vertex | T1 | N/A | N/A | Lateral |
    | NC Head | Vertex | Foramen magnum | N/A | 5 mm | Standard head |
    | NC C-spine | Skull base | T1 | N/A | 0.625 mm | Submillimeter |
    | NC Facial Bones | Frontal sinus | Mandible | N/A | 0.625 mm | Submillimeter for 3D |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (300 head / 250 other) |
    | Rotation Time | 1.0 / 0.5s |
    | Pitch | 0.5 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Head | Brain | 5 mm/5 mm | Brain/Bone | 3 | Brain and skull |
    | Sagittal | C-spine | C-spine | 2 mm/2 mm | Bone | 3 | C-spine alignment |
    | Axial | Face | Face | 1.25 mm/1 mm | Bone | N/A | Facial bones |
    | Coronal | Face | Face | 1.25 mm/1 mm | Bone | N/A | Facial coronal |


### Additional Reconstructions

3D face reconstruction. Le Fort classification. Orbital floor assessment

Category: Trauma

Protocol Type: Trauma
