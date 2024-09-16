import os
from pathlib import Path
import subprocess

# File manipulation


# open a text file in read mode -- allows to read the file and not write it
read_file = open("01_parse_data/inputFile.txt", "r")
# after opening the file print the file using .read()
print(read_file.read())

for line in read_file:
    split_lines = line.split()
    if split_lines[2] == "P":
        print(line)
read_file.close()

# Approach 1 - classic open mode
# open a text file in write mode -- allows to read and write the file
read_file = open("01_parse_data/inputFile.txt", "w")

# create files that will be used with the script
pass_file = open("passFile.txt", "w")
fail_file = open("failFile.txt", "w")

# loop in the file to find pass and failed
for line in read_file:
    split_lines = line.split()
    if split_lines[2] == "P":
        # write passed in the new above created file
        pass_file.write(line)
    else:
        # write failed in the new above created file
        fail_file.write(line)
read_file.close()
pass_file.close()
fail_file.close()

# Approach 2 - with Keyword
# a mode to append - otherwise it will just write the first line

with open("01_parse_data/inputFile.txt", "r") as source_file:
    for line in source_file:
        split_lines = line.split()
        print(split_lines)
        if split_lines[2] == 'P':
            with open("pass_file_1.txt", "a") as pass_2:
                pass_2.write(line)
        else:
            with open("fail_file_1.txt", "a") as fail_2:
                fail_2.write(line)

# in pycharm using the python3 arg returns a subprocess.CalledProcessError: Command '['python3', 'example.py']'
# returned non-zero exit status 9009. using a venv setup with python3 interpreter setup locally leads to changing
# all the calls made with python3 in the course to simply python

# check_call func usage
for i in range(5):
    subprocess.check_call(["python", "example.py"])


# Organize folders

SUB_DIRS = {
    "Documents": [".pdf", ".rtf", ".txt"],
    "Audio": [".m4a", ".m4b", ".mp3"],
    "Video": [".mov", ".avi", ".mp4"],
    "Images": [".jpg", ".jpeg", ".png"]
}


def choose_dir(value):
    # use suffixes keyword to access the data stored in the list that is value for dictionary keys
    for category, suffixes in SUB_DIRS.items():
        if value in suffixes:
            return category
    return "Misc"


# print(choose_dir(".txt"))  # print statement to check the function

# PEP8 naming errors will appear if items are named with capital letter in the middle of the name
def organize_dir():
    for item in os.scandir():
        if item.is_dir():
            continue
        file_path = Path(item)
        file_type = file_path.suffix
        directory = choose_dir(file_type)
        directory_path = Path(directory)
        # Check if the item is a directory
        # flip the statement for PEP8 standards
        if not directory_path.is_dir():
            directory_path.mkdir()
        # file path is updated to include the new dir path
        file_path.rename(directory_path.joinpath(file_path))


organize_dir()
