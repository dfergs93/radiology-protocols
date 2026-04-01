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

    - **Position:** Supine head-first with arms at sides
    - **NPO Status:** NPO 2 hours
    - **Pre-Medication:**
        - None typically. Consider anxiolytic if severe claustrophobia

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
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Scan from aortic arch through vertex. Use bolus tracking in arch. Minimize dental artifact with gantry angulation

    === "Nursing Notes"

        - Good antecubital IV access required - 20G minimum. Verify injection site for extravasation risk

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history and renal function

    === "Radiologist Notes"

        - Evaluate complete circle of Willis. Assess carotid bifurcations. Look for dissection. Check aneurysms

    === "Tips & Tricks"

        - Remove dentures. Minimize swallowing during neck acquisition

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
      title CTA Head and Neck (Arch to Vertex) Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (80-100 mL)    :active, contrast, 00:00, 17s
      Saline          :active, saline, after contrast, 4s
      section Head
      CTA Head    :crit, scan1, after saline, 3s
      section Neck
      CTA Neck    :crit, scan2, after contrast, 5s
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

Category: Neuro

Protocol Type: Vascular
