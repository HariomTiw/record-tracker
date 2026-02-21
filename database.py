import pandas as pd

base_file = "FEB-26.xlsx"

df = pd.read_excel(base_file)

print("Columns in base file:")
print(df.columns.tolist())
