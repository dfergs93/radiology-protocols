# CT Foot

**Last Updated:** 2024-01-15  
**Author:** Dr. Davis

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Foot | Contrast (N/A or 60s if contrast delay) | Calcaneus to Toes |

    === "Clinical Indications"

        - Foot fracture
        - Lisfranc injury
        - Tarsal fractures
        - Foreign body
        - Pre-operative planning

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet first
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
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Calcaneus through toes. Submillimeter. Weight-bearing position if able. Bilateral for comparison

    === "Nursing Notes"

        - No IV unless infection suspected

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Calcaneus. Talus. Navicular. Cuneiforms. Metatarsals. Phalanges. Lisfranc ligament. Plantar fascia

    === "Tips & Tricks"

        - Weight-bearing if possible. Bilateral comparison helpful

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
      title CT Foot Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 75 mL)    :active, contrast, 00:00, 30s
      Saline          :active, saline, after contrast, 8s
      section Extremities
      CT Foot    :done, scan1, 00:00, 5s
  ```

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Calcaneus | Toes | N/A | N/A | Lateral and AP |
    | CT Foot | Calcaneus | Toes | N/A or 60s if contrast | 0.625 mm | Submillimeter |

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
    | Axial | Foot | Foot | 1 mm/1 mm | Bone | N/A | Axial bone |
    | Coronal | Foot | Foot | 1.5 mm/1 mm | Bone | N/A | Coronal foot |
    | Sagittal | Foot | Foot | 1.5 mm/1 mm | Bone | N/A | Sagittal foot |
    | Oblique | Foot | Lisfranc | 1.5 mm | Bone | N/A | Lisfranc joint |


### Additional Reconstructions

Document Lisfranc alignment. Calcaneal angles. 3D if complex

Category: Msk

Protocol Type: Musculoskeletal
