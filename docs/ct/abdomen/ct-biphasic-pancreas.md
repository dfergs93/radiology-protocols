# CT Biphasic Pancreas

**Last Updated:** 2024-01-15  
**Author:** Dr. Williams

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Pancreatic Phase | Arterial (bolus tracked) | Diaphragm to Iliac crests |
        | Portal Venous | Contrast (70 sec delay) | Diaphragm to Iliac crests |

    === "Clinical Indications"

        - Pancreatic mass
        - Pancreatitis
        - Pancreatic cyst characterization

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30
        - **Allergy:** Check allergy history. Coordinate water intake
    
    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    - **Pre-Medication:** 
      Water PO: 900 mL water orally 15-30 min before scan for gastric/duodenal distension


-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Dual phase: Pancreatic arterial + Portal venous |
        | ROI Placement | Abdominal aorta |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        
        Full dose if eGFR > 30



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO phases: Pancreatic phase (40-45s or bolus track) + Portal venous (70s). Water for negative contrast

    === "Nursing Notes"

        - 18-20G IV. Ensure water intake for duodenal distension

    === "Radiologist Notes"
        - Pancreatic phase: optimal pancreatic enhancement and small lesions. Portal venous: liver and venous structures

    === "Tips & Tricks"

        - Water distension of duodenum helpful. Thin slices for pancreas

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Biphasic Pancreas Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.5 mL/kg)    :active, contrast, 00:00, 23s
      Saline (50mL)          :active, saline, after contrast, 11s
      section Scan Phase 1
      Pancreatic Phase    :crit, scan1, 00:40, 12s
      section Portal Venous Phase
      Portal Venous    :done, scan2, 01:10, 12s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Iliac crests | N/A | N/A | AP |
    | Pancreatic Phase | Diaphragm | Iliac crests | 40-45 sec or bolus track | 1-1.25 mm | Thin slices for small lesions |
    | Portal Venous | Diaphragm | Iliac crests | 70 sec | 2.5 mm | Standard PV phase |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto (reference 200-250) |
    | Rotation Time | 0.5s |
    | Pitch | 0.9-1.0 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Pancreatic | Pancreas | 1.5 mm/1.5 mm | Standard | 3 | Thin slice pancreas |
    | Axial | Portal venous | Abdomen | 2.5 mm/2.5 mm | Standard | 3 | Liver and vessels |
    | Coronal | Both phases | Abdomen | 2.5 mm/2.5 mm | Standard | 3 | Pancreatic and peripancreatic |
    | Curved MPR | Pancreatic | Pancreatic duct | 1.5 mm | Standard | 3 | Duct evaluation |


### Additional Reconstructions

Curved MPR pancreatic duct. MIP pancreatic vasculature

Category: Abdomen

Protocol Type: Contrast-Enhanced
