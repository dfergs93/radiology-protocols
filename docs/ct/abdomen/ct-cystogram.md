# CT Cystogram

**Last Updated:** 2024-01-15  
**Author:** Dr. Kim

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Portal Venous | Contrast (70 sec delay) | Diaphragm to Pubic symphysis |
        | Bladder Filling | Contrast (90 sec delay) | Standard coverage |
        | Cystogram | Contrast (100 sec delay) | Iliac crests to Below bladder |
        | Post-Void | Contrast (Immediate delay) | Iliac crests to Below bladder |

    === "Clinical Indications"

        - Bladder rupture
        - Bladder injury
        - Post-operative bladder assessment
        - Hematuria with bladder concern

-   __2. Patient Prep__

    ---

    - **Position:** Supine
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:**
        - Bladder contrast: 350-400 mL dilute contrast (30 mL contrast in 350 mL saline)

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 100 mL |
        | Flow Rate | 3-4 mL/s |

    ===   "Lab Requirements"
        
        eGFR > 30 for IV. Bladder instillation via Foley



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO components: 1) CT with IV contrast portal venous 2) Bladder filling via Foley with dilute contrast 3) Scan distended bladder 4) Post-void scan. Coordinate with nursing

    === "Nursing Notes"

        - Foley catheter required. Dilute contrast preparation (30mL in 350mL saline). Gravity fill bladder. Patient signals fullness

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Foley placement. Prepare dilute contrast

    === "Radiologist Notes"

        - Portal venous: solid organs. Cystogram: bladder integrity extravasation. Post-void: small leaks

    === "Tips & Tricks"

        - Adequate bladder distension critical. Gravity fill slowly. Clamp Foley during scan

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Cystogram Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (100 mL)    :active, contrast, 00:00, 28s
      Saline (20mL)          :active, saline, after contrast, 5s
      section Portal Venous Phase
      Portal Venous    :done, scan1, 01:10, 7s
      section Scan Phase 2
      Bladder Filling    :done, scan2, 01:30, 3s
      section Scan Phase 3
      Cystogram    :done, scan3, 01:40, 5s
      section Scan Phase 4
      Post-Void    :done, scan4, after scan3, 5s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Pubic symphysis | N/A | N/A | AP |
    | Portal Venous | Diaphragm | Pubic symphysis | 70 sec | 2.5 mm | Standard IV contrast |
    | Bladder Filling | N/A | N/A | 90 sec | N/A | Fill via Foley - not scanned |
    | Cystogram | Iliac crests | Below bladder | 100 sec | 2 mm | Scan distended bladder |
    | Post-Void | Iliac crests | Below bladder | Immediate | 2 mm | Scan after drainage |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 1 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Cystogram | Pelvis | 2 mm/2 mm | Standard | 3 | Distended bladder assessment |
    | Axial | Post-void | Pelvis | 2 mm/2 mm | Standard | 3 | Look for extravasation |
    | Coronal | Cystogram | Pelvis | 2.5 mm/2.5 mm | Standard | 3 | Bladder overview |
    | Sagittal | Cystogram | Pelvis | 2.5 mm/2.5 mm | Standard | 3 | Bladder dome and base |


### Additional Reconstructions

Compare distended vs post-void. Document extravasation location. 3D reformation if complex injury

Category: Abdomen

Protocol Type: Contrast-Enhanced
