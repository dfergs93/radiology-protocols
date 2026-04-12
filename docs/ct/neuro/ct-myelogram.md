---
title: CT Myelogram
slug: ct-myelogram
category: neuro
protocol_type: spine
last_updated: '2024-01-15'
author: Dr. Martinez
synonyms: []
clinical_indications:
- Post-myelogram CT
- Intrathecal contrast follow-up
- Spinal stenosis
- Nerve root compression
position: Supine. Post-lumbar puncture
npo: N/A
premedication: Intrathecal contrast already given
contrast:
  agent: Omnipaque 240 intrathecal
  volume: 10-15 mL IT
  flow_rate: N/A
tech_params:
  kv: '120'
  mas: Auto (reference 250)
  rotation_time: 0.5s
  pitch: Helical
series:
- name: CT Myelogram
  start: Region of interest
  end: Extended coverage
  delay: N/A
  thickness: 0.625 mm
  notes: Submillimeter for detail
recons:
- plane: Axial
  acquisition: Myelogram
  fov: Spine
  thickness_increment: 1 mm/1 mm
  kernel: Bone and Standard
  ir_strength: '3'
  notes: Nerve roots and thecal sac
- plane: Sagittal
  acquisition: Myelogram
  fov: Spine
  thickness_increment: 1.5 mm/1 mm
  kernel: Standard
  ir_strength: '3'
  notes: Thecal sac and compression
- plane: Coronal
  acquisition: Myelogram
  fov: Spine
  thickness_increment: 2 mm/1.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Coronal nerve roots
- plane: Oblique sagittal
  acquisition: Myelogram
  fov: Neural foramina
  thickness_increment: 1.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Foraminal nerve roots
notes:
  tech: Post-LP CT. Usually lumbar region. Thin slices. Axial and sagittal reformats.
    Assess nerve root sleeves and thecal sac
  nursing: Patient already had LP with IT contrast. Position comfortably
  rad: Nerve root sleeves. Thecal sac compression. Spinal stenosis. Disc herniations.
    Surgical planning detail
  tips: Post-LP headache precautions. Thin slices for nerve detail
  additional_recons: Oblique reformats for nerve roots. Document stenosis level and
    severity
safety:
  renal: N/A
  allergy: N/A
---

# CT Myelogram

**Last Updated:** 2024-01-15  
**Author:** Dr. Martinez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CT Myelogram | Non-contrast | Region of interest to Extended coverage |

    === "Clinical Indications"

        - Post-myelogram CT
        - Intrathecal contrast follow-up
        - Spinal stenosis
        - Nerve root compression

-   __2. Patient Prep__

    ---

    - **Position:** Supine. Post-lumbar puncture
    - **NPO Status:** N/A
    - **Pre-Medication:**
        - Intrathecal contrast already given

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 240 intrathecal |
        | Volume | 10-15 mL IT |
        | Flow Rate | N/A |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Post-LP CT. Usually lumbar region. Thin slices. Axial and sagittal reformats. Assess nerve root sleeves and thecal sac
        - Additional Recons: Oblique reformats for nerve roots. Document stenosis level and severity

    === "Nursing Notes"

        - Patient already had LP with IT contrast. Position comfortably

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Nerve root sleeves. Thecal sac compression. Spinal stenosis. Disc herniations. Surgical planning detail

    === "Tips & Tricks"

        - Post-LP headache precautions. Thin slices for nerve detail

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Coverage area | Based on region | N/A | N/A | AP and lateral |
    | CT Myelogram | Region of interest | Extended coverage | N/A | 0.625 mm | Submillimeter for detail |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Myelogram | Spine | 1 mm/1 mm | Bone and Standard | 3 | Nerve roots and thecal sac |
    | Sagittal | Myelogram | Spine | 1.5 mm/1 mm | Standard | 3 | Thecal sac and compression |
    | Coronal | Myelogram | Spine | 2 mm/1.5 mm | Standard | 3 | Coronal nerve roots |
    | Oblique sagittal | Myelogram | Neural foramina | 1.5 mm | Standard | 3 | Foraminal nerve roots |
