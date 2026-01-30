# MSK Protocol General

**Last Updated:** 2024-01-15  
**Author:** Dr. Lee

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | Non-contrast | Region to Region |
        | Contrast phase | Contrast (60-90 sec if done delay) | Region to Region |
        | Delayed phase | Contrast (5-10 min if done delay) | Region to Region |

    === "Clinical Indications"

        - Pre-operative planning
        - Post-operative assessment
        - Infection
        - Mass
        - Soft tissue tumor
        - Abscess

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A or eGFR > 30
        - **Allergy:** N/A or check allergy
    
    - **Position:** Depends on body part
    - **NPO Status:** NPO 2-4 hours if contrast
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 if contrast |
        | Volume | 100 mL if contrast |
        | Flow Rate | 2-3 mL/s |

    ===   "Lab Requirements"
        
        Contrast for infection mass post-op. NC for trauma hardware



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Field of view specific to region. Submillimeter if 3D needed. NC and/or contrast based on indication. Delayed phase (5-10 min) for infection/tumor

    === "Nursing Notes"

        - IV for contrast studies. Document indication

    === "Radiologist Notes"
        - NC: baseline bone soft tissue. Contrast: enhancement pattern. Delayed: washout or persistent enhancement. 3D for surgical planning

    === "Tips & Tricks"

        - Tailor protocol to clinical question. Bilateral for comparison

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title MSK Protocol General Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (100 mL if contrast)    :active, contrast, 00:00, 40s
      Saline (50mL)          :active, saline, after contrast, 20s
      section Scan Phase 3
      Contrast phase    :done, scan3, 01:30, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Region specific | Region specific | N/A | N/A | Two views |
    | Non-contrast | Region | Region | N/A | 0.625-1 mm | Baseline if done |
    | Contrast phase | Region | Region | 60-90 sec if done | 0.625-1 mm | Standard if done |
    | Delayed phase | Region | Region | 5-10 min if done | 1-2 mm | For infection/tumor |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200-250) |
    | Rotation Time | 0.5s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Acquisition | Region | 1-2 mm/1-2 mm | Bone and Standard | 3 | Primary images |
    | Coronal | Region | Region | 2 mm/2 mm | Bone and Standard | 3 | Coronal reformats |
    | Sagittal | Region | Region | 2 mm/2 mm | Bone and Standard | 3 | Sagittal reformats |
    | 3D if needed | Region | Bones | 0.625-1 mm source | Bone | N/A | 3D for surgical planning |


### Additional Reconstructions

Compare to contralateral side. Measure lesions. Bone and soft tissue windows

Category: Msk

Protocol Type: Contrast-Enhanced
