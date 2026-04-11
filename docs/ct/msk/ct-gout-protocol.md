---
title: CT Gout Protocol
slug: ct-gout-protocol
category: msk
protocol_type: non-contrast
last_updated: '2024-01-15'
author: Dr. Johnson
synonyms: []
clinical_indications:
- Gout
- Tophi
- Urate deposition
- CPPD
- Crystal arthropathy
position: Variable - affected joint
npo: N/A
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: Dual energy 80/140Sn or equivalent
  mas: Auto
  rotation_time: 0.5s
  pitch: Helical
series:
- name: DECT or CT
  start: Joint region
  end: Extended coverage
  delay: N/A
  thickness: 0.625-1 mm
  notes: Dual energy if available
recons:
- plane: Axial
  acquisition: Gout
  fov: Joints
  thickness_increment: 1 mm/1 mm
  kernel: Bone and Standard
  ir_strength: '3'
  notes: Standard images
- plane: DECT urate
  acquisition: Gout
  fov: Joints
  thickness_increment: Color overlay
  kernel: Urate algorithm
  ir_strength: N/A
  notes: Urate crystal map
- plane: 3D volume
  acquisition: Gout
  fov: Urate burden
  thickness_increment: Volumetric
  kernel: Urate
  ir_strength: N/A
  notes: Quantify total urate
- plane: Coronal
  acquisition: Gout
  fov: Joints
  thickness_increment: 1.5 mm
  kernel: Bone
  ir_strength: N/A
  notes: Joint erosions
notes:
  tech: Dual energy CT if available for urate detection. Single energy if not. Cover
    affected joint(s). Extended FOV if polyarticular
  nursing: No IV. Document affected joints
  rad: Urate crystals color-coded on DECT. Tophi. Joint erosions. Soft tissue deposits.
    Quantify urate burden
  tips: Dual energy preferred for urate detection
  additional_recons: Urate volume quantification. Color overlay. Document tophi locations
safety:
  renal: N/A
  allergy: N/A
---

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
        - Additional Recons: Urate volume quantification. Color overlay. Document tophi locations

    === "Nursing Notes"

        - No IV. Document affected joints

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Urate crystals color-coded on DECT. Tophi. Joint erosions. Soft tissue deposits. Quantify urate burden

    === "Tips & Tricks"

        - Dual energy preferred for urate detection

</div>

<div class="acquisition-diagram"></div>

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
