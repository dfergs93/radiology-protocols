import json
from typing import Dict, Any

def fleischner_calculator(size_mm: float, nodule_type: str, patient_risk: str, multiplicity: str) -> Dict[str, Any]:
    """
    Calculates the 2017 Fleischner Society recommendation for incidental pulmonary nodules.
    """
    nodule_type = nodule_type.lower()
    patient_risk = patient_risk.lower()
    multiplicity = multiplicity.lower()
    
    rec = "No recommendation found for given parameters."
    
    if nodule_type == 'solid':
        if multiplicity == 'single':
            if size_mm < 6:
                rec = "No routine follow-up" if patient_risk == 'low' else "Optional CT at 12 mo"
            elif 6 <= size_mm <= 8:
                rec = "CT 6–12 mo; consider CT 18–24 mo" if patient_risk == 'low' else "CT 6–12 mo and CT 18–24 mo"
            else: # > 8
                rec = "Consider CT ~3 mo, PET/CT and/or biopsy"
        else: # multiple
            if size_mm < 6:
                rec = "No routine follow-up" if patient_risk == 'low' else "Optional CT at 12 mo"
            elif 6 <= size_mm <= 8:
                rec = "CT 3–6 mo; consider CT 18–24 mo" if patient_risk == 'low' else "CT 3–6 mo and CT 18–24 mo"
            else: # > 8
                rec = "CT 3–6 mo ± PET/CT/biopsy"
    
    elif nodule_type == 'ground-glass':
        if multiplicity == 'single':
            if size_mm < 6:
                rec = "No routine follow-up"
            else: # >= 6
                rec = "CT 6–12 mo to confirm persistence, then q2y until 5y"
        else: # multiple
            if size_mm < 6:
                rec = "CT 3–6 mo; if stable, consider CT at 2 and 4y"
            else: # >= 6
                rec = "CT 3–6 mo; subsequent management guided by most suspicious nodule"
                
    elif nodule_type == 'part-solid':
        if multiplicity == 'single':
            if size_mm < 6:
                rec = "No routine follow-up"
            else: # >= 6
                rec = "CT 3–6 mo to confirm persistence; if persistent, annual CT until 5y (manage by solid component)"
        else: # multiple
            if size_mm < 6:
                rec = "CT 3–6 mo; if stable, consider CT at 2 and 4y"
            else: # >= 6
                rec = "CT 3–6 mo; subsequent management guided by most suspicious nodule"

    return {
        "guideline": "Fleischner Society 2017",
        "inputs": {
            "size_mm": size_mm,
            "nodule_type": nodule_type,
            "patient_risk": patient_risk,
            "multiplicity": multiplicity
        },
        "recommendation": rec,
        "link": "/pulmonary/fleischner/"
    }

def adrenal_washout_calculator(unenhanced_hu: float, venous_hu: float, delayed_hu: float) -> Dict[str, Any]:
    """
    Calculates absolute and relative adrenal washout to determine likelihood of adenoma.
    """
    absolute_washout = None
    relative_washout = None
    diagnosis = "Indeterminate"
    
    if unenhanced_hu is not None and venous_hu is not None and delayed_hu is not None:
        den = venous_hu - unenhanced_hu
        absolute_washout = ((venous_hu - delayed_hu) / den * 100) if den != 0 else 0
        
    if venous_hu is not None and delayed_hu is not None:
        relative_washout = ((venous_hu - delayed_hu) / venous_hu * 100) if venous_hu != 0 else 0
        
    if unenhanced_hu is not None and unenhanced_hu <= 10:
        diagnosis = "Lipid-rich adenoma (Based on unenhanced HU ≤ 10)"
    elif absolute_washout is not None and absolute_washout > 60:
        diagnosis = "Lipid-poor adenoma (Absolute Washout > 60%)"
    elif relative_washout is not None and relative_washout > 40:
        diagnosis = "Lipid-poor adenoma (Relative Washout > 40%)"
    else:
        diagnosis = "Indeterminate (Does not meet washout criteria for adenoma. Consider metastasis, pheochromocytoma, or adrenocortical carcinoma depending on clinical context.)"

    return {
        "guideline": "Adrenal Washout",
        "inputs": {
            "unenhanced_hu": unenhanced_hu,
            "venous_hu": venous_hu,
            "delayed_hu": delayed_hu
        },
        "results": {
            "absolute_washout_percent": round(float(absolute_washout), 1) if absolute_washout is not None else None,
            "relative_washout_percent": round(float(relative_washout), 1) if relative_washout is not None else None,
            "finding": diagnosis
        },
        "recommendation": diagnosis,
        "link": "/abdominal/adrenal/adrenal_washout/"
    }

# OpenAI Tool definitions
GUIDELINE_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "fleischner_calculator",
            "description": "Calculates the Fleischner Society 2017 recommendation for incidental pulmonary nodules.",
            "parameters": {
                "type": "object",
                "properties": {
                    "size_mm": {
                        "type": "number",
                        "description": "The size of the pulmonary nodule in millimeters (e.g., 6.5, 10)."
                    },
                    "nodule_type": {
                        "type": "string",
                        "enum": ["solid", "part-solid", "ground-glass"],
                        "description": "The attenuation type of the nodule."
                    },
                    "patient_risk": {
                        "type": "string",
                        "enum": ["low", "high"],
                        "description": "The patient's lung cancer risk level (high risk includes smoking history, family history, etc.). If not specified, ask or assume high for safety."
                    },
                    "multiplicity": {
                        "type": "string",
                        "enum": ["single", "multiple"],
                        "description": "Whether there is a single nodule or multiple nodules."
                    }
                },
                "required": ["size_mm", "nodule_type", "patient_risk", "multiplicity"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "adrenal_washout_calculator",
            "description": "Calculates the adrenal CT washout to determine if an adrenal mass is an adenoma.",
            "parameters": {
                "type": "object",
                "properties": {
                    "unenhanced_hu": {
                        "type": "number",
                        "description": "The Hounsfield Units (HU) on the unenhanced (non-contrast) phase."
                    },
                    "venous_hu": {
                        "type": "number",
                        "description": "The Hounsfield Units (HU) on the portal venous (60-90s) phase."
                    },
                    "delayed_hu": {
                        "type": "number",
                        "description": "The Hounsfield Units (HU) on the delayed (10-15 min) phase."
                    }
                },
                "required": ["unenhanced_hu", "venous_hu", "delayed_hu"]
            }
        }
    }
]

def execute_tool(tool_call) -> Dict[str, Any]:
    """Execute the appropriate guideline tool function based on the OpenAI tool call."""
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    
    if function_name == "fleischner_calculator":
        return fleischner_calculator(
            size_mm=arguments.get("size_mm"),
            nodule_type=arguments.get("nodule_type"),
            patient_risk=arguments.get("patient_risk"),
            multiplicity=arguments.get("multiplicity")
        )
    elif function_name == "adrenal_washout_calculator":
        return adrenal_washout_calculator(
            unenhanced_hu=arguments.get("unenhanced_hu"),
            venous_hu=arguments.get("venous_hu"),
            delayed_hu=arguments.get("delayed_hu")
        )
    else:
        raise ValueError(f"Unknown tool: {function_name}")
