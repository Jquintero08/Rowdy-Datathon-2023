import pandas as pd

# List of possible encodings to try
encodings = ['iso-8859-1']

# Replace 'your_input.csv' with the name of your input CSV file
input_file = "E:/Data-20231026T061813Z-001/Data/2017-18-crdc-data/2017-18 Public-Use Files/Data/SCH/CRDC/CSV/Enrollment.csv"

# Initialize DataFrame as None
df = None

# Try reading the CSV file with different encodings
for encoding in encodings:
    try:
        df = pd.read_csv(input_file, encoding=encoding)
        break  # If successful, exit the loop
    except UnicodeDecodeError:
        pass  # Try the next encoding if decoding fails

if df is None:
    print("Failed to read the CSV file. Please check the file encoding.")
else:
    # Loop through columns and apply the filtering logic
    for col in df.columns:
        for i, value in enumerate(df[col]):
            try:
                numeric_value = float(value)
                if numeric_value < 0:
                    df.at[i, col] = None
            except (ValueError, TypeError):
                pass  # Ignore non-numeric values

    # Replace 'filteredData.csv' with the name of the output CSV file
    output_file = 'filteredData.csv'

    # Save the modified data to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Filtered data saved to {output_file}")