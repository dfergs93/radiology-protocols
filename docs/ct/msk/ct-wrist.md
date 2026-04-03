# CT Wrist

**Last Updated:** 2024-01-15  
**Author:** Dr. Hayes

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Wrist | Contrast (N/A or immediate if arthrogram delay) | Distal radius/ulna to Mid-carpus |

    === "Clinical Indications"

        - Wrist fracture
        - Distal radius fracture
        - Carpal fracture
        - DRUJ
        - Scapholunate ligament

-   __2. Patient Prep__

    ---

    - **Position:** Prone with wrist extended (superman) or positioned for comfort
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

        - Distal radius/ulna through carpus. Submillimeter for carpal detail. Extended for forearm if needed

    === "Nursing Notes"

        - No IV unless contrast or arthrogram needed

        !!! warning "Safety First"
            - **Renal Function:** N/A or eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Distal radius fractures. Carpal fractures (scaphoid). DRUJ. Carpal alignment. Ligaments on arthrogram

    === "Tips & Tricks"

        - Position for comfort. Submillimeter for carpal bones

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Distal forearm | Carpus | N/A | N/A | AP lateral |
    | CT Wrist | Distal radius/ulna | Mid-carpus | N/A or immediate if arthrogram | 0.625 mm | Submillimeter |

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
    | Axial | Wrist | Wrist | 1 mm/0.75 mm | Bone | N/A | Axial bone |
    | Coronal | Wrist | Wrist | 1 mm/0.75 mm | Bone | N/A | Coronal wrist |
    | Sagittal | Wrist | Wrist | 1 mm/0.75 mm | Bone | N/A | Sagittal wrist |
    | Oblique sagittal | Wrist | Scaphoid | 1 mm | Bone | N/A | Scaphoid long axis |

### Additional Reconstructions

Scaphoid views. Carpal alignment. 3D if complex fracture

Category: Msk

Protocol Type: Musculoskeletal
