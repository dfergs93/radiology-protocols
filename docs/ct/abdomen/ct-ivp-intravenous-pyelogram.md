# CT IVP (Intravenous Pyelogram)

**Last Updated:** 2024-01-15  
**Author:** Dr. Anderson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast (optional) | Non-contrast | Top kidneys to Pubic symphysis |
        | Early Portal Venous | Contrast (60 sec from 1st delay) | Top kidneys to Iliac crests |
        | Excretory Phase | Contrast (90-120 sec from 2nd delay) | Top kidneys to Pubic symphysis |

    === "Clinical Indications"

        - Hematuria
        - Urothelial carcinoma
        - Collecting system evaluation
        - Hydronephrosis

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

        Full dose if eGFR > 30. Split bolus for combined nephrographic and excretory phases



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - COMPLEX protocol: 1) NC (optional stone protocol) 2) 1st contrast injection 3) Early PV 60s after 1st 4) WAIT 5-7 min 5) 2nd injection + saline 6) Excretory/IVP 90-120s after 2nd

    === "Nursing Notes"

        - 18-20G IV. Split bolus technique. May give Lasix 10-20mg IV for better opacification

    === "Radiologist Notes"
        - NC optional: detect stones. Early PV: renal parenchyma. Excretory: collecting system ureters bladder for urothelial lesions

    === "Tips & Tricks"

        - Split bolus critical for opacification. Lasix may help. Prone imaging optional for ureters

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT IVP (Intravenous Pyelogram) Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section First Injection
      Contrast bolus 1 (77mL)  :active, contrast1, 00:00, 19s
      Saline flush (50mL)                  :active, saline1, after contrast1, 12s
      section First Scan Phase
      First acquisition                    :crit, scan1, 00:20, 15s
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
    | Scout | Top kidneys | Pubic symphysis | N/A | N/A | AP |
    | Non-Contrast (optional) | Top kidneys | Pubic symphysis | N/A | 2 mm | Optional stone detection |
    | Early Portal Venous | Top kidneys | Iliac crests | 60 sec from 1st | 2.5 mm | Nephrographic phase |
    | Excretory Phase | Top kidneys | Pubic symphysis | 90-120 sec from 2nd | 1.25 mm | Collecting system opacification |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.375 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Non-contrast | KUB | 2 mm/2 mm | Standard | 3 | Stone detection if done |
    | Axial | Portal venous | Kidneys | 2.5 mm/2.5 mm | Standard | 3 | Renal parenchyma |
    | Axial | Excretory | Full urinary tract | 2 mm/2 mm | Standard | 3 | Urothelial surfaces |
    | Coronal | Excretory | Full urinary tract | 2.5 mm/2.5 mm | Standard | 3 | MIP urogram |


### Additional Reconstructions

MIP urogram coronal and sagittal. Curved MPR of ureters. 3D urogram

Category: Abdomen

Protocol Type: Contrast-Enhanced
