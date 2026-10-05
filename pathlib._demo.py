from pathlib import Path

file_path = Path("example.txt")

if not file_path.exists():
    file_path.touch()
    print(f"{file_path} Created.")

if file_path.exists():
    print(f"{file_path} exists")