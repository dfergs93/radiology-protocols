
"""
Batch create protocol markdown files from CSV
"""

import csv
import re
from pathlib import Path
from datetime import datetime

from protocol_template import PROTOCOL_TEMPLATE
from protocol_formatters import (
    clean_value,
    format_bullet_list,
    create_contrast_section,
    create_premedication_section,
    create_series_table,
    create_postproc_table,
    create_gantt_from_series,
    create_additional_recons_section,
    determine_protocol_type,
    create_acquisition_summary_table
)


def create_protocol_from_row(row):
    """Create a protocol markdown file from CSV row"""
    
    protocol_name = row['protocol_name']
    category = row.get('category', 'general').lower()
    
    content = PROTOCOL_TEMPLATE.format(
        protocol_name=protocol_name,
        last_updated=row.get('last_updated', datetime.now().strftime('%Y-%m-%d')),
        author=row.get('author', 'Radiology Department'),
        acquisition_summary_table=create_acquisition_summary_table(row), 
        clinical_indications_formatted=format_bullet_list(
            row.get('clinical_indications'), 'Standard indications', indent_level=8
        ),
        patient_positioning=clean_value(row.get('patient_positioning')),
        npo_status=clean_value(row.get('npo_status')),
        premedication_section=create_premedication_section(row),
        safety_renal_function=clean_value(row.get('safety_renal_function')),
        safety_allergy_check=clean_value(row.get('safety_allergy_check')),
        contrast_section=create_contrast_section(row),
        kv=clean_value(row.get('kv')),
        mas=clean_value(row.get('mas')),
        rotation_time=clean_value(row.get('rotation_time')),
        pitch=clean_value(row.get('pitch')),
        series_table=create_series_table(row),
        gantt_content=create_gantt_from_series(row),  # Changed from create_gantt_content
        postproc_table=create_postproc_table(row),
        additional_recons_section=create_additional_recons_section(row),
        tech_notes_formatted=format_bullet_list(
            row.get('tech_notes'), 'Follow standard protocol'
        ),
        nursing_notes_formatted=format_bullet_list(
            row.get('nursing_notes'), 'Standard nursing assessment'
        ),
        radiologist_notes_formatted=format_bullet_list(
            row.get('radiologist_notes'), 'Systematic review'
        ),
        artifact_tip_formatted=format_bullet_list(
            row.get('artifact_reduction_tip'), 'Follow standard imaging techniques'
        ),
        category=category.title(),
        protocol_type=determine_protocol_type(row)
    )
    
    filename = protocol_name.lower()
    filename = re.sub(r'[^\w\s-]', '', filename)
    filename = re.sub(r'[-\s]+', '-', filename)
    filepath = Path(f'ct/{category}/{filename}.md')
    
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(content, encoding='utf-8')
    
    print(f"✅ Created: {filepath}")
    
    return filepath


def batch_create(csv_file='protocols.csv'):
    """Create protocols from CSV file"""
    
    if not Path(csv_file).exists():
        print(f"❌ Error: CSV file '{csv_file}' not found")
        return
    
    print(f"\n📋 Reading protocols from: {csv_file}\n")
    
    protocols_created = 0
    errors = []
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            required_columns = ['protocol_name', 'category']
            if not all(col in reader.fieldnames for col in required_columns):
                print(f"❌ Error: CSV must contain: {', '.join(required_columns)}")
                return
            
            for row_num, row in enumerate(reader, start=2):
                if not row.get('protocol_name') or not row.get('protocol_name').strip():
                    continue
                
                try:
                    create_protocol_from_row(row)
                    protocols_created += 1
                except Exception as e:
                    error_msg = f"Row {row_num} ({row.get('protocol_name', 'Unknown')}): {str(e)}"
                    errors.append(error_msg)
                    print(f"⚠️  Warning: {error_msg}")
        
        print(f"\n{'='*60}")
        print(f"✅ Successfully created {protocols_created} protocols!")
        
        if errors:
            print(f"\n⚠️  {len(errors)} errors encountered:")
            for error in errors:
                print(f"   - {error}")
        
        print(f"{'='*60}\n")
        
    except Exception as e:
        print(f"❌ Fatal error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    import sys
    csv_file = sys.argv[1] if len(sys.argv) > 1 else 'protocols.csv'
    print("🚀 Starting batch protocol creation...")
    batch_create(csv_file)


