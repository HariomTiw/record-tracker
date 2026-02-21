import pandas as pd

# 1. Load your original Excel file
# Make sure "FEB-26.xlsx" is in the same folder as this script
input_file = "FEB-26.xlsx"
df = pd.read_excel(input_file, sheet_name="Sheet1")

# 2. Dictionary mapping Gujarati names to English (Generated from your file)
# This ensures 100% accuracy without needing an external translation library
name_map = {
    "પરમાર રંજનબેન": "Parmar Ranjanben",
    "વણઝારા ગીતાબેન": "Vanzara Gitaben",
    "રાઠોડ જાગૃતિબેન": "Rathod Jagrutiben",
    "વણઝારા કૈલાસબેન": "Vanzara Kailasben",
    "પરમાર પુષ્પાબેન": "Parmar Pushpaben",
    "મકવાણા મધુબેન": "Makwana Madhuben",
    "વાઘેલા હંસાબેન": "Vaghela Hansaben",
    "રાઠોડ ગીતાબેન": "Rathod Gitaben",
    "ચાવડા હંસાબેન": "Chavda Hansaben",
    "સોલંકી કૈલાસબેન": "Solanki Kailasben",
    "પરમાર રમીલાબેન": "Parmar Ramilaben",
    "વાઘેલા ભાવનાબેન": "Vaghela Bhavnaben",
    "વાઘેલા નિર્મળાબેન": "Vaghela Nirmalaben",
    "મકવાણા મંજુલાબેન": "Makwana Manjulaben",
    "વાઘેલા કમળાબેન": "Vaghela Kamalaben",
    "રાઠોડ દક્ષાબેન": "Rathod Dakshaben",
    "પરમાર સોનલબેન": "Parmar Sonalben",
    "વાઘેલા શારદાબેન": "Vaghela Shardaben",
    "વાઘેલા જશોદાબેન": "Vaghela Jashodaben",
    "પરમાર મધુબેન": "Parmar Madhuben",
    "સોલંકી રંજનબેન": "Solanki Ranjanben",
    "રાઠોડ કોકીલાબેન": "Rathod Kokilaben",
    "વાઘેલા ગીતાબેન": "Vaghela Gitaben",
    "વાઘેલા કાંતાબેન": "Vaghela Kantaben",
    "પરમાર ભગવતીબેન": "Parmar Bhagwatiben",
    "વાઘેલા મીનાબેન": "Vaghela Minaben",
    "પરમાર સવિતાબેન": "Parmar Savitaben",
    "ડાભી શારદાબેન": "Dabhi Shardaben",
    "પરમાર શારદાબેન": "Parmar Shardaben",
    "વાઘેલા ભારતીબેન": "Vaghela Bharatiben",
    "સોલંકી રેખાબેન": "Solanki Rekhaben",
    "વાઘેલા જાગૃતિબેન": "Vaghela Jagrutiben",
    "મકવાણા ગૌરીબેન": "Makwana Gauriben",
    "પરમાર જશુબેન": "Parmar Jashuben",
    "વાઘેલા કૈલાસબેન": "Vaghela Kailasben",
    "પરમાર કૈલાસબેન": "Parmar Kailasben",
    "વાઘેલા સંગીતાબેન": "Vaghela Sangitaben",
    "વાઘેલા સોનલબેન": "Vaghela Sonalben",
    "પરમાર ગીતાબેન": "Parmar Gitaben",
    "ચાવડા મધુબેન": "Chavda Madhuben",
    "પરમાર લીલાબેન": "Parmar Lilaben",
    "મકવાણા ગીતાબેન": "Makwana Gitaben"
}

# 3. Apply the translation
# Assuming the names are in the 2nd column (index 1). 
# We use the column name directly to be safe.
# Replace 'NAME' with the actual header of your 2nd column if it differs.
target_column = df.columns[1] 

# Map the names. If a name isn't in the list, it keeps the original text.
df[target_column] = df[target_column].map(name_map).fillna(df[target_column])

# 4. Save to a new Excel file
output_file = "FEB-26-English.xlsx"
df.to_excel(output_file, index=False)

print(f"✅ Success! File saved as: {output_file}")