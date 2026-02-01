# CT Shoulder

**Last Updated:** 2024-01-15  
**Author:** Dr. Lee

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Shoulder | Contrast (N/A or 60s if contrast delay) | Entire scapula to Proximal humerus |

    === "Clinical Indications"

        - Shoulder fracture
        - Proximal humerus
        - Glenoid
        - Scapula
        - Rotator cuff calcification

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A or eGFR > 30
        - **Allergy:** N/A or check allergy
    
    - **Position:** Supine with arm at side
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection/mass |
        | Volume | If contrast: 75 mL |
        | Flow Rate | 2-3 mL/s |

    ===   "Lab Requirements"
        
        NC for trauma. Contrast for infection or tumor



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Include entire scapula and proximal humerus. Submillimeter for glenoid detail. Y-views for scapula

    === "Nursing Notes"

        - No IV unless contrast indicated

    === "Radiologist Notes"
        - Proximal humerus fractures (Neer). Glenoid fractures. Scapular fractures. AC joint. Rotator cuff calcifications

    === "Tips & Tricks"

        - Include entire scapula. Submillimeter for glenoid

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Shoulder Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 75 mL)    :active, contrast, 00:00, 30s
      Saline (50mL)          :active, saline, after contrast, 20s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Include scapula | Proximal humerus | N/A | N/A | AP and Y-view |
    | CT Shoulder | Entire scapula | Proximal humerus | N/A or 60s if contrast | 0.625 mm | Submillimeter |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Shoulder | Shoulder | 1.5 mm/1 mm | Bone | N/A | Axial bone |
    | Coronal | Shoulder | Shoulder | 2 mm/1.5 mm | Bone | N/A | Coronal shoulder |
    | Sagittal | Shoulder | Shoulder | 2 mm/1.5 mm | Bone | N/A | Sagittal shoulder |
    | Oblique | Shoulder | Glenoid | 1.5 mm | Bone | N/A | Glenoid en face |


### Additional Reconstructions

3D reconstruction. Neer classification if proximal humerus. Glenoid version measurements

Category: Msk

Protocol Type: Musculoskeletal
