# CT Myelogram

**Last Updated:** 2024-01-15  
**Author:** Dr. Martinez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Myelogram | Non-contrast | Region of interest to Extended coverage |

    === "Clinical Indications"

        - Post-myelogram CT
        - Intrathecal contrast follow-up
        - Spinal stenosis
        - Nerve root compression

-   __2. Patient Prep__

    ---

    - **Position:** Supine. Post-lumbar puncture
    - **NPO Status:** N/A
    - **Pre-Medication:**
        - Intrathecal contrast already given

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 240 intrathecal |
        | Volume | 10-15 mL IT |
        | Flow Rate | N/A |

    ===   "Lab Requirements"
        
        Intrathecal contrast given by clinician via LP



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Post-LP CT. Usually lumbar region. Thin slices. Axial and sagittal reformats. Assess nerve root sleeves and thecal sac

    === "Nursing Notes"

        - Patient already had LP with IT contrast. Position comfortably

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Nerve root sleeves. Thecal sac compression. Spinal stenosis. Disc herniations. Surgical planning detail

    === "Tips & Tricks"

        - Post-LP headache precautions. Thin slices for nerve detail

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Myelogram Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Coverage area | Based on region | N/A | N/A | AP and lateral |
    | CT Myelogram | Region of interest | Extended coverage | N/A | 0.625 mm | Submillimeter for detail |

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
    | Axial | Myelogram | Spine | 1 mm/1 mm | Bone and Standard | 3 | Nerve roots and thecal sac |
    | Sagittal | Myelogram | Spine | 1.5 mm/1 mm | Standard | 3 | Thecal sac and compression |
    | Coronal | Myelogram | Spine | 2 mm/1.5 mm | Standard | 3 | Coronal nerve roots |
    | Oblique sagittal | Myelogram | Neural foramina | 1.5 mm | Standard | 3 | Foraminal nerve roots |


### Additional Reconstructions

Oblique reformats for nerve roots. Document stenosis level and severity

Category: Neuro

Protocol Type: Spine
