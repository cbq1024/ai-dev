import pandas as pd
from pathlib2 import Path


# Define the function to process xlsx files and save them as csv
def process_xlsx_to_csv(xlsx_file, output_dir):
    # Read the Excel file
    df = pd.read_excel(xlsx_file, engine='openpyxl')

    # Clean the dataframe
    df.columns = df.columns.str.strip()
    df = df.dropna().drop_duplicates(keep='first')

    # Define output CSV file path
    output_file = output_dir / f"{xlsx_file.stem}.csv"

    # Save the dataframe to CSV
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Saved {output_file}")


# Define the main function to iterate over all .xlsx files in a directory
def main():
    root_path = Path(__file__).resolve().parents[1]
    work_path = root_path / "books"
    data_path = root_path / "data" / "books"

    # Iterate through all .xlsx files in the work_path directory
    for xlsx_file in data_path.glob("user_*.xlsx"):
        process_xlsx_to_csv(xlsx_file, work_path)


# Call the main function when script is executed
if __name__ == "__main__":
    main()
