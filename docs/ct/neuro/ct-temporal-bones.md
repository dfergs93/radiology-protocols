---
title: CT Temporal Bones
slug: ct-temporal-bones
category: neuro
protocol_type: neuroradiology
last_updated: '2026-01-01'
author: 
synonyms: []
clinical_indications:
- Hearing loss
- Chronic otitis
- Cholesteatoma
- Temporal bone fracture
- Pre-operative cochlear implant
position: Supine head-first
npo: N/A
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: '120'
  mas: High mAs (300-400)
  rotation_time: Axial/Coronals
  pitch: Sequential or helical
series:
- name: Axial Temporal
  start: EAC
  end: Petrous apex
  delay: N/A
  thickness: 0.5-0.625 mm
  notes: Parallel to lateral SCC
- name: Coronal Temporal
  start: EAC
  end: IAC
  delay: N/A
  thickness: 0.5-0.625 mm
  notes: Perpendicular to petrous ridge
recons:
- plane: Axial
  acquisition: Temporal
  fov: Bilateral
  thickness_increment: 0.5 mm/0.5 mm
  kernel: Bone sharp
  ir_strength: N/A
  notes: Ultra HR bone
- plane: Coronal
  acquisition: Temporal
  fov: Bilateral
  thickness_increment: 0.5 mm/0.5 mm
  kernel: Bone sharp
  ir_strength: N/A
  notes: Coronal bone
- plane: Oblique sagittal
  acquisition: Temporal
  fov: Ossicles
  thickness_increment: 0.5 mm
  kernel: Bone
  ir_strength: N/A
  notes: Ossicular chain
- plane: Pöschl/Stenvers
  acquisition: Temporal
  fov: IAC
  thickness_increment: 0.75 mm
  kernel: Bone
  ir_strength: N/A
  notes: IAC oriented views
notes:
  tech: 'Temporal bones: external auditory canal to petrous apex. SUBMILLIMETER <0.625mm.
    Direct axial and direct coronal if possible. Ultra high resolution'
  nursing: No IV. Remove hearing aids and earrings
  rad: Ossicles. Cochlea. Semicircular canals. Internal auditory canal. Mastoid air
    cells. Cholesteatoma. Fracture. Tegmen
  tips: Submillimeter critical. Sharp bone kernel. Remove all metal
  additional_recons: Pöschl and Stenvers oblique reformats for IAC. Measure vestibular
    aqueduct
safety:
  renal: N/A
  allergy: N/A
---

# CT Temporal Bones

**Last Updated:** 2026-01-01
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Axial Temporal | Non-contrast | EAC to Petrous apex |
        | Coronal Temporal | Non-contrast | EAC to IAC |

    === "Clinical Indications"

        - Hearing loss
        - Chronic otitis
        - Cholesteatoma
        - Temporal bone fracture
        - Pre-operative cochlear implant

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

        - Temporal bones: external auditory canal to petrous apex. SUBMILLIMETER <0.625mm. Direct axial and direct coronal if possible. Ultra high resolution
        - Additional Recons: Pöschl and Stenvers oblique reformats for IAC. Measure vestibular aqueduct

    === "Nursing Notes"

        - No IV. Remove hearing aids and earrings

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Ossicles. Cochlea. Semicircular canals. Internal auditory canal. Mastoid air cells. Cholesteatoma. Fracture. Tegmen

    === "Tips & Tricks"

        - Submillimeter critical. Sharp bone kernel. Remove all metal

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | EAC level | Petrous apex | N/A | N/A | Lateral |
    | Axial Temporal | EAC | Petrous apex | N/A | 0.5-0.625 mm | Parallel to lateral SCC |
    | Coronal Temporal | EAC | IAC | N/A | 0.5-0.625 mm | Perpendicular to petrous ridge |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Temporal | Bilateral | 0.5 mm/0.5 mm | Bone sharp | N/A | Ultra HR bone |
    | Coronal | Temporal | Bilateral | 0.5 mm/0.5 mm | Bone sharp | N/A | Coronal bone |
    | Oblique sagittal | Temporal | Ossicles | 0.5 mm | Bone | N/A | Ossicular chain |
    | Pöschl/Stenvers | Temporal | IAC | 0.75 mm | Bone | N/A | IAC oriented views |
