import tkinter as tk
from tkinter import ttk, filedialog
import os
from convert_csv_to_parq import csv_to_parquet
from convert_excel_to_parq import excel_to_parquet


class ParquetEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Parquet Editor")
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        # Styling
        self.root.configure(bg="#f5f5f5")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TNotebook.Tab", font=("Segoe UI", 11, "bold"), padding=[10, 5])
        style.configure("TButton", font=("Segoe UI", 10), padding=6)

        # Notebook setup
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.home_tab = ttk.Frame(self.notebook)
        self.help_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.home_tab, text="Home")
        self.notebook.add(self.help_tab, text="Help")

        self.setup_home_tab()
        self.setup_help_tab()

    def setup_home_tab(self):
        home_frame = tk.Frame(self.home_tab, bg="white")
        home_frame.pack(expand=True, fill="both", padx=40, pady=40)

        title = tk.Label(
            home_frame,
            text="Welcome to Parquet Editor",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            fg="#333"
        )
        title.pack(pady=(10, 30))

        # Buttons
        csv_button = ttk.Button(home_frame, text="Convert CSV to Parquet", command=self.convert_csv)
        csv_button.pack(pady=10, ipadx=10, ipady=4)

        excel_button = ttk.Button(home_frame, text="Convert Excel to Parquet (with metadata)", command=self.convert_excel)
        excel_button.pack(pady=10, ipadx=10, ipady=4)

        footer = tk.Label(
            home_frame,
            text="Make sure your Excel sheet is named 'Data' for conversion.",
            font=("Segoe UI", 9),
            bg="white",
            fg="#777"
        )
        footer.pack(side="bottom", pady=20)

    def setup_help_tab(self):
        help_frame = tk.Frame(self.help_tab, bg="white")
        help_frame.pack(fill="both", expand=True, padx=30, pady=30)

        help_title = tk.Label(
            help_frame,
            text="Help & Support",
            font=("Segoe UI", 14, "bold"),
            bg="white",
            anchor="w"
        )
        help_title.pack(anchor="w", pady=(0, 10))

        help_text = (
            " \n\n-  To report bugs or suggest features, please open an issue on the GitHub repo:\n"
            "       https://github.com/Peter7168/parquet-editor  \n\n"
            "- Ensure your files are properly formatted before conversion:\n\n"
            "• CSV: No restrictions, all data in a column format in one sheet (No metadata customization).\n\n"
            "• Excel: One sheet named 'Data' (case-insensitive) for columnar data.\n"
            "  Metadata should be formatted as follows:\n"
            "  - Each sheet name represents a metadata tab in the output Parquet file.\n"
            "  - The metadata value should be written in the first cell (A1) of each sheet.\n\n"
            
        )

        help_label = tk.Label(
            help_frame,
            text=help_text,
            font=("Segoe UI", 10),
            justify="left",
            wraplength=500,  # wrap text at 500 pixels
            bg="white",
            fg="#444"
        )
        help_label.pack(anchor="w")


    def convert_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            output_path = os.path.splitext(file_path)[0] + ".parquet"
            csv_to_parquet(file_path)
            self._show_success("CSV", output_path)

    def convert_excel(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xls;*.xlsx")])
        if file_path:
            output_path = os.path.splitext(file_path)[0] + ".parquet"
            excel_to_parquet(file_path)
            self._show_success("Excel", output_path)

    def _show_success(self, filetype, path):
        success_win = tk.Toplevel(self.root)
        success_win.title("Success")
        success_win.geometry("400x120")
        success_win.resizable(False, False)
        tk.Label(success_win, text=f"{filetype} file converted successfully!", font=("Segoe UI", 12)).pack(pady=(20, 10))
        tk.Label(success_win, text=f"Saved to:\n{path}", font=("Segoe UI", 9), fg="#555").pack(pady=(0, 10))
        ttk.Button(success_win, text="OK", command=success_win.destroy).pack(pady=(0, 10))


if __name__ == "__main__":
    root = tk.Tk()
    app = ParquetEditorApp(root)
    root.mainloop()
