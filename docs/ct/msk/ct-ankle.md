# CT Ankle

**Last Updated:** 2024-01-15  
**Author:** Dr. Patel

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Ankle | Contrast (N/A or 60s if contrast delay) | Distal tib/fib to Hindfoot |

    === "Clinical Indications"

        - Ankle fracture
        - Ligament injury
        - Pilon fracture
        - Pre-operative planning
        - Hardware assessment

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet first
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
        
        NC for trauma. Contrast for infection or soft tissue mass



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Include distal tibia/fibula through hindfoot. Submillimeter for 3D. Bilateral scout for positioning. May scan bilateral for comparison

    === "Nursing Notes"

        - No IV unless contrast needed

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Malleolar fractures. Tibial plafond. Talus. Calcaneus. Syndesmosis. Ligaments on contrast

    === "Tips & Tricks"

        - Bilateral scout for symmetry. Submillimeter for 3D

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Ankle Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 75 mL)    :active, contrast, 00:00, 30s
      Saline (20mL)          :active, saline, after contrast, 8s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout Bilateral | Bilateral ankles | Feet | N/A | N/A | AP for positioning |
    | CT Ankle | Distal tib/fib | Hindfoot | N/A or 60s if contrast | 0.625 mm | Submillimeter |

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
    | Axial | Ankle | Ankle | 1 mm/1 mm | Bone | N/A | Bone algorithm |
    | Coronal | Ankle | Ankle | 1.5 mm/1 mm | Bone | N/A | Coronal ankle |
    | Sagittal | Ankle | Ankle | 1.5 mm/1 mm | Bone | N/A | Sagittal ankle |
    | 3D surface | Ankle | Bones | 0.625 mm source | Bone | N/A | 3D for complex fractures |


### Additional Reconstructions

3D reconstruction for surgical planning. Document fracture fragments

Category: Msk

Protocol Type: Musculoskeletal
