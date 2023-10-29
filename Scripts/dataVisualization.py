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

# Visualizing the data
plt.figure(figsize=(10,6))
plt.scatter(df['district_total'], df['total_title1_enrolled'], alpha=0.6, edgecolors="w", linewidth=0.5)
plt.xlabel('District Total')
plt.ylabel('Students in Poverty')
plt.title('Impoverished Students vs District Density')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Display the plot
plt.tight_layout()
plt.show()