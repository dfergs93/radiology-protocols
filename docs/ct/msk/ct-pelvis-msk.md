# CT Pelvis MSK

**Last Updated:** 2024-01-15  
**Author:** Dr. Kim

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Pelvis | Contrast (N/A or 60s if contrast delay) | Iliac crests to Proximal femurs |

    === "Clinical Indications"

        - Pelvic fracture
        - Sacral fracture
        - SI joint
        - Pelvic ring injury
        - Pre-operative planning

-   __2. Patient Prep__

    ---

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
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Iliac crests to proximal femurs. Submillimeter for 3D. Assess pelvic ring integrity. Inlet and outlet views

    === "Nursing Notes"

        - No IV unless contrast indicated

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Pelvic ring fractures (Young-Burgess). Sacral fractures (Denis). Acetabulum. SI joints. Symphysis pubis

    === "Tips & Tricks"

        - Submillimeter for 3D pelvic reconstruction

</div>


### Protocol Details
  ```mermaid
  ---
  displayMode: compact
  config:
    theme: default
    themeCSS: " #Saline{ fill: #4ed5ff; stroke: #2094f3; } "
  ---
    gantt
      title CT Pelvis MSK Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 100 mL)    :active, contrast, 00:00, 40s
      Saline          :active, saline, after contrast, 8s
      section Pelvis
      CT Pelvis    :done, scan1, 00:00, 5s
  ```

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Iliac crests | Proximal femurs | N/A | N/A | AP |
    | CT Pelvis | Iliac crests | Proximal femurs | N/A or 60s if contrast | 0.625 mm | Submillimeter for 3D |

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
    | Axial | Pelvis | Pelvis | 2 mm/2 mm | Bone | N/A | Axial bone |
    | Coronal | Pelvis | Pelvis | 2 mm/2 mm | Bone | N/A | Coronal pelvis |
    | Sagittal | Pelvis | Pelvis | 2 mm/2 mm | Bone | N/A | Sagittal sacrum |
    | Inlet/Outlet | Pelvis | Pelvic ring | 2-3 mm oblique | Bone | N/A | Pelvic ring views |


### Additional Reconstructions

3D pelvis. Inlet and outlet views. Young-Burgess classification. Measure displacement

Category: Msk

Protocol Type: Contrast-Enhanced
