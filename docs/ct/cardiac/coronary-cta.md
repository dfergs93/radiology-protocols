# Coronary CTA

**Last Updated:** 2026-02-02  
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Calcium Score | Non-contrast | Carina to Below heart |
        | Gated CTA | Arterial (bolus tracked) | 2cm above LAD to 2cm below heart apex |

    === "Clinical Indications"

        - Intermediate chest pain
        - Suspected infarct
        - Coronary artery dissection or aneurysm
        - Anomalous coronary artery
        - Stent patency

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
        
        Full dose if eGFR > 30, If low eGFR can use low dose calculation **Maximum Contrast Dose** = [(Patient Weight in kg/75 kg) * eGFR] *2



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
      Contrast (1.1 mL/kg)    :active, contrast, 00:00, 18s
      Saline (20mL)          :active, saline, after contrast, 4s
      section Arterial Phase
      Gated CTA    :crit, scan1, after contrast, 5s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Thoracic inlet | Below heart | N/A | N/A | AP lateral |
    | Calcium Score | Carina | Below heart | N/A | 3 mm | Calcium score |
    | Gated CTA | 2cm above LAD | 2cm below heart apex | Bolus tracked | 0.5-0.625 mm | Retrospective gating |

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
    | Axial | Calcium score | Heart | 3 mm/3 mm | Standard | 3 | For Agatston score calculation |
    | Axial | Calcium score | Chest | 1.5 mm/1.5 mm | Lung | 3 | Lung FOV for Extracardiac findings |
    | Axial | Gated CTA | Heart | 0.625 mm/0.625 mm | Cardiac | 3 | Native coronary assessment |
    | 3D VR | Gated CTA | Heart | 0.5 mm source | Cardiac | 3 | MPRs by 3D lab |


### Additional Reconstructions

Curved MPR of all coronaries.

Category: Cardiac

Protocol Type: Vascular
