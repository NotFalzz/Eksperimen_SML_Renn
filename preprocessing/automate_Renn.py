import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load RAW data
df = pd.read_csv("../credit_risk_raw/credit_risk_dataset.csv")

# Drop duplicates
df = df.drop_duplicates()

# Handle missing values
for col in df.select_dtypes(include="object"):
    df[col].fillna(df[col].mode()[0], inplace=True)

for col in df.select_dtypes(include="number"):
    df[col].fillna(df[col].median(), inplace=True)

# Encoding categorical
encoder = LabelEncoder()
for col in df.select_dtypes(include="object"):
    df[col] = encoder.fit_transform(df[col])

# Scaling numeric
scaler = StandardScaler()
num_cols = df.select_dtypes(include="number").columns
df[num_cols] = scaler.fit_transform(df[num_cols])

# Save preprocessed dataset
df.to_csv("credit_risk_preprocessing.csv", index=False)

print("✅ Preprocessing otomatis selesai")

