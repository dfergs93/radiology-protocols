# CTA Head

**Last Updated:** 2024-01-15  
**Author:** Dr. Thompson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Head (optional) | Non-contrast | Vertex to Foramen magnum |
        | CTA Head | Arterial (bolus tracked) | Skull base to Vertex |

    === "Clinical Indications"

        - Aneurysm screening
        - Subarachnoid hemorrhage
        - Vascular malformation
        - Intracranial stenosis

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
        | Volume | 75-100 mL |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Aortic arch or carotid |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - NC Head optional then CTA skull base to vertex. Bolus tracking. Submillimeter for 3D reconstruction

    === "Nursing Notes"

        - 20G IV minimum. Good bolus essential

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Assess circle of Willis. Aneurysms. Stenosis. Vascular malformations. Anatomic variants

    === "Tips & Tricks"

        - Minimize motion. Thin slices for small aneurysms

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CTA Head Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (75-100 mL)    :active, contrast, 00:00, 16s
      Saline (20mL)          :active, saline, after contrast, 4s
      section Arterial Phase
      CTA Head    :crit, scan1, after contrast, 3s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Vertex | C1 | N/A | N/A | Lateral |
    | NC Head (optional) | Vertex | Foramen magnum | N/A | 5 mm | Baseline if SAH |
    | CTA Head | Skull base | Vertex | Bolus tracked | 0.5-0.625 mm | Submillimeter for 3D |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5-0.6s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTA | Head | 0.75 mm/0.75 mm | Brain | 3 | Source images |
    | MIP | CTA | Circle of Willis | Thick slab | Brain | N/A | Vessel overview |
    | 3D VR | CTA | Intracranial vessels | 0.5 mm source | Brain | N/A | 3D angiogram |
    | Curved MPR | CTA | Individual vessels | 0.75 mm | Brain | 3 | Vessel-specific views |


### Additional Reconstructions

3D VR and MIP. Measure aneurysm if present. Assess A1 A2 dominance

Category: Neuro

Protocol Type: Vascular
