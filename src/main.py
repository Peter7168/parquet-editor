import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from convert_csv_to_parq import csv_to_parquet
from convert_excel_to_parq import excel_to_parquet

class ParquetEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Parquet Editor")
        self.root.geometry("600x400")

        # Set up the main notebook (tab container)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Create the tabs
        self.home_tab = ttk.Frame(self.notebook)
        self.help_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.home_tab, text="Home")
        self.notebook.add(self.help_tab, text="Help")

        # Set up the Home tab UI
        self.setup_home_tab()

        # Set up the Help tab UI
        self.setup_help_tab()

    def setup_home_tab(self):
        # Add a title label to the Home tab
        label = tk.Label(self.home_tab, text="Welcome to Parquet Editor", font=("Arial", 16))
        label.pack(pady=20)

        # Create buttons for CSV to Parquet and Excel to Parquet
        csv_button = tk.Button(self.home_tab, text="CSV to Parquet", command=self.convert_csv)
        csv_button.pack(pady=10)

        excel_button = tk.Button(self.home_tab, text="Excel to Parquet", command=self.convert_excel)
        excel_button.pack(pady=10)

    def setup_help_tab(self):
        # Add a label for Help tab
        help_label = tk.Label(self.help_tab, text="This is the help section. TODO: ADD instructions here", justify="left", padx=10, pady=10)
        help_label.pack()

    def convert_csv(self):
        # Open a file dialog to select a CSV file
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            output_path = os.path.splitext(file_path)[0] + ".parquet"
            csv_to_parquet(file_path)
            print(f"CSV file converted to: {output_path}")

    def convert_excel(self):
        # Open a file dialog to select an Excel file
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xls;*.xlsx")])
        if file_path:
            output_path = os.path.splitext(file_path)[0] + ".parquet"
            excel_to_parquet(file_path) 
            print(f"Excel file converted to: {output_path}")


# Create the Tkinter window (root)
root = tk.Tk()

# Create the app object
app = ParquetEditorApp(root)

# Start the Tkinter main loop
root.mainloop()
