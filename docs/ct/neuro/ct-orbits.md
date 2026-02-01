# CT Orbits

**Last Updated:** 2024-01-15  
**Author:** Dr. Davis

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Axial Orbits | Contrast (N/A or 60s if contrast delay) | Superior orbital rim to Maxillary sinus |

    === "Clinical Indications"

        - Orbital mass
        - Thyroid eye disease
        - Orbital cellulitis
        - Optic nerve assessment
        - Trauma

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A or verify eGFR > 30
        - **Allergy:** N/A or check allergy
    
    - **Position:** Supine head-first
    - **NPO Status:** NPO 2 hours if contrast
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 if contrast |
        | Volume | 75-100 mL if contrast |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        
        Contrast if mass/infection. NC for trauma/foreign body



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Orbits: superior orbital rim to maxillary sinus. Axial 1-2mm. Coronal reformats. NC for trauma. Contrast for masses/inflammation

    === "Nursing Notes"

        - Contrast for mass or inflammation. NC for trauma and metallic foreign body

    === "Radiologist Notes"
        - Extraocular muscles. Optic nerve. Globe integrity. Orbital fat. Preseptal vs postseptal. Masses. Foreign body

    === "Tips & Tricks"

        - Angle axial parallel to optic nerves. Thin slices

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Orbits Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (75-100 mL if contrast)    :active, contrast, 00:00, 25s
      Saline (50mL)          :active, saline, after contrast, 16s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Superior orbital rim | Maxillary sinus | N/A | N/A | Lateral |
    | Axial Orbits | Superior orbital rim | Maxillary sinus | N/A or 60s if contrast | 1-1.5 mm | Parallel to optic nerves |

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
    | Axial | Orbits | Orbits | 1.5 mm/1 mm | Bone and Standard | 3 | Bone for fractures soft tissue for pathology |
    | Coronal | Orbits | Orbits | 1.5 mm/1 mm | Bone and Standard | 3 | Coronal orbits |
    | Sagittal | Orbits | Optic nerve | 2 mm/1.5 mm | Standard | 3 | Optic nerve canal |
    | 3D if trauma | Orbits | Orbital bones | 1 mm source | Bone | N/A | 3D if complex fracture |


### Additional Reconstructions

Assess optic nerve canal. Measure EOMs if thyroid eye disease. Document foreign body

Category: Neuro

Protocol Type: Contrast-Enhanced
