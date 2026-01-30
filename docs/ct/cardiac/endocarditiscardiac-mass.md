# Endocarditis/Cardiac Mass

**Last Updated:** 2024-01-15  
**Author:** Dr. Martinez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Gated CTA | Arterial (bolus tracked) | Top of heart to Below heart |
        | Delayed phase | Contrast (180 sec delay) | Top of heart to Below heart |

    === "Clinical Indications"

        - Endocarditis
        - Cardiac mass
        - Valve vegetation
        - Intracardiac thrombus

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history
    
    - **Position:** Supine feet-first
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:** 
      HR < 65 preferred. Metoprolol if needed. Nitro not typically needed


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.1 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 200 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Retrospective gating. Cover entire heart. Focus on valves and chambers. May need delayed phase for perfusion

    === "Nursing Notes"

        - 20G IV. HR control helpful but not critical

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
      Contrast (1.1 mL/kg)    :active, contrast, 00:00, 17s
      Saline (50mL)          :active, saline, after contrast, 11s
      section Cardiac Acquisition
      Gated CTA    :crit, scan2, 00:25, 10s
      section Delayed Phase
      Delayed phase    :done, scan3, 03:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Top of chest | Diaphragm | N/A | N/A | AP lateral |
    | Gated CTA | Top of heart | Below heart | Bolus tracked | 0.5-0.625 mm | Retrospective ECG gating |
    | Delayed phase | Top of heart | Below heart | 180 sec | 2 mm | Optional for perfusion assessment |

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
    | Axial | Gated CTA | Heart | 0.75 mm/0.5 mm | Cardiac | 3 | Valve and chamber assessment |
    | Axial | Gated CTA | Heart | 0.75 mm/0.5 mm | Cardiac | 3 | Reformatted at multiple phases |
    | Short axis | Gated CTA | Heart | 2 mm | Cardiac | 3 | Valve en face views |
    | Long axis | Gated CTA | Heart | 2 mm | Cardiac | 3 | Chamber and valve evaluation |


### Additional Reconstructions

Multi-phase reconstructions. 4-chamber 2-chamber views. Valve-specific reformats

Category: Cardiac

Protocol Type: Cardiac Gated
