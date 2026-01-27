# CT Coronary Angiogram 

**Last Updated:** 2023-10-28
**Author:** Dr. John Smith

---

<div class="grid cards" markdown>

-   __1. Clinical Indications__

    ---
    - Intermediate Chest Pain
    - Anomalous coronary anatomy
    - Stent or CABG patency

-   __2. Patient Prep__

    ---
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30.
        - **Allergy:** Check history & follow pre-medication protocol if needed.

    - **Patient Positioning:** Supine, feet-first
    - **NPO Status:** No caffeine before study.
    - **Pre-Medication:**
      - If HR > 60, consider metoprolol 5mg iv up to x 3 prn to get HR down.
      - Must check BP < 100, if severe asthmatic, or 2nd/3rd degree heart block
      - Nitroglycerin 0.4 mg sl, give before angiogram.

-   __3. IV Contrast & Injection__

    ---
    - **Agent:** Isovue 370
    - **Volume:** 1.1 mL/kg
    - **Flow Rate:** 3-5 mL/s, approximate 20s bolus
    - **Timing Method:** Bolus Tracking
      - **ROI Placement:** Ascending Aorta
      - **Trigger Hounsfield Unit (HU):** 200 Hu
    - **Labs:** Full dose if eGFR > 30. Low dose possible using formula Max contrast volume = (eGFR*2) * (weight in kg/75).

-   __4. Special Notes__

    ---

    === "Tech Notes"

        - Make sure right patient
        - Confirm gating strategy
        - Coach patient through breathing strategy
    
    === "Nursing Notes"

        - Check for medication contraindications
        - Preference for nitroglycerin over metoprolol if borderline BP, but call radiologist to check
        - Check under tongue to make sure nitro has dissolved
    
    === "Radiologist Notes"

        - Quality Check for cardiac motion or breathing motion

</div>

### Protocol Details
  ```mermaid
      gantt
          title CT Contrast Protocol Timeline
          dateFormat mm:ss
          axisFormat %M:%S
          
          section Contrast
          Contrast bolus (80mL)    :active, contrast, 00:00, 20s
          Saline chaser (20mL)      :active, saline, after contrast, 5s
          
          section Coronary
          Arterial phase            :crit, chest_art, 00:25, 5s
          
  ```

<!-- This is our main set of role-based tabs -->
=== "For Radiologist (Overview)"

    #### Scan & Reconstruction Summary

    | Phase / Type         | Series / Recon Name | Key Features & Notes                                     |
    | :------------------- | :------------------ | :------------------------------------------------------- |
    | **Scan Acquisition** |                     |                                                          |
    |                      | Non-Contrast        | Covers the heart, for Calcium Score                      |
    |                      | Arterial            | Covers the heart, retrospective gating scanned at 0.6 mm |

=== "For Technologist (Full Protocol)"
    
    !!! tip "Reduce Artifact"
        Ensure patient's arms are raised fully above their head to avoid beam hardening artifact through the upper abdomen.

    #### Scan Parameters
    
    | Series Name       | Start Location | End Location  | Delay (sec)   | Slice Thickness | Notes                |
    | :---------------- | -------------- | ------------- | ------------- | --------------- | -------------------- |
    | 1. Scout/Topogram | Clavicle       | Diaphragm     | N/A           | N/A             | AP and Lateral       |
    | 2. Non-Contrast   | Top of Heart   | Base of Heart | N/A           | 3 mm            | Calcium Score        |
    | 3. Arterial Phase | Top of Heart   | Base of Heart | Bolus Tracked | 0.6 mm          | UHR - scan at 0.4 mm |

    #### Post-Processing Instructions

    | Plane    | Acquisition  | FOV        | Slice Thickness/Step | Kernel      | IR strength | Notes                                           |
    | :------- | ------------ | ---------- | -------------------- | ----------- | ----------- | ----------------------------------------------- |
    | Axial    | Non-contrast | Heart      | 3mm/3mm              | Mediastinal | 3           | Used for Agatston score calculation             |
    | Axial    | Non-contrast | Full Chest | 1mm/1mm              | Lung        | 3           | Lung Window                                     |
    | Axial    | Arterial     | Heart      | 0.6mm/0.6mm          | Vascular    | 3           | Choose cardiac cycle depending on HR and motion |
    | Sagittal | Arterial     | Full Chest | 3mm/3mm              | Mediastinal | 3           | Diagnostic series for non-cardiac findings      |
