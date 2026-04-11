---
title: CTV Chest Abdomen Pelvis
slug: ctv-chest-abdomen-pelvis
category: vascular
protocol_type: vascular
last_updated: '2024-01-15'
author: Dr. White
synonyms: []
clinical_indications:
- Superior vena cava syndrome
- Central venous occlusion
- Tumor staging with venous involvement
position: Supine with arms raised
npo: NPO 2-4 hours
premedication: ''
contrast:
  agent: Isovue 370
  volume: 2.0 mL/kg
  flow_rate: 3 mL/s
  duration: 40s
  timing: Fixed Delay (180s)
tech_params:
  kv: '120'
  mas: Auto (reference 200)
  rotation_time: 0.5s
  pitch: 1.0-1.2
series:
- name: CTV Venous Phase
  start: Thoracic inlet
  end: Proximal femur
  delay: 180 sec
  thickness: 0.625 mm
  notes: Extended venous phase
recons:
- plane: Axial
  acquisition: Venous
  fov: Chest
  thickness_increment: 2 mm/2 mm
  kernel: Standard
  ir_strength: '3'
  notes: SVC and central veins
- plane: Axial
  acquisition: Venous
  fov: Abdomen/Pelvis
  thickness_increment: 2.5 mm/2.5 mm
  kernel: Standard
  ir_strength: '3'
  notes: IVC and tributaries
- plane: Coronal
  acquisition: Venous
  fov: Full CAP
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: MIP full venous system
- plane: Sagittal
  acquisition: Venous
  fov: Full CAP
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: Sagittal venogram
notes:
  tech: Scan at 180 seconds. Include SVC through femoral veins. May need arm injection
    for SVC assessment
  nursing: 18-20G IV - may need bilateral arm IVs for SVC
  rad: Assess SVC IVC and major tributaries. Look for thrombosis compression or tumor
    invasion
  tips: Arms raised. For SVC consider bilateral arm injection
  additional_recons: 3D venogram MIP. Curved MPR of SVC and IVC
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history. May need bilateral IVs
---

# CTV Chest Abdomen Pelvis

**Last Updated:** 2024-01-15  
**Author:** Dr. White

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | CTV Venous Phase | Contrast (110 sec delay) | Thoracic inlet to Proximal femur |

    === "Clinical Indications"

        - Superior vena cava syndrome
        - Central venous occlusion
        - Tumor staging with venous involvement

-   __2. Patient Prep__

    ---

    - **Position:** Supine with arms raised
    - **NPO Status:** NPO 2-4 hours
    

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 2.0 mL/kg |
        | Flow Rate | 3 mL/s |
        | Duration | 40s |
        | Timing Method | Fixed Delay (180s) |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Scan at 180 seconds. Include SVC through femoral veins. May need arm injection for SVC assessment

    === "Nursing Notes"

        - 18-20G IV - may need bilateral arm IVs for SVC

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history. May need bilateral IVs

    === "Radiologist Notes"

        - Assess SVC IVC and major tributaries. Look for thrombosis compression or tumor invasion

    === "Tips & Tricks"

        - Arms raised. For SVC consider bilateral arm injection

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout/Topogram | Thoracic inlet | Proximal femur | N/A | N/A | AP full body |
    | CTV Venous Phase | Thoracic inlet | Proximal femur | 180 sec | 0.625 mm | Extended venous phase |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 120 |
    | mAs | Auto (reference 200) |
    | Rotation Time | 0.5s |
    | Pitch | 1.0-1.2 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Venous | Chest | 2 mm/2 mm | Standard | 3 | SVC and central veins |
    | Axial | Venous | Abdomen/Pelvis | 2.5 mm/2.5 mm | Standard | 3 | IVC and tributaries |
    | Coronal | Venous | Full CAP | 3 mm/3 mm | Standard | 3 | MIP full venous system |
    | Sagittal | Venous | Full CAP | 3 mm/3 mm | Standard | 3 | Sagittal venogram |

### Additional Reconstructions

3D venogram MIP. Curved MPR of SVC and IVC

Category: Vascular

Protocol Type: Vascular
