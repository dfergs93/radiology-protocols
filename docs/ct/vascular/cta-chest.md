# CTA Chest

**Last Updated:** 2024-01-15  
**Author:** Dr. Johnson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | Non-contrast | Lung apices to Costophrenic angles |
        | CTA Arterial Chest | Arterial (bolus tracked) | Lung apices to Costophrenic angles |
        | CT Delayed (optional) | Delayed (40 sec delay) | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Thoracic aortic aneurysm (not involving the aortic root)
        - Great vessel evaluation

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 2 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.2 mL/kg |
        | Flow Rate | 4 mL/s |
        | Duration | 15 - 20s |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta or main PA |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Choose ROI based on indication - ascending aorta for aortic pathology or main PA for PE

    === "Nursing Notes"

        - 20G IV minimum

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Assess aorta and great vessels. Measure aneurysm if present. Look for dissection flap

    === "Tips & Tricks"

        - Arms fully raised

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Lung apices | Adrenal glands | N/A | N/A | AP and lateral |
    | CTA Arterial Chest | Lung apices | Adrenal glands | Bolus tracked | 0.625 mm | Caudocranial direction |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.2 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Arterial | Chest | 1.25 mm/1.25 mm | Vascular | 3 | Primary diagnostic series |
    | Axial | Arterial | Chest | 2.5 mm/2.5 mm | Lung | 3 | Lung window for parenchyma |
    | Coronal | Arterial | Chest | 2.5 mm/2.5 mm | Vascular | 3 | MIP coronal great vessels |
    | Sagittal | Arterial | Chest | 2.5 mm/2.5 mm | Vascular | 3 | MIP sagittal aortic arch |

### Additional Reconstructions

3D VR of thoracic vasculature

Category: Vascular

Protocol Type: Vascular
