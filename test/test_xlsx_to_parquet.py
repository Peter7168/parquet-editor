from src.convert_excel_to_parq import excel_to_parquet
import pytest


EXCEL_PATH = "data/test_excel.xlsx"

# Method to test the conversion of CSV to Parquet
def test_convert_csv_to_parquet():
    excel_to_parquet(EXCEL_PATH)

