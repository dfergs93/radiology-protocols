---
title: CT IVP (Intravenous Pyelogram)
slug: ct-ivp-intravenous-pyelogram
category: abdomen
protocol_type: contrast-enhanced
last_updated: '2024-01-15'
author: Dr. Anderson
synonyms: []
clinical_indications:
- Hematuria
- Urothelial carcinoma
- Collecting system evaluation
- Hydronephrosis
position: Supine with arms raised
npo: NPO 4 hours
premedication: ''
contrast:
  agent: Isovue 370
  volume: 'Split bolus: 1st injection 1.1 mL/kg + 2nd injection 0.4 mL/kg'
  flow_rate: 4 mL/s
  duration: 18-20s + 5-10s
  timing: Split bolus technique
tech_params:
  kv: 100-120
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: 1.0-1.375
series:
- name: Non-Contrast (optional)
  start: Top kidneys
  end: Pubic symphysis
  delay: N/A
  thickness: 2 mm
  notes: Optional stone detection
- name: Early Portal Venous
  start: Top kidneys
  end: Iliac crests
  delay: 60 sec from 1st
  thickness: 2.5 mm
  notes: Nephrographic phase
- name: Excretory Phase
  start: Top kidneys
  end: Pubic symphysis
  delay: 90-120 sec from 2nd
  thickness: 1.25 mm
  notes: Collecting system opacification
recons:
- plane: Axial
  acquisition: Non-contrast
  fov: KUB
  thickness_increment: 2 mm/2 mm
  kernel: Standard
  ir_strength: '3'
  notes: Stone detection if done
- plane: Axial
  acquisition: Portal venous
  fov: Kidneys
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Renal parenchyma
- plane: Axial
  acquisition: Excretory
  fov: Full urinary tract
  thickness_increment: 2 mm/2 mm
  kernel: Standard
  ir_strength: '3'
  notes: Urothelial surfaces
- plane: Coronal
  acquisition: Excretory
  fov: Full urinary tract
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: MIP urogram
notes:
  tech: 'COMPLEX protocol: 1) NC (optional stone protocol) 2) 1st contrast injection
    3) Early PV 60s after 1st 4) WAIT 5-7 min 5) 2nd injection + saline 6) Excretory/IVP
    90-120s after 2nd'
  nursing: 18-20G IV. Split bolus technique. May give Lasix 10-20mg IV for better
    opacification
  rad: 'NC optional: detect stones. Early PV: renal parenchyma. Excretory: collecting
    system ureters bladder for urothelial lesions'
  tips: Split bolus critical for opacification. Lasix may help. Prone imaging optional
    for ureters
  additional_recons: MIP urogram coronal and sagittal. Curved MPR of ureters. 3D urogram
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# CT IVP (Intravenous Pyelogram)

**Last Updated:** 2024-01-15  
**Author:** Dr. Anderson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast (optional) | Non-contrast | Top kidneys to Pubic symphysis |
        | Early Portal Venous | Contrast (60 sec from 1st injection) | Top kidneys to Iliac crests |
        | Excretory Phase | Contrast (90-120 sec from 2nd injection) | Top kidneys to Pubic symphysis |

    === "Clinical Indications"

        - Hematuria
        - Urothelial carcinoma
        - Collecting system evaluation
        - Hydronephrosis

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | Split bolus: 1st injection 1.1 mL/kg + 2nd injection 0.4 mL/kg |
        | Flow Rate | 4 mL/s |
        | Duration | 18-20s + 5-10s |
        | Timing | Split bolus technique |

    ===   "Lab Requirements"

        Full dose if eGFR > 30. Split bolus for combined nephrographic and excretory phases

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - COMPLEX protocol: 1) NC (optional stone protocol) 2) 1st contrast injection 3) Early PV 60s after 1st 4) WAIT 5-7 min 5) 2nd injection + saline 6) Excretory/IVP 90-120s after 2nd

    === "Nursing Notes"

        - 18-20G IV. Split bolus technique. May give Lasix 10-20mg IV for better opacification

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - NC optional: detect stones. Early PV: renal parenchyma. Excretory: collecting system ureters bladder for urothelial lesions

    === "Tips & Tricks"

        - Split bolus critical for opacification. Lasix may help. Prone imaging optional for ureters

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Top kidneys | Pubic symphysis | N/A | N/A | AP |
    | Non-Contrast (optional) | Top kidneys | Pubic symphysis | N/A | 2 mm | Optional stone detection |
    | Early Portal Venous | Top kidneys | Iliac crests | 60 sec from 1st | 2.5 mm | Nephrographic phase |
    | Excretory Phase | Top kidneys | Pubic symphysis | 90-120 sec from 2nd | 1.25 mm | Collecting system opacification |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.375 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Non-contrast | KUB | 2 mm/2 mm | Standard | 3 | Stone detection if done |
    | Axial | Portal venous | Kidneys | 2.5 mm/2.5 mm | Standard | 3 | Renal parenchyma |
    | Axial | Excretory | Full urinary tract | 2 mm/2 mm | Standard | 3 | Urothelial surfaces |
    | Coronal | Excretory | Full urinary tract | 2.5 mm/2.5 mm | Standard | 3 | MIP urogram |

### Additional Reconstructions

MIP urogram coronal and sagittal. Curved MPR of ureters. 3D urogram

Category: Abdomen

Protocol Type: Contrast-Enhanced
