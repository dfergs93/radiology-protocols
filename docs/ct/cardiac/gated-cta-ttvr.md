# Gated CTA TTVR

**Last Updated:** 2024-01-15  
**Author:** Dr. Jackson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Gated CTA Chest | Arterial (bolus tracked) | Top of heart to Below heart |
        | Delayed CAP | Contrast (90 sec delay from CTA) | Diaphragm to Femoral heads |

    === "Clinical Indications"

        - Pre-TTVR planning
        - Tricuspid valve replacement planning
        - Tricuspid regurgitation

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    - **Pre-Medication:**
        - HR < 65 target. Premedication not required.

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | IsoVue 370 |
        | Volume | 2.0 mL/kg |
        | Flow Rate | 3.5 mL/s |
        | Duration | 30-50s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 180 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)
        There is a lower limit of 120 mL of contrast needed for the exam.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Gated CHEST with NO DOSE PULSING + delayed 90 sec CAP. TTVR post-processing required

    === "Nursing Notes"

        - 20G IV

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Measure tricuspid annulus. RA size. RV function. Coronary proximity. Access vessels. TTVR-specific measurements

    === "Tips & Tricks"

        - NO dose modulation. Full dose all cardiac phases

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
      title Gated CTA TTVR Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (140 mL)    :active, contrast, 00:00, 40s
      Saline          :active, saline, after contrast, 5s
      section Chest
      Gated CTA Chest    :crit, scan1, after saline, 5s
      section CAP
      Delayed CAP    :done, scan2, 02:15, 5s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Thoracic inlet | Femoral heads | N/A | N/A | AP lateral |
    | Gated CTA Chest | Top of heart | Below heart | Bolus tracked | 0.5 mm | NO DOSE PULSING - all phases |
    | Delayed CAP | Diaphragm | Femoral heads | 90 sec | 0.625 mm | Access planning |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | NO ECG MODULATION chest / Auto AP |
    | Rotation Time | 0.28 / 0.5s |
    | Pitch | 0.2-0.24 / 1.2-1.5 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated chest | Heart | 0.5 mm/0.5 mm | Cardiac | 3 | Tricuspid valve measurements |
    | Axial | Delayed CAP | AP | 2 mm/2 mm | Vascular | 3 | Access assessment |
    | Double oblique | Gated chest | Tricuspid valve | 0.5 mm | Cardiac | 3 | En face tricuspid annulus |
    | 3D VR | Delayed CAP | Iliofemoral | 1.5 mm | Vascular | 3 | Access planning |


### Additional Reconstructions

TTVR measurements: annulus dimensions area perimeter. RA volume. RV function. Coronary proximity. Access vessels

Category: Cardiac

Protocol Type: Cardiac Gated
