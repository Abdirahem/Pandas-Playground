import pandas as pd

# 0) Load the CSV
path = "people100.csv"
df = pd.read_csv(path)

# 1) Quick preview
df.head(10)

# 2) Size of the dataset (rows, columns)
df.shape

# 3) Column names
df.columns.tolist()

# 4) Data types + missing values per column
pd.DataFrame({
    "column": df.columns,
    "dtype": [df[c].dtype for c in df.columns],
    "non_null": [df[c].notna().sum() for c in df.columns],
    "nulls": [df[c].isna().sum() for c in df.columns],
})

# 5) Missing values summary (sorted)
df.isna().sum().sort_values(ascending=False)

# 6) Duplicate rows count
df.duplicated().sum()

# 7) Numeric summary (only numeric columns)
df.select_dtypes(include=["number"]).describe()

# 8) Value counts for categorical columns (top 10)
cat_cols = [c for c in df.columns if df[c].dtype == "object"]
for c in cat_cols:
    print("\n", c)
    print(df[c].value_counts(dropna=False).head(10))

# 9) Convert Date of birth to datetime
df["Date of birth"] = pd.to_datetime(df["Date of birth"], errors="coerce")

# 10) Create Age column (based on 2026-01-02)
today = pd.Timestamp("2026-01-02")
df["Age"] = ((today - df["Date of birth"]).dt.days / 365.25).round(1)

df[["First Name","Last Name","Sex","Date of birth","Age","Job Title"]].head(10)

# 11) Age statistics overall
df["Age"].describe()

# 12) Age statistics by Sex
df.groupby("Sex")["Age"].agg(["count","mean","median","min","max"]).round(1)

# 13) Most common job titles
df["Job Title"].value_counts().head(15)

# 14) Check uniqueness of key identifiers
pd.DataFrame({
    "field": ["User Id", "Email", "Phone"],
    "unique_values": [df["User Id"].nunique(), df["Email"].nunique(), df["Phone"].nunique()],
    "total_rows": [len(df)]*3
})

df.info()
