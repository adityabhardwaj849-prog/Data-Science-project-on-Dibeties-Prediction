import pandas as pd
df=pd.read_csv(r"C:\Users\adity\OneDrive\Documents\New folder\project\diabetes.csv")

print(df.mean(0, skipna=True))
