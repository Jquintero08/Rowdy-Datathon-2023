
from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import sqlite3

# PostgreSQL connection settings
host = '127.0.0.1'
port = '5432'
database = 'postgres'
username = 'postgres'
password = 'postgres'

# CSV file settings
csv_file1 = "E:/Filtered Data/LEA1 Filtered.csv"
csv_file2 = "E:/Filtered Data/Title 1 Status Filtered.csv"
csv_file3 = "E:/Filtered Data/Enrollment Filtered.csv"
encoding = 'iso-8859-1'

# Create a SQLAlchemy database engine
db_url1 = f'postgresql://{username}:{password}@{host}:{port}/{database}'
engine1 = create_engine(db_url1)
db_url2 = f'postgresql://{username}:{password}@{host}:{port}/{database}'
engine2 = create_engine(db_url2)
db_url3 = f'postgresql://{username}:{password}@{host}:{port}/{database}'
engine3 = create_engine(db_url3)
# Read the CSV data using pandas
df1 = pd.read_csv(csv_file1, encoding=encoding)
df2 = pd.read_csv(csv_file2, encoding=encoding)
df3 = pd.read_csv(csv_file3, encoding=encoding)
# Define the target table name
table_name1= 'school_data'
table_name2='poverty'
table_name3='enrollment'
# Use the `df.to_sql` method to create the table and load data
df1.to_sql(name=table_name1, con=engine1, if_exists='replace', index=False)
df2.to_sql(name=table_name2, con=engine2, if_exists='replace', index=False)
df3.to_sql(name=table_name3, con=engine3, if_exists='replace', index=False)
print(f"Table '{table_name1}' created and data loaded successfully.")
print(f"Table '{table_name2}' created and data loaded successfully.")
print(f"Table '{table_name3}' created and data loaded successfully.")
# PostgreSQL connection

conn_postgres = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=username,
    password=password
)

cursor = conn_postgres.cursor()


query1 = "SELECT * FROM school_data"
cursor.execute(query1)
data1 = cursor.fetchall()


df1 = pd.DataFrame(data1)
print(df1)

query2 = "SELECT * FROM poverty"
cursor.execute(query2)
data2 = cursor.fetchall()


df2 = pd.DataFrame(data2)
print(df2)



query3 = "SELECT * FROM enrollment"
cursor.execute(query3)
data3 = cursor.fetchall()


df3 = pd.DataFrame(data3)
print(df3)

# Close connections
cursor.close()

conn_postgres.close()
