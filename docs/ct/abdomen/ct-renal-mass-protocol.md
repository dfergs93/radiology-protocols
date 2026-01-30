# CT Renal Mass Protocol

**Last Updated:** 2024-01-15  
**Author:** Dr. Davis

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast | Non-contrast | Top kidneys to Iliac crests |
        | Corticomedullary | Contrast (20 sec after 1st injection delay) | Top kidneys to Iliac crests |
        | Nephrographic/IVP | Contrast (90-120 sec after 2nd injection delay) | Top kidneys to Pubic symphysis |

    === "Clinical Indications"

        - Renal mass characterization
        - Renal cell carcinoma staging
        - Complex cyst evaluation

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history
    
    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Contrast Details"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | Split bolus: 1st injection 1.1 mL/kg + 2nd injection 0.4 mL/kg |
        | Flow Rate | 4 mL/s |
        | Timing | Split bolus technique |

    ===   "Contrast Notes"

        Full dose if eGFR > 30. Split bolus technique



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - COMPLEX protocol: 1) NC 2) 1st contrast injection 3) Arterial 20s after 1st 4) WAIT 5-7 min 5) 2nd injection + saline 6) IVP/nephrographic 90-120s after 2nd

    === "Nursing Notes"

        - 18-20G IV. Explain split bolus technique and delay

    === "Radiologist Notes"
        - NC: fat/calcification. Arterial: vascular anatomy and hypervascular masses. Nephrographic/IVP: delayed enhancement and collecting system

    === "Tips & Tricks"

        - Split bolus timing critical. 5-7 min wait between injections

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Renal Mass Protocol Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section First Injection
      Contrast bolus 1 (77mL)  :active, contrast1, 00:00, 19s
      Saline flush (50mL)                  :active, saline1, after contrast1, 12s
      section First Scan Phase
      First acquisition                    :crit, scan1, after scan1, 15s
      section Wait Period
      Wait for second injection            :milestone, wait, after scan1, 05:00
      section Second Injection
      Contrast bolus 2 (28mL)  :active, contrast2, after wait, 7s
      Saline flush (50mL)                  :active, saline2, after contrast2, 12s
      section Second Scan Phase
      Second acquisition                   :done, scan2, after saline2, 20s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Iliac crests | N/A | N/A | AP |
    | Non-Contrast | Top kidneys | Iliac crests | N/A | 2.5 mm | Baseline - detect fat/calcium |
    | Corticomedullary | Top kidneys | Iliac crests | 20 sec after 1st injection | 1.25 mm | Arterial/nephrographic |
    | Nephrographic/IVP | Top kidneys | Pubic symphysis | 90-120 sec after 2nd injection | 1.25 mm | Delayed enhancement + collecting system |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 1 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Non-contrast | Kidneys | 2.5 mm/2.5 mm | Standard | 3 | Characterize mass |
    | Axial | Corticomedullary | Kidneys | 1.5 mm/1.5 mm | Standard | 3 | Vascular and cortical enhancement |
    | Axial | Nephrographic | Kidneys to pelvis | 2 mm/2 mm | Standard | 3 | Mass enhancement + urinary opacification |
    | Coronal | All phases | Kidneys | 2.5 mm/2.5 mm | Standard | 3 | Compare enhancement phases |


### Additional Reconstructions

Compare NC vs arterial vs nephrographic. Measure HU in mass. MIP urogram

Category: Abdomen

Protocol Type: Contrast-Enhanced
