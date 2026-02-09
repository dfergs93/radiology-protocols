---
title: Brain with and without contrast
---

# Brain with and without contrast

**Last Updated:** 2024-01-15  
**Author:** Dr. Smith

<div class="grid cards" markdown>

-  __1. Clinical Summary__

    ---

    === "Brief Summary"

        | Clinical Purpose | Sequences |
        |------------------|-----------|
        | Localization | Localizer |
        | Pre-contrast anatomical | T1 FLAIR |
        | Anatomical detail | T2 FSE |
        | Lesion detection | T2 FLAIR |
        | Enhancement detection | T1 +C, T1 +C, T1 +C |
        | Acute ischemia detection | DWI |


    === "Clinical Indications"

        - Evaluation for brain tumor or metastases

-  __2. Patient Prep__
    ---

    - **Position:** Supine head first
    - **NPO Status:** None required
    - **Premedication:** None

-  __3. Contrast Protocol__

    ---

    **Agent:** Gadavist  
    **Volume:** 0.1 mmol/kg  
    **Rate:** 2 mL/s  
    **Timing:** Before seq 5

-  __4. Special Notes__

    ---

    === "Technologist Notes"
        - Ensure patient can remain still for 30+ minutes

    === "Nursing Notes"
        - IV access required - 22g or larger

    === "Radiologist Notes"
        - Review DWI for acute infarct

    === "Tips & Tricks"
        - Review all sequences before starting
        - Verify contrast timing matches clinical question
        - Check image quality after each sequence
        - Communicate with patient regularly

</div>

## Acquisition Protocol

=== "Abbreviated Parameters"

    | Plane | Sequence Name | Comments |
    |-------|---------------|----------|
    | 3-plane | Localizer | Quick scout images |
    | Sagittal | T1 FLAIR | Pre-contrast T1 |
    | Axial | T2 FSE | T2 weighted imaging |
    | Axial | T2 FLAIR | Suppress CSF signal |
    | Axial | T1 +C | Post-contrast T1 |
    | Coronal | T1 +C | Post-contrast T1 coronal |
    | Sagittal | T1 +C | Post-contrast T1 sagittal |
    | Axial | DWI | Diffusion weighted imaging |

=== "Full Parameters"

    | Plane | Sequence | Pulse Seq | Options | TR | TE | TI/FA | ETL | BW | FOV | ST/Space | NEX | Matrix | Freq Dir | Slices | Time | Comments |
    |-------|----------|-----------|---------|----|----|-------|-----|----|----|----------|-----|--------|----------|--------|------|----------|
    | 3-plane | Localizer | GRE | Fast | 20 | 5 | 20 | 1 | 31.25 | 24 | 5/0 | 1 | 256x256 | A/P | 3 | 0:30 | Quick scout images |
    | Sagittal | T1 FLAIR | FLAIR | Fast | 2500 | 24 | 860 | 1 | 31.25 | 24 | 5/0 | 1 | 256x256 | A/P | 28 | 4:30 | Pre-contrast T1 |
    | Axial | T2 FSE | FSE | Fast | 4500 | 102 | 90 | 16 | 31.25 | 24 | 5/0 | 2 | 256x256 | A/P | 28 | 3:45 | T2 weighted imaging |
    | Axial | T2 FLAIR | FLAIR | Fast | 9000 | 120 | 2250 | 1 | 31.25 | 24 | 5/0 | 1 | 256x256 | A/P | 28 | 4:15 | Suppress CSF signal |
    | Axial | T1 +C | FLAIR | Fast | 2500 | 24 | 860 | 1 | 31.25 | 24 | 5/0 | 1 | 256x256 | A/P | 28 | 4:30 | Post-contrast T1 |
    | Coronal | T1 +C | FLAIR | Fast | 2500 | 24 | 860 | 1 | 31.25 | 24 | 5/0 | 1 | 256x256 | R/L | 28 | 4:30 | Post-contrast T1 coronal |
    | Sagittal | T1 +C | FLAIR | Fast | 2500 | 24 | 860 | 1 | 31.25 | 24 | 5/0 | 1 | 256x256 | A/P | 28 | 4:30 | Post-contrast T1 sagittal |
    | Axial | DWI | EPI | Asset | 8000 | 80 | N/A | 1 | 250 | 24 | 5/0 | 2 | 128x128 | A/P | 28 | 2:00 | Diffusion weighted imaging |
