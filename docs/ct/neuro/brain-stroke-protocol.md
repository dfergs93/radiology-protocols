# Brain Stroke Protocol

**Last Updated:** 2024-01-15  
**Author:** Dr. Williams

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Head | Non-contrast | Vertex to Foramen magnum |
        | CTA Head | Arterial (bolus tracked) | Skull base to Vertex |
        | CTA Neck | Contrast (Continues from head delay) | Aortic arch to Skull base |
        | CTP (optional) | Contrast (Auto-triggered delay) | Basal ganglia level to 8cm slab |

    === "Clinical Indications"

        - Acute stroke
        - CVA
        - Neurological deficit < 24 hours
        - Stroke code

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first
    - **NPO Status:** None - emergency
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 for CTA/CTP |
        | Volume | 100 mL |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Multi-phase stroke protocol |
        | ROI Placement | Multiple ROIs |
        | Trigger (HU) | Varies |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - STAT protocol: 1) NC Head 2) CTA Head/Neck (aortic arch to vertex) 3) CTP (optional). Minimize door-to-scan time

    === "Nursing Notes"

        - No IV for NC. Large bore for CTA/CTP. STAT coordination

        !!! warning "Safety First"
            - **Renal Function:** Emergency proceed
            - **Allergy:** STAT protocol

    === "Radiologist Notes"

        - NC: hemorrhage early ischemia hyperdense vessel. CTA: LVO large vessel occlusion. CTP: penumbra core mismatch

    === "Tips & Tricks"

        - STAT protocol. Minimize delays. LVO detection critical

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
      title Brain Stroke Protocol Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (100 mL)    :active, contrast, 00:00, 22s
      Saline          :active, saline, after contrast, 4s
      section Head
      CTA Head    :crit, scan1, after contrast, 3s
      section Neck
      CTA Neck    :crit, scan2, 00:00, 10s
      section Other
      CTP (optional)    :done, scan3, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Vertex | Aortic arch | N/A | N/A | STAT lateral |
    | NC Head | Vertex | Foramen magnum | N/A | 5 mm | STAT no contrast |
    | CTA Head | Skull base | Vertex | Bolus tracked aorta | 0.625 mm | Intracranial vessels |
    | CTA Neck | Aortic arch | Skull base | Continues from head | 0.625 mm | Extracranial vessels |
    | CTP (optional) | Basal ganglia level | 8cm slab | Auto-triggered | 5 mm dynamic | Perfusion if candidate |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (300 head) |
    | Rotation Time | 1.0 / 0.5s |
    | Pitch | 0.5 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | NC head | Brain | 5 mm/5 mm | Brain | 3 | STAT hemorrhage detection |
    | Axial | CTA head | Brain | 1 mm/1 mm | Brain | 3 | LVO detection |
    | MIP | CTA | Circle of Willis | Thick slab | Brain | N/A | Vessel overview |
    | CTP maps | CTP | Perfusion | Color maps | N/A | N/A | CBF CBV MTT Tmax maps |


### Additional Reconstructions

CTA MIP and 3D. CTP perfusion maps if done. ASPECTS score. LVO documentation

Category: Neuro

Protocol Type: Neuroradiology
