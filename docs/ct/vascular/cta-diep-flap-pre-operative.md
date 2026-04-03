# CTA DIEP Flap Pre-operative

**Last Updated:** 2024-01-15  
**Author:** Dr. Williams

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Arterial | Arterial (bolus tracked) | Mid-Liver to Greater Trochanters |

    === "Clinical Indications"

        - Pre-operative planning for DIEP flap breast reconstruction

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms at sides or on chest
    - **NPO Status:** NPO 2-4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Duration | 20s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Abdominal aorta |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Scan from mid-liver to greater trochanters. Remove tight-fitting underwear. If patient can exercise, do leg lifts on table before injection.

    === "Nursing Notes"

        - 18-20G IV

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Map perforator locations. Measure vessel caliber. Identify dominant perforators. Note relationship to umbilicus. Prefer perforators below umbilicus. 

    === "Tips & Tricks"

        - Arms positioned to not obscure anterior abdominal wall

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
      title CTA DIEP Flap Pre-operative Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (100 mL)    :active, contrast, 00:00, 20s
      Saline          :active, saline, after contrast, 5s
      section Other
      CTA Arterial    :crit, scan1, after contrast, 5s
  ```

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Xiphoid | Pubic symphysis | N/A | N/A | AP |
    | CTA Arterial | Xiphoid | Pubic symphysis | Bolus tracked | 0.625 mm | Focus on abdominal wall |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 0.9 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Abdomen | 1 mm/1 mm | Vascular | 3 | Thin slice for perforator mapping |
    | Coronal | Arterial | Abdomen | 1.5 mm/1.5 mm | Vascular | 3 | MIP to show perforator course |
    | Sagittal | Arterial | Abdomen | 2 mm/2 mm | Vascular | 3 | Lateral views of perforators |
    | 3D VR | Arterial | Anterior abd wall | 1 mm source | Vascular | 3 | 3D reconstruction for surgical planning |


### Additional Reconstructions

3D VR color-coded perforator map. Measure distances from umbilicus

Category: Vascular

Protocol Type: Vascular
