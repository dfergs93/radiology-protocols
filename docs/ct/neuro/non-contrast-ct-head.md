# Non-Contrast CT Head

**Last Updated:** 2026-01-03  
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast Head | Non-contrast | Vertex to Foramen magnum |

    === "Clinical Indications"

        - Acute stroke protocol
        - Head trauma
        - Headache - worst of life
        - Altered mental status

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A
        - **Allergy:** N/A
    
    - **Position:** Supine head-first
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Minimize patient motion. Gantry angle parallel to skull base to reduce orbital dose. Ensure head straight

    === "Nursing Notes"

        - No IV required. Explain importance of staying still

    === "Radiologist Notes"
        - Look for hyperdense MCA sign. Assess grey-white differentiation. Check for hemorrhage and mass effect

    === "Tips & Tricks"

        - Remove dentures and hearing aids. Secure head in holder

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Non-Contrast CT Head Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Vertex | C1 | N/A | N/A | Lateral scout |
    | Non-Contrast Head | Vertex | Foramen magnum | N/A | 5 mm | Angle parallel to hard palate |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 300) |
    | Rotation Time | 1s |
    | Pitch | 0.5 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Non-contrast | Brain | 5 mm/5 mm | Brain | 3 | Primary diagnostic - brain window |
    | Axial | Non-contrast | Brain | 5 mm/5 mm | Bone | N/A | Bone window for fractures |
    | Coronal | Non-contrast | Brain | 3 mm/3 mm | Brain | 3 | Optional - for skull base evaluation |
    | Sagittal | Non-contrast | Brain | 3 mm/3 mm | Brain | 3 | Optional - for midline structures |


### Additional Reconstructions

Thin slice 1.25mm if subtle fracture suspected

Category: Neuro

Protocol Type: Neuroradiology
