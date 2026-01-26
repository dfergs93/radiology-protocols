# CT Abdomen & Pelvis with IV Contrast

**Last Updated:** 2023-10-27
**Author:** Dr. Jane Doe

---

<div class="grid cards" markdown>

-   __1. Clinical Indications__

    ---
    - Abdominal pain
    - Suspected abscess
    - Cancer staging

-   __2. Patient Prep__

    ---
    !!! warning "Contrast Safety"
        - **Renal:** Verify eGFR > 30.
        - **Allergy:** Check history.

    - **NPO:** 4 hours prior to scan.
    - **Oral Contrast:** 1000 mL over 90 min.
    - **IV Access:** 20g or larger in AC.

-   __3. IV Contrast & Injection__

    ---
    - **Agent:** Isovue 370
    - **Volume:** 100 mL (Weight-based)
    - **Rate:** 4 mL/sec + Saline Chaser
    - **Timing:** Bolus Track @ 120 HU

</div>

---

## 4. Scan Parameters & Reconstructions

???+ note "Acquisition"

    | Series Name     | Start Location | End Location    | Delay   | Slice Thickness | Notes                  |
    |-----------------|----------------|-----------------|---------|-----------------|------------------------|
    | Scout           | Diaphragm      | Pubic Symphysis | N/A     | N/A             | AP and Lat             |
    | Portal Venous   | Diaphragm      | Pubic Symphysis | ~70 sec | 2.5 mm          | Primary diagnostic series |

???+ note "Reconstructions"

    | Plane     | Thickness & Algorithm | From Series     | Notes                                 |
    |-----------|-----------------------|-----------------|---------------------------------------|
    | Axial     | 2.5 mm Soft Tissue    | Portal Venous   | Send to PACS                          |
    | Axial     | 5.0 mm Bone           | Portal Venous   | For spine/pelvis fracture eval        |
    | Coronal   | 3.0 mm Soft Tissue    | Portal Venous   | Send to PACS                          |
    | Sagittal  | 3.0 mm Soft Tissue    | Portal Venous   | Send to PACS                          |


## 5. Final Notes for Technologist

!!! tip "Positioning"
    Ensure the patient's arms are raised above their head to reduce artifact.

!!! info "PACS"
    Verify all reconstructed series have been successfully sent before finishing the exam.