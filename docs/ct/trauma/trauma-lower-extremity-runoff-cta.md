# Trauma Lower Extremity Runoff CTA

**Last Updated:** 2024-01-15  
**Author:** Dr. Williams

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Arterial | Arterial (bolus tracked) | Coverage as needed to Distal to injury |

    === "Clinical Indications"

        - Extremity vascular injury
        - Penetrating trauma
        - Fracture with vascular concern
        - Pulseless extremity

-   __2. Patient Prep__

    ---

    - **Position:** Supine legs extended
    - **NPO Status:** None - trauma
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 125 mL |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Abdominal aorta or proximal to injury |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Proceed with trauma indication



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Extend coverage based on injury. Aorta to ankles if bilateral. May do unilateral focused study. Arterial phase

    === "Nursing Notes"

        - 18-20G IV. May need proximal IV if arm injury

        !!! warning "Safety First"
            - **Renal Function:** Check if available
            - **Allergy:** Trauma indication

    === "Radiologist Notes"

        - Assess arterial injury: transection pseudoaneurysm occlusion extravasation. Evaluate fracture relationship to vessels

    === "Tips & Tricks"

        - Tailor coverage to injury. Fast acquisition

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Trauma Lower Extremity Runoff CTA Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (125 mL)    :active, contrast, 00:00, 27s
      Saline (20mL)          :active, saline, after contrast, 4s
      section Arterial Phase
      CTA Arterial    :crit, scan1, after contrast, 5s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Aorta or pelvis | Ankles | N/A | N/A | AP legs |
    | CTA Arterial | Coverage as needed | Distal to injury | Bolus tracked | 0.625 mm | Arterial phase runoff |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5s |
    | Pitch | 1.2-1.5 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Legs | 1.5 mm/1.5 mm | Vascular | 3 | Assess vessels |
    | Coronal | Arterial | Legs | 2 mm/2 mm | Vascular | 3 | MIP overview |
    | Sagittal | Arterial | Injured area | 2 mm/2 mm | Vascular | 3 | Vessel-bone relationship |
    | 3D VR | Arterial | Vessels | 1 mm source | Vascular | 3 | 3D vascular anatomy |


### Additional Reconstructions

MIP and 3D VR. Document vascular injury. Measure vessel caliber

Category: Trauma

Protocol Type: Vascular
