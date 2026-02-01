# CT Complete Spine

**Last Updated:** 2024-01-15  
**Author:** Dr. Chen

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Complete Spine | Contrast (N/A or 60s if contrast delay) | Skull base to Sacrum |

    === "Clinical Indications"

        - Spine trauma pan-scan
        - Multi-level disease
        - Metastatic survey
        - Infection

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A or verify eGFR
        - **Allergy:** N/A or check allergy
    
    - **Position:** Supine
    - **NPO Status:** None - usually trauma
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection/mets |
        | Volume | If contrast: 125 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        
        NC for trauma. Contrast for mets or infection



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Skull base to sacrum. LONG COVERAGE. Submillimeter. Sagittal and coronal entire spine. May do in segments

    === "Nursing Notes"

        - No IV unless contrast needed. Complete spine coverage

    === "Radiologist Notes"
        - Entire spine alignment. Fractures all levels. Spinal canal. Paraspinal masses. Metastatic disease

    === "Tips & Tricks"

        - Long coverage. May need multiple acquisitions

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Complete Spine Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 125 mL)    :active, contrast, 00:00, 41s
      Saline (50mL)          :active, saline, after contrast, 16s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Skull base | Sacrum | N/A | N/A | Full AP and lateral |
    | Complete Spine | Skull base | Sacrum | N/A or 60s if contrast | 0.625-1 mm | Submillimeter entire spine |

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
    | Axial | Spine | Full spine | 2 mm/2 mm | Bone | 3 | Axial entire spine |
    | Sagittal | Spine | Full spine | 2 mm/1.5 mm | Bone | 3 | Sagittal full spine |
    | Coronal | Spine | Full spine | 2.5 mm/2 mm | Bone | 3 | Coronal full spine |


### Additional Reconstructions

Sagittal and coronal bone reconstructions. Oblique for foramina

Category: Neuro

Protocol Type: Spine
