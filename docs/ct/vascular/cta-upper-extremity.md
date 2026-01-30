# CTA Upper Extremity

**Last Updated:** 2024-01-15  
**Author:** Dr. Davis

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Scout/Topogram | Non-contrast | Aortic arch to Fingertips |
        | CTA Arterial | Arterial (bolus tracked) | Aortic arch to Fingertips |

    === "Clinical Indications"

        - Upper extremity arterial insufficiency
        - Trauma
        - Dialysis access planning
        - Thoracic outlet syndrome

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history. IV in opposite arm
    
    - **Position:** Supine with affected arm raised above head or at side depending on indication
    - **NPO Status:** NPO 2 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 100 mL |
        | Flow Rate | 4 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Subclavian artery |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Scan from aortic arch to fingertips. May need bilateral for comparison. Position arm to demonstrate pathology

    === "Nursing Notes"

        - 20G IV in contralateral arm

    === "Radiologist Notes"
        - Assess subclavian axillary brachial radial ulnar arteries. Look for stenosis occlusion or injury

    === "Tips & Tricks"

        - Position arm to avoid overlap with torso. May need special positioning for TOS

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CTA Upper Extremity Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (100 mL)    :active, contrast, 00:00, 25s
      Saline (50mL)          :active, saline, after contrast, 12s
      section Arterial Phase
      CTA Arterial    :crit, scan2, 00:25, 16s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Aortic arch | Fingertips | N/A | N/A | AP of arm |
    | CTA Arterial | Aortic arch | Fingertips | Bolus tracked | 0.625 mm | Include arch through hand |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 0.9 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Full arm | 1.5 mm/1.5 mm | Vascular | 3 | Primary diagnostic |
    | Coronal | Arterial | Full arm | 2 mm/2 mm | Vascular | 3 | MIP full vessel course |
    | Sagittal | Arterial | Full arm | 2 mm/2 mm | Vascular | 3 | Lateral MIP |
    | 3D VR | Arterial | Full arm | 1 mm source | Vascular | 3 | 3D reconstruction |


### Additional Reconstructions

MIP and 3D VR. Subtract bones for vessel visualization

Category: Vascular

Protocol Type: Vascular
