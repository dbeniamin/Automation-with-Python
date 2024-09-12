# Parsing data with python in various format files data
import csv
import json
import xml.etree.ElementTree as ET

# .txt file parsing
filepath = "groceries.txt"
# reading and closing the file
with open(filepath, "r")as file_txt:
    data = file_txt.read()

print("data:", data)
# transfer to a list and split at spaces
parsed_data = data.split(" ")
print("parsed data:", parsed_data)
# extracting items at various index in the generated list
print("item at index 2:", parsed_data[2])


# .csv file parsing
# the path can be directly accessed in the with syntax

# file_path = "groceries.csv"
with open("groceries.csv", "r") as file_csv:
    csv_reader = csv.reader(file_csv)
    headers = next(csv_reader)
    for row in csv_reader:
        row[1] = int(row[1])
        print(row)


# .json file parsing
# the path can be directly accessed in the with syntax

file_path = "groceries.json"

with open("groceries.json", "r") as file_json:
    data = file_json.read()
parsed_data = json.loads(data)

print("apples quant:", parsed_data["apples"])


# .xml file parsing

file_path_xml = "groceries.xml"
tree = ET.parse(file_path_xml)
root = tree.getroot()

for item in root.findall("grocery_item"):
    name = item.find("name").text
    price = item.find("price").text
    print(name, price)
