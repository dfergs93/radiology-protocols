# Coronary CTA

**Last Updated:** 2024-01-15  
**Author:** Dr. Johnson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | Non-contrast | Top of heart to Below heart |
        | Gated CTA | Arterial (bolus tracked) | Top of heart to Below heart |

    === "Clinical Indications"

        - Intermediate chest pain
        - Suspected infarct
        - Coronary artery dissection or aneurysm
        - Anomalous coronary artery
        - Stent patency

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check metoprolol contraindications. BP > 100 required
    
    - **Position:** Supine feet-first
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:** 
      HR < 60 target. Metoprolol 5mg IV increments up to 15mg. Nitro 0.4mg SL before scan


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.1-1.3 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 200 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Retrospective ECG gating. 3mm slices. Cover entire heart. 75% R-R interval typical. Ensure ECG leads well connected

    === "Nursing Notes"

        - 20G IV minimum. HR control critical - target < 60. Nitro administration

    === "Radiologist Notes"
        - Calculate Agatston score. Give CAD-RADS score. Check function look for potential focal wall motion abnormalities

    === "Tips & Tricks"

        - Full chest coverage essential. Extended FOV. Low pitch for retrospective gating

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Coronary CTA Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.1-1.3 mL/kg)    :active, contrast, 00:00, 17s
      Saline (50mL)          :active, saline, after contrast, 11s
      section Arterial Phase
      Gated CTA    :crit, scan1, 00:25, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Thoracic inlet | Below heart | N/A | N/A | AP lateral |
    | Non-contrast | Top of heart | Below heart | N/A | 3 mm | Calcium score |
    | Gated CTA | Top of heart | Below heart | Bolus tracked | 0.5-0.625 mm | Retrospective gating |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto ECG modulation |
    | Rotation Time | 0.28s |
    | Pitch | 0.2-0.24 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated CTA | Heart | 0.75 mm/0.5 mm | Cardiac | 3 | Thin slice for grafts and native vessels |
    | Curved MPR | Gated CTA | Heart | 0.75 mm | Cardiac | 3 | Vessels |
    | Axial | Gated CTA | Heart | 0.75 mm/0.5 mm | Cardiac | 3 | Native coronary assessment |
    | 3D VR | Gated CTA | Heart/grafts | 0.5 mm source | Cardiac | 3 | 3D overview grafts and native vessels |


### Additional Reconstructions

Curved MPR of all grafts. Label LIMA RIMA SVG. 3D VR color-coded

Category: Cardiac

Protocol Type: Vascular
