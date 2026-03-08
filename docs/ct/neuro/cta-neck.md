# CTA Neck

**Last Updated:** 2024-01-15  
**Author:** Dr. Kim

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTA Neck | Arterial (bolus tracked) | Aortic arch to Skull base |

    === "Clinical Indications"

        - Carotid stenosis
        - Vertebral artery dissection
        - Neck vessel assessment
        - Pre-CEA planning

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first
    - **NPO Status:** NPO 2 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 90-100 mL |
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

        - Aortic arch to skull base. Bolus tracking in arch. Submillimeter. Minimize swallowing during scan

    === "Nursing Notes"

        - 20G IV antecubital preferred

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Assess carotid bifurcations. Stenosis grading. Vertebral arteries. Dissection. Plaque morphology

    === "Tips & Tricks"

        - Minimize swallowing. Submillimeter acquisition

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
      title CTA Neck Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (90-100 mL)    :active, contrast, 00:00, 20s
      Saline          :active, saline, after contrast, 4s
      section Neck
      CTA Neck    :crit, scan1, after contrast, 5s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Aortic arch | Skull base | N/A | N/A | AP lateral |
    | CTA Neck | Aortic arch | Skull base | Bolus tracked | 0.625 mm | Caudocranial |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 0.9 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTA | Neck | 1 mm/1 mm | Vascular | 3 | Source images |
    | Coronal | CTA | Neck | 1.5 mm | Vascular | 3 | Vessel overview |
    | Sagittal | CTA | Carotids | 1.5 mm | Vascular | 3 | Vertebral arteries |
    | Curved MPR | CTA | Carotid bifurcations | 1 mm | Vascular | 3 | Stenosis measurement |


### Additional Reconstructions

Curved MPR both carotid bifurcations. Measure stenosis (NASCET). 3D VR. MIP

Category: Neuro

Protocol Type: Vascular
