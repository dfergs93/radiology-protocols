---
title: Gated CTA Chest Post-op Cardiac Valve
slug: gated-cta-chest-post-op-cardiac-valve
category: cardiac
protocol_type: cardiac gated
last_updated: '2024-01-15'
author: Dr. Thompson
synonyms: []
clinical_indications:
- Post-operative valve assessment
- Prosthetic valve evaluation
- Post-surgical complications
position: Supine feet-first
npo: NPO 2-4 hours
premedication: HR < 65 preferred. Metoprolol if needed
contrast:
  agent: Isovue 370
  volume: 1.3 mL/kg
  flow_rate: 4-5 mL/s
  duration: 15 sec
  timing: Bolus Tracking
  roi: Ascending aorta
  trigger: 200 HU
tech_params:
  kv: 130-140
  mas: Auto ECG modulation
  rotation_time: 0.28s
  pitch: 0.2-0.24
series:
- name: Gated CTA
  start: Top of heart
  end: Below heart
  delay: Bolus tracked
  thickness: 0.5-0.625 mm
  notes: Retrospective gating HIGH kV
recons:
- plane: Axial
  acquisition: Gated CTA
  fov: Heart
  thickness_increment: 0.75 mm/0.75 mm
  kernel: Cardiac
  ir_strength: '3'
  notes: Prosthetic valve assessment
- plane: Axial
  acquisition: Gated CTA
  fov: Heart
  thickness_increment: Multi-phase
  kernel: Cardiac
  ir_strength: '3'
  notes: Multiple cardiac phases for motion
- plane: Short axis
  acquisition: Gated CTA
  fov: Valve level
  thickness_increment: 1 mm
  kernel: Cardiac
  ir_strength: '3'
  notes: En face valve views
- plane: Long axis
  acquisition: Gated CTA
  fov: Heart
  thickness_increment: Multi-phase
  kernel: Cardiac
  ir_strength: '3'
  notes: Valve motion assessment
notes:
  tech: Retrospective gating. INCREASED kV to 130-140 for metal artifact reduction.
    Increased contrast 1.3 mL/kg. Extended reconstruction phases
  nursing: 20G IV minimum
  rad: Assess prosthetic valve function. Look for paravalvular leak. Evaluate perivalvular
    complications. Metal artifact reduction critical | Increased kVP and increased
    contrast volume with thinner cuts help with seeing through metallic artifact to
    evaluate for thrombus.
  tips: High kV (130-140) critical for metal artifact. Increased contrast volume
  additional_recons: Multi-phase reconstructions. Valve-specific views. Paravalvular
    assessment
safety:
  renal: Verify eGFR > 30
  allergy: Check allergy history
---

# Gated CTA Chest Post-op Cardiac Valve

**Last Updated:** 2024-01-15  
**Author:** Dr. Thompson

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Non-contrast | Non-contrast | Lung Apices to Diaphragm |
        | Gated CTA | Arterial (bolus tracked) | Top of heart to Below heart |

    === "Clinical Indications"

        - Post-operative valve assessment
        - Prosthetic valve evaluation
        - Post-surgical complications

-   __2. Patient Prep__

    ---

    - **Position:** Supine feet-first
    - **NPO Status:** NPO 2-4 hours
    - **Pre-Medication:**
        - HR < 65 preferred. Metoprolol if needed

-   __3. IV Contrast & Injection__    

    ---
    
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volume | 1.3 mL/kg |
        | Flow Rate | 4-5 mL/s |
        | Duration | 15 sec |
        | Timing Method | Bolus Tracking |
        | ROI Placement | Ascending aorta |
        | Trigger (HU) | 200 HU |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \(2*\left[\frac{\text{Patient Weight}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - Retrospective gating. INCREASED kV to 130-140 for metal artifact reduction. Increased contrast 1.3 mL/kg. Extended reconstruction phases

    === "Nursing Notes"

        - 20G IV minimum

        !!! warning "Safety First"
            - **Renal Function:** Verify eGFR > 30
            - **Allergy:** Check allergy history

    === "Radiologist Notes"

        - Assess prosthetic valve function. Look for paravalvular leak. Evaluate perivalvular complications. Metal artifact reduction critical
        - Increased kVP and increased contrast volume with thinner cuts help with seeing through metallic artifact to evaluate for thrombus.

    === "Tips & Tricks"

        - High kV (130-140) critical for metal artifact. Increased contrast volume

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scout | Top of chest | Diaphragm | N/A | N/A | AP lateral |
    | Gated CTA | Top of heart | Below heart | Bolus tracked | 0.5-0.625 mm | Retrospective gating HIGH kV |

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | 130-140 |
    | mAs | Auto ECG modulation |
    | Rotation Time | 0.28s |
    | Pitch | 0.2-0.24 |

=== "Post-Processing"

    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Gated CTA | Heart | 0.75 mm/0.75 mm | Cardiac | 3 | Prosthetic valve assessment |
    | Axial | Gated CTA | Heart | Multi-phase | Cardiac | 3 | Multiple cardiac phases for motion |
    | Short axis | Gated CTA | Valve level | 1 mm | Cardiac | 3 | En face valve views |
    | Long axis | Gated CTA | Heart | Multi-phase | Cardiac | 3 | Valve motion assessment |

### Additional Reconstructions

Multi-phase reconstructions. Valve-specific views. Paravalvular assessment

Category: Cardiac

Protocol Type: Cardiac Gated
