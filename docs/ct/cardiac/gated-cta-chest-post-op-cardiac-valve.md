# Gated CTA Chest Post-op Cardiac Valve

**Last Updated:** 2024-01-15  
**Author:** Dr. Thompson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Gated CTA | Arterial (bolus tracked) | Top of heart to Below heart |

    === "Clinical Indications"

        - Post-operative valve assessment
        - Prosthetic valve evaluation
        - Post-surgical complications

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history
    
    - **Position:** Supine feet-first
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:** 
      HR < 65 preferred. Metoprolol if needed


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.3 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 200 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30. Increased volume for metal artifact



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Retrospective gating. INCREASED kV to 130-140 for metal artifact reduction. Increased contrast 1.3 mL/kg. Extended reconstruction phases

    === "Nursing Notes"

        - 20G IV minimum

    === "Radiologist Notes"
        - Assess prosthetic valve function. Look for paravalvular leak. Evaluate perivalvular complications. Metal artifact reduction critical

    === "Tips & Tricks"

        - High kV (130-140) critical for metal artifact. Increased contrast volume

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Gated CTA Chest Post-op Cardiac Valve Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.3 mL/kg)    :active, contrast, 00:00, 20s
      Saline (50mL)          :active, saline, after contrast, 11s
      section Arterial Phase
      Gated CTA    :crit, scan1, 00:25, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Top of chest | Diaphragm | N/A | N/A | AP lateral |
    | Gated CTA | Top of heart | Below heart | Bolus tracked | 0.5-0.625 mm | Retrospective gating HIGH kV |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 130-140 |
    | mAs | Auto ECG modulation |
    | Rotation Time | 0.28s |
    | Pitch | 0.2-0.24 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated CTA | Heart | 0.75 mm/0.75 mm | Cardiac | 3 | Prosthetic valve assessment |
    | Axial | Gated CTA | Heart | Multi-phase | Cardiac | 3 | Multiple cardiac phases for motion |
    | Short axis | Gated CTA | Valve level | 1 mm | Cardiac | 3 | En face valve views |
    | Long axis | Gated CTA | Heart | Multi-phase | Cardiac | 3 | Valve motion assessment |


### Additional Reconstructions

Multi-phase reconstructions. Valve-specific views. Paravalvular assessment

Category: Cardiac

Protocol Type: Cardiac Gated
