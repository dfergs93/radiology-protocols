"""
Formatting functions for protocol generation
"""
import re

def clean_value(value):
    """Clean and format CSV values"""
    if not value or value.lower() in ['n/a', 'none', '']:
        return 'N/A'
    return value.strip()

def clean_gantt_time_value(value):
    """Clean and format time values for Gantt charts so that all are in mm:ss format"""
    colon_pos = value.find(':')
    if not value or colon_pos == -1 or value.lower() in ['n/a', 'none', '']:
        return '00:36'  # Default duration
    value = value.strip().lower()
    mm = '00'
    ss = '00'
    mm = value[:colon_pos].zfill(2)
    ss = value[colon_pos + 1:].zfill(2)
    return f"{mm}:{ss}" 

def create_gantt_from_series(row, indent_level=6):
    """Generate Gantt chart from series acquisition data
    
    Args:
        row: CSV row data
        indent_level: Number of spaces to indent each Gantt line
    """
    gantt_lines = []
    
    # Extract contrast info if present
    contrast_agent = clean_value(row.get('contrast_agent'))
    has_contrast = contrast_agent not in ['N/A', 'None', '']
    volume = clean_value(row.get('contrast_volume'))
    
    if has_contrast:
        flow_rate = clean_value(row.get('contrast_flow_rate'))
        
        # Special handling for split bolus
        if 'split bolus' in volume.lower():
            # Parse the two injection volumes
            first_vol, second_vol = parse_split_bolus_volumes(volume)
            rate_ml_s = parse_flow_rate(flow_rate)
            
            if rate_ml_s:
                # First injection timing
                first_duration = int(first_vol / rate_ml_s)
                first_saline_duration = int(50 / rate_ml_s)
                
                # Second injection timing (comes after wait)
                second_duration = int(second_vol / rate_ml_s)
                second_saline_duration = int(50 / rate_ml_s)
                
                # Calculate wait time between injections
                # For renal mass/IVP: typically 5-7 minutes
                wait_time_seconds = calculate_split_bolus_wait(row)
                wait_minutes = wait_time_seconds // 60
                wait_seconds = wait_time_seconds % 60
                wait_time_str = f"{wait_minutes:02d}:{wait_seconds:02d}"
                
                gantt_lines.append("section First Injection")
                gantt_lines.append(f"Contrast bolus 1 ({first_vol:.0f}mL)  :active, contrast1, 00:00, {first_duration}s")
                gantt_lines.append(f"Saline flush (50mL)                  :active, saline1, after contrast1, {first_saline_duration}s")
                
                # Determine first scan timing from series data
                first_scan_delay = get_first_scan_delay(row)
                
                gantt_lines.append("section First Scan Phase")
                gantt_lines.append(f"First acquisition                    :crit, scan1, {first_scan_delay}, 15s")
                
                # Wait period between injections
                gantt_lines.append("section Wait Period")
                gantt_lines.append(f"Wait for second injection            :milestone, wait, after scan1, {wait_time_str}")
                
                gantt_lines.append("section Second Injection")
                gantt_lines.append(f"Contrast bolus 2 ({second_vol:.0f}mL)  :active, contrast2, after wait, {second_duration}s")
                gantt_lines.append(f"Saline flush (50mL)                  :active, saline2, after contrast2, {second_saline_duration}s")
                
                # Second scan timing
                second_scan_delay = get_second_scan_delay(row)
                
                gantt_lines.append("section Second Scan Phase")
                gantt_lines.append(f"Second acquisition                   :done, scan2, after saline2, 20s")
        else:
            # Standard single injection
            contrast_ml = parse_volume(volume)
            rate_ml_s = parse_flow_rate(flow_rate)
            
            if contrast_ml and rate_ml_s:
                contrast_duration = int(contrast_ml / rate_ml_s)
                
                gantt_lines.append("section Contrast Injection")
                gantt_lines.append(f"Contrast ({volume})    :active, contrast, 00:00, {contrast_duration}s")
                
                # Add saline if flow rate specified
                if rate_ml_s > 0:
                    saline_duration = int(50 / rate_ml_s)
                    gantt_lines.append(f"Saline (50mL)          :active, saline, after contrast, {saline_duration}s")
    
    # Process each series (skip for split bolus as we handle it above)
    if 'split bolus' not in volume.lower():
        for i in range(1, 5):
            series_name = clean_value(row.get(f'series_{i}_name'))
            if series_name == 'N/A' or 'scout' in series_name.lower():
                continue
            
            delay = clean_value(row.get(f'series_{i}_delay'))
            
            # Skip non-contrast or N/A delays
            if delay == 'N/A':
                continue
            
            # Parse delay
            delay_time = parse_delay_time(delay)
            if not delay_time:
                continue
            
            # Estimate scan duration based on coverage
            start_loc = clean_value(row.get(f'series_{i}_start'))
            end_loc = clean_value(row.get(f'series_{i}_end'))
            scan_duration = estimate_scan_duration(start_loc, end_loc, row)
            
            # Determine section name and style
            section_name = determine_section_name(series_name, i)
            scan_style = determine_scan_style(series_name, delay)
            
            gantt_lines.append(f"section {section_name}")
            gantt_lines.append(f"{series_name}    :{scan_style}, scan{i}, {delay_time}, {scan_duration}s")
    
    if not gantt_lines:
        gantt_lines.append("section Acquisition")
        gantt_lines.append("Standard scan    :done, scan1, 00:00, 10s")
    
    # Join with proper indentation (indent_level spaces for each line)
    indent = '\n' + ' ' * indent_level
    return indent.join([''] + gantt_lines)


def parse_split_bolus_volumes(volume_str):
    """Parse split bolus volumes from string
    
    Example: 'Split bolus: 1st injection 1.1 mL/kg + 2nd injection 0.4 mL/kg'
    Returns: (first_volume_ml, second_volume_ml) assuming 70kg patient
    """
    # Extract first injection
    first_match = re.search(r'1st.*?([\d.]+)\s*ml/kg', volume_str.lower())
    first_multiplier = float(first_match.group(1)) if first_match else 1.1
    
    # Extract second injection
    second_match = re.search(r'2nd.*?([\d.]+)\s*ml/kg', volume_str.lower())
    second_multiplier = float(second_match.group(1)) if second_match else 0.4
    
    # Assume 70kg standard patient
    return (first_multiplier * 70, second_multiplier * 70)


def calculate_split_bolus_wait(row):
    """Calculate wait time between split bolus injections based on protocol
    
    Returns: wait time in seconds
    """
    protocol_name = row.get('protocol_name', '').lower()
    
    # Renal mass protocol: 5-7 minutes
    if 'renal mass' in protocol_name:
        return 5 * 60  # 5 minutes (300 seconds)
    
    # IVP protocol: 5-7 minutes  
    if 'ivp' in protocol_name or 'pyelogram' in protocol_name:
        return 5 * 60  # 5 minutes
    
    # Default
    return 6 * 60  # 6 minutes


def get_first_scan_delay(row):
    """Get timing for first scan in split bolus protocol"""
    # Look for arterial or corticomedullary phase
    for i in range(1, 5):
        series_name = clean_value(row.get(f'series_{i}_name'))
        delay = clean_value(row.get(f'series_{i}_delay'))
        
        if 'arterial' in series_name.lower() or 'corticomedullary' in series_name.lower():
            return parse_delay_time(delay) or "00:20"
    
    # Default arterial timing
    return "00:20"


def get_second_scan_delay(row):
    """Get timing for second scan in split bolus protocol"""
    # Second scan is typically immediate after second injection + saline
    # This is represented as "after saline2" in the gantt
    return "after saline2"

def parse_volume(volume_str):
    """Parse contrast volume from string like '100 mL' or '1.5 mL/kg'"""
    if not volume_str or volume_str == 'N/A':
        return None
    
    # Handle mL/kg - assume 70kg standard patient
    if 'ml/kg' in volume_str.lower() or 'ml / kg' in volume_str.lower():
        try:
            multiplier = float(re.search(r'([\d.]+)', volume_str).group(1))
            return multiplier * 70  # Standard 70kg patient
        except:
            return None
    
    # Handle fixed mL
    try:
        return float(re.search(r'([\d.]+)', volume_str).group(1))
    except:
        return None


def parse_flow_rate(flow_str):
    """Parse flow rate from string like '4 mL/s' or '3-4 mL/s'"""
    if not flow_str or flow_str == 'N/A':
        return None
    
    try:
        # Handle range like '3-4' - take average
        if '-' in flow_str:
            nums = re.findall(r'([\d.]+)', flow_str)
            return sum(float(n) for n in nums) / len(nums)
        else:
            return float(re.search(r'([\d.]+)', flow_str).group(1))
    except:
        return None


def parse_delay_time(delay_str):
    """Parse delay time and convert to mm:ss format"""
    if not delay_str or delay_str == 'N/A':
        return None
    
    # Handle 'Bolus tracked' or similar
    if 'bolus' in delay_str.lower() or 'track' in delay_str.lower():
        return "00:25"  # Standard arterial timing
    
    # Handle 'Immediate' or 'After'
    if 'immediate' in delay_str.lower() or 'after' in delay_str.lower():
        return "after scan1"
    
    # Handle numeric seconds like '70 sec' or '60s'
    sec_match = re.search(r'(\d+)\s*s', delay_str.lower())
    if sec_match:
        total_sec = int(sec_match.group(1))
        minutes = total_sec // 60
        seconds = total_sec % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    # Handle mm:ss format already
    if re.match(r'\d{2}:\d{2}', delay_str):
        return delay_str
    
    # Handle plain numbers (assume seconds)
    try:
        total_sec = int(delay_str)
        minutes = total_sec // 60
        seconds = total_sec % 60
        return f"{minutes:02d}:{seconds:02d}"
    except:
        return None


def estimate_scan_duration(start_loc, end_loc, row):
    """Estimate scan duration based on coverage area"""
    if start_loc == 'N/A' or end_loc == 'N/A':
        return 10  # Default
    
    # Coverage estimates (in seconds)
    coverage_map = {
        # Head/Neck
        ('vertex', 'foramen magnum'): 5,
        ('skull base', 'vertex'): 8,
        ('aortic arch', 'vertex'): 25,
        
        # Chest
        ('lung apices', 'costophrenic angles'): 10,
        ('lung apices', 'diaphragm'): 8,
        ('thoracic inlet', 'diaphragm'): 12,
        
        # Abdomen/Pelvis
        ('diaphragm', 'iliac crests'): 12,
        ('diaphragm', 'pubic symphysis'): 25,
        
        # Full body
        ('thoracic inlet', 'pubic symphysis'): 35,
        ('lung apices', 'pubic symphysis'): 30,
        
        # Extremities
        ('distal femur', 'ankle'): 15,
        ('aorta', 'ankle'): 45,
    }
    
    # Normalize locations
    start = start_loc.lower()
    end = end_loc.lower()
    
    # Check map
    for (s, e), duration in coverage_map.items():
        if s in start and e in end:
            return duration
    
    # Default based on pitch
    pitch = clean_value(row.get('pitch'))
    try:
        pitch_val = float(pitch) if pitch != 'N/A' else 1.0
        # Higher pitch = faster scan
        base_duration = 15
        return int(base_duration / pitch_val)
    except:
        return 10


def determine_section_name(series_name, index):
    """Determine Gantt section name from series"""
    series_lower = series_name.lower()
    
    if 'arterial' in series_lower:
        return 'Arterial Phase'
    elif 'portal' in series_lower or 'venous' in series_lower:
        return 'Portal Venous Phase'
    elif 'delayed' in series_lower or 'delay' in series_lower:
        return 'Delayed Phase'
    elif 'nephrographic' in series_lower:
        return 'Nephrographic Phase'
    elif 'excretory' in series_lower or 'ivp' in series_lower:
        return 'Excretory Phase'
    elif 'gated' in series_lower or 'cardiac' in series_lower:
        return 'Cardiac Acquisition'
    else:
        return f'Scan Phase {index}'


def determine_scan_style(series_name, delay):
    """Determine Gantt bar style based on phase type
    
    Returns appropriate Mermaid gantt style:
    - crit (red): Arterial phases
    - done (purple): Portal venous/delayed phases
    - active (green): Contrast injection
    - task (blue): Saline/other
    """
    series_lower = series_name.lower()
    delay_lower = delay.lower() if delay != 'N/A' else ''
    
    # Arterial phases - critical (RED)
    if any(word in series_lower for word in ['arterial', 'cta', 'angiogram', 'corticomedullary']):
        return 'crit'
    
    # Bolus tracked - critical (RED)
    if 'bolus' in delay_lower or 'track' in delay_lower:
        return 'crit'
    
    # Portal venous, delayed - done (PURPLE)
    if any(word in series_lower for word in ['portal', 'venous', 'delayed', 'washout', 
                                               'equilibrium', 'nephrographic', 'excretory']):
        return 'done'
    
    # Gated/dynamic - done (PURPLE)
    if any(word in series_lower for word in ['gated', 'dynamic', 'perfusion', 'ctp']):
        return 'done'
    
    # Non-contrast - task (BLUE)
    if delay == 'N/A' or delay_lower == 'n/a':
        return 'task'
    
    # Default - done (PURPLE)
    return 'done'

def format_bullet_list(text, default='None specified', indent_level=4):
    """Convert pipe-separated or newline text to markdown list"""
    if not text or text.strip().lower() in ['n/a', 'none', '']:
        return f'{" " * indent_level}- {default}'
    
    if '|' in text:
        items = [item.strip() for item in text.split('|') if item.strip()]
    else:
        items = [line.strip() for line in text.split('\n') if line.strip()]
    
    if not items:
        return f'{" " * indent_level}- {default}'
    
    return '\n'.join([f'{" " * indent_level}- {item}' for item in items])


def create_contrast_section(row):
    """Generate contrast section based on protocol"""
    agent = clean_value(row.get('contrast_agent'))
    
    if agent == 'N/A' or agent == 'None':
        return """!!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.
"""
    
    volume = clean_value(row.get('contrast_volume'))
    if 'split bolus' in volume.lower():
        return f"""
    ===   "Contrast Details"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | {agent} |
        | Volume | {volume} |
        | Flow Rate | {clean_value(row.get('contrast_flow_rate'))} |
        | Timing | {clean_value(row.get('contrast_timing_method'))} |

    ===   "Contrast Notes"

        {clean_value(row.get('contrast_labs_notes'))}

"""
    
    contrast_content = f"""
    ===   "Injection Parameters"
        
        | Parameter | Value |
        |-----------|-------|
        | Agent | {agent} |
        | Volume | {volume} |
        | Flow Rate | {clean_value(row.get('contrast_flow_rate'))} |
"""
    
    if clean_value(row.get('contrast_roi_placement')) != 'N/A':
        contrast_content += f"""        | Timing Method | {clean_value(row.get('contrast_timing_method'))} |
        | ROI Placement | {clean_value(row.get('contrast_roi_placement'))} |
        | Trigger (HU) | {clean_value(row.get('contrast_trigger_hu'))} |
"""
    
    contrast_content += f"""
    ===   "Lab Requirements"
        
        {clean_value(row.get('contrast_labs_notes'))}

"""
    
    return contrast_content


def create_premedication_section(row):
    """Generate premedication section"""
    premed = clean_value(row.get('premedication_notes'))
    if premed == 'N/A' or premed.lower() == 'none':
        return ''
    
    return f"""- **Pre-Medication:** 
      {premed}
"""

def create_acquisition_summary_table(row):
    """Generate acquisition summary table for clinical overview"""
    summary_rows = []
    
    for i in range(1, 5):
        series_name = clean_value(row.get(f'series_{i}_name'))
        if series_name == 'N/A' or series_name == 'Scout':
            continue
        
        # Determine phase type from series name or delay
        delay = clean_value(row.get(f'series_{i}_delay'))
        
        # Extract FOV from start/end
        start = clean_value(row.get(f'series_{i}_start'))
        end = clean_value(row.get(f'series_{i}_end'))
        
        if start != 'N/A' and end != 'N/A':
            fov = f"{start} to {end}"
        else:
            fov = "Standard coverage"
        
        # Determine phase type
        if delay == 'N/A':
            phase = "Non-contrast"
        elif 'bolus' in delay.lower() or 'track' in delay.lower():
            phase = "Arterial (bolus tracked)"
        else:
            phase = f"Contrast ({delay} delay)"
        
        summary_rows.append(
            f"        | {series_name} | {phase} | {fov} |"
        )
    
    if not summary_rows:
        return """        | Series | Phase | Coverage |
        |:-------|:------|:---------|
        | Standard | Per protocol | Region of interest |"""
    
    table = """        | Series | Phase | Coverage |
        |:-------|:------|:---------|
"""
    table += '\n'.join(summary_rows)
    
    return table

def create_series_table(row):
    """Generate series acquisition table"""
    series_rows = []
    
    for i in range(1, 5):
        series_name = clean_value(row.get(f'series_{i}_name'))
        if series_name == 'N/A':
            continue
        
        series_rows.append(
            f"    | {series_name} | "  # Added 4 spaces at start
            f"{clean_value(row.get(f'series_{i}_start'))} | "
            f"{clean_value(row.get(f'series_{i}_end'))} | "
            f"{clean_value(row.get(f'series_{i}_delay'))} | "
            f"{clean_value(row.get(f'series_{i}_thickness'))} | "
            f"{clean_value(row.get(f'series_{i}_notes'))} |"
        )
    
    if not series_rows:
        return (
            "    | Standard acquisition | Per protocol | "
            "Per protocol | Per indication | Per protocol | "
            "Standard helical |"
        )
    
    table = (
        "    | Series Name | Start Location | End Location | "
        "Delay | Slice Thickness | Notes |\n"
        "    |:------------|:---------------|:-------------|:"
        "------|:----------------|:------|\n"
    )
    table += '\n'.join(series_rows)
    
    return table


def create_postproc_table(row):
    """Generate post-processing reconstruction table"""
    postproc_rows = []
    
    for i in range(1, 5):
        plane = clean_value(row.get(f'postproc_{i}_plane'))
        if plane == 'N/A':
            continue
        
        postproc_rows.append(
            f"    | {plane} | "  # Added 4 spaces at start
            f"{clean_value(row.get(f'postproc_{i}_acq'))} | "
            f"{clean_value(row.get(f'postproc_{i}_fov'))} | "
            f"{clean_value(row.get(f'postproc_{i}_thickness'))} | "
            f"{clean_value(row.get(f'postproc_{i}_kernel'))} | "
            f"{clean_value(row.get(f'postproc_{i}_ir'))} | "
            f"{clean_value(row.get(f'postproc_{i}_notes'))} |"
        )
    
    if not postproc_rows:
        return (
            "    | Axial | Source | Standard | 2.5 mm/2.5 mm | "
            "Standard | 3 | Primary diagnostic series |"
        )
    
    table = (
        "    | Plane | Acquisition | FOV | Thickness/Increment | "
        "Kernel | IR Strength | Notes |\n"
        "    |:------|:------------|:----|:--------------------|:"
        "-------|:------------|:------|\n"
    )
    table += '\n'.join(postproc_rows)
    
    return table

def create_gantt_content(row):
    """Generate Gantt chart content"""
    gantt_lines = []
    
    contrast_vol = clean_value(row.get('gantt_contrast_volume'))
    if contrast_vol != 'N/A':
        gantt_lines.append(
            f"\n      section Contrast Injection\n"
            f"      Contrast ({contrast_vol})    :active, contrast, "
            f"00:00, {clean_value(row.get('gantt_contrast_duration'))}\n"
            f"      Saline ({clean_value(row.get('gantt_saline_volume'))})      "
            f":active, saline, after contrast, "
            f"{clean_value(row.get('gantt_saline_duration'))}"
        )
    
    scan_section = clean_value(row.get('gantt_scan_section'))
    scan_phase = clean_value(row.get('gantt_scan_phase'))
    scan_style = clean_value(row.get('gantt_scan_style'))
    scan_delay = clean_gantt_time_value(row.get('gantt_scan_delay')) 
    scan_duration = clean_value(row.get('gantt_scan_duration'))
    
    if scan_section != 'N/A' and scan_phase != 'N/A':
        gantt_lines.append(
            f"\n      section {scan_section}\n"
            f"      {scan_phase}    :{scan_style}, scan1, "
            f"{scan_delay}, {scan_duration}"
        )
    
    if not gantt_lines:
        return "\n      section Acquisition\n      Standard scan    :done, scan1, 00:00, 10s"
    
    return ''.join(gantt_lines)


def create_additional_recons_section(row):
    """Generate additional reconstructions section"""
    additional = clean_value(row.get('additional_recons'))
    if additional == 'N/A':
        return ''
    
    return f"\n### Additional Reconstructions\n\n{additional}\n"


def determine_protocol_type(row):
    """Determine protocol type from various fields"""
    protocol_name = row.get('protocol_name', '').lower()
    
    if 'gated' in protocol_name or 'cardiac' in protocol_name:
        return 'Cardiac Gated'
    elif 'cta' in protocol_name or 'ctv' in protocol_name:
        return 'Vascular'
    elif 'trauma' in protocol_name:
        return 'Trauma'
    elif 'hrct' in protocol_name or 'lung' in protocol_name:
        return 'Chest/Pulmonary'
    elif any(x in protocol_name for x in ['brain', 'head', 'stroke', 'sinus', 'temporal']):
        return 'Neuroradiology'
    elif any(x in protocol_name for x in ['spine', 'myelogram']):
        return 'Spine'
    elif any(x in protocol_name for x in ['ankle', 'foot', 'knee', 'hip', 'shoulder', 'elbow', 'wrist', 'hand']):
        return 'Musculoskeletal'
    elif clean_value(row.get('contrast_agent')) == 'N/A':
        return 'Non-Contrast'
    else:
        return 'Contrast-Enhanced'

