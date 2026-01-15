import pandas as pd

# 1. Load the data
file_path = 'Film_Noir_Dataset.xlsx'
df = pd.read_excel(file_path)

# 2. Rename columns for easier coding
# This maps the long Excel names to simple Python variables
df = df.rename(columns={
    'Noir Score (1-10)': 'noir_score',
    'Lead Actor': 'lead_actor',
    'Lead Actress': 'lead_actress'
})

# Normalize other column names to lowercase/no spaces
df.columns = [c.lower().replace(' ', '_') for c in df.columns]

# Now we can use 'noir_score' safely
print("New Column Names:", df.columns.tolist())

# 3. Fill missing values
df['noir_score'] = df['noir_score'].fillna(df['noir_score'].mean())

# 4. Feature Engineering for Tableau
df['decade'] = (df['year'] // 10) * 10
df['decade'] = df['decade'].astype(str) + "s"

# Categorize endings for visual analysis
df['is_tragic'] = df['ending'].apply(lambda x: True if x.lower() in ['tragic', 'bitter'] else False)

# 5. Export the clean version
df.to_excel('cleaned_film_noir_data.xlsx', index=False)
print("Done! 'cleaned_film_noir_data.xlsx' is ready for Tableau.")