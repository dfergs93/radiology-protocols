# Gated CTA TMVR

**Last Updated:** 2024-01-15  
**Author:** Dr. Rodriguez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Calcium Score | Non-Contrast | Carina to Base of heart |
        | Gated CTA Chest | Arterial (bolus tracked) |  Carina to Base of heart |
        | Delayed CAP | Contrast (80 sec delay from CTA) | Diaphragm to Femoral heads |

    === "Clinical Indications"

        - Pre-TMVR planning
        - Mitral valve replacement planning
        - Mitral regurgitation

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
        | Volume | 1.1 mL/kg |
        | Flow Rate | 5 mL/s |
        | Duration | 15s |
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

        - Gated CHEST with NO DOSE PULSING (full dose all phases) + delayed 90 sec CAP. TMVR post-processing required

    === "Nursing Notes"

        - 20G IV

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Measure mitral annulus. LA size. LVOT assessment. Coronary proximity. Access vessels. TMVR-specific measurements

    === "Tips & Tricks"

        - NO dose modulation for gated chest. Full radiation all phases for valve assessment

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
      title Gated CTA TMVR Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.1 mL/kg)    :active, contrast, 00:00, 15s
      Saline          :active, saline, after contrast, 5s
      section Chest
      Gated CTA Chest    :crit, scan1, after saline, 5s
      section CAP
      Delayed CAP    :done, scan2, 01:40, 5s
  ```

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Thoracic inlet | Femoral heads | N/A | N/A | AP lateral |
    | Calcium Score | Carina | Base of heart | N/A | 2.5 mm | Calcium scoring |
    | Gated CTA Chest | Carina| Base of heart | Bolus tracked | 0.5 mm | NO DOSE PULSING - retrospective all phases |
    | Delayed CAP | Diaphragm | Femoral heads | 90 sec | 0.625 mm | Access planning and coronaries |

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
    | Axial | Calcium Score | Apex of heart to Base of heart | 2.5 mm/2.5 mm | Cardiac | 3 | Calcium scoring |
    | Axial | Gated chest | Heart | 0.5 mm/0.5 mm | Cardiac | 3 | Mitral valve measurements |
    | Axial | Delayed CAP | AP | 2 mm/2 mm | Vascular | 3 | Access vessels |
    | Double oblique | Gated chest | Mitral valve | 0.5 mm | Cardiac | 3 | En face mitral annulus |
    | 3D VR | Delayed CAP | Iliofemoral | 1.5 mm | Vascular | 3 | Access planning |


### Additional Reconstructions

TMVR measurements: annulus dimensions. LVOT area. Coronary heights. LA volume. Access vessels

Category: Cardiac

Protocol Type: Cardiac Gated
