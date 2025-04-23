import csv

data = {}
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = sum(int(row[f"Subject{i}"]) for i in range(1, 4))
        data[row["Roll No"]] = {
            "name": row["Name"],
            "marks": [int(row[f"Subject{i}"]) for i in range(1, 4)],
            "total": total
        }

print("Student Data:", data)
