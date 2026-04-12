---
title: CT Biphasic Pancreas
slug: ct-biphasic-pancreas
category: abdomen
protocol_type: contrast-enhanced
last_updated: '2024-01-15'
author: Dr. Williams
synonyms: []
clinical_indications:
- Pancreatic mass
- Pancreatitis
- Pancreatic cyst characterization
position: Supine with arms raised
npo: NPO 4 hours
premedication: 'Water PO: 900 mL water orally 15-30 min before scan for gastric/duodenal
  distension'
contrast:
  agent: Isovue 370
  volume: 1.5 mL/kg
  flow_rate: 4-5 mL/s
  duration: 25s
  timing: 'Dual phase: Pancreatic arterial + Portal venous'
  roi: Abdominal aorta
  trigger: 150 HU
tech_params:
  kv: '100'
  mas: Auto (reference 200-250)
  rotation_time: 0.5s
  pitch: 0.9-1.0
series:
- name: Pancreatic Phase
  start: Diaphragm
  end: Iliac crests
  delay: 40-45 sec or bolus track
  thickness: 1-1.25 mm
  notes: Thin slices for small lesions
- name: Portal Venous
  start: Diaphragm
  end: Lesser Trochanter
  delay: 70 sec
  thickness: 2.5 mm
  notes: Standard PV phase
recons:
- plane: Axial
  acquisition: Pancreatic
  fov: Pancreas
  thickness_increment: 1.5 mm/1.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Thin slice pancreas
- plane: Axial
  acquisition: Portal venous
  fov: Abdomen
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Liver and vessels
- plane: Coronal
  acquisition: Both phases
  fov: Abdomen
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Pancreatic and peripancreatic
- plane: Curved MPR
  acquisition: Pancreatic
  fov: Pancreatic duct
  thickness_increment: 1.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Duct evaluation
notes:
  tech: 'TWO phases: Pancreatic phase (40-45s or bolus track) + Portal venous (70s).
    Water for negative contrast'
  nursing: 18-20G IV. Ensure water intake for duodenal distension
  rad: 'Pancreatic phase: optimal pancreatic enhancement and small lesions. Portal
    venous: liver and venous structures'
  tips: Water distension of duodenum helpful. Thin slices for pancreas
  additional_recons: Curved MPR pancreatic duct. MIP pancreatic vasculature
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history. Coordinate water intake
---

# CT Biphasic Pancreas

**Last Updated:** 2024-01-15  
**Author:** Dr. Williams

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Pancreatic Phase | Delayed Arterial (bolus tracked+16s scan delay) | Diaphragm to Iliac crests |
        | Portal Venous | Contrast (70 sec delay) | Diaphragm to Lesser trochanters |

    === "Clinical Indications"

        - Pancreatic mass
        - Pancreatitis
        - Pancreatic cyst characterization

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    - **Pre-Medication:**
        - Water PO: 900 mL water orally 15-30 min before scan for gastric/duodenal distension

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.5 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Duration | 25s |
        | Timing Method | Dual phase: Pancreatic arterial + Portal venous |
        | ROI Placement | Abdominal aorta |
        | Trigger (HU) | 150 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - TWO phases: Pancreatic phase (40-45s or bolus track) + Portal venous (70s). Water for negative contrast
        - Additional Recons: Curved MPR pancreatic duct. MIP pancreatic vasculature

    === "Nursing Notes"

        - 18-20G IV. Ensure water intake for duodenal distension

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history. Coordinate water intake

    === "Radiologist Notes"

        - Pancreatic phase: optimal pancreatic enhancement and small lesions. Portal venous: liver and venous structures

    === "Tips & Tricks"

        - Water distension of duodenum helpful. Thin slices for pancreas

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Diaphragm | Iliac crests | N/A | N/A | AP |
    | Pancreatic Phase | Diaphragm | Iliac crests | 40-45 sec or bolus track | 1-1.25 mm | Thin slices for small lesions |
    | Portal Venous | Diaphragm | Lesser Trochanter | 70 sec | 2.5 mm | Standard PV phase |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Pancreatic | Pancreas | 1.5 mm/1.5 mm | Standard | 3 | Thin slice pancreas |
    | Axial | Portal venous | Abdomen | 2.5 mm/2.5 mm | Standard | 3 | Liver and vessels |
    | Coronal | Both phases | Abdomen | 2.5 mm/2.5 mm | Standard | 3 | Pancreatic and peripancreatic |
    | Curved MPR | Pancreatic | Pancreatic duct | 1.5 mm | Standard | 3 | Duct evaluation |
