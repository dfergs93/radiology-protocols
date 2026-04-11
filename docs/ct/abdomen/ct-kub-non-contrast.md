---
title: CT KUB Non-Contrast
slug: ct-kub-non-contrast
category: abdomen
protocol_type: non-contrast
last_updated: '2024-01-15'
author: Dr. Johnson
synonyms: []
clinical_indications:
- Nephrolithiasis
- Renal colic
- Flank pain
- Hematuria
position: Supine with arms raised
npo: None required
premedication: ''
contrast:
  agent: N/A
  type: non-contrast
tech_params:
  kv: 100-120
  mas: Low dose (50-100 ref)
  rotation_time: 0.5s
  pitch: 1.375-1.5
series:
- name: Non-Contrast KUB
  start: Top of kidneys
  end: Pubic symphysis
  delay: N/A
  thickness: 1-2 mm
  notes: Low dose technique
recons:
- plane: Axial
  acquisition: Non-contrast
  fov: KUB
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: Stone detection
- plane: Axial
  acquisition: Non-contrast
  fov: KUB
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Bone
  ir_strength: N/A
  notes: Bone window for stones
- plane: Coronal
  acquisition: Non-contrast
  fov: KUB
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Coronal stone overview
- plane: MIP
  acquisition: Non-contrast
  fov: Kidneys/ureters
  thickness_increment: 5 mm slab
  kernel: Standard
  ir_strength: N/A
  notes: Stone localization
notes:
  tech: LOW DOSE protocol. Reduced mAs. Cover kidneys to pubic symphysis. Stone protocol
    settings
  nursing: No IV needed. No oral contrast. Explain low radiation technique
  rad: Look for stones - measure size and location. Check for hydronephrosis. Assess
    for alternative diagnoses
  tips: Low dose protocol. Reduced mAs. Image quality adequate for stones
  additional_recons: Thin slice 1mm for small stones. Stone size measurements
safety:
  renal: N/A
  allergy: N/A
---

# CT KUB Non-Contrast

**Last Updated:** 2024-01-15  
**Author:** Dr. Johnson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-Contrast KUB | Non-contrast | Top of kidneys to Pubic symphysis |

    === "Clinical Indications"

        - Nephrolithiasis
        - Renal colic
        - Flank pain
        - Hematuria

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** None required
    

-   __3. IV Contrast & Injection__    

    ---
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - LOW DOSE protocol. Reduced mAs. Cover kidneys to pubic symphysis. Stone protocol settings
        - Additional Recons: Thin slice 1mm for small stones. Stone size measurements

    === "Nursing Notes"

        - No IV needed. No oral contrast. Explain low radiation technique

        !!! warning "Safety First"
            - **Renal Function:** N/A
            - **Allergy:** N/A

    === "Radiologist Notes"

        - Look for stones - measure size and location. Check for hydronephrosis. Assess for alternative diagnoses

    === "Tips & Tricks"

        - Low dose protocol. Reduced mAs. Image quality adequate for stones

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Top of kidneys | Pubic symphysis | N/A | N/A | AP scout |
    | Non-Contrast KUB | Top of kidneys | Pubic symphysis | N/A | 1-2 mm | Low dose technique |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Low dose (50-100 ref) |
    | Rotation Time | 0.5s |
    | Pitch | 1.375-1.5 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Non-contrast | KUB | 2.5 mm/2.5 mm | Standard | 3 | Stone detection |
    | Axial | Non-contrast | KUB | 2.5 mm/2.5 mm | Bone | N/A | Bone window for stones |
    | Coronal | Non-contrast | KUB | 3 mm/3 mm | Standard | 3 | Coronal stone overview |
    | MIP | Non-contrast | Kidneys/ureters | 5 mm slab | Standard | N/A | Stone localization |
