# CTA Pelvis Cyclist Iliac Artery Maneuver

**Last Updated:** 2024-01-15  
**Author:** Dr. Rodriguez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Resting Position | Arterial (bolus tracked) | Mid-liver to 3cm below greater trochanter |
        | CTA Hip Flexion | Contrast (Immediately after delay) | Mid-liver to 3cm below greater trochanter |

    === "Clinical Indications"

        - External iliac artery endofibrosis
        - Cyclist with exercise-induced leg symptoms

-   __2. Patient Prep__

    ---

    - **Position:** Supine initially then with hip flexion
    - **NPO Status:** NPO 2-4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | Split bolus: 1st injection 1.1 mL/kg + 2nd injection 1.1 mL/kg |
        | Flow Rate | 4 mL/s |
        | Duration | 1st injection 18s + 2nd injection 18s |
        | Timing Method | Dual position: Resting + Hip flexion cycling position |
        | ROI Placement | External iliac artery |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO acquisitions: 1) Resting supine 2) Hip flexion simulating cycling position. Bilateral imaging for comparison

    === "Nursing Notes"

        - 18-20G IV

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history. Explain hip flexion positioning

    === "Radiologist Notes"

        - Compare resting vs flexed position. Look for iliac artery kinking stenosis or occlusion with hip flexion. Common in competitive cyclists

    === "Tips & Tricks"

        - Position patient with knees bent and hips flexed to simulate cycling. May need positioning aids

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
      title CTA Pelvis Cyclist Iliac Artery Maneuver Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.1 mL/kg)    :active, contrast, 00:00, 18s
      Saline          :active, saline, after contrast, 5s
      Contrast bolus 2 (1.1 mL/kg)  :active, contrast2, 01:00, 18s
      Saline                  :active, saline2, after contrast2, 5s
      section Extremities
      CTA Resting Position    :crit, scan1, after saline, 5s
      CTA Hip Flexion    :crit, scan2, after saline2, 5s
  ```

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | L3 | Proximal femur | N/A | N/A | AP pelvis |
    | CTA Resting Position | L3 | Mid femur | Bolus tracked | 0.625 mm | Supine resting position |
    | CTA Hip Flexion | L3 | Mid femur | Immediately after | 0.625 mm | Hips flexed 90 degrees - cycling position |

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
    | Axial | Resting | Pelvis | 1.5 mm/1.5 mm | Vascular | 3 | Baseline iliac artery anatomy |
    | Axial | Flexion | Pelvis | 1.5 mm/1.5 mm | Vascular | 3 | Assess for kinking with flexion |
    | Coronal | Both phases | Pelvis | 2 mm/2 mm | Vascular | 3 | MIP comparison rest vs flexion |
    | Sagittal | Both phases | Pelvis | 2 mm/2 mm | Vascular | 3 | Lateral view iliac course |


### Additional Reconstructions

Side-by-side MIP of rest vs flexion. Measure degree of stenosis. 3D VR

Category: Vascular

Protocol Type: Vascular
