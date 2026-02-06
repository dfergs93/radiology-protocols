# CT Triple Phase Liver

**Last Updated:** 2024-01-15  
**Author:** Dr. Lee

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast | Non-contrast | Diaphragm to Iliac crests |
        | Late Arterial | Arterial (bolus tracked) | Diaphragm to Iliac crests |
        | Portal Venous | Contrast (70 sec delay) | Diaphragm to Pubic symphysis |
        | Delayed Phase | Contrast (300 sec delay) | Diaphragm to Iliac crests |

    === "Clinical Indications"

        - Liver lesion characterization
        - HCC surveillance
        - Liver mass protocol

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    - **Pre-Medication:**
        - None typically. Oral contrast optional

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Triple phase: NC + Arterial + Portal Venous + Delayed |
        | ROI Placement | Abdominal aorta |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - FOUR acquisitions: 1) NC abdomen 2) Late arterial (bolus track or 30-35s) 3) Portal venous 70s 4) Delayed 5 min. FOV: Abdomen for NC/Art/Delay. Full AP for PV

    === "Nursing Notes"

        - 18-20G IV. High flow rate critical

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - NC: characterize lesion. Arterial: hypervascular lesions HCC. Portal: most liver lesions. Delayed: washout pattern

    === "Tips & Tricks"

        - High flow rate. Extended 5 min delay. Breath hold coaching

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Triple Phase Liver Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.5 mL/kg)    :active, contrast, 00:00, 25s
      Saline (20mL)          :active, saline, after contrast, 4s
      section Arterial Phase
      Late Arterial    :crit, scan1, 00:30, 7s
      section Portal Venous Phase
      Portal Venous    :done, scan2, 01:10, 7s
      section Delayed Phase
      Delayed Phase    :done, scan3, 05:00, 7s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Iliac crests | N/A | N/A | AP |
    | Non-Contrast | Diaphragm | Iliac crests | N/A | 2.5 mm | Liver FOV |
    | Late Arterial | Diaphragm | Iliac crests | 30-35 sec or bolus track | 1.25 mm | Liver FOV - hypervascular lesions |
    | Portal Venous | Diaphragm | Pubic symphysis | 70 sec | 2.5 mm | Full AP FOV |
    | Delayed Phase | Diaphragm | Iliac crests | 300 sec | 2.5 mm | Liver FOV - washout assessment |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto (reference 200-250) |
    | Rotation Time | 0.5s |
    | Pitch | 0.9-1.0 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | All phases | Liver | 2.5 mm/2.5 mm | Standard | 3 | Compare all phases |
    | Axial | Portal venous | Full AP | 2.5 mm/2.5 mm | Standard | 3 | Full abdomen pelvis PV |
    | Coronal | All phases | Liver | 3 mm/3 mm | Standard | 3 | Coronal comparison |
    | Subtraction | Arterial - NC | Liver | 2.5 mm | Standard | 3 | Enhance lesion conspicuity |


Category: Abdomen

Protocol Type: Contrast-Enhanced
