# CT Soft Tissue Neck

**Last Updated:** 2024-01-15  
**Author:** Dr. Thompson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Contrast Neck | Contrast (60-70 sec delay) | Skull base to Thoracic inlet |

    === "Clinical Indications"

        - Neck mass
        - Deep neck infection
        - Abscess
        - Airway assessment
        - Lymphadenopathy

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history
    
    - **Position:** Supine head-first
    - **NPO Status:** NPO 2 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 100 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30. Contrast essential



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Skull base to thoracic inlet. 60-70 sec delay for venous phase. Arms down. Minimize swallowing. May need NC if calcium assessment

    === "Nursing Notes"

        - 18-20G IV. Coach no swallowing during scan

    === "Radiologist Notes"
        - Assess neck spaces. Retropharyngeal. Parapharyngeal. Masticator. Parotid. Submandibular. Thyroid. Lymph nodes. Abscess vs phlegmon

    === "Tips & Tricks"

        - Arms down. Minimize swallowing. Quiet breathing

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Soft Tissue Neck Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (100 mL)    :active, contrast, 00:00, 33s
      Saline (50mL)          :active, saline, after contrast, 16s
      section Scan Phase 1
      Contrast Neck    :done, scan1, 01:00, 15s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Skull base | Thoracic inlet | N/A | N/A | Lateral |
    | Contrast Neck | Skull base | Thoracic inlet | 60-70 sec | 1-2 mm | Venous phase |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200-250) |
    | Rotation Time | 0.5s |
    | Pitch | 1 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Neck | Neck | 2.5 mm/2 mm | Standard | 3 | Soft tissue neck |
    | Coronal | Neck | Neck | 3 mm/2.5 mm | Standard | 3 | Coronal neck spaces |
    | Sagittal | Neck | Midline | 3 mm/2.5 mm | Standard | 3 | Airway and retropharyngeal |


### Additional Reconstructions

Assess all neck spaces. Measure lymph nodes. Airway diameter if concern

Category: Neuro

Protocol Type: Contrast-Enhanced
