# CTA Pelvis Prostate Artery Embolization

**Last Updated:** 2024-01-15  
**Author:** Dr. Jackson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Arterial | Arterial (bolus tracked) | L3 to Proximal femur |

    === "Clinical Indications"

        - Pre-procedural planning for prostate artery embolization
        - Benign prostatic hyperplasia

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history
    
    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 2-4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 100 mL |
        | Flow Rate | 3-4 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Common iliac artery |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Scan from L3 to proximal femur. Arterial phase essential. Focus on internal iliac branches and prostate supply

    === "Nursing Notes"

        - 18-20G IV

    === "Radiologist Notes"
        - Identify prostate artery origins (usually anterior division of internal iliac). Map anatomy for IR. Note variants and anastomoses

    === "Tips & Tricks"

        - Full bladder helpful for prostate visualization. Coordinate with IR before scan

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CTA Pelvis Prostate Artery Embolization Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (100 mL)    :active, contrast, 00:00, 28s
      Saline (50mL)          :active, saline, after contrast, 14s
      section Arterial Phase
      CTA Arterial    :crit, scan1, 00:25, 16s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | L3 | Proximal femur | N/A | N/A | AP pelvis |
    | CTA Arterial | L3 | Proximal femur | Bolus tracked | 0.625 mm | Focus on internal iliac branches |

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
    | Axial | Arterial | Pelvis | 1 mm/1 mm | Vascular | 3 | Identify prostate artery origins |
    | Coronal | Arterial | Pelvis | 1.5 mm/1.5 mm | Vascular | 3 | MIP of iliac vessels |
    | Sagittal | Arterial | Pelvis | 1.5 mm/1.5 mm | Vascular | 3 | Lateral view pelvic vessels |
    | 3D VR | Arterial | Pelvis | 0.75 mm source | Vascular | 3 | 3D roadmap for interventional radiologist |


### Additional Reconstructions

3D VR with prostate vessels highlighted. Curved MPR of internal iliac branches. Measure vessel diameters

Category: Vascular

Protocol Type: Vascular
