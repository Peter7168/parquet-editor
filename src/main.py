import tkinter as tk
from tkinter import ttk, filedialog
import os
import threading
from convert_csv_to_parq import csv_to_parquet
from convert_excel_to_parq import excel_to_parquet


class ParquetEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Parquet Editor")
        self.root.geometry("600x450")
        self.root.resizable(True, True)

        self.root.configure(bg="#f5f5f5")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TNotebook.Tab", font=("Segoe UI", 11, "bold"), padding=[10, 5])
        style.configure("TButton", font=("Segoe UI", 10), padding=6)

        self.main_container = tk.Frame(self.root, bg="white")
        self.main_container.pack(fill="both", expand=True)

        self.loading_frame = None  # placeholder for loading overlay

        self.show_home_screen()

    def show_home_screen(self):
        self.clear_main_container()
        home_frame = tk.Frame(self.main_container, bg="white")
        home_frame.pack(fill="both", expand=True)

        title = tk.Label(
            home_frame,
            text="Welcome to Parquet Editor",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            fg="#333"
        )
        title.pack(pady=(20, 30))

        csv_button = ttk.Button(home_frame, text="Convert CSV to Parquet", command=self.convert_csv)
        csv_button.pack(pady=10, ipadx=10, ipady=4)

        excel_button = ttk.Button(home_frame, text="Convert Excel to Parquet (with metadata)", command=self.convert_excel)
        excel_button.pack(pady=10, ipadx=10, ipady=4)

        help_button = ttk.Button(home_frame, text="Help & Support", command=self.show_help_screen)
        help_button.pack(pady=10)

        footer = tk.Label(
            home_frame,
            text="Make sure your Excel sheet is named 'Data' for conversion.",
            font=("Segoe UI", 9),
            bg="white",
            fg="#777"
        )
        footer.pack(side="bottom", pady=20)

    def show_help_screen(self):
        self.clear_main_container()
        help_frame = tk.Frame(self.main_container, bg="white")
        help_frame.pack(fill="both", expand=True)

        help_title = tk.Label(
            help_frame,
            text="Help & Support",
            font=("Segoe UI", 14, "bold"),
            bg="white"
        )
        help_title.pack(anchor="w", pady=(20, 10), padx=30)

        help_text = (
            "\n- Report bugs or suggest features on GitHub:\n"
            "    https://github.com/Peter7168/parquet-editor\n\n"
            "- Ensure your files are properly formatted:\n\n"
            "• CSV: Plain table with rows and columns.\n"
            "• Excel: Sheet named 'Data' (case-insensitive).\n"
            "  Metadata sheets should contain metadata in cell A1.\n"
        )

        help_label = tk.Label(
            help_frame,
            text=help_text,
            font=("Segoe UI", 10),
            justify="left",
            wraplength=540,
            bg="white",
            fg="#444"
        )
        help_label.pack(anchor="w", padx=30)

        back_button = ttk.Button(help_frame, text="Back", command=self.show_home_screen)
        back_button.pack(pady=20)

    def show_success_screen(self, filetype, path):
        self.clear_main_container()
        success_frame = tk.Frame(self.main_container, bg="white")
        success_frame.pack(fill="both", expand=True)

        msg = tk.Label(
            success_frame,
            text=f"{filetype} file converted successfully!",
            font=("Segoe UI", 16, "bold"),
            fg="#228B22",
            bg="white"
        )
        msg.pack(pady=(60, 20))

        path_label = tk.Label(
            success_frame,
            text=f"Saved to:\n{path}",
            font=("Segoe UI", 10),
            fg="#444",
            bg="white",
            justify="center"
        )
        path_label.pack(pady=(0, 20))

        back_btn = ttk.Button(
            success_frame,
            text="Convert More Files",
            command=self.show_home_screen
        )
        back_btn.pack(pady=(0, 10), ipadx=10, ipady=4)

    def show_error_screen(self, error_message):
        self.clear_main_container()
        error_frame = tk.Frame(self.main_container, bg="white")
        error_frame.pack(fill="both", expand=True)

        error_msg = tk.Label(
            error_frame,
            text=f"Error: {error_message}",
            font=("Segoe UI", 16, "bold"),
            fg="#FF6347",  # Red color for error
            bg="white",
            wraplength=540,  # Set maximum width for text wrapping
            justify="center"
        )
        error_msg.pack(pady=(60, 20), padx=30)

        back_button = ttk.Button(
            error_frame,
            text="Convert Another File",
            command=self.show_home_screen
        )
        back_button.pack(pady=(0, 10), ipadx=10, ipady=4)


    def show_loading_screen(self):
        # Create a semi-transparent overlay by using a solid color for background
        self.loading_frame = tk.Frame(self.root, bg="#f5f5f5")  # Use a solid color here
        self.loading_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        loading_label = tk.Label(
            self.loading_frame,
            text="Converting file, please wait...",
            font=("Segoe UI", 12, "bold"),
            bg="#f5f5f5",  # Solid color background for label
            fg="#333"
        )
        loading_label.pack(pady=(150, 20))

        progress = ttk.Progressbar(self.loading_frame, mode='indeterminate', length=300)
        progress.pack()
        progress.start(10)

    def hide_loading_screen(self):
        if self.loading_frame:
            self.loading_frame.destroy()
            self.loading_frame = None

    def convert_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.show_loading_screen()
            threading.Thread(target=self._convert_csv_thread, args=(file_path,), daemon=True).start()

    def _convert_csv_thread(self, file_path):
        output_path = os.path.splitext(file_path)[0] + ".parquet"
        csv_to_parquet(file_path)
        self.root.after(0, lambda: (self.hide_loading_screen(), self.show_success_screen("CSV", output_path)))

    def convert_excel(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xls;*.xlsx")])
        if file_path:
            self.show_loading_screen()
            threading.Thread(target=self._convert_excel_thread, args=(file_path,), daemon=True).start()

    def _convert_excel_thread(self, file_path):
        try:
            output_path = os.path.splitext(file_path)[0] + ".parquet"
            excel_to_parquet(file_path)
            self.root.after(0, lambda: (self.hide_loading_screen(), self.show_success_screen("Excel", output_path)))
        except ValueError as e:
            # If Excel conversion fails, show error message in the UI
            self.root.after(0, lambda e=e: (self.hide_loading_screen(), self.show_error_screen(str(e))))


    def clear_main_container(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ParquetEditorApp(root)
    root.mainloop()
