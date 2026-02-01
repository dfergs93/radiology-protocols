# CTA SCAD/FMD Protocol

**Last Updated:** 2024-01-15  
**Author:** Dr. Hayes

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast Head | Non-contrast | Vertex to Foramen magnum |
        | CTA Neck | Arterial (bolus tracked) | Aortic arch to Vertex |
        | CTA CAP | Contrast (35 sec after neck delay) | Diaphragm to Pubic symphysis |
        | Post-contrast Head | Contrast (After CAP delay) | Vertex to Foramen magnum |

    === "Clinical Indications"

        - Spontaneous coronary artery dissection screening
        - Fibromuscular dysplasia screening
        - Multi-vessel arterial assessment

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history. Explain arm repositioning
    
    - **Position:** Supine with arms initially UP then DOWN
    - **NPO Status:** NPO 4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 150 mL total |
        | Flow Rate | 4 mL/s |
        | Timing Method | Multi-phase: NC Head + CTA Neck + CTA CAP arms up + Post-contrast Head arms down |
        | ROI Placement | Multiple ROIs |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30. Large volume for multiple phases



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - FOUR acquisitions: 1) NC Head arms down 2) CTA Neck bolus track 3) CTA CAP arms up 4) Post Head arms down. Patient repositions arms between scans

    === "Nursing Notes"

        - 20G IV minimum. Verify good flow for multiple phases

    === "Radiologist Notes"
        - Screen all vascular beds for FMD. Look for beading stenosis aneurysm dissection. Assess renal carotid vertebral intracranial arteries

    === "Tips & Tricks"

        - Coach patient on arm repositioning. Multiple phases require good IV. Plan scan sequence carefully

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CTA SCAD/FMD Protocol Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (150 mL total)    :active, contrast, 00:00, 37s
      Saline (50mL)          :active, saline, after contrast, 12s
      section Arterial Phase
      CTA Neck    :crit, scan1, 00:25, 25s
      section Arterial Phase
      CTA CAP    :crit, scan2, 00:35, 25s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Non-contrast Head | Vertex | Foramen magnum | N/A | 5 mm | Arms down - baseline |
    | CTA Neck | Aortic arch | Vertex | Bolus tracked | 0.625 mm | Arms down - carotid/vertebral |
    | CTA CAP | Diaphragm | Pubic symphysis | 35 sec after neck | 0.625 mm | Arms UP - renal and mesenteric |
    | Post-contrast Head | Vertex | Foramen magnum | After CAP | 1.25 mm | Arms DOWN - intracranial vessels |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto (reference 200-250) |
    | Rotation Time | 0.5s |
    | Pitch | 0.9-1.2 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | All phases | Respective FOV | Phase-specific | Vascular | 3 | Comprehensive arterial assessment |
    | Coronal | CTA phases | Full body | 2-3 mm/2-3 mm | Vascular | 3 | MIP of all arterial territories |
    | Sagittal | CTA phases | Full body | 2-3 mm/2-3 mm | Vascular | 3 | Lateral views all vessels |
    | 3D VR | CTA phases | Full body | 1 mm source | Vascular | 3 | 3D reconstruction multi-territory |


### Additional Reconstructions

Comprehensive MIP and 3D VR of all vascular beds. Measure vessel diameters. Document FMD findings

Category: Vascular

Protocol Type: Vascular
