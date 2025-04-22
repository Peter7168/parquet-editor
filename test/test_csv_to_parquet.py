from src.convert_csv_to_parq import csv_to_parquet
import pytest


CSV_PATH = "data/test_csv.csv"

# Method to test the conversion of CSV to Parquet
def test_convert_csv_to_parquet():
    csv_to_parquet(CSV_PATH)

