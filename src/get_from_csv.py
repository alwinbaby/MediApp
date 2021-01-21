import csv
from pathlib import Path


def get_from_csv(file_name: str):
    path = Path(__file__).parent / f"../csv/{file_name}.csv"
    with path.open(newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = []
        for row in reader:
            rows.append([row[column] for column in reader.fieldnames])
        return rows
