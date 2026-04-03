# Gated CTA Heart Left Atrial Mapping

**Last Updated:** 2024-01-15  
**Author:** Dr. Kim

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Flash CTA | Arterial | Carina to Below Heart |
        | Delayed | Delayed (30s)| Carina to Mid Heart |

    === "Clinical Indications"

        - Pre-ablation planning
        - Atrial fibrillation
        - Pulmonary vein anatomy

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet-first
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:**
        - HR < 65 preferred. Premedication not required.

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.1 mL/kg |
        | Flow Rate | 5 mL/s |
        | Duration | 15 sec |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Left Atrium |
        | Trigger (HU) | 200 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Retrospective gating. Focus on left atrium and pulmonary veins. Thin slices critical. Extended coverage for all PV ostia

    === "Nursing Notes"

        - 20G IV

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Map pulmonary vein anatomy (number ostia diameters). Left atrial appendage morphology. Esophageal position. LA size

    === "Tips & Tricks"

        - Thin slices essential. Complete PV coverage. Document variants

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
      title Gated CTA Heart Left Atrial Mapping Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.1 mL/kg)    :active, contrast, 00:00, 15s
      Saline          :active, saline, after contrast, 4s
      section Other
      Gated CTA    :crit, scan1, after saline, 5s
      Delayed CTA    :crit, scan2, 00:30, 5s
  ```

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Top of chest | Below heart | N/A | N/A | AP lateral |
    | Gated CTA | Pulmonary veins | Below LA | Bolus tracked | 0.5 mm | Retrospective - thin slices critical |
    | Delayed CTA | Pulmonary veins | Below LA | 40s | 0.5 mm | Retrospective - thin slices critical |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto ECG modulation |
    | Rotation Time | 0.28s |
    | Pitch | 0.2-0.24 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated CTA | LA/PV | 0.5 mm/0.5 mm | Cardiac | 3 | Primary PV anatomy |
    | Coronal | Gated CTA | LA/PV | 0.75 mm | Cardiac | 3 | PV ostia en face |
    | Sagittal | Gated CTA | LA/PV | 0.75 mm | Cardiac | 3 | Lateral PV views |
    | Axial | Delayed CTA | LA/PV | 0.5 mm/0.5 mm | Cardiac | 3 | Left Atrial Appendage Thrombus |

### Additional Reconstructions

3D LA reconstruction. PV ostia measurements (diameter area). LAA morphology. Esophageal position

Category: Cardiac

Protocol Type: Cardiac Gated
