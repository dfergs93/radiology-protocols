# CT Coronary Angiogram

**Last Updated:** 2026-01-01
**Protocol Author:** Duncan Ferguson, MD
**Approved By:**

## 1. Clinical Indications

- Intermediate Chest Pain
- Anomalous coronary anatomy
- Stent or CABG patency

## 2. Patient Prep

- **IV Access:** 18-20G preferrable left upper extremity, right upper extremity, then lower extremities
- **Pre-Medication:**
- If HR > 60, consider metoprolol 5mg iv up to x 3 prn to get HR down.
- Must check BP < 100, if severe asthmatic, or 2nd/3rd degree heart block
- **Labs:** Full dose if eGFR > 30. Low dose possible using formula Max contrast volume = (eGFR*2) * (weight in kg/75).

## 3. IV Contrast & Injection Parameters

- **Agent:** Isovue 370
- **Volume:** 1.5 mL/kg
- **Flow Rate:** 3-5 mL/s, approximate 20s bolus
- **Saline Chaser:** 15 - 20s
- **Timing Method:** Bolus Tracking
  - **ROI Placement:** Ascending Aorta
  - **Trigger Hounsfield Unit (HU):** 200 Hu

## 4. Scan Parameters


| Series Name       | Start Location | End Location  | Delay (sec)   | Slice Thickness | Notes                |
| :------------------ | ---------------- | --------------- | --------------- | ----------------- | ---------------------- |
| 1. Scout/Topogram | Clavicle       | Diaphragm     | N/A           | N/A             | AP and Lateral       |
| 2. Non-Contrast   | Top of Heart   | Base of Heart | N/A           | 3 mm            | Calcium Score        |
| 3. Arterial Phase | Top of Heart   | Base of Heart | Bolus Tracked | 0.6 mm          | UHR - scan at 0.4 mm |

## 5. Reconstructions & Post-Processing


| Plane    | Acquisition  | FOV        | Slice Thickness/Step | Kernel      | IR strength | Notes                                           |
| :--------- | -------------- | ------------ | ---------------------- | ------------- | ------------- | ------------------------------------------------- |
| Axial    | Non-contrast | Heart      | 3mm/3mm              | Mediastinal | 3           | Used for Agatston score calculation             |
| Axial    | Non-contrast | Full Chest | 1mm/1mm              | Lung        | 3           | Lung Window                                     |
| Axial    | Arterial     | Heart      | 0.6mm/0.6mm          | Vascular    | 3           | Choose cardiac cycle depending on HR and motion |
| Sagittal | Arterial     | Full Chest | 3mm/3mm              | Mediastinal | 3           | Diagnostic series for non-cardiac findings      |

## 6. Acquisition Plane Examples (Optional)

<!-- To add images, place them in an 'images' folder and link to them using HTML. -->

<!-- Example: <img src="../images/ct_abdomen/abdomen_coronal_plane.png" width="300"> -->

## 7. Notes for Radiologist / Technologist

- For technologists: Ensure patient has followed oral contrast instructions precisely.
- For radiologists: Please correlate with prior imaging from [Date].
