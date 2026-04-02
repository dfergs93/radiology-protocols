# CT Hand

**Last Updated:** 2024-01-15  
**Author:** Dr. Chen

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Hand | Contrast (N/A or 60s if contrast delay) | Distal radius/ulna to Fingertips |

    === "Clinical Indications"

        - Hand fracture
        - Scaphoid fracture
        - Metacarpal fracture
        - Foreign body
        - Pre-operative planning

-   __2. Patient Prep__

    ---

    - **Position:** Prone with hand extended (superman position) or supine with arm at side
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection |
        | Volume | If contrast: 50 mL |
        | Flow Rate | 2 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Distal radius/ulna through fingertips. Submillimeter. Position hand flat. Bilateral scout for comparison

    === "Nursing Notes"

        - No IV unless infection suspected

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Carpal fractures (scaphoid navicular lunate). Metacarpals. Phalanges. CMC joints. Foreign bodies

    === "Tips & Tricks"

        - Superman position preferred. Submillimeter for scaphoid

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
      title CT Hand Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 50 mL)    :active, contrast, 00:00, 25s
      Saline          :active, saline, after contrast, 10s
      section Extremities
      CT Hand    :done, scan1, 00:00, 5s
  ```

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Distal radius/ulna | Fingertips | N/A | N/A | AP and lateral |
    | CT Hand | Distal radius/ulna | Fingertips | N/A or 60s if contrast | 0.625 mm | Submillimeter |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 150-200) |
    | Rotation Time | 0.5s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Hand | Hand | 1 mm/0.75 mm | Bone | N/A | Thin axial |
    | Coronal | Hand | Hand | 1 mm/0.75 mm | Bone | N/A | Coronal hand |
    | Sagittal | Hand | Hand | 1 mm/0.75 mm | Bone | N/A | Sagittal hand |
    | Oblique sagittal | Hand | Scaphoid | 1 mm | Bone | N/A | Scaphoid long axis |


### Additional Reconstructions

Scaphoid-specific views. 3D if complex. Document foreign body location

Category: Msk

Protocol Type: Musculoskeletal
