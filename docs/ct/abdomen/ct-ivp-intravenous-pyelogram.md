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
        | Early Portal Venous | Contrast (60 sec from 1st injection) | Top kidneys to Iliac crests |
        | Excretory Phase | Contrast (90-120 sec from 2nd injection) | Top kidneys to Pubic symphysis |

    === "Clinical Indications"

        - Hematuria
        - Urothelial carcinoma
        - Collecting system evaluation
        - Hydronephrosis

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | Split bolus: 1st injection 1.1 mL/kg + 2nd injection 0.4 mL/kg |
        | Flow Rate | 4 mL/s |
        | Timing | Split bolus technique |

    ===   "Lab Requirements"

        Full dose if eGFR > 30. Split bolus for combined nephrographic and excretory phases



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - COMPLEX protocol: 1) NC (optional stone protocol) 2) 1st contrast injection 3) Early PV 60s after 1st 4) WAIT 5-7 min 5) 2nd injection + saline 6) Excretory/IVP 90-120s after 2nd

    === "Nursing Notes"

        - 18-20G IV. Split bolus technique. May give Lasix 10-20mg IV for better opacification

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - NC optional: detect stones. Early PV: renal parenchyma. Excretory: collecting system ureters bladder for urothelial lesions

    === "Tips & Tricks"

        - Split bolus critical for opacification. Lasix may help. Prone imaging optional for ureters

</div>


### Protocol Details
  ```mermaid
  ---
  displayMode: compact
  config:
    theme: default
    themeCSS: " #Saline{ fill: #4ed5ff; stroke: #2094f3; } "
  ---
    gantt
      title CT IVP (Intravenous Pyelogram) Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast bolus 1 (1.1mL/kg)  :active, contrast1, 00:00, 19s
      Saline                  :active, saline1, after contrast1, 5s
      Contrast bolus 2 (0.4mL/kg)  :active, contrast2, 07:00, 7s
      Saline                  :active, saline2, after contrast2, 5s
      section First Scan Phase
      First acquisition                    :crit, scan1, 00:20, 10s
      section Second Scan Phase
      Second acquisition                   :done, scan2, 09:00, 10s
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
