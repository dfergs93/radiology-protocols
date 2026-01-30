# CTA Lower Extremity Free Flap

**Last Updated:** 2024-01-15  
**Author:** Dr. Kim

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Scout/Topogram | Non-contrast | Iliac crest to Ankle |
        | CTA Arterial | Arterial (bolus tracked) | Iliac crest to Ankle |

    === "Clinical Indications"

        - Pre-operative planning for free flap harvest (fibula ALT anterolateral thigh)

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history
    
    - **Position:** Supine with legs extended
    - **NPO Status:** NPO 2-4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 120 mL |
        | Flow Rate | 4 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Femoral artery |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Scan from iliac crest to ankle. Focus on perforators in region of interest. Arterial phase critical for mapping

    === "Nursing Notes"

        - 18-20G IV

    === "Radiologist Notes"
        - Map perforator vessels. Measure vessel caliber and length. Identify dominant pedicle. Note anatomic variants

    === "Tips & Tricks"

        - Legs straight and not rotated. Mark skin over region of interest if possible

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CTA Lower Extremity Free Flap Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (120 mL)    :active, contrast, 00:00, 30s
      Saline (50mL)          :active, saline, after contrast, 12s
      section Arterial Phase
      CTA Arterial    :crit, scan2, 00:25, 16s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Iliac crest | Ankle | N/A | N/A | AP both legs for comparison |
    | CTA Arterial | Iliac crest | Ankle | Bolus tracked | 0.625 mm | Bilateral for comparison and variants |

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
    | Axial | Arterial | Thighs/Legs | 1 mm/1 mm | Vascular | 3 | Thin slice for perforator identification |
    | Coronal | Arterial | Full legs | 1.5 mm/1.5 mm | Vascular | 3 | MIP to show perforator course |
    | Sagittal | Arterial | Full legs | 2 mm/2 mm | Vascular | 3 | Lateral perforator views |
    | 3D VR | Arterial | Region of interest | 0.75 mm source | Vascular | 3 | Color-coded perforator map for surgery |


### Additional Reconstructions

3D VR perforator map. Curved MPR of main vessels. Measure perforator locations from bony landmarks

Category: Vascular

Protocol Type: Vascular
