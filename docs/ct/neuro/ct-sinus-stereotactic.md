# CT Sinus Stereotactic

**Last Updated:** 2024-01-15  
**Author:** Dr. Chen

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Stereotactic Sinus | Non-contrast | Frontal sinus to Hard palate |

    === "Clinical Indications"

        - Pre-operative sinus surgery planning
        - Image-guided surgery
        - ENT surgical navigation

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first. Surgical planning position
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Submillimeter isotropic acquisition. DICOM for surgical navigation system. May need fiducial markers. Entire sinus anatomy

    === "Nursing Notes"

        - Position as for surgery. Fiducials if required

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Complete sinus anatomy for surgical navigation. Ostiomeatal complex. Skull base. Lamina papyracea

    === "Tips & Tricks"

        - Isotropic voxels essential. DICOM for navigation

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Sinus Stereotactic Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Frontal sinus | Hard palate | N/A | N/A | Lateral |
    | Stereotactic Sinus | Frontal sinus | Hard palate | N/A | 0.625 mm | Isotropic submillimeter |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | Helicals |
    | Pitch | Pitch for isotropic |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Stereo | Sinuses | 0.625 mm/0.625 mm | Bone | N/A | Isotropic bone |
    | Coronal | Stereo | Sinuses | 0.625 mm/0.625 mm | Bone | N/A | Isotropic coronal |
    | Sagittal | Stereo | Sinuses | 0.625 mm/0.625 mm | Bone | N/A | Isotropic sagittal |
    | 3D surface | Stereo | Sinuses | 0.625 mm source | Bone | N/A | Surface rendering for navigation |


### Additional Reconstructions

Export DICOM to surgical navigation system. Isotropic 0.625mm

Category: Neuro

Protocol Type: Neuroradiology
