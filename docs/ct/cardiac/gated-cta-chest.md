# Gated CTA Chest

**Last Updated:** 2024-01-15  
**Author:** Dr. Anderson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | Non-contrast | Top of heart to Below heart |
        | Gated CTA | Arterial (bolus tracked) | Top of heart to Below heart |
        | Stent delay (optional) | Contrast (40 sec delay) | Top of heart to Below heart |

    === "Clinical Indications"

        - Coronary artery disease
        - Chest pain
        - Anomalous coronaries
        - Coronary CTA

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check metoprolol contraindications
    
    - **Position:** Supine feet-first
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:** 
      HR < 60 target. Metoprolol 5mg IV up to 15mg total. Nitro 0.4mg SL. Check BP > 100


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.1 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 200 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Retrospective ECG gating. Cover heart. Bolus tracking in ascending aorta. Optional stent protocol: add 40 sec delayed phase

    === "Nursing Notes"

        - 20G IV minimum. HR control critical. Nitro administration. Monitor BP

    === "Radiologist Notes"
        - Assess coronaries for stenosis plaque. Evaluate anomalous anatomy. Stent patency if applicable. Cardiac function from multi-phase

    === "Tips & Tricks"

        - HR control essential. Coach breathing. Gating quality check

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Gated CTA Chest Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.1 mL/kg)    :active, contrast, 00:00, 17s
      Saline (50mL)          :active, saline, after contrast, 11s
      section Arterial Phase
      Gated CTA    :crit, scan1, 00:25, 10s
      section Delayed Phase
      Stent delay (optional)    :done, scan2, 00:40, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Top of chest | Diaphragm | N/A | N/A | AP lateral |
    | Non-contrast | Top of heart | Below heart | N/A | 3 mm | Calcium score |
    | Gated CTA | Top of heart | Below heart | Bolus tracked | 0.5-0.625 mm | Retrospective ECG gating |
    | Stent delay (optional) | Top of heart | Below heart | 40 sec | 0.5-0.625 mm | Optional for stent assessment |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto ECG modulation |
    | Rotation Time | 0.28s |
    | Pitch | 0.2-0.24 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated CTA | Heart | 0.75 mm/0.5 mm | Cardiac | 3 | Primary coronary assessment |
    | Curved MPR | Gated CTA | Each coronary | 0.75 mm | Cardiac | 3 | Vessel-specific reconstructions |
    | Axial | Non-contrast | Heart | 3 mm/3 mm | Standard | 3 | Calcium scoring |
    | Short/long axis | Gated CTA | Heart | Multi-phase | Cardiac | 3 | Functional assessment |


### Additional Reconstructions

Curved MPR all coronaries. Short/long axis. Multi-phase for function. Calcium score

Category: Cardiac

Protocol Type: Cardiac Gated
