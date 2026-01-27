# MRI Brain without and with Contrast

**Last Updated:** 2023-10-27
**Author:** Dr. Emily White

---

<div class="grid cards" markdown>

-   __1. Clinical Indications__

    ---
    - Multiple sclerosis evaluation
    - Seizure
    - Suspected tumor or mass

-   __2. Patient & Contrast Prep__

    ---
    !!! warning "Safety First"
        - **Screening:** Full MRI safety screen for implants/devices.
        - **Renal:** Check eGFR > 30 for contrast.
    
    - **IV Access:** 22g or larger.
    - **Contrast Agent:** Gadavist (0.1 mmol/kg)

</div>

---

## Protocol Details

=== "For Radiologist (Overview)"

    #### Sequence & Reconstruction Summary

    | Phase / Type | Sequence / Recon            | Key Features & Notes              |
    |:-------------|:----------------------------|:----------------------------------|
    | **Pre-Contrast** |                             |                                   |
    |              | Sagittal T1 SE                | Midline Anatomy                   |
    |              | Axial T2 FLAIR                | Excellent for MS Lesions          |
    |              | Axial DWI                     | For Acute Stroke                  |
    | **Post-Contrast**|                             |                                   |
    |              | Axial T1 SE                   | <span class="badge">FatSat</span> |
    |              | 3D T1 MPRAGE                  | <span class="badge">3D</span> Isotropic Volume |
    | **Reconstructions**|                         |                                   |
    |              | Coronal & Sagittal Reformats  | From 3D MPRAGE                    |
    |              | ADC Map                       | From DWI                          |


=== "For Technologist (Full Protocol)"

    #### Positioning & Coil
    - **Positioning:** Supine, head-first.
    - **Coil:** Multi-channel Head Coil.
    - **Landmark:** Center at the nasion.

    !!! tip "Straighten the Head"
        Use the laser alignment to ensure the head is perfectly straight. This is critical for good reformats.

    #### Sequence Parameters
    
    | Plane      | Sequence Name    | Slice Thickness | Notes                                      |
    |------------|------------------|-----------------|--------------------------------------------|
    | Sagittal   | T1 SE            | 5 mm            | Localizer and midline anatomy.             |
    | Axial      | T2 FSE           | 5 mm            | Standard T2 for pathology.                 |
    | Axial      | T2 FLAIR         | 5 mm            | Excellent for periventricular lesions (MS).|
    | Axial      | DWI              | 5 mm            | Run before contrast. Generates ADC map.    |
    | Coronal    | T2 FSE           | 4 mm            | For temporal lobes and hippocampus.        |
    | **---ADMINISTER IV CONTRAST---** | | | |
    | Axial      | T1 SE FatSat     | 5 mm            | Post-contrast, check for fat saturation.   |
    | Sagittal   | T1 MPRAGE 3D     | 1 mm (isotropic) | High-res post-contrast volume.             |
    
    #### Post-Processing Instructions

    - **Reconstructions:**
        - From the **3D T1 MPRAGE**, create:
            - 3mm Axial reformats
            - 3mm Coronal reformats
            - 3mm Sagittal reformats
    - **Sending:** Send all acquired series and all three reformatted series to PACS.

