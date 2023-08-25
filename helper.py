import os
import json
import glob
from pathlib import Path


# CONVERT
# Convert files from .qmd to .ipynb
for i in glob.iglob('slides/*.qmd'):
    os.system(f"quarto convert {i}")


# MOVE FILES
source_folder = Path('slides/')
destination_folder = Path('code/')
# Alle .ipynb Dateien im Quellordner durchlaufen
for filepath in source_folder.glob('*.ipynb'):
    # Ziel-Pfad konstruieren
    destination = destination_folder / filepath.name
    # Datei verschieben
    filepath.rename(destination)


# REPLACE . . .
folder_path = Path('code/')
# Alle .ipynb Dateien im Ordner durchlaufen
for file_path in folder_path.glob('*.ipynb'):
    with file_path.open('r', encoding='utf-8') as file:
        notebook_content = json.load(file)

    # Durch alle Zellen im Notebook gehen
    for cell in notebook_content['cells']:
        # Ersetze ". . ." durch "" in der Zelle, wenn es sich um eine Textzelle handelt
        if cell['cell_type'] == 'markdown':
            cell['source'] = [line.replace('. . .', '')
                              for line in cell['source']]

    # Den modifizierten Inhalt zurück in die Datei schreiben
    with file_path.open('w', encoding='utf-8') as file:
        json.dump(notebook_content, file, ensure_ascii=False, indent=4)


# REPLACE YAML
folder_path = Path('code/')
# Iterate over all .ipynb files in the folder
for file_path in folder_path.glob('*.ipynb'):
    with file_path.open('r', encoding='utf-8') as file:
        notebook_content = json.load(file)

    # Find and remove the first markdown cell
    for index, cell in enumerate(notebook_content['cells']):
        if cell['cell_type'] == 'raw':
            del notebook_content['cells'][index]
            break

    # Write the modified content back to the file
    with file_path.open('w', encoding='utf-8') as file:
        json.dump(notebook_content, file, ensure_ascii=False, indent=4)
