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
    
    !!! warning "Safety First"
        - **Renal Function:** Emergency proceed
        - **Allergy:** STAT protocol
    
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
        
        Proceed emergently. Time is brain



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - STAT protocol: 1) NC Head 2) CTA Head/Neck (aortic arch to vertex) 3) CTP (optional). Minimize door-to-scan time

    === "Nursing Notes"

        - No IV for NC. Large bore for CTA/CTP. STAT coordination

    === "Radiologist Notes"
        - NC: hemorrhage early ischemia hyperdense vessel. CTA: LVO large vessel occlusion. CTP: penumbra core mismatch

    === "Tips & Tricks"

        - STAT protocol. Minimize delays. LVO detection critical

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Brain Stroke Protocol Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (100 mL)    :active, contrast, 00:00, 22s
      Saline (50mL)          :active, saline, after contrast, 11s
      section Arterial Phase
      CTA Head    :crit, scan1, 00:25, 8s
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
