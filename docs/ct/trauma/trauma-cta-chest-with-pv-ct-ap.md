# Trauma CTA Chest with PV CT AP

**Last Updated:** 2024-01-15  
**Author:** Dr. Lee

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Chest | Arterial (bolus tracked) | Lung apices to Diaphragm |
        | Portal Venous AP | Contrast (70 sec from start delay) | Diaphragm to Pubic symphysis |

    === "Clinical Indications"

        - Blunt thoracic trauma
        - Aortic injury
        - Great vessel injury
        - Multi-trauma

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** eGFR > 30 if known
        - **Allergy:** Trauma indication
    
    - **Position:** Supine with arms raised
    - **NPO Status:** None - trauma
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 125 mL |
        | Flow Rate | 4 mL/s |
        | Timing Method | Dual phase: CTA Chest arterial + Portal venous AP |
        | ROI Placement | Descending aorta |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Proceed if possible. Document medical necessity



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO acquisitions: 1) CTA CHEST arterial (bolus track) 2) Portal venous ABDOMEN/PELVIS 70s. Chest arterial for aorta/vessels

    === "Nursing Notes"

        - Large bore IV 18-20G. Verify flow

    === "Radiologist Notes"
        - Chest arterial: aortic injury (intimal flap pseudoaneurysm). AP portal venous: solid organ injury

    === "Tips & Tricks"

        - Trauma indication. Fast scan. Good IV essential

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Trauma CTA Chest with PV CT AP Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (125 mL)    :active, contrast, 00:00, 31s
      Saline (50mL)          :active, saline, after contrast, 12s
      section Scan Phase 2
      CTA Chest    :crit, scan2, 00:25, 8s
      section Portal Venous Phase
      Portal Venous AP    :done, scan3, 01:10, 25s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Pubic symphysis | N/A | N/A | AP full |
    | CTA Chest | Lung apices | Diaphragm | Bolus tracked | 0.625 mm | Arterial phase |
    | Portal Venous AP | Diaphragm | Pubic symphysis | 70 sec from start | 0.625 mm | Portal venous phase |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.2 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTA chest | Chest | 1.25 mm/1.25 mm | Vascular | 3 | Aorta and great vessels |
    | Axial | PV AP | Abdomen/Pelvis | 2.5 mm/2.5 mm | Standard | 3 | Solid organs |
    | Coronal | CTA chest | Chest | 2 mm/2 mm | Vascular | 3 | Aorta overview |
    | Sagittal | CTA chest | Aorta | 2 mm/2 mm | Vascular | 3 | Sagittal aorta |


### Additional Reconstructions

3D aorta and great vessels. Curved MPR aorta. Grade aortic injury

Category: Trauma

Protocol Type: Vascular
