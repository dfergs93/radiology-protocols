---
title: Trauma Head C-Spine and Facial Bones
slug: trauma-head-c-spine-and-facial-bones
category: trauma
protocol_type: trauma
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Facial trauma
- Maxillofacial fractures
- Orbital fractures with head/spine injury
position: Supine head-first. C-collar on
npo: None - trauma
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: '120'
  mas: Auto (300 head / 250 other)
  rotation_time: 1.0 / 0.5s
  pitch: '0.5'
series:
- name: NC Head
  start: Vertex
  end: Foramen magnum
  delay: N/A
  thickness: 5 mm
  notes: Standard head
- name: NC C-spine
  start: Skull base
  end: T1
  delay: N/A
  thickness: 0.625 mm
  notes: Submillimeter
- name: NC Facial Bones
  start: Frontal sinus
  end: Mandible
  delay: N/A
  thickness: 0.625 mm
  notes: Submillimeter for 3D
recons:
- plane: Axial
  acquisition: Head
  fov: Brain
  thickness_increment: 5 mm/5 mm
  kernel: Brain/Bone
  ir_strength: '3'
  notes: Brain and skull
- plane: Sagittal
  acquisition: C-spine
  fov: C-spine
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: '3'
  notes: C-spine alignment
- plane: Axial
  acquisition: Face
  fov: Face
  thickness_increment: 1.25 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Facial bones
- plane: Coronal
  acquisition: Face
  fov: Face
  thickness_increment: 1.25 mm/1 mm
  kernel: Bone
  ir_strength: N/A
  notes: Facial coronal
notes:
  tech: 'THREE acquisitions: 1) Head 2) C-spine 3) Facial bones. Face: submillimeter
    helical for 3D. C-collar remains'
  nursing: C-collar precautions. Document mechanism of injury
  rad: 'Head: intracranial injury. C-spine: fractures. Face: Le Fort midface orbital
    mandible fractures'
  tips: C-collar on. Remove dentures if safe
  additional_recons: 3D face reconstruction. Le Fort classification. Orbital floor
    assessment
safety:
  renal: N/A
  allergy: N/A
---

# Trauma Head C-Spine and Facial Bones

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Head | Non-contrast | Vertex to Foramen magnum |
        | NC C-spine | Non-contrast | Skull base to T1 |
        | NC Facial Bones | Non-contrast | Frontal sinus to Mandible |

    === "Clinical Indications"

        - Facial trauma
        - Maxillofacial fractures
        - Orbital fractures with head/spine injury

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first. C-collar on
    - **NPO Status:** None - trauma
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - THREE acquisitions: 1) Head 2) C-spine 3) Facial bones. Face: submillimeter helical for 3D. C-collar remains
        - Additional Recons: 3D face reconstruction. Le Fort classification. Orbital floor assessment

    === "Nursing Notes"

        - C-collar precautions. Document mechanism of injury

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Head: intracranial injury. C-spine: fractures. Face: Le Fort midface orbital mandible fractures

    === "Tips & Tricks"

        - C-collar on. Remove dentures if safe

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Vertex | T1 | N/A | N/A | Lateral |
    | NC Head | Vertex | Foramen magnum | N/A | 5 mm | Standard head |
    | NC C-spine | Skull base | T1 | N/A | 0.625 mm | Submillimeter |
    | NC Facial Bones | Frontal sinus | Mandible | N/A | 0.625 mm | Submillimeter for 3D |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Head | Brain | 5 mm/5 mm | Brain/Bone | 3 | Brain and skull |
    | Sagittal | C-spine | C-spine | 2 mm/2 mm | Bone | 3 | C-spine alignment |
    | Axial | Face | Face | 1.25 mm/1 mm | Bone | N/A | Facial bones |
    | Coronal | Face | Face | 1.25 mm/1 mm | Bone | N/A | Facial coronal |
