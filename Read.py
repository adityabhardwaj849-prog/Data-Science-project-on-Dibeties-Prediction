import pandas as pd
df = pd.read_csv("diabetes.csv")

print(df.mean(0, skipna=True))
