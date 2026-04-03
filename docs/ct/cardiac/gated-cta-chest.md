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
        | Stent delay (optional) | Contrast (40 sec delay) | Stent coverage |

    === "Clinical Indications"

        - Thoracic aortic dissection
        - Chest pain radiating to the back
        - Follow up thoracic aortic aneurysm

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet-first
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:**
        - HR < 60 target. Premedication not required.

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.1 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Duration | 20s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 200 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Retrospective ECG gating. Cover heart. Bolus tracking in ascending aorta. Optional stent protocol: add 40 sec delayed phase

    === "Nursing Notes"

        - 20G IV minimum. HR control critical. Nitro administration. Monitor BP

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check metoprolol contraindications

    === "Radiologist Notes"

        - Assess coronaries for stenosis plaque. Evaluate anomalous anatomy. Stent patency if applicable. Cardiac function from multi-phase

    === "Tips & Tricks"

        - HR control essential. Coach breathing. Gating quality check

</div>

<div class="acquisition-diagram"></div>

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
