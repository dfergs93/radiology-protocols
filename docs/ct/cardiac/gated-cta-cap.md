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
        | Flash Non-contrast | Non-contrast | Thoracic inlet to Pubic symphysis |
        | Gated CTA Chest | Arterial (bolus tracked) | Thoracic inlet to Diaphragm |
        | Flash CTA AP | Contrast (Immediate after chest delay) | Diaphragm to Pubic symphysis |
        | Stent delay (optional) | Contrast (40 sec delay) | Stent coverage |

    === "Clinical Indications"

        - Aortic dissection
        - Aortic aneurysm with cardiac involvement
        - Combined cardiac and aortic pathology

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:**
        - HR < 65 target. Premedication not required.

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.6 mL/kg |
        | Flow Rate | 4 mL/s |
        | Duration | 20-24s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 180 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO acquisitions: 1) Gated retrospective CHEST 2) Flash helical ABDOMEN/PELVIS. Chest gated for aortic root. AP flash arterial

    === "Nursing Notes"

        - 20G IV minimum

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Gated chest: assess aortic root valve coronaries. Flash AP: assess aorta and branches. Combined cardiac and vascular

    === "Tips & Tricks"

        - Arms up. Careful timing between gated and flash acquisitions

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
      title Gated CTA CAP Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.6 mL/kg)    :active, contrast, 00:00, 24s
      Saline          :active, saline, after contrast, 5s
      section Chest
      Gated CTA Chest    :crit, scan1, after saline, 5s
      section Abdomen/Pelvis
      Flash CTA AP    :crit, scan2, after scan1, 5s
      section Stent Delay
      Stent Delay    :crit, scan3, 00:40, 5s
  ```

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Thoracic inlet | Pubic symphysis | N/A | N/A | Full AP lateral |
    | Flash Non-contrast | Thoracic inlet | Pubic symphysis | N/A | 0.625 mm | Non-contrast |
    | Gated CTA Chest | Thoracic inlet | Diaphragm | Bolus tracked | 0.5-0.625 mm | Retrospective gating chest |
    | Flash CTA AP | Diaphragm | Pubic symphysis | Immediate after chest | 0.625 mm | High pitch helical - no gating |
    | Stent Delay (optional) | Diaphragm | Pubic symphysis | 40 sec | 0.625 mm | Stent coverage |

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
