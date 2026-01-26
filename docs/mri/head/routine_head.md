# Routine Head

**Last Updated:** 2015-05-02
**Protocol Author:** Dr. Duncan Ferguson

---

## 1. Clinical Indications
- Bleed
- Routine Head

## 2. Patient Prep & Screening
- Standard MRI safety screening.m
- Patient to change into scrubs.
- No IV contrast needed for routine exam.

## 3. Positioning & Coil
- **Positioning:** Supine, head first.
- **Coil:** HRBRAIN, NV Array, HNS
- **Landmark:** Center to head

## 4. Sequence Parameters
| #     | Series Description          | Plane   | Pulse Sequence  | Imaging Options              | TR       | TE      | TI/FA            | ETL       | BW   | FOV            | Slice Thickness/Space       | NEX  | Matrix Fr/Ph  | Frequency Direction | # Slices | Time     | Comments                                      | Images |
|-------|-----------------------------|---------|-----------------|------------------------------|----------|---------|------------------|-----------|------|----------------|-----------------------------|------|---------------|---------------------|----------|----------|-----------------------------------------------|--------|
|   1   |   3Pl-Locs/Cal              |   3     |   Loc   FGRE    |   Seq, Fast                  |   N      |   N     |                  |   N N     |      |   24           |   5/5mm                     |   1  |   256   128   |   U                 |          |   0:14   |                                               |        |
|   2   |   SAG T1 FLAIR              |   O/S   |   FSE-XL        |   Seq,TRF   Fast             |   2100   |   24    |   750            |   5 31    |      |   24           |   4/1mm                     |   2  |   320   256   |   S/I               |   27     |   3:47   |   Max Slices=28                               |        |
|   3   |   HiRes Axial DWI   1000b   |   O/A   |   SE            |   EPI,DIFF,Asset             |   8000   |   Min   |                  |   16      |      |   24           |   5/0.5mm                   |   4  |   128   256   |   R/L               |   27     |   2:16   |   Diff,Dir=All   ST is different   ADC Map    |        |
|   4   |   Axial T2   FRFSE          |   O/A   |   FRFSE-   XL   |   FC,TRF   Fast,FR           |   2717   |   85    |                  |   16 31   |      |   22           |   4/1mm   (0.75)            |   2  |   384   256   |   A/P               |   28     |   2:43   |   Angle to AC-PC   Keep #30~32                |        |
|   5   |   Axial T2   FLAIR          |   O/A   |   T2flair       |   FC,EDR,TRF   Fast,ZIP512   |   8000   |   120   |   2000           |   25      |      |   22           |   4/1mm                     |   2  |   256   224   |   A/P               |   28     |   4:48   |   Don’t change   TR ,TE                       |        |
|   6   |   T1 SPGR   IR PREPPED      |   O/A   |   SPGR          |   Fast,IrP                   |   N      |   Min   |   450   /   12   |   N 15    |      |   25   (0.75)  |   1.4mm   Locs   Slab:126   |   1  |   256   256   |   A/P               |   126    |   5:28   |   Angle to AC-PC   COR-Reformat   4x4mm/22cm  |        |
|   7   |   (opt)Axial DWI   1000b    |   O/A   |   SE            |   EPI,DIFF,Asset             |   8000   |   Min   |                  |   16      |      |   28           |   5/0.5mm                   |   1  |   128   192   |   R/L               |   27     |   :40    |   Diff,Dir=All   ADC Map                      |        |
|   8   |                             |         |                 |                              |          |         |                  |           |      |                |                             |      |               |                     |          |          |                                               |        |
| 9     |                             |         |                 |                              |          |         |                  |           |      |                |                             |      |               |                     |          |          |                                               |        |
| 10    |                             |         |                 |                              |          |         |                  |           |      |                |                             |      |               |                     |          |          |                                               |        |

## 5. Notes for Radiologist

## 6. Notes for Technologist
-Axial - The slices should be parallel to a line of AC and PC or hard palate. Include from the base of the skull to the top of the head. Slices for T2 FSE and FLAIR
and same coverage for DWI.
* AX T2 FLAIR: Keep 30~32slices - Mar 2023
SPGR - COR Reformat Only(4x4mm,FOV=22cm) - Jan 4.2013
* Axial DWI(HiRes) – HDx(4NEX), HDe(2NEX)as per Dr. DH, GS – May01/2015
## 7. Notes for Nurses

## 8. Resources
- Links to videos, pdfs, other resources to help understand acquisition or interpretation