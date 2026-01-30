# CT Knee

**Last Updated:** 2024-01-15  
**Author:** Dr. Thompson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Scout Bilateral | Non-contrast | Bilateral knees to Extended |
        | CT Knee | Contrast (N/A or 60s if contrast delay) | Distal femur to Proximal tib/fib |

    === "Clinical Indications"

        - Knee fracture
        - Tibial plateau
        - Patellar fracture
        - Pre-operative planning
        - Hardware evaluation

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A or eGFR > 30
        - **Allergy:** N/A or check allergy
    
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
        
        NC for trauma. Contrast for infection or tumor



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Distal femur through proximal tibia/fibula. Submillimeter. Extended FOV for alignment. Bilateral scout

    === "Nursing Notes"

        - No IV unless contrast indicated

    === "Radiologist Notes"
        - Tibial plateau fractures (Schatzker). Femoral condyles. Patella. Fibula. Cruciate ligaments on contrast. Menisci

    === "Tips & Tricks"

        - Bilateral scout for alignment assessment

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Knee Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 75 mL)    :active, contrast, 00:00, 30s
      Saline (50mL)          :active, saline, after contrast, 20s
      section Scan Phase 2
      CT Knee    :done, scan2, 01:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout Bilateral | Bilateral knees | Extended | N/A | N/A | AP for alignment |
    | CT Knee | Distal femur | Proximal tib/fib | N/A or 60s if contrast | 0.625 mm | Submillimeter |

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
    | Axial | Knee | Knee | 1.5 mm/1 mm | Bone | N/A | Bone algorithm |
    | Coronal | Knee | Knee | 1.5 mm/1 mm | Bone | N/A | Coronal knee |
    | Sagittal | Knee | Knee | 1.5 mm/1 mm | Bone | N/A | Sagittal knee |
    | 3D surface | Knee | Bones | 0.625 mm source | Bone | N/A | 3D for surgical planning |


### Additional Reconstructions

Schatzker classification if tibial plateau. Measure alignment. 3D reconstruction

Category: Msk

Protocol Type: Musculoskeletal
