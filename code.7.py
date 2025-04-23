import pickle

class Employee:
    def __init__(self, code, name, doj, salary):
        self.empcode = code
        self.empname = name
        self.doj = doj
        self.salary = salary

emp = Employee("E001", "Alice", "2023-01-01", 50000)

# Serialize
with open("employee.dat", "wb") as f:
    pickle.dump(emp, f)

# Deserialize
with open("employee.dat", "rb") as f:
    loaded_emp = pickle.load(f)

print("Deserialized Employee:", vars(loaded_emp))
