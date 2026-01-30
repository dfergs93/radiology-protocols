# Trauma Chest CT

**Last Updated:** 2024-01-15  
**Author:** Dr. Martinez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Chest | Non-contrast | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Blunt chest trauma
        - Rib fractures
        - Pneumothorax
        - Hemothorax

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A
        - **Allergy:** N/A
    
    - **Position:** Supine with arms raised if possible
    - **NPO Status:** None - trauma
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Single acquisition lung apices to costophrenic angles. RIB REFORMATS required. Submillimeter acquisition

    === "Nursing Notes"

        - Trauma precautions. Arms up if able

    === "Radiologist Notes"
        - Pneumothorax hemothorax. Rib fractures (count and location). Pulmonary contusion. Aortic injury. Sternal/scapular fractures

    === "Tips & Tricks"

        - Submillimeter acquisition critical for rib detail

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title Trauma Chest CT Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | AP and lateral |
    | NC Chest | Lung apices | Costophrenic angles | N/A | 0.625-1 mm | Submillimeter for ribs |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.2 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Chest | Chest | 2.5 mm/2.5 mm | Standard | 3 | Mediastinal window |
    | Axial | Chest | Chest | 2.5 mm/2.5 mm | Lung | 3 | Lung window |
    | Coronal | Chest | Chest | 2.5 mm/2.5 mm | Bone | N/A | Rib overview |
    | Oblique sagittal | Chest | Ribs | 2 mm/2 mm | Bone | N/A | Rib reformats all ribs |


### Additional Reconstructions

Dedicated rib reformats (oblique sagittal each rib). Count fractures. 3D chest wall

Category: Trauma

Protocol Type: Trauma
