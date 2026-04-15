---
title: CT Sinus Stereotactic
slug: ct-sinus-stereotactic
category: neuro
protocol_type: neuroradiology
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Pre-operative sinus surgery planning
- Image-guided surgery
- ENT surgical navigation
position: Supine head-first. Surgical planning position
npo: N/A
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: '120'
  mas: Auto (reference 200)
  rotation_time: Helicals
  pitch: Pitch for isotropic
series:
- name: Stereotactic Sinus
  start: Frontal sinus
  end: Hard palate
  delay: N/A
  thickness: 0.625 mm
  notes: Isotropic submillimeter
recons:
- plane: Axial
  acquisition: Stereo
  fov: Sinuses
  thickness_increment: 0.625 mm/0.625 mm
  kernel: Bone
  ir_strength: N/A
  notes: Isotropic bone
- plane: Coronal
  acquisition: Stereo
  fov: Sinuses
  thickness_increment: 0.625 mm/0.625 mm
  kernel: Bone
  ir_strength: N/A
  notes: Isotropic coronal
- plane: Sagittal
  acquisition: Stereo
  fov: Sinuses
  thickness_increment: 0.625 mm/0.625 mm
  kernel: Bone
  ir_strength: N/A
  notes: Isotropic sagittal
- plane: 3D surface
  acquisition: Stereo
  fov: Sinuses
  thickness_increment: 0.625 mm source
  kernel: Bone
  ir_strength: N/A
  notes: Surface rendering for navigation
notes:
  tech: Submillimeter isotropic acquisition. DICOM for surgical navigation system.
    May need fiducial markers. Entire sinus anatomy
  nursing: Position as for surgery. Fiducials if required
  rad: Complete sinus anatomy for surgical navigation. Ostiomeatal complex. Skull
    base. Lamina papyracea
  tips: Isotropic voxels essential. DICOM for navigation
  additional_recons: Export DICOM to surgical navigation system. Isotropic 0.625mm
safety:
  renal: N/A
  allergy: N/A
---

# CT Sinus Stereotactic

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Stereotactic Sinus | Non-contrast | Frontal sinus to Hard palate |

    === "Clinical Indications"

        - Pre-operative sinus surgery planning
        - Image-guided surgery
        - ENT surgical navigation

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first. Surgical planning position
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Submillimeter isotropic acquisition. DICOM for surgical navigation system. May need fiducial markers. Entire sinus anatomy
        - Additional Recons: Export DICOM to surgical navigation system. Isotropic 0.625mm

    === "Nursing Notes"

        - Position as for surgery. Fiducials if required

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Complete sinus anatomy for surgical navigation. Ostiomeatal complex. Skull base. Lamina papyracea

    === "Tips & Tricks"

        - Isotropic voxels essential. DICOM for navigation

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Frontal sinus | Hard palate | N/A | N/A | Lateral |
    | Stereotactic Sinus | Frontal sinus | Hard palate | N/A | 0.625 mm | Isotropic submillimeter |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Stereo | Sinuses | 0.625 mm/0.625 mm | Bone | N/A | Isotropic bone |
    | Coronal | Stereo | Sinuses | 0.625 mm/0.625 mm | Bone | N/A | Isotropic coronal |
    | Sagittal | Stereo | Sinuses | 0.625 mm/0.625 mm | Bone | N/A | Isotropic sagittal |
    | 3D surface | Stereo | Sinuses | 0.625 mm source | Bone | N/A | Surface rendering for navigation |
