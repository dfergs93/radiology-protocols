# Trauma Code AAA

**Last Updated:** 2024-01-15  
**Author:** Dr. Davis

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast CAP | Non-contrast | Diaphragm to Pubic symphysis |
        | Arterial CAP | Contrast (25-30 sec delay) | Diaphragm to Pubic symphysis |
        | Portal Venous CAP | Contrast (70 sec delay) | Diaphragm to Pubic symphysis |

    === "Clinical Indications"

        - Ruptured AAA
        - Aortic emergency
        - Hemodynamic instability with abdominal pain

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** None - emergency
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 125 mL |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Triple phase: NC + Arterial + Portal venous |
        | ROI Placement | Abdominal aorta |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Proceed emergently. Life-saving indication



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - RAPID triple phase: 1) NC CAP (hematoma) 2) Arterial CAP (active bleed bolus track 25-30s) 3) Portal venous CAP (70s). STAT protocol

    === "Nursing Notes"

        - Large bore IV 18G minimum. Blood products ready

        !!! warning "Safety First"
            - **Renal Function:** Emergent - proceed
            - **Allergy:** Document emergency

    === "Radiologist Notes"

        - NC: retroperitoneal hematoma. Arterial: active extravasation aneurysm morphology. Portal: solid organs

    === "Tips & Tricks"

        - STAT protocol. Minimize delays. Notify vascular surgery

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Trauma Code AAA Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (125 mL)    :active, contrast, 00:00, 27s
      Saline (20mL)          :active, saline, after contrast, 4s
      section Arterial Phase
      Arterial CAP    :crit, scan1, 00:25, 7s
      section Portal Venous Phase
      Portal Venous CAP    :done, scan2, 01:10, 7s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Pubic symphysis | N/A | N/A | STAT |
    | Non-Contrast CAP | Diaphragm | Pubic symphysis | N/A | 2.5 mm | RAPID - hematoma |
    | Arterial CAP | Diaphragm | Pubic symphysis | 25-30 sec | 0.625 mm | Active bleeding + aneurysm |
    | Portal Venous CAP | Diaphragm | Pubic symphysis | 70 sec | 2.5 mm | Organs and venous |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | High mAs (300 reference) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.375 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | All phases | CAP | 2.5 mm/2.5 mm | Vascular/Standard | 3 | Compare phases |
    | Coronal | Arterial | CAP | 2.5 mm/2.5 mm | Vascular | 3 | Aorta and bleeding |
    | Sagittal | Arterial | Aorta | 2 mm/2 mm | Vascular | 3 | Aorta extent |
    | 3D VR | Arterial | Aorta | 1.5 mm | Vascular | 3 | STAT 3D for EVAR planning |


### Additional Reconstructions

Measure aneurysm. Identify bleeding site. EVAR measurements if stable

Category: Trauma

Protocol Type: Trauma
