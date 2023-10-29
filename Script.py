import psycopg2
import csv

def create_table(cursor, table_name, column_names):
    columns = ', '.join([f'"{name}" VARCHAR' for name in column_names])
    cursor.execute(f'CREATE TABLE {table_name} ({columns});')


def insert_data(cursor, table_name, column_names, data):
    columns = ', '.join(column_names)
    values_placeholder = ', '.join(['%s'] * len(column_names))
    cursor.executemany(
        f'INSERT INTO {table_name} ({columns}) VALUES ({values_placeholder});',
        data
    )

def main():
    # Database connection parameters
    params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'postgres',
        'host': '192.168.2.4',
        'port': '34567'
    }

    # Connect to the database
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()

    # Read the CSV file
    csv_file_path = 'data.csv'
    with open(csv_file_path, newline='', encoding='utf-8', errors='replace') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')  # assuming tab-delimited
        header = next(csv_reader)  # get the header row
        data = list(csv_reader)  # get the data rows

    header_str = ','.join(header)  # Join the header list into a single string
    # Create the table
    table_name = 'school_data'
    create_table(cursor, table_name, header_str)

    # Insert the data
    insert_data(cursor, table_name, header, data)

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()