# Coronary CTA Post-CABG

**Last Updated:** 2026-02-02  
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Calcium Score | Non-contrast | Lung apices to Diaphragm |
        | Gated CTA | Arterial (bolus tracked) | Lung apices to 2cm below heart apex |

    === "Clinical Indications"

        - Post-CABG graft patency assessment
        - Recurrent chest pain post-bypass

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet-first
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:**
        - HR < 60 target.
        - **Metoprolol** 5mg IV increments up to 15mg. Metoprolol contraindications include sBP < 100, 2nd/3rd degree heart block, and inhaler dependent asthma.
        - **Nitroglycerin** 0.4mg SL 5 minutes before scan. Nitroglycerin contraindications include sBP < 100, PDE5 inhibitors within 48 hrs, severe aortic stenosis.

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
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Non-valsalva breathing technique, cardiac breathing instruction. Put in study notes if patient unable to follow breathing instructions.
        - If high HR variability, can trigger by millisecond (200ms - 450 ms pulse range). Revolution CT is better for Afib.
        - Target End diastole if HR < 65bpm. Target End systole if HR > 86bpm. Target End diastole to End systole if HR 66 - 75 bpm

    === "Nursing Notes"

        - 20G IV minimum. Check for metoprolol or nitroglycerin contraindications. Nitro is priority over metoprolol if BP is borderline.

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Assess all grafts: LIMA RIMA SVG. Check anastomoses. Native vessel disease. Graft patency vs occlusion. Check functional series for WMA.

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
      title Coronary CTA Post-CABG Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.1 mL/kg)    :active, contrast, 00:00, 18s
      Saline (20mL)          :active, saline, after contrast, 4s
      section Arterial Phase
      Gated CTA    :crit, scan1, after contrast, 5s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Thoracic inlet | Below heart | N/A | N/A | AP lateral |
    | Calcium Score | Lung apices | Diaphragm | N/A | 1.5 mm | Calcium score |
    | Gated CTA | Lung apices | 2cm below heart apex | Bolus tracked | 0.5-0.625 mm | Retrospective gating - full chest FOV |

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
    | Axial | Calcium score | Chest | 3 mm/3 mm | Standard | 3 | For Agatston score calculation |
    | Axial | Gated CTA | Full chest | 0.6 mm/0.6 mm | Cardiac | 3 | Thin slice for grafts and native vessels |
    | Sagittal | Gated CTA | Chest | 2 mm/2 mm | Standard | 3 | Extracardiac assessment |
    | 3D VR | Gated CTA | Heart/grafts | 0.5 mm source | Cardiac | 3 | MPRs by 3D lab |


### Additional Reconstructions

Curved MPR of all grafts. Label LIMA RIMA SVG.

Category: Cardiac

Protocol Type: Vascular
