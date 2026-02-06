# CT Facial Bones

**Last Updated:** 2024-01-15  
**Author:** Dr. Martinez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Facial Bones | Non-contrast | Frontal sinus to Mandible |

    === "Clinical Indications"

        - Facial trauma
        - Orbital fractures
        - Zygoma fractures
        - Nasal fractures
        - Mandible fractures

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Frontal sinus to mandible. Submillimeter for 3D. Axial acquisition with multiplanar reformats. Remove dentures

    === "Nursing Notes"

        - Remove all facial metal. Dentures out

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Le Fort classification. Orbital floor. Zygoma. Nasal bones. Mandible. NOE complex. 3D for surgical planning

    === "Tips & Tricks"

        - Remove dentures and facial metal

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Facial Bones Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Frontal sinus | Mandible | N/A | N/A | Lateral |
    | Facial Bones | Frontal sinus | Mandible | N/A | 0.625 mm | Submillimeter for 3D |

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
    | Axial | Face | Face | 1.25 mm/1 mm | Bone | N/A | Axial bone windows |
    | Coronal | Face | Face | 1.25 mm/1 mm | Bone | N/A | Coronal face |
    | Sagittal | Face | Midface | 2 mm/1.5 mm | Bone | N/A | Sagittal midline |
    | 3D | Face | Facial bones | 0.625 mm source | Bone | N/A | 3D surface rendering |


### Additional Reconstructions

3D surface rendering. Document Le Fort if present. Orbital floor assessment

Category: Neuro

Protocol Type: Non-Contrast
