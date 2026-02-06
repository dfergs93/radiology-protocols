# CT Temporal Bones

**Last Updated:** 2024-01-15  
**Author:** Dr. Anderson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Axial Temporal | Non-contrast | EAC to Petrous apex |
        | Coronal Temporal | Non-contrast | EAC to IAC |

    === "Clinical Indications"

        - Hearing loss
        - Chronic otitis
        - Cholesteatoma
        - Temporal bone fracture
        - Pre-operative cochlear implant

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

        - Temporal bones: external auditory canal to petrous apex. SUBMILLIMETER <0.625mm. Direct axial and direct coronal if possible. Ultra high resolution

    === "Nursing Notes"

        - No IV. Remove hearing aids and earrings

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Ossicles. Cochlea. Semicircular canals. Internal auditory canal. Mastoid air cells. Cholesteatoma. Fracture. Tegmen

    === "Tips & Tricks"

        - Submillimeter critical. Sharp bone kernel. Remove all metal

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Temporal Bones Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | EAC level | Petrous apex | N/A | N/A | Lateral |
    | Axial Temporal | EAC | Petrous apex | N/A | 0.5-0.625 mm | Parallel to lateral SCC |
    | Coronal Temporal | EAC | IAC | N/A | 0.5-0.625 mm | Perpendicular to petrous ridge |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | High mAs (300-400) |
    | Rotation Time | Axial/Coronals |
    | Pitch | Sequential or helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Temporal | Bilateral | 0.5 mm/0.5 mm | Bone sharp | N/A | Ultra HR bone |
    | Coronal | Temporal | Bilateral | 0.5 mm/0.5 mm | Bone sharp | N/A | Coronal bone |
    | Oblique sagittal | Temporal | Ossicles | 0.5 mm | Bone | N/A | Ossicular chain |
    | Pöschl/Stenvers | Temporal | IAC | 0.75 mm | Bone | N/A | IAC oriented views |


### Additional Reconstructions

Pöschl and Stenvers oblique reformats for IAC. Measure vestibular aqueduct

Category: Neuro

Protocol Type: Neuroradiology
