import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os


def excel_to_parquet(excel_path):
    # Load the Excel file
    xl = pd.ExcelFile(excel_path)
    
    # Find the sheet named "data" (case-insensitive)
    data_sheet_name = next((s for s in xl.sheet_names if s.lower() == "data"), None)
    
    if not data_sheet_name:
        raise ValueError("No sheet named 'data' found (case-insensitive match).")
    
    # Read the main data sheet
    df = xl.parse(data_sheet_name)

    # Collect metadata from other sheets
    metadata = {}
    for sheet in xl.sheet_names:
        if sheet.lower() != "data":
            sheet_df = xl.parse(sheet, header=None)
            if not sheet_df.empty:
                value = str(sheet_df.iat[0, 0])
                metadata[sheet] = value

    # Convert object columns to string to avoid ArrowTypeError
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str)

    # Convert DataFrame to Arrow Table
    table = pa.Table.from_pandas(df, preserve_index=False)



    # Attach metadata
    if metadata:
        # Convert dict to bytes
        meta_bytes = {k: str(v).encode("utf8") for k, v in metadata.items()}
        table = table.replace_schema_metadata(meta_bytes)

    # Define output path
    base = os.path.splitext(excel_path)[0]
    output_path = f"{base}.parquet"

    # Write Parquet file
    pq.write_table(table, output_path)
    print(f"Parquet file written to: {output_path}")
