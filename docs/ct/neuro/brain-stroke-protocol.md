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
        | CTA Arch to Vertex | Arterial (bolus tracked) | Aortic arch to Vertex |
        | CTP (optional) | Contrast (Auto-triggered delay) | Skull base to Vertex |

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
        | Agent | IsoVue 370 for CTA/CTP |
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

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Vertex | Aortic arch | N/A | N/A | STAT lateral |
    | NC Head | Skull base | Vertex | N/A | 5 mm | STAT no contrast |
    | CTA Arch to Vertex | Aortic arch | Vertex | Bolus tracked aorta | 0.625 mm | Intracranial vessels |
    | CTP (optional) | Skull base | Vertex | Auto-triggered | 5 mm dynamic | Perfusion if candidate |

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
    | Axial | CTA Arch to Vertex | Head and Neck | 1 mm/1 mm | Brain | 3 | LVO detection |
    | MIP | CTA | Circle of Willis | Thick slab | Brain | N/A | Vessel overview |
    | CTP maps | CTP | Perfusion | Color maps | N/A | N/A | CBF CBV MTT Tmax maps |

### Additional Reconstructions

CTA MIP and 3D. CTP perfusion maps if done. ASPECTS score. LVO documentation

Category: Neuro

Protocol Type: Neuroradiology
