---
title: CT Orbits
slug: ct-orbits
category: neuro
protocol_type: contrast-enhanced
last_updated: '2024-01-15'
author: Dr. Davis
synonyms: []
clinical_indications:
- Orbital mass
- Thyroid eye disease
- Orbital cellulitis
- Optic nerve assessment
- Trauma
position: Supine head-first
npo: NPO 2 hours if contrast
premedication: ''
contrast:
  agent: Omnipaque 350 if contrast
  volume: 75-100 mL if contrast
  flow_rate: 3 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 200-250)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: Axial Orbits
  start: Superior orbital rim
  end: Maxillary sinus
  delay: N/A or 60s if contrast
  thickness: 1-1.5 mm
  notes: Parallel to optic nerves
recons:
- plane: Axial
  acquisition: Orbits
  fov: Orbits
  thickness_increment: 1.5 mm/1 mm
  kernel: Bone and Standard
  ir_strength: '3'
  notes: Bone for fractures soft tissue for pathology
- plane: Coronal
  acquisition: Orbits
  fov: Orbits
  thickness_increment: 1.5 mm/1 mm
  kernel: Bone and Standard
  ir_strength: '3'
  notes: Coronal orbits
- plane: Sagittal
  acquisition: Orbits
  fov: Optic nerve
  thickness_increment: 2 mm/1.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Optic nerve canal
- plane: 3D if trauma
  acquisition: Orbits
  fov: Orbital bones
  thickness_increment: 1 mm source
  kernel: Bone
  ir_strength: N/A
  notes: 3D if complex fracture
notes:
  tech: 'Orbits: superior orbital rim to maxillary sinus. Axial 1-2mm. Coronal reformats.
    NC for trauma. Contrast for masses/inflammation'
  nursing: Contrast for mass or inflammation. NC for trauma and metallic foreign body
  rad: Extraocular muscles. Optic nerve. Globe integrity. Orbital fat. Preseptal vs
    postseptal. Masses. Foreign body
  tips: Angle axial parallel to optic nerves. Thin slices
  additional_recons: Assess optic nerve canal. Measure EOMs if thyroid eye disease.
    Document foreign body
safety:
  renal: N/A or verify eGFR > 30
  allergy: N/A or check allergy
---

# CT Orbits

**Last Updated:** 2024-01-15  
**Author:** Dr. Davis

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Axial Orbits | Contrast (N/A or 60s if contrast delay) | Superior orbital rim to Maxillary sinus |

    === "Clinical Indications"

        - Orbital mass
        - Thyroid eye disease
        - Orbital cellulitis
        - Optic nerve assessment
        - Trauma

-   __2. Patient Prep__

    ---

    - **Position:** Supine head-first
    - **NPO Status:** NPO 2 hours if contrast
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 if contrast |
        | Volume | 75-100 mL if contrast |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Orbits: superior orbital rim to maxillary sinus. Axial 1-2mm. Coronal reformats. NC for trauma. Contrast for masses/inflammation
        - Additional Recons: Assess optic nerve canal. Measure EOMs if thyroid eye disease. Document foreign body

    === "Nursing Notes"

        - Contrast for mass or inflammation. NC for trauma and metallic foreign body

        !!! warning "Safety First"
            - **Renal Function:** N/A or verify eGFR > 30
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Extraocular muscles. Optic nerve. Globe integrity. Orbital fat. Preseptal vs postseptal. Masses. Foreign body

    === "Tips & Tricks"

        - Angle axial parallel to optic nerves. Thin slices

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Superior orbital rim | Maxillary sinus | N/A | N/A | Lateral |
    | Axial Orbits | Superior orbital rim | Maxillary sinus | N/A or 60s if contrast | 1-1.5 mm | Parallel to optic nerves |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Orbits | Orbits | 1.5 mm/1 mm | Bone and Standard | 3 | Bone for fractures soft tissue for pathology |
    | Coronal | Orbits | Orbits | 1.5 mm/1 mm | Bone and Standard | 3 | Coronal orbits |
    | Sagittal | Orbits | Optic nerve | 2 mm/1.5 mm | Standard | 3 | Optic nerve canal |
    | 3D if trauma | Orbits | Orbital bones | 1 mm source | Bone | N/A | 3D if complex fracture |
