import pandas as pd
import re

# 1. Load CSV file
df = pd.read_csv("youfilename.csv")

# 2. Remove names that are all uppercase
df = df[~(df['first_name'].str.isupper() | df['last_name'].str.isupper())]

# 3. Remove duplicate names (based on first and last name)
df = df.drop_duplicates(subset=['first_name', 'last_name'])

# 4. Remove entries with non-English characters in first or last names
# English letters: a-z, A-Z, space, hyphen, apostrophe allowed
def is_english_name(text):
    return bool(re.match(r"^[A-Za-z\s\-']+$", str(text)))

df = df[df['first_name'].apply(is_english_name) & df['last_name'].apply(is_english_name)]

# 5. Save the cleaned data
df.to_csv("cleaned_data.csv", index=False)
