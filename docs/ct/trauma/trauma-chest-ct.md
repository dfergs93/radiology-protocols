---
title: Trauma Chest CT
slug: trauma-chest-ct
category: trauma
protocol_type: trauma
last_updated: '2024-01-15'
author: Dr. Martinez
synonyms: []
clinical_indications:
- Blunt chest trauma
- Rib fractures
- Pneumothorax
- Hemothorax
position: Supine with arms raised if possible
npo: None - trauma
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: '120'
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: 1.0-1.2
series:
- name: NC Chest
  start: Lung apices
  end: Costophrenic angles
  delay: N/A
  thickness: 0.625-1 mm
  notes: Submillimeter for ribs
- name: CTA Chest
  start: Arterial (bolus tracked)
  end: Lung apices to Costophrenic angles
  delay: Bolus tracked
  thickness: 0.625 mm
  notes: Evaluate for aortic injury
recons:
- plane: Axial
  acquisition: Chest
  fov: Chest
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Mediastinal window
- plane: Axial
  acquisition: Chest
  fov: Chest
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Lung
  ir_strength: '3'
  notes: Lung window
- plane: Axial
  acquisition: CTA Chest
  fov: Chest
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Evaluate for aortic injury
- plane: Coronal
  acquisition: Chest
  fov: Chest
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Bone
  ir_strength: N/A
  notes: Rib overview
- plane: Oblique sagittal
  acquisition: Chest
  fov: Ribs
  thickness_increment: 2 mm/2 mm
  kernel: Bone
  ir_strength: N/A
  notes: Rib reformats all ribs
notes:
  tech: Single acquisition lung apices to costophrenic angles. RIB REFORMATS required.
    Submillimeter acquisition
  nursing: Trauma precautions. Arms up if able
  rad: Pneumothorax hemothorax. Rib fractures (count and location). Pulmonary contusion.
    Aortic injury. Sternal/scapular fractures
  tips: Submillimeter acquisition critical for rib detail
  additional_recons: Dedicated rib reformats (oblique sagittal each rib). Count fractures.
    3D chest wall
safety:
  renal: N/A
  allergy: N/A
---

# Trauma Chest CT

**Last Updated:** 2024-01-15  
**Author:** Dr. Martinez

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | NC Chest | Non-contrast | Lung apices to Costophrenic angles |
        | CTA Chest | Arterial (bolus tracked) | Lung apices to Costophrenic angles |

    === "Clinical Indications"

        - Blunt chest trauma
        - Rib fractures
        - Pneumothorax
        - Hemothorax

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised if possible
    - **NPO Status:** None - trauma
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Single acquisition lung apices to costophrenic angles. RIB REFORMATS required. Submillimeter acquisition
        - Additional Recons: Dedicated rib reformats (oblique sagittal each rib). Count fractures. 3D chest wall

    === "Nursing Notes"

        - Trauma precautions. Arms up if able

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Pneumothorax hemothorax. Rib fractures (count and location). Pulmonary contusion. Aortic injury. Sternal/scapular fractures

    === "Tips & Tricks"

        - Submillimeter acquisition critical for rib detail

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Lung apices | Costophrenic angles | N/A | N/A | AP and lateral |
    | NC Chest | Lung apices | Costophrenic angles | N/A | 0.625-1 mm | Submillimeter for ribs |
    | CTA Chest | Arterial (bolus tracked) | Lung apices to Costophrenic angles | Bolus tracked | 0.625 mm | Evaluate for aortic injury |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Chest | Chest | 2.5 mm/2.5 mm | Standard | 3 | Mediastinal window |
    | Axial | Chest | Chest | 2.5 mm/2.5 mm | Lung | 3 | Lung window |
    | Axial | CTA Chest | Chest | 2.5 mm/2.5 mm | Standard | 3 | Evaluate for aortic injury |
    | Coronal | Chest | Chest | 2.5 mm/2.5 mm | Bone | N/A | Rib overview |
    | Oblique sagittal | Chest | Ribs | 2 mm/2 mm | Bone | N/A | Rib reformats all ribs |
