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
        
        NC for trauma foreign body. Contrast for infection



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
  config:
    theme: default
  ---
    gantt
      title CT Hand Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (If contrast: 50 mL)    :active, contrast, 00:00, 25s
      Saline (20mL)          :active, saline, after contrast, 10s
  ```


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
