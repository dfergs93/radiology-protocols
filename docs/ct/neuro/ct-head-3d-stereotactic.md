---
title: CT Head 3D Stereotactic
slug: ct-head-3d-stereotactic
category: neuro
protocol_type: neuroradiology
last_updated: '2024-01-15'
author: Dr. Lee
synonyms: []
clinical_indications:
- Stereotactic surgery planning
- DBS planning
- Biopsy planning
- Surgical navigation
- Gamma knife
position: Supine in surgical position. Head in frame if required
npo: N/A
premedication: ''
contrast:
  agent: None typically. Contrast optional
  volume: 'If contrast: 100 mL'
  flow_rate: 3 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 300)
  rotation_time: Helicals
  pitch: Pitch for isotropic
series:
- name: Stereotactic Head
  start: Vertex
  end: Skull base
  delay: N/A (or 60-90s if contrast)
  thickness: 0.5-0.625 mm
  notes: Isotropic submillimeter
recons:
- plane: Axial
  acquisition: Stereo
  fov: Brain
  thickness_increment: 0.5 mm/0.5 mm
  kernel: Brain (Bone if needed)
  ir_strength: '3'
  notes: Isotropic axial
- plane: Coronal
  acquisition: Stereo
  fov: Brain
  thickness_increment: 0.5 mm/0.5 mm
  kernel: Brain
  ir_strength: '3'
  notes: Isotropic coronal
- plane: Sagittal
  acquisition: Stereo
  fov: Brain
  thickness_increment: 0.5 mm/0.5 mm
  kernel: Brain
  ir_strength: '3'
  notes: Isotropic sagittal midline
- plane: 3D surface
  acquisition: Stereo
  fov: Brain
  thickness_increment: 0.5 mm source
  kernel: Brain
  ir_strength: '3'
  notes: Surface for navigation
notes:
  tech: Submillimeter ISOTROPIC acquisition. Vertex to skull base. DICOM for surgical
    planning. Frame or fiducials if required
  nursing: Position exactly as for surgery. Frame placement if required
  rad: Isotropic high-resolution for surgical targeting. Anatomic landmarks. Tumor
    if contrast
  tips: Isotropic voxels critical. Export DICOM to surgical planning
  additional_recons: Export to surgical navigation. Isotropic 0.5mm. Coordinates for
    targeting
safety:
  renal: N/A or verify eGFR
  allergy: N/A or check allergy
---

# CT Head 3D Stereotactic

**Last Updated:** 2024-01-15  
**Author:** Dr. Lee

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Stereotactic Head | Contrast (N/A (or 60-90s if contrast) delay) | Vertex to Skull base |

    === "Clinical Indications"

        - Stereotactic surgery planning
        - DBS planning
        - Biopsy planning
        - Surgical navigation
        - Gamma knife

-   __2. Patient Prep__

    ---

    - **Position:** Supine in surgical position. Head in frame if required
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast optional |
        | Volume | If contrast: 100 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Submillimeter ISOTROPIC acquisition. Vertex to skull base. DICOM for surgical planning. Frame or fiducials if required
        - Additional Recons: Export to surgical navigation. Isotropic 0.5mm. Coordinates for targeting

    === "Nursing Notes"

        - Position exactly as for surgery. Frame placement if required

        !!! warning "Safety First"
            - **Renal Function:** N/A or verify eGFR
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Isotropic high-resolution for surgical targeting. Anatomic landmarks. Tumor if contrast

    === "Tips & Tricks"

        - Isotropic voxels critical. Export DICOM to surgical planning

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Vertex | Skull base | N/A | N/A | Lateral |
    | Stereotactic Head | Vertex | Skull base | N/A (or 60-90s if contrast) | 0.5-0.625 mm | Isotropic submillimeter |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 300) |
    | Rotation Time | Helicals |
    | Pitch | Pitch for isotropic |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Stereo | Brain | 0.5 mm/0.5 mm | Brain (Bone if needed) | 3 | Isotropic axial |
    | Coronal | Stereo | Brain | 0.5 mm/0.5 mm | Brain | 3 | Isotropic coronal |
    | Sagittal | Stereo | Brain | 0.5 mm/0.5 mm | Brain | 3 | Isotropic sagittal midline |
    | 3D surface | Stereo | Brain | 0.5 mm source | Brain | 3 | Surface for navigation |
