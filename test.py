import pandas as pd

df = pd.read_csv('operations.csv')

df = df.dropna(axis=1, how='all')

df = df.dropna()

for col in df.select_dtypes(include=['object']):
    try:
        df[col] = df[col].astype(float)
    except ValueError:
        pass

df = df.drop_duplicates()

df = df.reset_index(drop=True)


df.to_csv('test.csv', index=False)
