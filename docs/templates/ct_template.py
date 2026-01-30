"""
Template for protocol markdown generation
This is a copy of protocol_template.py in the main codebase for documentation generation purposes.
Copy made on Jan 30 2026.
"""

PROTOCOL_TEMPLATE = """# {protocol_name}

**Last Updated:** {last_updated}  
**Author:** {author}

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

{acquisition_summary_table}

    === "Clinical Indications"

{clinical_indications_formatted}

-   __2. Patient Prep__

    ---
    
    !!! warning "Safety First"
        - **Renal Function:** {safety_renal_function}
        - **Allergy:** {safety_allergy_check}
    
    - **Position:** {patient_positioning}
    - **NPO Status:** {npo_status}
    {premedication_section}

-   __3. IV Contrast & Injection__    

    ---
    {contrast_section}

-   __4. Special Notes__

    ---

    === "Technologist Notes"

    {tech_notes_formatted}

    === "Nursing Notes"

    {nursing_notes_formatted}

    === "Radiologist Notes"
    {radiologist_notes_formatted}

    === "Tips & Tricks"

    {artifact_tip_formatted}

</div>


### Protocol Details
  ```mermaid
    gantt
      title {protocol_name} Timeline
      dateFormat mm:ss
      axisFormat %M:%S 
      {gantt_content}
  ```


=== "Series Acquisition"

{series_table}

=== "Technical Parameters"

    | Parameter | Value |
    |-----------|-------|
    | kV | {kv} |
    | mAs | {mas} |
    | Rotation Time | {rotation_time}s |
    | Pitch | {pitch} |

=== "Post-Processing"

{postproc_table}

{additional_recons_section}
Category: {category}

Protocol Type: {protocol_type}
"""
