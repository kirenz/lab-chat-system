import csv
import os

# Define:
lab_name = "lab-chat-system"
github_folder = "code"
output_filename = "output.csv"


def list_notebook_files(directory="code"):
    # List all files in the given directory
    files = os.listdir(directory)

    # Filter out only .ipynb files
    notebook_files = [file for file in files if file.endswith('.ipynb')]

    return notebook_files


# Usage:
notebook_files = list_notebook_files()


def generate_csv(lab_name, github_folder, notebook_files, output_filename):
    # Initialize list to store data rows
    data = []
    header = ["nr", "lab", "github", "name", "colab", "link"]
    data.append(header)

    base_url = "https://colab.research.google.com/github/kirenz/{}/blob/main/{}/{} "

    # Loop through each notebook file and generate the required data
    for idx, file in enumerate(notebook_files, start=1):
        colab_link = base_url.format(lab_name, github_folder, file)
        markdown_link = "- [💻 {}]({})".format(file, colab_link)

        row = [idx, lab_name, github_folder, file, colab_link, markdown_link]
        data.append(row)

    # Write the data to the CSV file
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


generate_csv(lab_name, github_folder, notebook_files, output_filename)
