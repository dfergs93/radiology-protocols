# CTV Head

**Last Updated:** 2024-01-15  
**Author:** Dr. Rodriguez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Head | Non-contrast | Vertex to Foramen magnum |
        | CTV Head | Contrast (60-90 sec delay delay) | Skull base to Vertex |

    === "Clinical Indications"

        - Venous sinus thrombosis
        - Dural sinus thrombosis
        - Intracranial hypertension
        - Venous malformation

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
        | Flow Rate | 3-4 mL/s |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - NC Head then delayed venous CTV (60-90 sec). Skull base to vertex. Assess venous sinuses

    === "Nursing Notes"

        - 18-20G IV

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - NC: hemorrhage. CTV: filling defects in sinuses. Venous thrombosis. Cortical vein thrombosis

    === "Tips & Tricks"

        - Delayed timing 60-90 sec. Look for filling defects

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CTV Head Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (75-100 mL)    :active, contrast, 00:00, 21s
      Saline (20mL)          :active, saline, after contrast, 5s
      section Scan Phase 1
      CTV Head    :done, scan1, 01:00, 3s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Vertex | C1 | N/A | N/A | Lateral |
    | NC Head | Vertex | Foramen magnum | N/A | 5 mm | Baseline |
    | CTV Head | Skull base | Vertex | 60-90 sec delay | 0.625-1 mm | Venous phase |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5-0.6s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTV | Head | 1 mm/1 mm | Brain | 3 | Venous sinuses |
    | MIP | CTV | Sinuses | Thick slab | Brain | N/A | Venogram overview |
    | 3D VR | CTV | Venous system | 1 mm source | Brain | N/A | 3D venogram |
    | Sagittal | CTV | Midline | 1.5 mm | Brain | 3 | Sagittal sinus |


### Additional Reconstructions

3D VR venogram. MIP maximum intensity projection. Document filling defects

Category: Neuro

Protocol Type: Vascular
