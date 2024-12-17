# Updating REACH Participation Agreement Status

Follow these steps to update the REACH Participation Agreement Status:

## 1. Identify New Schools
1. Open the spreadsheet: [REACH Participation Agreement Status](https://docs.google.com/spreadsheets/d/19XpoiOgO45ko2Ud4zuNUMM1wSEGbiIMckvYBQpv8bnk/edit?gid=569911717#gid=569911717).
2. Scroll to the latest entries and review **Column D** (“Completed RSSI survey?”).
   - Any rows without “Yes” or “No” are new schools that need to be updated.

## 2. Populate "Yes/No" for New Rows
1. Locate the last **Yes/No** cell in Column D.
2. Click and hold the bottom-right corner of this cell, then drag it down to the last blank **Yes/No** cell that needs to be updated.
   - This extends the formula to populate the new rows.

## 3. Validate RCDTS Numbers
1. Navigate to **Column G** (“What is your school’s RCDTS?”).
   - The RCDTS is a critical linking element and must be accurate.
2. Validate each RCDTS using the [ISBE RCDTS Lookup Tool](https://www.isbe.net/Pages/RCDTS-Lookup.aspx):
   - Enter the RCDTS number.
   - Confirm that the school name matches the name in the spreadsheet.
   - If no match is found, look up the school or district name to identify the correct RCDTS ID.

## 4. Correct and Format RCDTS Numbers
1. For each RCDTS number:
   - Add an apostrophe (`'`) before the number to ensure leading zeros are preserved.
   - Double-check that all leading zeros remain intact after adding the apostrophe.

## 5. Transfer Data to the GitHub Repository
1. Clone the **reach_pa_upload** GitHub repository to your local system.
   - Ensure it contains the `reach_pa_upload.py` script and the `participation_agreement_status.xlsx` sheet.
2. Copy the **Timestamp** and **RCDTS** values for the new schools.
3. Open the `participation_agreement_status.xlsx` file and paste these values as new rows in the sheet.
4. Save the file.

## 6. Run the Upload Script
1. Open a terminal.
2. Navigate (`cd`) to the directory containing the `reach_pa_upload.py` script.
3. Run the script:
   ```bash
   python reach_pa_upload.py
