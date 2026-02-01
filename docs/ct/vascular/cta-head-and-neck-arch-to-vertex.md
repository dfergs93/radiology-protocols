# CTA Head and Neck (Arch to Vertex)

**Last Updated:** 2026-01-04  
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Neck | Arterial (bolus tracked) | Aortic arch to Skull base |
        | CTA Head | Contrast (Immediate delay) | Skull base to Vertex |

    === "Clinical Indications"

        - Stroke workup
        - Carotid stenosis
        - Vertebral artery dissection
        - Aneurysm screening

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history and renal function
    
    - **Position:** Supine head-first with arms at sides
    - **NPO Status:** NPO 2 hours
    - **Pre-Medication:** 
      None typically. Consider anxiolytic if severe claustrophobia


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 80-100 mL |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Aortic arch |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Scan from aortic arch through vertex. Use bolus tracking in arch. Minimize dental artifact with gantry angulation

    === "Nursing Notes"

        - Good antecubital IV access required - 20G minimum. Verify injection site for extravasation risk

    === "Radiologist Notes"
        - Evaluate complete circle of Willis. Assess carotid bifurcations. Look for dissection. Check aneurysms

    === "Tips & Tricks"

        - Remove dentures. Minimize swallowing during neck acquisition

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CTA Head and Neck (Arch to Vertex) Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (80-100 mL)    :active, contrast, 00:00, 17s
      Saline (50mL)          :active, saline, after contrast, 11s
      section Arterial Phase
      CTA Neck    :crit, scan1, 00:25, 16s
      section Arterial Phase
      CTA Head    :crit, scan2, after scan1, 8s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Aortic arch | Vertex | N/A | N/A | AP and lateral |
    | CTA Neck | Aortic arch | Skull base | Bolus tracked | 0.625 mm | Arterial phase - caudocranial |
    | CTA Head | Skull base | Vertex | Immediate | 0.625 mm | Same bolus as neck - single acquisition |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5s |
    | Pitch | 0.9 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTA | Neck | 1 mm/1 mm | Vascular | 3 | Submillimeter for carotid assessment |
    | Axial | CTA | Head | 1 mm/1 mm | Vascular | 3 | Submillimeter for circle of Willis |
    | Coronal | CTA | Neck | 2 mm/2 mm | Vascular | 3 | MIP for carotid overview |
    | Sagittal | CTA | Full | 2 mm/2 mm | Vascular | 3 | MIP for vertebral arteries |


### Additional Reconstructions

MIP and 3D VR reconstructions of vessels. Curved MPR of carotids

Category: Vascular

Protocol Type: Vascular
