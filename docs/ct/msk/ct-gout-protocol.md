# CT Gout Protocol

**Last Updated:** 2024-01-15  
**Author:** Dr. Johnson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | DECT or CT | Non-contrast | Joint region to Extended coverage |

    === "Clinical Indications"

        - Gout
        - Tophi
        - Urate deposition
        - CPPD
        - Crystal arthropathy

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** N/A
        - **Allergy:** N/A
    
    - **Position:** Variable - affected joint
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.


-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Dual energy CT if available for urate detection. Single energy if not. Cover affected joint(s). Extended FOV if polyarticular

    === "Nursing Notes"

        - No IV. Document affected joints

    === "Radiologist Notes"
        - Urate crystals color-coded on DECT. Tophi. Joint erosions. Soft tissue deposits. Quantify urate burden

    === "Tips & Tricks"

        - Dual energy preferred for urate detection

</div>


### Protocol Details
  ```mermaid
  ---
  config:
    theme: default
  ---
    gantt
      title CT Gout Protocol Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      
      section Acquisition
      Standard scan    :done, scan1, 00:00, 10s
  ```


=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Joint region | Extended as needed | N/A | N/A | Appropriate views |
    | DECT or CT | Joint region | Extended coverage | N/A | 0.625-1 mm | Dual energy if available |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | Dual energy 80/140Sn or equivalent |
    | mAs | Auto |
    | Rotation Time | 0.5s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gout | Joints | 1 mm/1 mm | Bone and Standard | 3 | Standard images |
    | DECT urate | Gout | Joints | Color overlay | Urate algorithm | N/A | Urate crystal map |
    | 3D volume | Gout | Urate burden | Volumetric | Urate | N/A | Quantify total urate |
    | Coronal | Gout | Joints | 1.5 mm | Bone | N/A | Joint erosions |


### Additional Reconstructions

Urate volume quantification. Color overlay. Document tophi locations

Category: Msk

Protocol Type: Non-Contrast
