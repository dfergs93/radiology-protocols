# CT Adrenal Mass Protocol

**Last Updated:** 2024-01-15  
**Author:** Dr. Thompson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast | Non-contrast | Diaphragm to Kidneys |
        | Portal Venous | Contrast (70 sec delay) | Diaphragm to Kidneys |
        | 15 Minute Delay | Contrast (900 sec delay) | Diaphragm to Kidneys |

    === "Clinical Indications"

        - Adrenal mass characterization
        - Adenoma vs metastasis
        - Incidentaloma workup

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 3-4 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - THREE phases: 1) Non-contrast for absolute HU 2) Portal venous 70s 3) 15 MINUTE delayed for washout. All phases cover adrenals

    === "Nursing Notes"

        - 18-20G IV. Patient must wait 15 min for delayed phase

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history. Explain 15 min delay

    === "Radiologist Notes"

        - NC: lipid-rich adenoma < 10 HU. Portal venous: enhancement. 15 min delay: calculate washout (adenoma shows washout)

    === "Tips & Tricks"

        - Patient wait time 15 min. Measure HU carefully with ROI in same location

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
      title CT Adrenal Mass Protocol Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.5 mL/kg)    :active, contrast, 00:00, 32s
      Saline          :active, saline, after contrast, 5s
      section Other
      Portal Venous    :done, scan1, 01:10, 5s
      15 Minute Delay    :done, scan2, 15:00, 5s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Kidneys | N/A | N/A | AP |
    | Non-Contrast | Diaphragm | Kidneys | N/A | 2.5 mm | Measure absolute HU in mass |
    | Portal Venous | Diaphragm | Kidneys | 70 sec | 2.5 mm | Enhanced HU measurement |
    | 15 Minute Delay | Diaphragm | Kidneys | 900 sec | 2.5 mm | Delayed HU for washout calculation |

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
    | Axial | All phases | Adrenals | 2.5 mm/2.5 mm | Standard | 3 | ROI measurements in mass |
    | Axial | All phases | Adrenals | 2.5 mm/2.5 mm | Standard | 3 | Compare enhancement |
    | Coronal | Portal venous | Adrenals | 3 mm/3 mm | Standard | 3 | Anatomic overview |


### Additional Reconstructions

Calculate absolute washout: (Enhanced HU - Delayed HU)/(Enhanced HU - NC HU) x 100. >60% suggests adenoma. Measure HU in all phases

Category: Abdomen

Protocol Type: Contrast-Enhanced
