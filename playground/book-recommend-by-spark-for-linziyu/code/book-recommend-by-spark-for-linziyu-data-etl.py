import numpy as np
import pandas as pd
from pathlib2 import Path


def date_covert(data):
    try:
        converted_date = pd.to_datetime(data, format="%m/%d/%Y")
        return converted_date.strftime("%Y-%m-%d")
    except ValueError:
        return np.nan


def process_data(input_dir, output_dir):
    df = pd.read_csv(input_dir, on_bad_lines='skip')

    df.columns = df.columns.str.strip()
    df['publication_date'] = df['publication_date'].apply(lambda x: date_covert(x))
    df = df.dropna().drop_duplicates(keep='first')

    output_file = output_dir / f"{input_dir.stem}.csv"
    print(df['language_code'].unique())
    df.to_csv(output_file, index=False, encoding='utf-8')

    print(f"Saved {output_file}")


def main():
    root_path = Path(__file__).resolve().parents[1]
    source_data_path = root_path / "data" / "uncleaned"
    cleand_data_path = root_path / "data" / "cleaned"

    for file in source_data_path.glob("*.csv"):
        process_data(file, cleand_data_path)


if __name__ == "__main__":
    main()
