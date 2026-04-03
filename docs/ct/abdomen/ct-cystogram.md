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
        | Non-Contrast | Non-Contrast | Diaphragm to Pubic symphysis |
        | Cystogram | Contrast (100 sec delay) | Diaphragm to Pubic symphysis |

    === "Clinical Indications"

        - Bladder rupture
        - Bladder injury
        - Post-operative bladder assessment

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
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO components: 1) Non-contrast CT 2) Bladder filling via Foley with dilute contrast 3) Scan distended bladder. Coordinate with nursing

    === "Nursing Notes"

        - Foley catheter required. Dilute contrast preparation (30mL in 350mL saline). Gravity fill bladder. Patient signals fullness

        !!! warning "Safety First"
            - **Renal Function:** eGFR doesn't matter, contrast not excreted
            - **Allergy:** Foley placement. Prepare dilute contrast

    === "Radiologist Notes"

        - Cystogram: bladder integrity extravasation

    === "Tips & Tricks"

        - Adequate bladder distension critical. Gravity fill slowly. Clamp Foley during scan

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Pubic symphysis | N/A | N/A | AP |
    | Non-Contrast | Diaphragm | Pubic symphysis | 70 sec | 2.5 mm | Standard IV contrast |
    | Bladder Filling | N/A | N/A | 90 sec | N/A | Fill via Foley - not scanned |
    | Cystogram | Iliac crests | Below bladder | 100 sec | 2 mm | Scan distended bladder |

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
    | Axial | Non-Contrast | Pelvis | 2 mm/2 mm | Standard | 3 | Pre-contrast |
    | Axial | Cystogram | Pelvis | 2 mm/2 mm | Standard | 3 | Distended bladder assessment |
    | Coronal | Cystogram | Pelvis | 2.5 mm/2.5 mm | Standard | 3 | Bladder overview |
    | Sagittal | Cystogram | Pelvis | 2.5 mm/2.5 mm | Standard | 3 | Bladder dome and base |

### Additional Reconstructions

Compare distended vs non-contrast. Document extravasation location. 3D reformation if complex injury

Category: Abdomen

Protocol Type: Contrast-Enhanced
