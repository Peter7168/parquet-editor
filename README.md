# Parquet Editor (UNDER DEVELOPMENT)

Parquet Editor is a lightweight desktop application that converts CSV or Excel files into Parquet format. It allows users to **embed custom metadata** into the Parquet files when converting **Excel files**, making it a powerful tool for generating structured and enriched Parquet files with personalized metadata for various use cases.

## What It Does

- **CSV to Parquet Conversion**: Converts CSV files into Parquet format. The output contains only the data from the CSV without any additional metadata.

- **Excel to Parquet Conversion (with Custom Metadata)**: Converts Excel files with the following structure:
  - A sheet named `Data` (case-insensitive) contains the main table data.
  - **Other sheets in the Excel file are used as custom metadata.** Each sheet name becomes a metadata key, and the value in cell `A1` of each sheet is used as the corresponding metadata value.
  - This allows users to embed **custom metadata** directly into the Parquet file, enhancing its structure and making it ready for more complex data workflows.

## Supported File Types

| File Type | Extension        |Custom Metadata Support     |
|-----------|------------------|----------------------------|
| CSV       | `.csv`           | No                         |
| Excel     | `.xlsx`, `.xls`  | Yes       |

## Key Features

- **Custom Metadata**: Easily embed custom metadata into Parquet files by converting Excel files where each sheet represents a metadata entry. The metadata content is taken from the first cell (`A1`) of each sheet and is stored as key-value pairs in the Parquet file schema.
  
- **CSV to Parquet**: Simple conversion from CSV to Parquet with no metadata included, ideal for straightforward data storage.

- **Easy to Use**: A user-friendly GUI that allows for seamless file selection and conversion without needing technical expertise.

## Help and Support

To report bugs or request features, open an issue at:  
[https://github.com/Peter7168/parquet-editor](https://github.com/Peter7168/parquet-editor)

## Technical Overview

- **GUI**: Built with **Tkinter** for a lightweight, user-friendly desktop interface.
- **File Processing**: Conversion and metadata embedding powered by **Pandas** and **PyArrow**.
- **Standalone**: Packaged into a self-contained `.exe` using **PyInstaller**, so no Python installation is required to run the application.

## Notes

- The application allows users to convert files quickly while adding custom metadata, which can be helpful for data management, testing, and generating custom datasets.
- No external dependencies are required to run the executable—just launch and use!
