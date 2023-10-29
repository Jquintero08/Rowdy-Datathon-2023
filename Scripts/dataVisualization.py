from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

# Database connection parameters
host = '10.0.0.40'
port = '34567'
database = 'postgres'
username = 'postgres'
password = 'postgres'

# Connection string
connection_string = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string)

# Querying the data
query = "SELECT district_total, total_title1_enrolled FROM school_summary"
df = pd.read_sql(query, engine)

# Remove data points where the district population is less than 100
df = df[df['district_total'] >= 100]

# Constrain 'total_title1_enrolled' to be between 1 (to exclude 0) and 100,000
df = df[(df['total_title1_enrolled'] > 0) & (df['total_title1_enrolled'] <= 100000)]

# Remove the top 10 extreme values for 'district_total' and 'total_title1_enrolled'
sorted_district = df['district_total'].sort_values(ascending=False).iloc[10:]
sorted_title1 = df['total_title1_enrolled'].sort_values(ascending=False).iloc[10:]

df_filtered = df[df['district_total'].isin(sorted_district) & df['total_title1_enrolled'].isin(sorted_title1)]

# Visualizing the data
plt.figure(figsize=(10,6))
plt.scatter(df_filtered['total_title1_enrolled'], df_filtered['district_total'], alpha=0.6, edgecolors="w", linewidth=0.5)
plt.xlabel('District Total')
plt.ylabel('Students in Poverty')
plt.title('Impoverished Students vs District Density (Filtered Data)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Display the plot
plt.tight_layout()
plt.show()