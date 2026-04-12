---
title: CT Complete Spine
slug: ct-complete-spine
category: neuro
protocol_type: spine
last_updated: '2024-01-15'
author: Dr. Chen
synonyms: []
clinical_indications:
- Spine trauma pan-scan
- Multi-level disease
- Metastatic survey
- Infection
position: Supine
npo: None - usually trauma
premedication: ''
contrast:
  agent: None typically. Contrast if infection/mets
  volume: 'If contrast: 125 mL'
  flow_rate: 3 mL/s
tech_params:
  kv: '120'
  mas: Auto (reference 250)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: Complete Spine
  start: Skull base
  end: Sacrum
  delay: N/A or 60s if contrast
  thickness: 0.625-1 mm
  notes: Submillimeter entire spine
recons:
- plane: Axial
  acquisition: Spine
  fov: Full spine
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: '3'
  notes: Axial entire spine
- plane: Sagittal
  acquisition: Spine
  fov: Full spine
  thickness_increment: 2 mm/1.5 mm
  kernel: Bone
  ir_strength: '3'
  notes: Sagittal full spine
- plane: Coronal
  acquisition: Spine
  fov: Full spine
  thickness_increment: 2.5 mm/2 mm
  kernel: Bone
  ir_strength: '3'
  notes: Coronal full spine
notes:
  tech: Skull base to sacrum. LONG COVERAGE. Submillimeter. Sagittal and coronal entire
    spine. May do in segments
  nursing: No IV unless contrast needed. Complete spine coverage
  rad: Entire spine alignment. Fractures all levels. Spinal canal. Paraspinal masses.
    Metastatic disease
  tips: Long coverage. May need multiple acquisitions
  additional_recons: Sagittal and coronal bone reconstructions. Oblique for foramina
safety:
  renal: N/A or verify eGFR
  allergy: N/A or check allergy
---

# CT Complete Spine

**Last Updated:** 2024-01-15  
**Author:** Dr. Chen

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Complete Spine | Contrast (N/A or 60s if contrast delay) | Skull base to Sacrum |

    === "Clinical Indications"

        - Spine trauma pan-scan
        - Multi-level disease
        - Metastatic survey
        - Infection

-   __2. Patient Prep__

    ---

    - **Position:** Supine
    - **NPO Status:** None - usually trauma
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | None typically. Contrast if infection/mets |
        | Volume | If contrast: 125 mL |
        | Flow Rate | 3 mL/s |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Skull base to sacrum. LONG COVERAGE. Submillimeter. Sagittal and coronal entire spine. May do in segments
        - Additional Recons: Sagittal and coronal bone reconstructions. Oblique for foramina

    === "Nursing Notes"

        - No IV unless contrast needed. Complete spine coverage

        !!! warning "Safety First"
            - **Renal Function:** N/A or verify eGFR
            - **Allergy:** N/A or check allergy

    === "Radiologist Notes"

        - Entire spine alignment. Fractures all levels. Spinal canal. Paraspinal masses. Metastatic disease

    === "Tips & Tricks"

        - Long coverage. May need multiple acquisitions

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Skull base | Sacrum | N/A | N/A | Full AP and lateral |
    | Complete Spine | Skull base | Sacrum | N/A or 60s if contrast | 0.625-1 mm | Submillimeter entire spine |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Spine | Full spine | 2 mm/2 mm | Bone | 3 | Axial entire spine |
    | Sagittal | Spine | Full spine | 2 mm/1.5 mm | Bone | 3 | Sagittal full spine |
    | Coronal | Spine | Full spine | 2.5 mm/2 mm | Bone | 3 | Coronal full spine |
