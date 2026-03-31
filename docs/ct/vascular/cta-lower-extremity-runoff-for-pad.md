# CTA Lower Extremity Runoff for PAD

**Last Updated:** 2024-01-15  
**Author:** Dr. Anderson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Arterial | Arterial (bolus tracked) | Renal arteries to Foot |
        | CTA Runoff | Immediately after CTA | Mid Thigh to Foot |

    === "Clinical Indications"

        - Peripheral arterial disease
        - Claudication
        - Critical limb ischemia
        - Pre-operative bypass planning

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised. Legs straight
    - **NPO Status:** NPO 2-4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 150 mL |
        | Flow Rate | 4 mL/s |
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

        - Scan from renal arteries to feet. Use automatic bolus tracking. Extend delay if known severe PAD. Cover tibial vessels to ankle

    === "Nursing Notes"

        - 18-20G IV antecubital

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Assess aortoiliac femoral popliteal and tibial vessels. Grade stenoses. Identify occlusions. Assess runoff vessels

    === "Tips & Tricks"

        - Ensure legs are straight and not rotated. Remove shoes and metal

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
      title CTA Lower Extremity Runoff for PAD Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (150 mL)    :active, contrast, 00:00, 37s
      Saline          :active, saline, after contrast, 5s
      section Other
      CTA Arterial    :crit, scan1, after contrast, 5s
      CTA Runoff    :done, scan2, after CTA Arterial, 5s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Renal arteries | Feet | N/A | N/A | AP full legs |
    | CTA Arterial | Renal arteries | Ankle | Bolus tracked | 0.625 mm | May need slower table speed if severe PAD |
    | CTA Runoff | Mid Thigh | Foot | Immediately after CTA | 0.625 mm | Runoff phase to evaluate distal vessels |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5s |
    | Pitch | 1.2-1.5 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Pelvis/Legs | 2 mm/2 mm | Vascular | 3 | Assess all vessel segments |
    | Coronal | Arterial | Full legs | 3 mm/3 mm | Vascular | 3 | MIP full arterial tree |
    | Sagittal | Arterial | Full legs | 3 mm/3 mm | Vascular | 3 | Lateral views of vessels |
    | 3D VR | Arterial | Full legs | 1.5 mm source | Vascular | 3 | 3D for surgical planning |


### Additional Reconstructions

MIP and 3D VR. Curved MPR of each arterial segment. Bone subtraction for vessels.

Category: Vascular

Protocol Type: Vascular
