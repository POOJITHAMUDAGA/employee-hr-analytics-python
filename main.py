employees = [
    {
        "Id": "E001",
        "Name": "Joshvin",
        "Department": "Finance",
        "Designation": "Financial Analyst",
        "Experience": 3,
        "Basic_Salary": 35000
    },
    {
        "Id": "E002",
        "Name": "Gagana Anvika",
        "Department": "Marketing",
        "Designation": "Sales Executive",
        "Experience": 2,
        "Basic_Salary": 30000
    },
    {
        "Id": "E003",
        "Name": "Bharani",
        "Department": "IT",
        "Designation": "Python Developer",
        "Experience": 4,
        "Basic_Salary": 40000
    },
    {
        "Id": "E004",
        "Name": "Bhargavi",
        "Department": "IT",
        "Designation": "Java Developer",
        "Experience": 5,
        "Basic_Salary": 50000
    },
    {
        "Id": "E005",
        "Name": "Sreenivas",
        "Department": "HR",
        "Designation": "HR Analyst",
        "Experience": 6,
        "Basic_Salary": 43000
    },
    {
        "Id": "E006",
        "Name": "Gowthami",
        "Department": "Finance",
        "Designation": "Accountant",
        "Experience": 4,
        "Basic_Salary": 40000
    },
    {
        "Id": "E007",
        "Name": "Arjun",
        "Department": "HR",
        "Designation": "HR Analyst",
        "Experience": 5,
        "Basic_Salary": 45000
    },
    {
        "Id": "E008",
        "Name": "Aditi",
        "Department": "Marketing",
        "Designation": "Sales Executive",
        "Experience": 6,
        "Basic_Salary": 46000
    },
    {
        "Id": "E009",
        "Name": "Vikram",
        "Department": "IT",
        "Designation": "Python Developer",
        "Experience": 3,
        "Basic_Salary": 34000
    },
    {
        "Id": "E010",
        "Name": "Ashok",
        "Department": "Marketing",
        "Designation": "Sales Executive",
        "Experience": 2,
        "Basic_Salary": 29000
    }
]

print(employees)
print("\nEMPLOYEE HR ANALYTICS")
print("-" * 50)

for employee in employees :
    print(f"ID: {employee['Id']}")
    print(f"Name:{employee['Name']}")
    print(f"Department:{employee['Department']}")
    print(f"Designation:{employee['Designation']}")
    print(f"Experience:{employee['Experience']} years")
    print(f"Basic Salary:{employee['Basic_Salary']}/-")
    print("-" * 50)
# HR Analytics

total_employees = len(employees)

total_salary = sum(employee["Basic_Salary"]for employee in employees)
average_salary = total_salary / total_employees

print("\nHR ANALYTICS SUMMARY")
print("-" * 50)
print(f"Total Employees :{total_employees}")
print(f"Average Salary :{average_salary: .2f}/-")

#Department - wise Employee Count

department_count = {}

for employee in employees :
    department = employee["Department"]
    if department in department_count : department_count[department]+= 1
    else:
        department_count[department]= 1

print("\nDEPARTMENT - WISE EMPLOYEE COUNT")
print("-" * 50)
for department, count in department_count.items() :
 print(f"{department}:{count}")

#Highest and Lowest Salary

highest_salary_employee = max(employees, key=lambda x: x["Basic_Salary"])
lowest_salary_employee =  min(employees, key=lambda x: x["Basic_Salary"])
print("\nSALARY ANALYSIS")
print("-" * 50)

print(f"Highest Salary:{highest_salary_employee['Name']} - /- {highest_salary_employee['Basic_Salary']}")
print(f"Lowest Salary:{lowest_salary_employee['Name']} - /- {lowest_salary_employee['Basic_Salary']}")

# Average Salary by Department

department_salary = {}
department_count_salary = {}

for employee in employees:
    department = employee["Department"]
    salary = int(employee["Basic_Salary"])

    if department in department_salary:
        department_salary[department] += salary
        department_count_salary[department] += 1
    else:
        department_salary[department] = salary
        department_count_salary[department] = 1

print("\nAVERAGE SALARY BY DEPARTMENT")
print("-" * 50)

for department in department_salary:
    average = department_salary[department] / department_count_salary[department]
    print(f"{department}: ₹{average:.2f}")

    print("\nEMPLOYEE SEARCH")
print("-" * 50)

search_id = input("Enter Employee ID: ")

found = False

for employee in employees:
    if employee["Id"] == search_id:
        print("\nEmployee Found")
        print("-" * 30)
        print(f"ID: {employee['Id']}")
        print(f"Name: {employee['Name']}")
        print(f"Department: {employee['Department']}")
        print(f"Designation: {employee['Designation']}")
        print(f"Experience: {employee['Experience']} years")
        print(f"Basic Salary: ₹{employee['Basic_Salary']}")
        found = True
        break

if not found:
    print("Employee ID not found.")

    print("\nDEPARTMENT SEARCH")
print("-" * 50)

search_department = input("Enter Department: ")

found = False

for employee in employees:
    if employee["Department"].lower() == search_department.lower():
        print(f"\nID: {employee['Id']}")
        print(f"Name: {employee['Name']}")
        print(f"Designation: {employee['Designation']}")
        print(f"Experience: {employee['Experience']} years")
        print(f"Basic Salary: ₹{employee['Basic_Salary']}")
        print("-" * 30)
        found = True

if not found:
    print("Department not found.")

    print("\nSALARY RANGE SEARCH")
print("-" * 50)

min_salary = int(input("Enter minimum salary: "))
max_salary = int(input("Enter maximum salary: "))

found = False

for employee in employees:
    salary = int(employee["Basic_Salary"])

    if min_salary <= salary <= max_salary:
        print(f"\nID: {employee['Id']}")
        print(f"Name: {employee['Name']}")
        print(f"Department: {employee['Department']}")
        print(f"Designation: {employee['Designation']}")
        print(f"Basic Salary: ₹{salary}")
        print("-" * 30)
        found = True

if not found:
    print("No employees found in this salary range.")

    # Experience-wise Analysis

print("\nEXPERIENCE ANALYSIS")
print("-" * 50)

total_experience = sum(employee["Experience"] for employee in employees)
average_experience = total_experience / len(employees)

print(f"Average Experience: {average_experience:.2f} years")

experienced_employees = [
    employee for employee in employees
    if employee["Experience"] >= 5
]

print("\nEmployees with 5+ Years Experience")
print("-" * 50)

for employee in experienced_employees:
    print(
        f"{employee['Name']} - "
        f"{employee['Experience']} years - "
        f"{employee['Designation']}"
    )

    # Experience-wise Salary Analysis

print("\nEXPERIENCE-WISE SALARY ANALYSIS")
print("-" * 50)

experience_salary = {}

for employee in employees:
    experience = employee["Experience"]
    salary = employee["Basic_Salary"]

    if experience not in experience_salary:
        experience_salary[experience] = []

    experience_salary[experience].append(salary)

for experience, salaries in sorted(experience_salary.items()):
    average_salary = sum(salaries) / len(salaries)
    print(f"{experience} years: ₹{average_salary:.2f}")

    # Salary Range Analysis

print("\nSALARY RANGE ANALYSIS")
print("-" * 50)

salary_ranges = {
    "Below ₹30,000": 0,
    "₹30,000 - ₹39,999": 0,
    "₹40,000 - ₹49,999": 0,
    "₹50,000 and above": 0
}

for employee in employees:
    salary = employee["Basic_Salary"]

    if salary < 30000:
        salary_ranges["Below ₹30,000"] += 1
    elif salary < 40000:
        salary_ranges["₹30,000 - ₹39,999"] += 1
    elif salary < 50000:
        salary_ranges["₹40,000 - ₹49,999"] += 1
    else:
        salary_ranges["₹50,000 and above"] += 1

for salary_range, count in salary_ranges.items():
    print(f"{salary_range}: {count} employees")

    # Experience and Salary Comparison

print("\nEXPERIENCE & SALARY COMPARISON")
print("-" * 50)

for employee in employees:
    if employee["Experience"] >= 4 and employee["Basic_Salary"] < 40000:
        print(
            f"{employee['Name']} - "
            f"{employee['Experience']} years - "
            f"₹{employee['Basic_Salary']}"
        )

        # Designation-wise Salary Analysis

print("\nDESIGNATION-WISE SALARY ANALYSIS")
print("-" * 50)

designation_salary = {}

for employee in employees:
    designation = employee["Designation"]
    salary = employee["Basic_Salary"]

    if designation not in designation_salary:
        designation_salary[designation] = []

    designation_salary[designation].append(salary)

for designation, salaries in designation_salary.items():
    average_salary = sum(salaries) / len(salaries)
    print(f"{designation}: ₹{average_salary:.2f}")

    # Department-wise Salary Analysis

print("\nDEPARTMENT-WISE SALARY ANALYSIS")
print("-" * 50)

department_salary = {}

for employee in employees:
    department = employee["Department"]
    salary = employee["Basic_Salary"]

    if department not in department_salary:
        department_salary[department] = []

    department_salary[department].append(salary)

for department, salaries in department_salary.items():
    average_salary = sum(salaries) / len(salaries)
    print(f"{department}: ₹{average_salary:.2f}")

    # Highest and Lowest Salary by Department

print("\nHIGHEST & LOWEST SALARY BY DEPARTMENT")
print("-" * 50)

department_employees = {}

for employee in employees:
    department = employee["Department"]

    if department not in department_employees:
        department_employees[department] = []

    department_employees[department].append(employee)

for department, dept_employees in department_employees.items():

    highest = max(dept_employees, key=lambda x: x["Basic_Salary"])
    lowest = min(dept_employees, key=lambda x: x["Basic_Salary"])

    print(f"\n{department}")
    print(f"Highest: {highest['Name']} - ₹{highest['Basic_Salary']}")
    print(f"Lowest: {lowest['Name']} - ₹{lowest['Basic_Salary']}")

    import matplotlib.pyplot as plt

# -------------------------------
# DATA VISUALIZATION
# -------------------------------

# 1. Average Salary by Department
departments = []
average_salaries = []

for department in department_salary:
    departments.append(department)

    total = 0
    count = 0

    for employee in employees:
        if employee["Department"] == department:
            total += employee["Basic_Salary"]
            count += 1

    average_salaries.append(total / count)
    
plt.figure(figsize=(8, 5))
plt.bar(departments, average_salaries)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 2. Employee Salary Comparison
names = []
salaries = []

for employee in employees:
    names.append(employee["Name"])
    salaries.append(employee["Basic_Salary"])

plt.figure(figsize=(10, 5))
plt.bar(names, salaries)
plt.title("Employee Salary Comparison")
plt.xlabel("Employee")
plt.ylabel("Basic Salary (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


