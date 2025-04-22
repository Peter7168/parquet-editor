import pandas as pd
import os


def csv_to_parquet(csv_path, engine="pyarrow"):
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"File not found: {csv_path}")
    
    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Get same folder and file name
    base_dir = os.path.dirname(csv_path)
    base_name = os.path.splitext(os.path.basename(csv_path))[0]
    parquet_path = os.path.join(base_dir, f"{base_name}.parquet")

    # Save as Parquet
    df.to_parquet(parquet_path, engine=engine, index=False)
    print(f"Parquet saved at: {parquet_path}")
