# Gated CTA CAP

**Last Updated:** 2024-01-15  
**Author:** Dr. Lee

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Gated CTA Chest | Arterial (bolus tracked) | Thoracic inlet to Diaphragm |
        | Flash CTA AP | Contrast (Immediate after chest delay) | Diaphragm to Pubic symphysis |

    === "Clinical Indications"

        - Aortic dissection
        - Aortic aneurysm with cardiac involvement
        - Combined cardiac and aortic pathology

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history
    
    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:** 
      HR < 65 target. Metoprolol 5mg IV prn. Nitro 0.4mg SL


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 140 mL |
        | Flow Rate | 4 mL/s |
        | Timing Method | Dual phase: Gated chest + Flash AP |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 180 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30. Large volume needed



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO acquisitions: 1) Gated retrospective CHEST 2) Flash helical ABDOMEN/PELVIS. Chest gated for aortic root. AP flash arterial

    === "Nursing Notes"

        - 20G IV minimum

    === "Radiologist Notes"
        - Gated chest: assess aortic root valve coronaries. Flash AP: assess aorta and branches. Combined cardiac and vascular

    === "Tips & Tricks"

        - Arms up. Careful timing between gated and flash acquisitions

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Gated CTA CAP Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (140 mL)    :active, contrast, 00:00, 35s
      Saline (50mL)          :active, saline, after contrast, 12s
      section Arterial Phase
      Gated CTA Chest    :crit, scan1, 00:25, 12s
      section Arterial Phase
      Flash CTA AP    :crit, scan2, after scan1, 25s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Thoracic inlet | Pubic symphysis | N/A | N/A | Full AP lateral |
    | Gated CTA Chest | Thoracic inlet | Diaphragm | Bolus tracked | 0.5-0.625 mm | Retrospective gating chest |
    | Flash CTA AP | Diaphragm | Pubic symphysis | Immediate after chest | 0.625 mm | High pitch helical - no gating |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto ECG chest / High mAs AP |
    | Rotation Time | 0.28 chest / 0.5 APs |
    | Pitch | 0.2-0.24 chest / 1.2-1.5 AP |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated chest | Chest | 0.75 mm/0.75 mm | Cardiac | 3 | Aortic root and valve |
    | Axial | Flash AP | Abdomen/Pelvis | 2 mm/2 mm | Vascular | 3 | Abdominal aorta and branches |
    | Coronal | Both | Full CAP | 2.5 mm/2.5 mm | Vascular | 3 | MIP full aorta |
    | Sagittal | Both | Full CAP | 2.5 mm/2.5 mm | Vascular | 3 | Curved MPR entire aorta |


### Additional Reconstructions

Curved MPR full aorta. Aortic valve reformats. 3D VR

Category: Cardiac

Protocol Type: Cardiac Gated
