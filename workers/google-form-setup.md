# Google Form Setup — Protocol Change Requests

Submissions from the "Request a Change" button will be collected in a
Google Sheet you own. No GitHub account required for users.

---

## 1. Create the form

1. Go to [forms.google.com](https://forms.google.com) → **Blank form**
2. Title: `Protocol Change Request`
3. Add **Question 1**
   - Type: **Short answer**
   - Label: `Subject`
4. Add **Question 2**
   - Type: **Paragraph**
   - Label: `Details`
5. Settings → **Responses** → turn off "Limit to 1 response" and
   turn off "Collect email addresses" so no sign-in is required.
6. Click **Send** (or **Preview**) and note the URL — you need the
   form ID from it (the long string between `/d/e/` and `/viewform`).

---

## 2. Find the entry IDs

Each form field has a hidden `entry.XXXXXXXXX` ID used for submission.

1. Open the form preview in your browser.
2. Right-click → **View Page Source** (or open DevTools → Elements).
3. Search for `entry.` — you will see entries like:
   ```
   entry.123456789   ← Subject field
   entry.987654321   ← Details field
   ```
   Copy both numbers (including the `entry.` prefix).

---

## 3. Configure the site

Edit `docs/javascripts/institution-config.json`:

```json
{
  "google_form_url": "https://docs.google.com/forms/d/e/YOUR_FORM_ID/formResponse",
  "google_form_entry_title": "entry.123456789",
  "google_form_entry_body": "entry.987654321"
}
```

Replace `YOUR_FORM_ID` and the entry values with your actual values.

---

## 4. Link responses to a Sheet (optional but recommended)

In the form editor → **Responses** tab → click the Google Sheets icon
→ **Create a new spreadsheet**. All submissions appear there instantly.

---

## Notes

- The `feedback_url` field is still used as a fallback if `google_form_url`
  is not set (opens GitHub new-issue page).
- Submissions are fire-and-forget: the site shows a confirmation
  immediately after sending. If the form URL is misconfigured,
  submissions will silently drop — test with a real submission after setup.
