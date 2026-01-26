# MRI Template Name

**Last Updated:** 2025-07-21
**Protocol Author:** Dr. Duncan Ferguson

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
        - Ensure Respiratory bellows and ECG gating is adequate
        - Center coil over area of interest
    
    === "Nursing Notes"

        - Check for medication contraindications
    
    === "Radiologist Notes"

        - Quality Check for cardiac motion or breathing motion

</div>

### Sequence Parameters

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

=== "Full Sequence Parameters"

    | #     | Series Description          | Plane   | Pulse Sequence  | Imaging Options              | TR       | TE      | TI/FA            | ETL       | BW   | FOV            | Slice Thickness/Space       | NEX  | Matrix Fr/Ph  | Frequency Direction | # Slices | Time     | Comments                                      | Images |
    |-------|-----------------------------|---------|-----------------|------------------------------|----------|---------|------------------|-----------|------|----------------|-----------------------------|------|---------------|---------------------|----------|----------|-----------------------------------------------|--------|
    |   1   |   3Pl-Locs/Cal              |   3     |   Loc   FGRE    |   Seq, Fast                  |   N      |   N     |                  |   N N     |      |   24           |   5/5mm                     |   1  |   256   128   |   U                 |          |   0:14   |                                               |        |
    |   2   |   SAG T1 FLAIR              |   O/S   |   FSE-XL        |   Seq,TRF   Fast             |   2100   |   24    |   750            |   5 31    |      |   24           |   4/1mm                     |   2  |   320   256   |   S/I               |   27     |   3:47   |   Max Slices=28                               |        |
    |   3   |   HiRes Axial DWI   1000b   |   O/A   |   SE            |   EPI,DIFF,Asset             |   8000   |   Min   |                  |   16      |      |   24           |   5/0.5mm                   |   4  |   128   256   |   R/L               |   27     |   2:16   |   Diff,Dir=All   ST is different   ADC Map    |        |
    |   4   |   Axial T2   FRFSE          |   O/A   |   FRFSE-   XL   |   FC,TRF   Fast,FR           |   2717   |   85    |                  |   16 31   |      |   22           |   4/1mm   (0.75)            |   2  |   384   256   |   A/P               |   28     |   2:43   |   Angle to AC-PC   Keep #30~32                |        |
    |   5   |   Axial T2   FLAIR          |   O/A   |   T2flair       |   FC,EDR,TRF   Fast,ZIP512   |   8000   |   120   |   2000           |   25      |      |   22           |   4/1mm                     |   2  |   256   224   |   A/P               |   28     |   4:48   |   Don’t change   TR ,TE                       |        |
    |   6   |   T1 SPGR   IR PREPPED      |   O/A   |   SPGR          |   Fast,IrP                   |   N      |   Min   |   450   /   12   |   N 15    |      |   25   (0.75)  |   1.4mm   Locs   Slab:126   |   1  |   256   256   |   A/P               |   126    |   5:28   |   Angle to AC-PC   COR-Reformat   4x4mm/22cm  |        |
    |   7   |   (opt)Axial DWI   1000b    |   O/A   |   SE            |   EPI,DIFF,Asset             |   8000   |   Min   |                  |   16      |      |   28           |   5/0.5mm                   |   1  |   128   192   |   R/L               |   27     |   :40    |   Diff,Dir=All   ADC Map                      |        |
    |   8   |                             |         |                 |                              |          |         |                  |           |      |                |                             |      |               |                     |          |          |                                               |        |
    | 9     |                             |         |                 |                              |          |         |                  |           |      |                |                             |      |               |                     |          |          |                                               |        |
    | 10    |                             |         |                 |                              |          |         |                  |           |      |                |                             |      |               |                     |          |          |                                               |        |

### Resources
- Links to videos, pdfs, other resources to help understand acquisition or interpretation