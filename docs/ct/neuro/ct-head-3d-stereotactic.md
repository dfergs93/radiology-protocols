# CT Head 3D Stereotactic

**Last Updated:** 2024-01-15  
**Author:** Dr. Lee

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Stereotactic Head | Contrast (N/A (or 60-90s if contrast) delay) | Vertex to Skull base |

    === "Clinical Indications"

        - Stereotactic surgery planning
        - DBS planning
        - Biopsy planning
        - Surgical navigation
        - Gamma knife

-   __2. Patient Prep__

    ---

    - **Position:** Supine in surgical position. Head in frame if required
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast optional |
        | Volume | If contrast: 100 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        
        No contrast unless tumor. Stereotactic protocol



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Submillimeter ISOTROPIC acquisition. Vertex to skull base. DICOM for surgical planning. Frame or fiducials if required

    === "Nursing Notes"

        - Position exactly as for surgery. Frame placement if required

        !!! warning "Safety First"
            - **Renal Function:** N/A or verify eGFR
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Isotropic high-resolution for surgical targeting. Anatomic landmarks. Tumor if contrast

    === "Tips & Tricks"

        - Isotropic voxels critical. Export DICOM to surgical planning

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Head 3D Stereotactic Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 100 mL)    :active, contrast, 00:00, 33s
      Saline (20mL)          :active, saline, after contrast, 6s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Vertex | Skull base | N/A | N/A | Lateral |
    | Stereotactic Head | Vertex | Skull base | N/A (or 60-90s if contrast) | 0.5-0.625 mm | Isotropic submillimeter |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 300) |
    | Rotation Time | Helicals |
    | Pitch | Pitch for isotropic |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Stereo | Brain | 0.5 mm/0.5 mm | Brain (Bone if needed) | 3 | Isotropic axial |
    | Coronal | Stereo | Brain | 0.5 mm/0.5 mm | Brain | 3 | Isotropic coronal |
    | Sagittal | Stereo | Brain | 0.5 mm/0.5 mm | Brain | 3 | Isotropic sagittal midline |
    | 3D surface | Stereo | Brain | 0.5 mm source | Brain | 3 | Surface for navigation |


### Additional Reconstructions

Export to surgical navigation. Isotropic 0.5mm. Coordinates for targeting

Category: Neuro

Protocol Type: Neuroradiology
