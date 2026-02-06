# Gated CTA CAP Sternotomy Revision

**Last Updated:** 2024-01-15  
**Author:** Dr. Williams

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Gated CTA Chest | Arterial (bolus tracked) | Thoracic inlet to Diaphragm |
        | Flash AP | Contrast (Immediate delay) | Diaphragm to Pubic symphysis |
        | Venogram Chest | Contrast (60 sec delay) | Thoracic inlet to Diaphragm |

    === "Clinical Indications"

        - Pre-operative planning for redo sternotomy
        - Retrosternal structures assessment

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    - **Pre-Medication:**
        - HR < 65. Metoprolol IV prn. Nitro 0.4mg SL

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 150 mL |
        | Flow Rate | 4 mL/s |
        | Timing Method | Triple phase: Gated chest + AP arterial + Chest venous |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 180 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30. Large volume protocol



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - THREE acquisitions: 1) Gated CHEST 2) Flash AP arterial 3) CHEST venogram 60 sec delay. Venous for retrosternal structures

    === "Nursing Notes"

        - 20G IV

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Large contrast load - verify renal function

    === "Radiologist Notes"

        - Gated: cardiac anatomy. Arterial: systemic vessels. VENOUS: retrosternal veins and adherent structures critical for surgical planning

    === "Tips & Tricks"

        - Venous phase critical for surgical planning. Map all retrosternal structures

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Gated CTA CAP Sternotomy Revision Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (150 mL)    :active, contrast, 00:00, 37s
      Saline (20mL)          :active, saline, after contrast, 5s
      section Arterial Phase
      Gated CTA Chest    :crit, scan1, after contrast, 6s
      section Scan Phase 2
      Flash AP    :crit, scan2, after scan1, 7s
      section Scan Phase 3
      Venogram Chest    :done, scan3, 01:00, 6s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Thoracic inlet | Pubic symphysis | N/A | N/A | AP lateral full |
    | Gated CTA Chest | Thoracic inlet | Diaphragm | Bolus tracked | 0.5-0.625 mm | Retrospective gating |
    | Flash AP | Diaphragm | Pubic symphysis | Immediate | 0.625 mm | Arterial phase AP |
    | Venogram Chest | Thoracic inlet | Diaphragm | 60 sec | 1 mm | Retrosternal venous structures |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto ECG chest / High mAs other |
    | Rotation Time | 0.28 / 0.5s |
    | Pitch | 0.2-0.24 / 1.2-1.5 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated chest | Chest | 0.75 mm/0.75 mm | Cardiac | 3 | Cardiac and coronary anatomy |
    | Axial | Venogram | Chest | 1.25 mm/1.25 mm | Standard | 3 | Critical for retrosternal structures |
    | Coronal | All phases | Chest | 2 mm/2 mm | Standard | 3 | Anterior chest wall structures |
    | 3D VR | Venogram | Chest | 1 mm source | Standard | 3 | 3D map retrosternal vessels for surgery |


### Additional Reconstructions

3D VR venogram highlighting retrosternal veins. Distance measurements sternum to heart

Category: Cardiac

Protocol Type: Cardiac Gated
