# CT Template 

**Last Updated:** 2023-10-28
**Author:** Dr. John Smith

---

<div class="grid cards" markdown>

-   __1. Clinical Indications__

    ---
    - Abdominal pain of unknown etiology
    - Suspected abscess or infection
    - Cancer staging / surveillance

-   __2. Patient Prep__

    ---
    !!! warning "Safety First"
        - **Renal Function:** Verify eGFR > 30.
        - **Allergy:** Check history & follow pre-medication protocol if needed.

    - **Patient Positioning:** Supine, feet-first
    - **NPO Status:** NPO for 4 hours.
    - **Oral Contrast:** 1000 mL solution over 90 mins.
    - **Medications:** None.

-   __3. IV Contrast & Injection__

    ---
    - **IV Access:** 20g or larger IV in antecubital fossa.
    - **Agent:** Isovue 370
    - **Volume:** 100 mL (or weight-based)
    - **Rate:** 4 mL/sec + 40mL Saline Chaser
    - **Timing:** Bolus Tracking in Aorta @ 120 HU

-   __4. Special Notes__

    ---

    === "Tech Notes"

        - Make sure right patient
        - Confirm gating strategy
        - Coach patient through breathing strategy
    
    === "Nursing Notes"

        - Check for medication contraindications
    
    === "Radiologist Notes"

        - Quality Check for cardiac motion or breathing motion

</div>

### Protocol Details
  ```mermaid
      gantt
          title CT Contrast Protocol Timeline
          dateFormat mm:ss
          axisFormat %M:%S
          
          section Contrast
          Contrast bolus (100mL)    :active, contrast, 00:00, 25s
          Saline chaser (50mL)      :active, saline, after contrast, 12s
          
          section Chest
          Arterial phase            :crit, chest_art, 00:25, 5s
          
          section Abdo Pel
          Portal venous phase       :done, pelvis_pv, 01:15, 5s
          Delayed phase             :pelvis_del, 03:00, 5s
  ```

<!-- This is our main set of role-based tabs -->
=== "For Radiologist (Overview)"

    #### Scan & Reconstruction Summary

    | Phase / Type      | Series / Recon Name         | Key Features & Notes                          |
    |:------------------|:----------------------------|:----------------------------------------------|
    | **Scan Acquisition** |                             |                                               |
    |                   | Portal Venous Phase         | ~70 sec delay. Acquired at **2.5mm** thickness |
    | **Reconstructions**  |                             | *All recons created from Portal Venous data*  |
    |                   | Axial Soft Tissue           | 2.5mm thickness                               |
    |                   | Axial Bone Algorithm        | 5.0mm thickness                               |
    |                   | Coronal Soft Tissue         | 3.0mm thickness                               |
    |                   | Sagittal Soft Tissue        | 3.0mm thickness                               |

=== "For Technologist (Full Protocol)"
    
    !!! tip "Reduce Artifact"
        Ensure patient's arms are raised fully above their head to avoid beam hardening artifact through the upper abdomen.

    #### Scan Parameters
    
    | Series Name         | Start Location   | End Location      | Delay (sec) | Slice Thickness | Notes                                      |
    |---------------------|------------------|-------------------|-------------|-----------------|--------------------------------------------|
    | 1. Scout/Topogram   | Diaphragm        | Pubic Symphysis   | N/A         | N/A             | AP and Lateral                             |
    | 2. Portal Venous    | Diaphragm        | Pubic Symphysis   | ~70 sec     | 2.5 mm          | Primary diagnostic series. Use Bolus Tracking. |

    #### Post-Processing Instructions

    !!! info "Reconstruction Source"
        All of the following reconstructions should be generated from the **Portal Venous** series.

    | Plane     | Thickness & Algorithm | From Series     | Notes                                 |
    |-----------|-----------------------|-----------------|---------------------------------------|
    | Axial     | 2.5 mm Soft Tissue    | Portal Venous   | Send to PACS                          |
    | Axial     | 5.0 mm Bone           | Portal Venous   | For spine/pelvis fracture eval        |
    | Coronal   | 3.0 mm Soft Tissue    | Portal Venous   | Send to PACS                          |
    | Sagittal  | 3.0 mm Soft Tissue    | Portal Venous   | Send to PACS                          |
