# CT Upper Extremity

**Last Updated:** 2024-01-15  
**Author:** Dr. White

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Upper Extremity | Contrast (N/A or 60s if contrast delay) | Proximal to injury to Distal to injury |

    === "Clinical Indications"

        - Upper extremity fracture
        - Humerus
        - Radius/ulna
        - Forearm
        - Elbow injury

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A or eGFR > 30
        - **Allergy:** N/A or check allergy
    
    - **Position:** Supine with arm positioned
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection |
        | Volume | If contrast: 75 mL |
        | Flow Rate | 2-3 mL/s |

    ===   "Lab Requirements"
        
        NC for trauma. Contrast for infection or soft tissue mass



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - FOV based on region: shoulder to hand. Submillimeter for fracture detail. Position for comfort and coverage

    === "Nursing Notes"

        - No IV unless contrast needed

    === "Radiologist Notes"
        - Fractures. Alignment. Intra-articular extension. Comminution. Soft tissue injury on contrast

    === "Tips & Tricks"

        - Position for patient comfort and diagnostic quality

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Upper Extremity Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 75 mL)    :active, contrast, 00:00, 30s
      Saline (50mL)          :active, saline, after contrast, 20s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Region specific | Extended | N/A | N/A | AP and lateral |
    | CT Upper Extremity | Proximal to injury | Distal to injury | N/A or 60s if contrast | 0.625-1 mm | Submillimeter |

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
    | Axial | Upper extremity | Region | 1-2 mm/1-2 mm | Bone | N/A | Bone windows |
    | Coronal | Upper extremity | Region | 2 mm/2 mm | Bone | N/A | Coronal |
    | Sagittal | Upper extremity | Region | 2 mm/2 mm | Bone | N/A | Sagittal |
    | 3D surface | Upper extremity | Bones | 0.625 mm source | Bone | N/A | 3D if complex |


### Additional Reconstructions

Document fracture location alignment. Soft tissue windows if contrast

Category: Msk

Protocol Type: Contrast-Enhanced
