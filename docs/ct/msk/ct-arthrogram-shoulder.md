# CT Arthrogram Shoulder

**Last Updated:** 2024-01-15  
**Author:** Dr. Patel

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Arthrogram | Contrast (Immediate post-injection delay) | Acromion to Proximal humerus |

    === "Clinical Indications"

        - Labral tear
        - Rotator cuff tear
        - Capsular injury
        - Shoulder instability

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A
        - **Allergy:** Contrast reaction history
    
    - **Position:** Supine with arm at side
    - **NPO Status:** N/A
    - **Pre-Medication:** 
      Intra-articular contrast injection by radiologist


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 240 or 300 diluted |
        | Volume | 12-15 mL intra-articular |
        | Flow Rate | N/A |

    ===   "Lab Requirements"
        
        Arthrogram contrast injected under fluoro or US



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Post-arthrogram CT. Inject glenohumeral joint. Immediate CT after injection. Thin slices for labrum

    === "Nursing Notes"

        - Radiologist performs injection. Patient to CT immediately after

    === "Radiologist Notes"
        - Labral tears. Rotator cuff tears. Capsular tears. Glenohumeral ligaments. Paralabral cysts

    === "Tips & Tricks"

        - Scan immediately after injection. Thin slices for labrum

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Arthrogram Shoulder Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Scan Phase 2
      CT Arthrogram    :done, scan2, after scan1, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Shoulder region | Proximal humerus | N/A | N/A | AP |
    | CT Arthrogram | Acromion | Proximal humerus | Immediate post-injection | 0.625 mm | Submillimeter for labrum |

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
    | Axial | Arthrogram | Shoulder | 1 mm/0.75 mm | Standard | 3 | Thin for labral detail |
    | Coronal | Arthrogram | Shoulder | 1.5 mm/1 mm | Standard | 3 | Coronal oblique shoulder |
    | Sagittal | Arthrogram | Shoulder | 1.5 mm/1 mm | Standard | 3 | Sagittal oblique |
    | Abduction ABER | Arthrogram | Shoulder | 1.5 mm | Standard | 3 | ABER position if done |


### Additional Reconstructions

Oblique coronal and sagittal. Assess labrum rotator cuff capsule. Document contrast extravasation

Category: Msk

Protocol Type: Musculoskeletal
