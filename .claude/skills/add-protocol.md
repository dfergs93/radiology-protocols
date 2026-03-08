# Add New Protocol

Scaffolds and validates a new CT protocol markdown file.

## Usage

```
/add-protocol <category> <protocol_name>
```

## Arguments

- `category`: CT subcategory (e.g., `abdomen`, `chest`, `neuro`, `cardiac`, `vascular`, `msk`, `trauma`)
- `protocol_name`: Protocol name in kebab-case (e.g., `ct-pulmonary-embolism`)

## Example

```
/add-protocol chest ct-pulmonary-embolism
```

Creates: `docs/ct/chest/ct-pulmonary-embolism.md`

## Template Structure

The generated file includes:
- H1 title
- Clinical Indications section
- Patient Preparation section
- Injection Parameters table (contrast agent, volume, flow rate, timing)
- Series Acquisition table (with Mermaid Gantt diagram)
- Acquisition Summary table
- Key Clinical Notes section

## Next Steps

1. Fill in the clinical indications and patient prep
2. Complete the contrast parameters and acquisition series
3. Create the Mermaid Gantt timing diagram
4. Add the protocol to `csv/protocols.csv` if providing indications for Protocoller
5. Run `python scripts/build_vectordb.py` to index

## Validation

The skill will:
- Check that the file path is valid
- Warn if category doesn't exist (but allow creation)
- Verify the markdown has required H1 title
- Test that Mermaid diagram syntax is valid
