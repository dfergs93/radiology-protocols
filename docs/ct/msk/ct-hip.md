# CT Hip

**Last Updated:** 2024-01-15  
**Author:** Dr. Anderson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Pelvis/Hips | Contrast (N/A or 60s if contrast delay) | Iliac crests to Proximal femurs |

    === "Clinical Indications"

        - Hip fracture
        - Acetabular fracture
        - Femoral neck
        - Pre-operative planning
        - FAI assessment

-   __2. Patient Prep__

    ---

    - **Position:** Supine
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection/mass |
        | Volume | If contrast: 100 mL |
        | Flow Rate | 2-3 mL/s |

    ===   "Lab Requirements"
        
        NC for trauma. Contrast for infection AVN or tumor



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Iliac crests through proximal femurs. Bilateral for comparison. Submillimeter for 3D acetabular reconstructions

    === "Nursing Notes"

        - No IV unless contrast indicated

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Femoral neck fractures. Acetabular fractures (Judet/Letournel). Hip dislocation. FAI morphology. AVN

    === "Tips & Tricks"

        - Bilateral coverage. Submillimeter for acetabular 3D

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Hip Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 100 mL)    :active, contrast, 00:00, 40s
      Saline (20mL)          :active, saline, after contrast, 8s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Iliac crests | Proximal femurs | N/A | N/A | AP |
    | CT Pelvis/Hips | Iliac crests | Proximal femurs | N/A or 60s if contrast | 0.625 mm | Submillimeter for 3D |

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
    | Axial | Hips | Pelvis/hips | 2 mm/2 mm | Bone | N/A | Axial bone |
    | Coronal | Hips | Pelvis/hips | 2 mm/2 mm | Bone | N/A | Coronal hips |
    | Sagittal | Hips | Each hip | 2 mm/2 mm | Bone | N/A | Sagittal hips |
    | Judet views | Hips | Acetabulum | 2 mm oblique | Bone | N/A | Obturator and iliac obliques |


### Additional Reconstructions

3D pelvis. Judet oblique views. Letournel classification. FAI measurements (alpha angle)

Category: Msk

Protocol Type: Musculoskeletal
