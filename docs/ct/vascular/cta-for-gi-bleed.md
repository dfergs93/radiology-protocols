# CTA for GI Bleed

**Last Updated:** 2026-01-05  
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | Non-contrast | Diaphragm to Pubic symphysis |
        | Arterial Phase | Contrast (25 sec delay) | Diaphragm to Pubic symphysis |
        | Delayed Phase | Contrast (90 sec delay) | Diaphragm to Pubic symphysis |

    === "Clinical Indications"

        - Active GI bleeding
        - Hematemesis
        - Melena with hemodynamic instability
        - Hematochezia

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO if possible (emergent study)
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Duration | 20s |
        | Timing Method | Triple phase: Arterial + Portal Venous + Delayed |
        | ROI Placement | Abdominal aorta |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - High flow rate critical for arterial phase. Scan arterial at 25 sec then portal at 70 sec then delayed at 90-180 sec. Look for active extravasation

    === "Nursing Notes"

        - Large bore IV 18-20G essential. Verify with saline test

        !!! warning "Safety First"
            - **Renal Function:** eGFR > 30 preferred but can proceed emergently
            - **Allergy:** Document allergy history. Emergency indication overrides mild allergy

    === "Radiologist Notes"

        - Look for arterial extravasation (early) and pooling (delayed). Note location and potential source vessel

    === "Tips & Tricks"

        - Arms raised to avoid artifacts. Fast table speed to cover area quickly in arterial phase

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Diaphragm | Pubic symphysis | N/A | N/A | AP scout |
    | Arterial Phase | Diaphragm | Pubic symphysis | 25 sec | 0.625 mm | High flow rate 5 mL/s critical |
    | Delayed Phase | Diaphragm | Pubic symphysis | 90 sec | 0.625 mm | Extended delay to see pooling of contrast |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto (reference 300) |
    | Rotation Time | 0.5s |
    | Pitch | 1.375 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Full AP | 2.5 mm/2.5 mm | Standard | 3 | Look for arterial blush/extravasation |
    | Axial | Delayed | Full AP | 2.5 mm/2.5 mm | Standard | 3 | Look for contrast pooling in bowel |
    | Coronal | All phases | Full AP | 3 mm/3 mm | Standard | 3 | MIP to track extravasation |

### Additional Reconstructions

MIP of all three phases side-by-side for comparison

Category: Vascular

Protocol Type: Vascular
