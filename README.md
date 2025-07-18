# Clean Member Records

This script processes a CSV file containing member records and performs data cleaning operations to remove entries that do not meet certain quality standards.

---

## Description

The goal of this script is to clean up a dataset of member names by applying the following filters:

### ✅ Remove all-uppercase names
Excludes entries where either the first name or last name is written entirely in capital letters (e.g., `JOHN`, `DOE`).

###  Remove duplicate entries
Drops any rows that have the same first and last name combination as another row.

### Remove non-English characters
Filters out names that contain non-English characters or symbols, such as:
- Punctuation: `?`, `.`, `!`, etc.
- Accented letters: `é`, `ñ`, etc.
- Numbers or emojis
- Non-Latin characters (e.g., Chinese, Arabic, Cyrillic)

Only names containing English alphabets (`A–Z` or `a–z`), spaces, hyphens, and apostrophes are allowed.

### Export the cleaned dataset
Saves the final filtered dataset to a file named `cleaned_data.csv`.

---

## 🛠How to Use

1. Make sure you have Python installed.
2. Install `pandas` if not already installed:
   ```bash
   pip install pandas

python [file_name].py
#sample data
first_name,last_name
John,Doe
JANE,SMITH
Jörg,Müller
Alice,O'Neil
