---
title: CT Facial Bones
slug: ct-facial-bones
category: neuro
protocol_type: non-contrast
last_updated: '2024-01-15'
author: Dr. Martinez
synonyms: []
clinical_indications:
- Facial trauma
- Orbital fractures
- Zygoma fractures
- Nasal fractures
- Mandible fractures
position: Supine head-first
npo: N/A
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: '120'
  mas: Auto (reference 250)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: Facial Bones
  start: Frontal sinus
  end: Mandible
  delay: N/A
  thickness: 0.625 mm
  notes: Submillimeter for 3D
recons:
- plane: Axial
  acquisition: Face
  fov: Face
  thickness_increment: 1.25 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Axial bone windows
- plane: Coronal
  acquisition: Face
  fov: Face
  thickness_increment: 1.25 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Coronal face
- plane: Sagittal
  acquisition: Face
  fov: Midface
  thickness_increment: 2 mm/1.5 mm
  kernel: Bone
  ir_strength: N/A
  notes: Sagittal midline
- plane: 3D
  acquisition: Face
  fov: Facial bones
  thickness_increment: 0.625 mm source
  kernel: Bone
  ir_strength: N/A
  notes: 3D surface rendering
notes:
  tech: Frontal sinus to mandible. Submillimeter for 3D. Axial acquisition with multiplanar
    reformats. Remove dentures
  nursing: Remove all facial metal. Dentures out
  rad: Le Fort classification. Orbital floor. Zygoma. Nasal bones. Mandible. NOE complex.
    3D for surgical planning
  tips: Remove dentures and facial metal
  additional_recons: 3D surface rendering. Document Le Fort if present. Orbital floor
    assessment
safety:
  renal: N/A
  allergy: N/A
---

# CT Facial Bones

**Last Updated:** 2024-01-15  
**Author:** Dr. Martinez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Facial Bones | Non-contrast | Frontal sinus to Mandible |

    === "Clinical Indications"

        - Facial trauma
        - Orbital fractures
        - Zygoma fractures
        - Nasal fractures
        - Mandible fractures

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first
    - **NPO Status:** N/A
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Frontal sinus to mandible. Submillimeter for 3D. Axial acquisition with multiplanar reformats. Remove dentures

    === "Nursing Notes"

        - Remove all facial metal. Dentures out

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Le Fort classification. Orbital floor. Zygoma. Nasal bones. Mandible. NOE complex. 3D for surgical planning

    === "Tips & Tricks"

        - Remove dentures and facial metal

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Frontal sinus | Mandible | N/A | N/A | Lateral |
    | Facial Bones | Frontal sinus | Mandible | N/A | 0.625 mm | Submillimeter for 3D |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 250) |
    | Rotation Time | 0.5s |
    | Pitch | Helical |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Face | Face | 1.25 mm/1 mm | Bone | N/A | Axial bone windows |
    | Coronal | Face | Face | 1.25 mm/1 mm | Bone | N/A | Coronal face |
    | Sagittal | Face | Midface | 2 mm/1.5 mm | Bone | N/A | Sagittal midline |
    | 3D | Face | Facial bones | 0.625 mm source | Bone | N/A | 3D surface rendering |

### Additional Reconstructions

3D surface rendering. Document Le Fort if present. Orbital floor assessment

Category: Neuro

Protocol Type: Non-Contrast
