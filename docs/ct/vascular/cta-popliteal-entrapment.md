# CTA Popliteal Entrapment

**Last Updated:** 2024-01-15  
**Author:** Dr. Thompson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Scout/Topogram | Non-contrast | Distal femur to Ankle |
        | CTA Neutral Position | Arterial (bolus tracked) | Distal femur to Ankle |
        | CTA Plantarflexion | Contrast (Immediately after delay) | Distal femur to Ankle |

    === "Clinical Indications"

        - Popliteal entrapment syndrome
        - Exercise-induced leg pain
        - Young patient with claudication

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history. Explain plantarflexion maneuver to patient
    
    - **Position:** Supine with legs extended in neutral position
    - **NPO Status:** NPO 2-4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 100 mL |
        | Flow Rate | 4 mL/s |
        | Timing Method | Dual position: Neutral + Plantarflexion |
        | ROI Placement | Popliteal artery |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO acquisitions required: 1) Neutral position 2) Active plantarflexion. Both legs scanned for comparison. Coach patient on plantarflexion technique

    === "Nursing Notes"

        - 18-20G IV antecubital

    === "Radiologist Notes"
        - Compare neutral vs plantarflexion images. Look for popliteal artery compression deviation or occlusion with plantarflexion. Assess muscle anatomy

    === "Tips & Tricks"

        - Coach patient on maintaining plantarflexion during second acquisition. Use foot straps if needed

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CTA Popliteal Entrapment Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (100 mL)    :active, contrast, 00:00, 25s
      Saline (50mL)          :active, saline, after contrast, 12s
      section Scan Phase 2
      CTA Neutral Position    :crit, scan2, 00:25, 15s
      section Scan Phase 3
      CTA Plantarflexion    :crit, scan3, after scan1, 15s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Distal femur | Ankle | N/A | N/A | AP both legs |
    | CTA Neutral Position | Distal femur | Ankle | Bolus tracked | 0.625 mm | Both legs neutral resting position |
    | CTA Plantarflexion | Distal femur | Ankle | Immediately after | 0.625 mm | Patient actively plantarflexes both feet - point toes |

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
    | Axial | Neutral | Both legs | 1.5 mm/1.5 mm | Vascular | 3 | Baseline popliteal artery anatomy |
    | Axial | Plantarflexion | Both legs | 1.5 mm/1.5 mm | Vascular | 3 | Assess for compression with maneuver |
    | Coronal | Both phases | Both legs | 2 mm/2 mm | Vascular | 3 | MIP comparison neutral vs flexion |
    | Sagittal | Both phases | Both legs | 2 mm/2 mm | Vascular | 3 | Lateral view popliteal fossa |


### Additional Reconstructions

Side-by-side comparison of neutral vs plantarflexion. 3D VR showing muscle-vessel relationship

Category: Vascular

Protocol Type: Vascular
