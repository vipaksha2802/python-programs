import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # Read CSV file
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each CSV row into a dictionary
        for row in csvReader:
            jsonArray.append(row)

    # Write data to JSON file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


# File paths
csvFilePath = 'data.csv'
jsonFilePath = 'data.json'

# Convert CSV to JSON
csv_to_json(csvFilePath, jsonFilePath)

print("CSV file successfully converted to JSON.")