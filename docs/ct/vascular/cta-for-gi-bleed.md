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
        | Arterial Phase | Contrast (25 sec delay) | Diaphragm to Pubic symphysis |
        | Portal Venous Phase | Contrast (70 sec delay) | Diaphragm to Pubic symphysis |
        | Delayed Phase | Contrast (90-180 sec delay) | Diaphragm to Pubic symphysis |

    === "Clinical Indications"

        - Active GI bleeding
        - Hematemesis
        - Melena with hemodynamic instability
        - Hematochezia

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** eGFR > 30 preferred but can proceed emergently
        - **Allergy:** Document allergy history. Emergency indication overrides mild allergy
    
    - **Position:** Supine with arms raised
    - **NPO Status:** NPO if possible (emergent study)
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 125 mL |
        | Flow Rate | 5 mL/s |
        | Timing Method | Triple phase: Arterial + Portal Venous + Delayed |
        | ROI Placement | Abdominal aorta |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Can proceed with eGFR > 30 in emergency. Document medical necessity



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - High flow rate critical for arterial phase. Scan arterial at 25 sec then portal at 70 sec then delayed at 90-180 sec. Look for active extravasation

    === "Nursing Notes"

        - Large bore IV 18-20G essential. Must achieve 5 mL/s flow rate. Verify with saline test

    === "Radiologist Notes"
        - Look for arterial extravasation (early) and pooling (delayed). Note location and potential source vessel

    === "Tips & Tricks"

        - Arms raised to avoid artifacts. Fast table speed to cover area quickly in arterial phase

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CTA for GI Bleed Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (125 mL)    :active, contrast, 00:00, 25s
      Saline (50mL)          :active, saline, after contrast, 10s
      section Arterial Phase
      Arterial Phase    :crit, scan1, 00:25, 25s
      section Portal Venous Phase
      Portal Venous Phase    :done, scan2, 01:10, 25s
      section Delayed Phase
      Delayed Phase    :done, scan3, 01:30, 25s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Diaphragm | Pubic symphysis | N/A | N/A | AP scout |
    | Arterial Phase | Diaphragm | Pubic symphysis | 25 sec | 0.625 mm | High flow rate 5 mL/s critical |
    | Portal Venous Phase | Diaphragm | Pubic symphysis | 70 sec | 0.625 mm | Standard portal venous timing |
    | Delayed Phase | Diaphragm | Pubic symphysis | 90-180 sec | 0.625 mm | Extended delay to see pooling of contrast |

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
    | Axial | Portal venous | Full AP | 2.5 mm/2.5 mm | Standard | 3 | Confirm bleeding and assess organs |
    | Axial | Delayed | Full AP | 2.5 mm/2.5 mm | Standard | 3 | Look for contrast pooling in bowel |
    | Coronal | All phases | Full AP | 3 mm/3 mm | Standard | 3 | MIP to track extravasation |


### Additional Reconstructions

MIP of all three phases side-by-side for comparison

Category: Vascular

Protocol Type: Vascular
