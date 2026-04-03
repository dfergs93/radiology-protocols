# CTA Chest Abdomen Pelvis

**Last Updated:** 2024-01-15  
**Author:** Dr. Smith

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | Non-contrast | Thoracic inlet to Pubic symphysis |
        | CTA Arterial | Arterial (bolus tracked) | Thoracic inlet to Pubic symphysis |
        | Stent Delay (optional) | Delayed (40 sec delay) | 1cm above and below stent  |
        | Vasculitis Delayed (optional) | Delayed (90 sec delay) | Thoracic inlet to Pubic symphysis |

    === "Clinical Indications"

        - Aortic aneurysm
        - Vasculitis
        - Trauma pan-scan

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised above head
    - **NPO Status:** NPO 2-4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.1 mL/kg |
        | Flow Rate | 4 mL/s |
        | Duration | 20s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Descending thoracic aorta |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Single acquisition from thoracic inlet to pubic symphysis. Caudocranial direction. Bolus track in descending aorta

    === "Nursing Notes"

        - 20G IV minimum. Antecubital or proximal forearm preferred

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Assess entire aorta for dissection/aneurysm. Measure aortic dimensions. Check branch vessels

    === "Tips & Tricks"

        - Arms completely raised. ECG monitoring if known dissection

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Thoracic inlet | Pubic symphysis | N/A | N/A | AP and lateral |
    | CTA Arterial | Thoracic inlet | Pubic symphysis | Bolus tracked | 0.625 mm | Caudocranial from feet to head |
    | Stent Delay (optional) | Top of Stent | Bottom of Stent | 40 sec | 0.625 mm | Stent coverage |
    | Vasculitis Delayed (optional) | Thoracic inlet | Pubic symphysis | 90 sec | 0.625 mm | Wall enhancement/thickening |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.2 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Chest | 2 mm/2 mm | Vascular | 3 | Thoracic aorta evaluation |
    | Axial | Arterial | Abdomen/Pelvis | 2.5 mm/2.5 mm | Vascular | 3 | Abdominal aorta and branches |
    | Coronal | Arterial | Full CAP | 3 mm/3 mm | Vascular | 3 | MIP full aorta overview |
    | Sagittal | Arterial | Full CAP | 3 mm/3 mm | Vascular | 3 | Sagittal MIP and curved MPR of aorta |

### Additional Reconstructions

3D VR and curved MPR of entire aorta

Category: Vascular

Protocol Type: Vascular
