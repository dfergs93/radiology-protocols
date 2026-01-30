# CTA Abdomen Pelvis

**Last Updated:** 2024-01-15  
**Author:** Dr. Martinez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Scout/Topogram | Non-contrast | Diaphragm to Femoral heads |
        | CTA Arterial | Arterial (bolus tracked) | Diaphragm to Femoral heads |

    === "Clinical Indications"

        - Abdominal aortic aneurysm
        - Mesenteric ischemia
        - Renal artery stenosis
        - Pre-EVAR planning

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history
    
    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    - **Pre-Medication:** 
      Oral contrast optional - omit for vascular indication


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 125 mL |
        | Flow Rate | 4 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Abdominal aorta at celiac |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30. Critical for renal artery assessment



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Caudocranial scan direction. Include renal arteries to femoral bifurcation minimum

    === "Nursing Notes"

        - 18-20G IV antecubital

    === "Radiologist Notes"
        - Measure AAA if present. Assess renal and mesenteric arteries. Evaluate iliac vessels

    === "Tips & Tricks"

        - Arms raised. No oral contrast for pure vascular study

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CTA Abdomen Pelvis Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (125 mL)    :active, contrast, 00:00, 31s
      Saline (50mL)          :active, saline, after contrast, 12s
      section Arterial Phase
      CTA Arterial    :crit, scan2, 00:25, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Diaphragm | Femoral heads | N/A | N/A | AP lateral |
    | CTA Arterial | Diaphragm | Femoral heads | Bolus tracked | 0.625 mm | Caudocranial direction |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.375 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Abdomen | 2 mm/2 mm | Vascular | 3 | Abdominal aorta and visceral branches |
    | Axial | Arterial | Pelvis | 2.5 mm/2.5 mm | Vascular | 3 | Iliac vessels |
    | Coronal | Arterial | Full AP | 3 mm/3 mm | Vascular | 3 | MIP coronal aorta and branches |
    | Sagittal | Arterial | Full AP | 3 mm/3 mm | Vascular | 3 | Curved MPR of aorta |


### Additional Reconstructions

3D VR and curved MPR. Measure AAA in 3 planes

Category: Vascular

Protocol Type: Vascular
