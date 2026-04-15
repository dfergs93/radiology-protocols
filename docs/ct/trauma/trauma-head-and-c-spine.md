---
title: Trauma Head and C-Spine
slug: trauma-head-and-c-spine
category: trauma
protocol_type: trauma
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Trauma head injury
- C-spine clearance
- Multi-trauma assessment
position: Supine head-first. Cervical collar in place
npo: None - trauma
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: '120'
  mas: Auto (300 head / 250 spine)
  rotation_time: 1.0 head / 0.5 spines
  pitch: '0.5'
series:
- name: NC Head
  start: Vertex
  end: Foramen magnum
  delay: N/A
  thickness: 5 mm
  notes: Parallel to hard palate
- name: NC C-spine
  start: Skull base
  end: T1
  delay: N/A
  thickness: 0.625 mm
  notes: Helical submillimeter
recons:
- plane: Axial
  acquisition: Head
  fov: Brain
  thickness_increment: 5 mm/5 mm
  kernel: Brain
  ir_strength: '3'
  notes: Brain and bone windows
- plane: Sagittal
  acquisition: C-spine
  fov: C-spine
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: '3'
  notes: Midline and parasagittal
- plane: Coronal
  acquisition: C-spine
  fov: C-spine
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: '3'
  notes: Coronal alignment
- plane: Axial
  acquisition: C-spine
  fov: C-spine
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: '3'
  notes: Axial bone windows
notes:
  tech: 'TWO acquisitions: 1) Head vertex to C1 2) C-spine skull base to T1. Head:
    5mm axial. C-spine: 0.625mm with reformats. Minimize movement'
  nursing: Maintain cervical precautions. C-collar remains on. Document GCS
  rad: 'Head: acute hemorrhage skull fractures. C-spine: fractures alignment ligamentous
    injury'
  tips: Keep C-collar on. Minimize patient movement
  additional_recons: 'C-spine: Sagittal and coronal bone reformats. 3D if complex
    fracture'
safety:
  renal: N/A
  allergy: N/A
---

# Trauma Head and C-Spine

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

    === "Clinical Indications"

        - Trauma head injury
        - C-spine clearance
        - Multi-trauma assessment

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first. Cervical collar in place
    - **NPO Status:** None - trauma
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO acquisitions: 1) Head vertex to C1 2) C-spine skull base to T1. Head: 5mm axial. C-spine: 0.625mm with reformats. Minimize movement
        - Additional Recons: C-spine: Sagittal and coronal bone reformats. 3D if complex fracture

    === "Nursing Notes"

        - Maintain cervical precautions. C-collar remains on. Document GCS

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Head: acute hemorrhage skull fractures. C-spine: fractures alignment ligamentous injury

    === "Tips & Tricks"

        - Keep C-collar on. Minimize patient movement

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout Head | Vertex | C1 | N/A | N/A | Lateral |
    | NC Head | Vertex | Foramen magnum | N/A | 5 mm | Parallel to hard palate |
    | Scout C-spine | Skull base | T1 | N/A | N/A | AP and lateral |
    | NC C-spine | Skull base | T1 | N/A | 0.625 mm | Helical submillimeter |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Head | Brain | 5 mm/5 mm | Brain | 3 | Brain and bone windows |
    | Sagittal | C-spine | C-spine | 2 mm/2 mm | Bone | 3 | Midline and parasagittal |
    | Coronal | C-spine | C-spine | 2 mm/2 mm | Bone | 3 | Coronal alignment |
    | Axial | C-spine | C-spine | 2 mm/2 mm | Bone | 3 | Axial bone windows |
