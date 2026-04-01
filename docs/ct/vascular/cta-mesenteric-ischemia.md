# CTA Mesenteric Ischemia

**Last Updated:** 2024-01-15  
**Author:** Dr. Lee

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | N/A | Diaphragm to Lesser Trochanters |
        | Arterial Phase | Contrast (25 sec delay) | Diaphragm to Lesser Trochanters |
        | Portal Venous | Contrast (70 sec delay) | Diaphragm to Lesser Trochanters |

    === "Clinical Indications"

        - Acute mesenteric ischemia
        - Chronic mesenteric ischemia
        - Bowel infarction

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO (emergent - as patient presents)
    - **Pre-Medication:**
        - None - emergent study

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 5 mL/s |
        | Duration | 20s |
        | Timing Method | Dual phase: Arterial + Portal Venous |
        | ROI Placement | Abdominal aorta at celiac |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)



-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Arterial phase at 25 sec for vessel assessment. Portal venous at 70 sec for bowel perfusion. High flow rate critical

    === "Nursing Notes"

        - 18-20G IV required for 5 mL/s flow. Must be patent

        !!! warning "Safety First"
            - **Renal Function:** eGFR > 30 preferred
            - **Allergy:** Emergency study - document indication

    === "Radiologist Notes"

        - Arterial: assess celiac SMA IMA origins. Portal: look for bowel wall enhancement. Check for pneumatosis

    === "Tips & Tricks"

        - Fast scan. High flow rate essential

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
      title CTA Mesenteric Ischemia Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Contrast Injection
      Contrast (1.5 mL/kg)    :active, contrast, 00:00, 25s
      Saline          :active, saline, after contrast, 5s
      section Other
      Arterial Phase    :crit, scan1, after saline, 5s
      Portal Venous    :done, scan2, 01:10, 5s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Diaphragm | Pubic symphysis | N/A | N/A | AP |
    | Arterial Phase | Diaphragm | Iliac crests | 25 sec | 0.625 mm | Focus on celiac SMA IMA |
    | Portal Venous | Diaphragm | Pubic symphysis | 70 sec | 0.625 mm | Assess bowel wall enhancement |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto (reference 300) |
    | Rotation Time | 0.5s |
    | Pitch | 1.375 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Abdomen | 2 mm/2 mm | Vascular | 3 | Mesenteric vessel origins |
    | Axial | Portal venous | Full AP | 2.5 mm/2.5 mm | Standard | 3 | Bowel wall assessment |
    | Coronal | Arterial | Abdomen | 2.5 mm/2.5 mm | Vascular | 3 | MIP of mesenteric vessels |
    | Sagittal | Arterial | Abdomen | 2.5 mm/2.5 mm | Vascular | 3 | Curved MPR SMA from origin |


### Additional Reconstructions

MIP and 3D VR of celiac and SMA. Curved MPR of vessels

Category: Vascular

Protocol Type: Vascular
