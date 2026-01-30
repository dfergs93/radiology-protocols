# Gated CTA TAVR

**Last Updated:** 2024-01-15  
**Author:** Dr. Davis

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Gated CTA Chest | Arterial (bolus tracked) | Thoracic inlet to Diaphragm |
        | Flash CTA AP | Contrast (After gated delay) | Diaphragm to Femoral heads |

    === "Clinical Indications"

        - Pre-TAVR planning
        - Aortic stenosis valve replacement planning

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history
    
    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    - **Pre-Medication:** 
      HR < 65 target. Metoprolol IV. Nitro 0.4mg SL


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 140 mL |
        | Flow Rate | 4 mL/s |
        | Timing Method | Dual phase: Gated chest + Flash AP |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 180 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Gated CHEST retrospective + Flash AP. Gated for valve measurements. AP for access planning. TAVR post-processing required

    === "Nursing Notes"

        - 20G IV antecubital

    === "Radiologist Notes"
        - Measure aortic annulus (3 diameters). Coronary heights. Access vessels (iliofemoral). Valve calcium. Comprehensive TAVR measurements

    === "Tips & Tricks"

        - TAVR-specific measurements protocol. Thin slices critical

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Gated CTA TAVR Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (140 mL)    :active, contrast, 00:00, 35s
      Saline (50mL)          :active, saline, after contrast, 12s
      section Cardiac Acquisition
      Gated CTA Chest    :crit, scan2, 00:25, 12s
      section Scan Phase 3
      Flash CTA AP    :crit, scan3, after scan1, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Thoracic inlet | Femoral heads | N/A | N/A | AP lateral full |
    | Gated CTA Chest | Thoracic inlet | Diaphragm | Bolus tracked | 0.5 mm | Retrospective gating for valve |
    | Flash CTA AP | Diaphragm | Femoral heads | After gated | 0.625 mm | Iliofemoral access planning |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto ECG chest / High mAs AP |
    | Rotation Time | 0.28 / 0.5s |
    | Pitch | 0.2-0.24 / 1.2-1.5 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated chest | Heart | 0.5 mm/0.5 mm | Cardiac | 3 | Aortic valve and root measurements |
    | Axial | Flash AP | AP | 2 mm/2 mm | Vascular | 3 | Access vessel assessment |
    | Double oblique | Gated chest | Aortic valve | 0.5 mm | Cardiac | 3 | En face aortic annulus for sizing |
    | 3D VR | Flash AP | Iliofemoral | 1.5 mm source | Vascular | 3 | 3D access planning |


### Additional Reconstructions

TAVR measurements: annulus area perimeter diameters. Coronary heights. Sinus of Valsalva. STJ. Ascending aorta. Access vessels

Category: Cardiac

Protocol Type: Cardiac Gated
