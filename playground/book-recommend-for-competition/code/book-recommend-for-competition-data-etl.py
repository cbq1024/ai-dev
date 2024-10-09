import pandas as pd
from pathlib2 import Path


def process_xlsx_to_csv(xlsx_file, output_dir):
    """
    将 xlsx 处理为 csv
    :param xlsx_file:  xlsx_file
    :param output_dir: a directory to save csv file
    """
    df = pd.read_excel(xlsx_file, engine='openpyxl')

    df.columns = df.columns.str.strip()
    df = df.dropna().drop_duplicates(keep='first')

    output_file = output_dir / f"{xlsx_file.stem}.csv"
    df.to_csv(output_file, index=False, encoding='utf-8')

    print(f"Saved {output_file}")


def main():
    root_path = Path(__file__).resolve().parents[1]
    source_data_path = root_path / "data" / "uncleaned"
    cleand_data_path = root_path / "data" / "cleaned"

    for xlsx_file in source_data_path.glob("*.xlsx"):
        process_xlsx_to_csv(xlsx_file, cleand_data_path)


if __name__ == "__main__":
    main()
