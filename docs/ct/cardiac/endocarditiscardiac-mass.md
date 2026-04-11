---
title: Endocarditis/Cardiac Mass
slug: endocarditiscardiac-mass
category: cardiac
protocol_type: cardiac gated
last_updated: '2026-02-02'
author: ''
synonyms: []
clinical_indications:
- Endocarditis
- Cardiac mass
- Valve vegetation
- Intracardiac thrombus
position: Supine feet-first
npo: NPO 2-4 hours
premedication: HR < 65 preferred. No premedication typically given.
contrast:
  agent: Isovue 370
  volume: 1.6 mL/kg
  flow_rate: 3-4 mL/s
  duration: 35 sec
tech_params:
  kv: 100-120
  mas: Auto ECG modulation
  rotation_time: 0.28s
  pitch: 0.2-0.24
series:
- name: Non-contrast
  start: Top of heart
  end: Below heart
  delay: N/A
  thickness: 3 mm
  notes: Flash Non-contrast
- name: Gated CTA
  start: Top of heart
  end: Below heart
  delay: 30 sec
  thickness: 0.5-0.625 mm
  notes: Retrospective ECG gating
- name: Delayed phase
  start: Lung Apices
  end: Diaphragm
  delay: 70 sec
  thickness: 1 mm
  notes: To detect for abscess, vegetation, masses
recons:
- plane: Axial
  acquisition: Non-contrast
  fov: Heart
  thickness_increment: 3 mm/3 mm
  kernel: Standard
  ir_strength: '3'
  notes: For dense material or calcifications
- plane: Axial
  acquisition: Gated CTA
  fov: Heart
  thickness_increment: 0.75 mm/0.5 mm
  kernel: Cardiac
  ir_strength: '3'
  notes: Reformatted at best cardiac phase
- plane: Axial
  acquisition: Gated CTA
  fov: Heart
  thickness_increment: 1 mm/1 mm
  kernel: Standard
  ir_strength: '3'
  notes: Functional series for valve assessment
- plane: Axial
  acquisition: Delayed
  fov: Chest
  thickness_increment: 1 mm/1 mm
  kernel: Standard
  ir_strength: '3'
  notes: Mass, vegetations
notes:
  tech: Non-valsalva breathing technique, cardiac breathing instruction. | Injection
    duration is fixed 35 sec fixed 30 sec scan delay. Retrospective gating trigger
    at 30-70% (End sys - end dia).  Reconstruct  at 5% intervals.
  nursing: 18-20G IV. HR control helpful but not critical
  rad: Assess all valves for vegetations. Evaluate myocardium for abscess. Look for
    intracardiac masses. Check for complications
  tips: Multiple cardiac phases helpful for valve motion. Thin slices for vegetations
  additional_recons: Multi-phase reconstructions. 4-chamber 2-chamber views. Valve-specific
    reformats
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# Endocarditis/Cardiac Mass

**Last Updated:** 2026-02-02  
**Author:** 

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | Non-contrast | Top of heart to Below heart |
        | Gated CTA | Contrast (30 sec delay) | Top of heart to Below heart |
        | Delayed phase | Contrast (70 sec delay) | Lung Apices to Diaphragm |

    === "Clinical Indications"

        - Endocarditis
        - Cardiac mass
        - Valve vegetation
        - Intracardiac thrombus

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet-first
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:**
        - HR < 65 preferred. No premedication typically given.

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.6 mL/kg |
        | Flow Rate | 3-4 mL/s |
        | Duration | 35 sec |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Non-valsalva breathing technique, cardiac breathing instruction.
        - Injection duration is fixed 35 sec fixed 30 sec scan delay. Retrospective gating trigger at 30-70% (End sys - end dia).  Reconstruct  at 5% intervals.

    === "Nursing Notes"

        - 18-20G IV. HR control helpful but not critical

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Assess all valves for vegetations. Evaluate myocardium for abscess. Look for intracardiac masses. Check for complications

    === "Tips & Tricks"

        - Multiple cardiac phases helpful for valve motion. Thin slices for vegetations

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Top of chest | Diaphragm | N/A | N/A | AP lateral |
    | Non-contrast | Top of heart | Below heart | N/A | 3 mm | Flash Non-contrast |
    | Gated CTA | Top of heart | Below heart | 30 sec | 0.5-0.625 mm | Retrospective ECG gating |
    | Delayed phase | Lung Apices | Diaphragm | 70 sec | 1 mm | To detect for abscess, vegetation, masses |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 100-120 |
    | mAs | Auto ECG modulation |
    | Rotation Time | 0.28s |
    | Pitch | 0.2-0.24 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Non-contrast | Heart | 3 mm/3 mm | Standard | 3 | For dense material or calcifications |
    | Axial | Gated CTA | Heart | 0.75 mm/0.5 mm | Cardiac | 3 | Reformatted at best cardiac phase |
    | Axial | Gated CTA | Heart | 1 mm/1 mm | Standard | 3 | Functional series for valve assessment |
    | Axial | Delayed | Chest | 1 mm/1 mm | Standard | 3 | Mass, vegetations |

### Additional Reconstructions

Multi-phase reconstructions. 4-chamber 2-chamber views. Valve-specific reformats

Category: Cardiac

Protocol Type: Cardiac Gated
