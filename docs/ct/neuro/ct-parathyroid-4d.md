# CT Parathyroid 4D

**Last Updated:** 2024-01-15  
**Author:** Dr. Kim

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast | Non-contrast | Skull base to Carina |
        | Arterial Phase | Contrast (25 sec delay) | Skull base to Carina |
        | Venous Phase | Contrast (55 sec delay) | Skull base to Carina |

    === "Clinical Indications"

        - Hyperparathyroidism
        - Parathyroid adenoma localization
        - Pre-operative parathyroid planning

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history
    
    - **Position:** Supine head-first with arms down
    - **NPO Status:** NPO 4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 75-100 mL |
        | Flow Rate | 4 mL/s |
        | Timing Method | 4D multi-phase |
        | ROI Placement | Carotid artery |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - FOUR phases: 1) NC 2) Arterial 25s 3) Venous 55s 4) Delayed/washout 90s. Skull base to mediastinum. Parathyroid enhances early washes out

    === "Nursing Notes"

        - 18-20G IV. High flow rate for arterial

    === "Radiologist Notes"
        - NC: baseline. Arterial: parathyroid lights up. Venous: thyroid enhances. Delayed: parathyroid washes out faster than thyroid

    === "Tips & Tricks"

        - Four phase critical. Look for early enhancement and washout

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Parathyroid 4D Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (75-100 mL)    :active, contrast, 00:00, 18s
      Saline (50mL)          :active, saline, after contrast, 12s
      section Arterial Phase
      Arterial Phase    :crit, scan3, 00:25, 15s
      section Portal Venous Phase
      Venous Phase    :done, scan4, 00:55, 15s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Skull base | Carina | N/A | N/A | AP lateral |
    | Non-Contrast | Skull base | Carina | N/A | 2.5 mm | Baseline |
    | Arterial Phase | Skull base | Carina | 25 sec | 2 mm | Parathyroid enhancement |
    | Venous Phase | Skull base | Carina | 55 sec | 2 mm | Thyroid enhancement |

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
    | Axial | All phases | Neck | 2 mm/2 mm | Standard | 3 | Compare all four phases |
    | Axial | Arterial | Neck | 2 mm/2 mm | Standard | 3 | Peak parathyroid enhancement |
    | Subtraction | Arterial - NC | Neck | 2 mm | Standard | 3 | Enhance parathyroid conspicuity |
    | Coronal | Arterial | Neck | 2.5 mm | Standard | 3 | Ectopic adenoma search |


### Additional Reconstructions

Subtraction images. Compare all phases. Document location for surgeon. Measure size

Category: Neuro

Protocol Type: Contrast-Enhanced
