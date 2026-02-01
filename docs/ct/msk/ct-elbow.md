# CT Elbow

**Last Updated:** 2024-01-15  
**Author:** Dr. Martinez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Elbow | Contrast (N/A or 60s if contrast delay) | Distal humerus to Proximal radius/ulna |

    === "Clinical Indications"

        - Elbow fracture
        - Radial head fracture
        - Olecranon fracture
        - Coronoid
        - Terrible triad

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A or eGFR > 30
        - **Allergy:** N/A or check allergy
    
    - **Position:** Supine with elbow extended if possible or positioned for comfort
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

        - Distal humerus through proximal radius/ulna. Submillimeter. Position extended if possible. Bilateral for comparison

    === "Nursing Notes"

        - No IV unless contrast needed

    === "Radiologist Notes"
        - Distal humerus fractures. Radial head. Olecranon. Coronoid. Elbow dislocation. Terrible triad

    === "Tips & Tricks"

        - Position extended if possible. Submillimeter for detail

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Elbow Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 75 mL)    :active, contrast, 00:00, 30s
      Saline (50mL)          :active, saline, after contrast, 20s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Distal humerus | Proximal forearm | N/A | N/A | AP lateral |
    | CT Elbow | Distal humerus | Proximal radius/ulna | N/A or 60s if contrast | 0.625 mm | Submillimeter |

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
    | Axial | Elbow | Elbow | 1.5 mm/1 mm | Bone | N/A | Axial bone |
    | Coronal | Elbow | Elbow | 1.5 mm/1 mm | Bone | N/A | Coronal elbow |
    | Sagittal | Elbow | Elbow | 1.5 mm/1 mm | Bone | N/A | Sagittal elbow |
    | 3D surface | Elbow | Bones | 0.625 mm source | Bone | N/A | 3D for complex fractures |


### Additional Reconstructions

Document terrible triad if present. Radial head-capitellum alignment. 3D reconstruction

Category: Msk

Protocol Type: Musculoskeletal
