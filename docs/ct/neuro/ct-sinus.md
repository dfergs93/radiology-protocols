# CT Sinus

**Last Updated:** 2024-01-15  
**Author:** Dr. Hayes

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Coronal Sinus | Non-contrast | Frontal sinus to Maxillary sinus |
        | Axial reformat | Contrast (From coronal delay) | Frontal to Maxillary |

    === "Clinical Indications"

        - Sinusitis
        - Sinus disease
        - Pre-operative sinus surgery
        - Nasal obstruction

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

        - Coronal acquisition skull base through maxillary sinuses. Submillimeter for anatomy. Bone and soft tissue windows

    === "Nursing Notes"

        - No IV. Remove dentures and metal

    === "Radiologist Notes"
        - Assess all sinuses. Ostiomeatal complex. Anatomic variants. Mucosal thickening. Polyps. Bony anatomy

    === "Tips & Tricks"

        - Direct coronal preferred. Submillimeter for anatomy

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Sinus Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Frontal sinus | Maxillary sinus | N/A | N/A | Lateral |
    | Coronal Sinus | Frontal sinus | Maxillary sinus | N/A | 0.625 mm | Direct coronal if possible |
    | Axial reformat | Frontal | Maxillary | From coronal | 0.625 mm | Reformatted from coronal |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | Axial or coronals |
    | Pitch | N/A |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Coronal | Sinus | Sinuses | 1.25 mm/0.75 mm | Bone | N/A | Bone window |
    | Coronal | Sinus | Sinuses | 3 mm/2 mm | Standard | 3 | Soft tissue |
    | Axial | Sinus | Sinuses | 2 mm/2 mm | Bone | N/A | Axial bone |
    | Sagittal | Sinus | Sinuses | 2 mm/2 mm | Bone | N/A | Midline and lateral |


### Additional Reconstructions

Document anatomic variants (Haller cells concha bullosa). OMC assessment

Category: Neuro

Protocol Type: Neuroradiology
