---
title: Trauma Code AAA
slug: trauma-code-aaa
category: trauma
protocol_type: trauma
last_updated: '2024-01-15'
author: Dr. Davis
synonyms: []
clinical_indications:
- Ruptured AAA
- Aortic emergency
- Hemodynamic instability with abdominal pain
position: Supine with arms raised
npo: None - emergency
premedication: ''
contrast:
  agent: Omnipaque 350
  volume: 125 mL
  flow_rate: 4-5 mL/s
  timing: 'Triple phase: NC + Arterial + Portal venous'
  roi: Abdominal aorta
  trigger: 150 HU
tech_params:
  kv: 100-120
  mas: High mAs (300 reference)
  rotation_time: 0.5s
  pitch: 1.0-1.375
series:
- name: Non-Contrast CAP
  start: Diaphragm
  end: Pubic symphysis
  delay: N/A
  thickness: 2.5 mm
  notes: RAPID - hematoma
- name: Arterial CAP
  start: Diaphragm
  end: Pubic symphysis
  delay: 25-30 sec
  thickness: 0.625 mm
  notes: Active bleeding + aneurysm
- name: Portal Venous CAP
  start: Diaphragm
  end: Pubic symphysis
  delay: 70 sec
  thickness: 2.5 mm
  notes: Organs and venous
recons:
- plane: Axial
  acquisition: All phases
  fov: CAP
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Vascular/Standard
  ir_strength: '3'
  notes: Compare phases
- plane: Coronal
  acquisition: Arterial
  fov: CAP
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Aorta and bleeding
- plane: Sagittal
  acquisition: Arterial
  fov: Aorta
  thickness_increment: 2 mm/2 mm
  kernel: Vascular
  ir_strength: '3'
  notes: Aorta extent
- plane: 3D VR
  acquisition: Arterial
  fov: Aorta
  thickness_increment: 1.5 mm
  kernel: Vascular
  ir_strength: '3'
  notes: STAT 3D for EVAR planning
notes:
  tech: 'RAPID triple phase: 1) NC CAP (hematoma) 2) Arterial CAP (active bleed bolus
    track 25-30s) 3) Portal venous CAP (70s). STAT protocol'
  nursing: Large bore IV 18G minimum. Blood products ready
  rad: 'NC: retroperitoneal hematoma. Arterial: active extravasation aneurysm morphology.
    Portal: solid organs'
  tips: STAT protocol. Minimize delays. Notify vascular surgery
  additional_recons: Measure aneurysm. Identify bleeding site. EVAR measurements if
    stable
safety:
  renal: Emergent - proceed
  allergy: Document emergency
---

# Trauma Code AAA

**Last Updated:** 2024-01-15  
**Author:** Dr. Davis

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast CAP | Non-contrast | Diaphragm to Pubic symphysis |
        | Arterial CAP | Contrast (25-30 sec delay) | Diaphragm to Pubic symphysis |
        | Portal Venous CAP | Contrast (70 sec delay) | Diaphragm to Pubic symphysis |

    === "Clinical Indications"

        - Ruptured AAA
        - Aortic emergency
        - Hemodynamic instability with abdominal pain

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** None - emergency
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volume | 125 mL |
        | Flow Rate | 4-5 mL/s |
        | Timing Method | Triple phase: NC + Arterial + Portal venous |
        | ROI Placement | Abdominal aorta |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - RAPID triple phase: 1) NC CAP (hematoma) 2) Arterial CAP (active bleed bolus track 25-30s) 3) Portal venous CAP (70s). STAT protocol

    === "Nursing Notes"

        - Large bore IV 18G minimum. Blood products ready

        !!! warning "Safety First"
            - **Renal Function:** Emergent - proceed
            - **Allergy:** Document emergency

    === "Radiologist Notes"

        - NC: retroperitoneal hematoma. Arterial: active extravasation aneurysm morphology. Portal: solid organs

    === "Tips & Tricks"

        - STAT protocol. Minimize delays. Notify vascular surgery

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Pubic symphysis | N/A | N/A | STAT |
    | Non-Contrast CAP | Diaphragm | Pubic symphysis | N/A | 2.5 mm | RAPID - hematoma |
    | Arterial CAP | Diaphragm | Pubic symphysis | 25-30 sec | 0.625 mm | Active bleeding + aneurysm |
    | Portal Venous CAP | Diaphragm | Pubic symphysis | 70 sec | 2.5 mm | Organs and venous |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | High mAs (300 reference) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.375 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | All phases | CAP | 2.5 mm/2.5 mm | Vascular/Standard | 3 | Compare phases |
    | Coronal | Arterial | CAP | 2.5 mm/2.5 mm | Vascular | 3 | Aorta and bleeding |
    | Sagittal | Arterial | Aorta | 2 mm/2 mm | Vascular | 3 | Aorta extent |
    | 3D VR | Arterial | Aorta | 1.5 mm | Vascular | 3 | STAT 3D for EVAR planning |

### Additional Reconstructions

Measure aneurysm. Identify bleeding site. EVAR measurements if stable

Category: Trauma

Protocol Type: Trauma
