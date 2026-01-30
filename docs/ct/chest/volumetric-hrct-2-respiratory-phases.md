# Volumetric HRCT 2 Respiratory Phases

**Last Updated:** 2024-01-15  
**Author:** Dr. White

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Volumetric Inspiration | Contrast (Full inspiration delay) | Lung apices to Costophrenic angles |
        | Limited Expiration | Contrast (Full expiration delay) | Carina to Costophrenic angles |

    === "Clinical Indications"

        - Interstitial lung disease initial evaluation
        - ILD diagnosis
        - Diffuse lung disease

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A
        - **Allergy:** N/A
    
    - **Position:** Supine with arms raised
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO acquisitions: 1) Full INSPIRATION 2) Limited EXPIRATION (carina to bases). Volumetric (contiguous thin slice). Coach breathing

    === "Nursing Notes"

        - No IV. Careful breath hold coaching. Inspiration and expiration

    === "Radiologist Notes"
        - ILD pattern recognition. Honeycombing. Ground glass. Reticular. Mosaic attenuation on expiration

    === "Tips & Tricks"

        - Volumetric contiguous slices. Coach breathing carefully

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Volumetric HRCT 2 Respiratory Phases Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | AP lateral |
    | Volumetric Inspiration | Lung apices | Costophrenic angles | Full inspiration | 1 mm | Contiguous 1mm slices |
    | Limited Expiration | Carina | Costophrenic angles | Full expiration | 1 mm | Limited coverage expiration |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 150-200) |
    | Rotation Time | 0.5s |
    | Pitch | 1 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Inspiration | Chest | 1 mm/1 mm | Lung | 3 | Thin slice ILD assessment |
    | Axial | Expiration | Lower lungs | 1 mm/1 mm | Lung | 3 | Air trapping assessment |
    | Coronal | Inspiration | Chest | 1.5 mm | Lung | 3 | ILD distribution |
    | Sagittal | Inspiration | Chest | 2 mm | Lung | 3 | Craniocaudal distribution |


### Additional Reconstructions

Thin slice for ILD detail. Compare inspiration vs expiration. Quantitative analysis if available

Category: Chest

Protocol Type: Chest/Pulmonary
