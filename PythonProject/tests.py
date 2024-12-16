import pandas as pd
# Sample data
data = {'Sales week start date': ['2024-01-01', '2024-01-08', '2024-01-15']}
df = pd.DataFrame(data)

# Convert to datetime
df['Sales week start date'] = pd.to_datetime(df['Sales week start date'])

# Verify conversion
print(df.dtypes)