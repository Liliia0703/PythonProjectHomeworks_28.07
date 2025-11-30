import csv
import json
import logging
import os
import xml.etree.ElementTree as ET

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

json_logger = logging.getLogger("json_logger")
json_logger.setLevel(logging.ERROR)

json_file_handler = logging.FileHandler("json_Markiv.log", encoding="utf-8")
json_logger.addHandler(json_file_handler)

RESULT_CSV = "result_Marko.csv"

def remove_csv_duplicates():
    folder = "ideas_for_test/work_with_csv"
    file1 = os.path.join(folder, "file1.csv")
    file2 = os.path.join(folder, "file2.csv")

    rows = []

    for file in [file1, file2]:
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(tuple(row))

    unique = set(rows)

    with open(RESULT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for row in unique:
            writer.writerow(row)


def validate_json_files():
    folder = "ideas_for_test/work_with_json"

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        try:
            with open(path, "r", encoding="utf-8") as f:
                json.load(f)

        except Exception as e:

            json_logger.error(f"{filename} — invalid JSON: {e}")


def find_incoming_value(group_number):
    path = "ideas_for_test/work_with_xml/groups.xml"

    tree = ET.parse(path)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number").text

        if number == str(group_number):
            incoming = group.find("timingExbytes/incoming").text
            logging.info(f"Group {group_number}: incoming = {incoming}")
            return

    logging.error("Group not found")

if __name__ == "__main__":
    remove_csv_duplicates()
    validate_json_files()
    find_incoming_value(155)