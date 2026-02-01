# CT Lower Extremity

**Last Updated:** 2024-01-15  
**Author:** Dr. Rodriguez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Lower Extremity | Contrast (N/A or 60s if contrast delay) | Proximal to injury to Distal to injury |

    === "Clinical Indications"

        - Lower extremity fracture
        - Tibia/fibula
        - Femur
        - Post-operative hardware assessment

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A or eGFR > 30
        - **Allergy:** N/A or check allergy
    
    - **Position:** Supine
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection |
        | Volume | If contrast: 100 mL |
        | Flow Rate | 2-3 mL/s |

    ===   "Lab Requirements"
        
        NC for trauma. Contrast for infection osteomyelitis



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - FOV based on region: hip to ankle. Submillimeter for fracture. Extended coverage for alignment

    === "Nursing Notes"

        - No IV unless contrast needed

    === "Radiologist Notes"
        - Fractures. Alignment. Comminution. Intra-articular extension. Hardware position. Infection on contrast

    === "Tips & Tricks"

        - Extended coverage for alignment measurements

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Lower Extremity Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 100 mL)    :active, contrast, 00:00, 40s
      Saline (50mL)          :active, saline, after contrast, 20s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Region specific | Extended | N/A | N/A | AP and lateral |
    | CT Lower Extremity | Proximal to injury | Distal to injury | N/A or 60s if contrast | 0.625-1 mm | Submillimeter |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200-250) |
    | Rotation Time | 0.5s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Lower extremity | Region | 2 mm/2 mm | Bone | N/A | Bone windows |
    | Coronal | Lower extremity | Region | 2 mm/2 mm | Bone | N/A | Coronal |
    | Sagittal | Lower extremity | Region | 2 mm/2 mm | Bone | N/A | Sagittal |
    | 3D surface | Lower extremity | Bones | 0.625 mm source | Bone | N/A | 3D reconstruction |


### Additional Reconstructions

Alignment measurements. Hardware position. 3D for surgical planning

Category: Msk

Protocol Type: Contrast-Enhanced
