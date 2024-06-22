from pathlib import Path

current_directory = Path.cwd()

for item in current_directory.iterdir():
    print(f'{item} {item.is_file()} {item.is_dir()}')


current_directory = Path.cwd()
# Path(f'{current_directory}/nowy/text_dir').mkdir(exist_ok=True)
# Path(f'{current_directory}/nowy/text_nowy.txt').touch()

Path('plik.txt').touch()

# rzucenie wyjątkiem jeśli plik istnieje
Path('plik.txt').touch(exist_ok=False)
