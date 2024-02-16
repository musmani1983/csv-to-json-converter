import csv
import json


def csv_to_json(csv_file, json_file):
    # Read CSV file and convert it to JSON
    data = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    # Write data to JSON file
    with open(json_file, 'w') as jsonfile:
        jsonfile.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    csv_file = input("Enter the CSV file name: ")
    json_file = input("Enter the JSON file name (output): ")

    csv_to_json(csv_file, json_file)
    print(f"Conversion from {csv_file} to {json_file} is complete.")
