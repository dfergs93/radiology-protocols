# CT Enterography

**Last Updated:** 2024-01-15  
**Author:** Dr. Martinez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Delayed Arterial | Contrast (45 sec delay) | Diaphragm to Pubic symphysis |
        | Renal Delay | 300 sec | 1-2cm above and below kidneys |

    === "Clinical Indications"

        - Crohn disease
        - Small bowel obstruction
        - Obscure GI bleeding
        - Small bowel mass

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours solids
    - **Pre-Medication:**
        - Neutral oral contrast (VoLumen): 1st bottle (450mL) at 90 min. 2nd bottle (450mL) at 60 min. Half bottle (225mL) at 30 min. Other half (225mL) at 5 min before scan

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Duration | 25s |
        | Timing Method | Empiric Delay (45s) |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Enterographic phase (45 sec). High volume neutral oral for bowel distension. 25 second injection. Scan 45 sec from start

    === "Nursing Notes"

        - 18-20G IV. Ensure adequate oral contrast intake (total ~1350mL). May need anti-peristaltic agent

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history. Coordinate oral contrast timing

    === "Radiologist Notes"

        - Assess bowel wall enhancement and thickness. Look for strictures fistulas abscesses. Mesenteric vascularity

    === "Tips & Tricks"

        - Adequate oral contrast distension critical. High injection rate

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
      title CT Enterography Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.5 mL/kg)    :active, contrast, 00:00, 25s
      Saline          :active, saline, after contrast, 4s
      section Other
      Enteric Phase    :done, scan1, 00:45, 7s
      Renal Delay    :done, scan2, 04:00, 7s
  ```

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Pubic symphysis | N/A | N/A | AP |
    | Enteric Phase | Diaphragm | Pubic symphysis | 45 sec | 0.625 mm | Optimal small bowel enhancement |
    | Renal Delay | 1-2cm above kidneys | 1-2cm below kidneys | 300 sec | 0.625 mm | Renal Delay series |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.375 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Enteric | Full AP | 2.5 mm/2.5 mm | Standard | 3 | Primary diagnostic |
    | Coronal | Enteric | Full AP | 3 mm/3 mm | Standard | 3 | Bowel loop assessment |
    | Sagittal | Enteric | Full AP | 3 mm/3 mm | Standard | 3 | Mesenteric evaluation |
    | MIP | Enteric | Mesenteric vessels | 5 mm slab | Vascular | 3 | Vascular assessment |


### Additional Reconstructions

Curved MPR of bowel segments. Mesenteric vascular assessment

Category: Abdomen

Protocol Type: Contrast-Enhanced
