
# Command to generate .exe with icon
pyinstaller --onefile --windowed --icon=src/icon/icon.ico --add-data "src/icon/icon.ico;src/icon" src/main.py

pyinstaller --onefile --windowed --icon=src/icon/icon.ico --add-data "src/icon/icon.ico;src/icon" --paths=src src/main.py

