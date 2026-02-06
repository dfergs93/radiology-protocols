# Endocarditis/Cardiac Mass

**Last Updated:** 2026-02-02  
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | Non-contrast | Top of heart to Below heart |
        | Gated CTA | Contrast (30 sec delay) | Top of heart to Below heart |
        | Delayed phase | Contrast (70 sec delay) | Top of heart to Below heart |

    === "Clinical Indications"

        - Endocarditis
        - Cardiac mass
        - Valve vegetation
        - Intracardiac thrombus

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet-first
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:**
        - HR < 65 preferred. No premedication typically given.

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.6 mL/kg |
        | Flow Rate | 3-4 mL/s |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30, If low eGFR can use low dose calculation **Maximum Contrast Dose** = [(Patient Weight in kg/75 kg) * eGFR] *2



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Non-valsalva breathing technique, cardiac breathing instruction.
        - Injection duration is fixed 35 sec fixed 30 sec scan delay. Retrospective gating trigger at 30-70% (End sys - end dia).  Reconstruct  at 5% intervals.

    === "Nursing Notes"

        - 18-20G IV. HR control helpful but not critical

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Assess all valves for vegetations. Evaluate myocardium for abscess. Look for intracardiac masses. Check for complications

    === "Tips & Tricks"

        - Multiple cardiac phases helpful for valve motion. Thin slices for vegetations

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Endocarditis/Cardiac Mass Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.6 mL/kg)    :active, contrast, 00:00, 34s
      Saline (20mL)          :active, saline, after contrast, 5s
      section Arterial Phase
      Gated CTA    :crit, scan1, 00:30, 5s
      section Delayed Phase
      Delayed phase    :done, scan2, 01:10, 5s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Top of chest | Diaphragm | N/A | N/A | AP lateral |
    | Non-contrast | Top of heart | Below heart | N/A | 3 mm | Flash Non-contrast |
    | Gated CTA | Top of heart | Below heart | 30 sec | 0.5-0.625 mm | Retrospective ECG gating |
    | Delayed phase | Top of heart | Below heart | 70 sec | 1 mm | To detect for abscess, vegetation, masses |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto ECG modulation |
    | Rotation Time | 0.28s |
    | Pitch | 0.2-0.24 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Non-contrast | Heart | 3 mm/3 mm | Standard | 3 | For dense material or calcifications |
    | Axial | Gated CTA | Heart | 0.75 mm/0.5 mm | Cardiac | 3 | Reformatted at best cardiac phase |
    | Axial | Gated CTA | Heart | 1 mm/1 mm | Standard | 3 | Functional series for valve assessment |
    | Axial | Delayed | Chest | 1 mm/1 mm | Standard | 3 | Mass, vegetations |


### Additional Reconstructions

Multi-phase reconstructions. 4-chamber 2-chamber views. Valve-specific reformats

Category: Cardiac

Protocol Type: Cardiac Gated
