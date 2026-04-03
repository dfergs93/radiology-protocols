# Non-Contrast CT Chest Low Dose

**Last Updated:** 2024-01-15  
**Author:** Dr. Kim

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Low Dose Chest | Non-contrast | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Non Contrast chest for patient's age < 60

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - LOW DOSE technique. Reduced mAs 30-50% of standard. Helical acquisition. High IR strength

    === "Nursing Notes"

        - No IV. Explain screening purpose and low radiation

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Lung nodule detection. Measure nodules. Lung-RADS classification. Emphysema assessment

    === "Tips & Tricks"

        - Low dose protocol. High iterative reconstruction. Nodule measurement software

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | Low dose AP |
    | Low Dose Chest | Lung apices | Costophrenic angles | N/A | 1-1.25 mm | Low dose helical |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Low dose (40-60 reference) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.2 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Chest | Chest | 1.25 mm/1.25 mm | Lung | High IR 4-5 | Thin slice nodule detection |
    | Axial | Chest | Chest | 2.5 mm/2.5 mm | Standard | 3 | Mediastinal window |
    | Coronal | Chest | Chest | 2 mm/2 mm | Lung | High IR | Coronal overview |
    | MIP | Chest | Lungs | 5 mm slab | Lung | N/A | Nodule detection |

### Additional Reconstructions

CAD nodule detection. Measure all nodules ≥3mm. Lung-RADS reporting

Category: Chest

Protocol Type: Non-Contrast
