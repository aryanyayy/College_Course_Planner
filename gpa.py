import csv

COURSES, HISTORY = "data/courses.csv", "data/gpa.csv"
POINTS = {"O": 10, "A+": 10, "A": 9, "B+": 8, "B": 7, "C+": 6, "C": 5, "D": 4, "F": 0}
FIELDS = ["semester", "credits", "sgpa"]

def read(path):
    with open(path, newline="") as f: return list(csv.DictReader(f))

def save(rows):
    with open(HISTORY, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(rows)

def number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0: return value
        except ValueError: pass
        print("Enter a non-negative number.")

def calculator():
    operations = {"1": lambda a,b: a+b, "2": lambda a,b: a-b,
                  "3": lambda a,b: a*b, "4": lambda a,b: a/b, "5": lambda a,b: a/b*100}
    while True:
        print("\n" + "-"*35 + "\n             MINI CALCULATOR\n" + "-"*35)
        print("1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)")
        print("4. Division (/)\n5. Percentage (%)\n0. Back")
        choice = input("Select operation: ").strip()
        if choice == "0": break
        if choice not in operations: print("Invalid choice."); continue
        a, b = number("Enter first number: "), number("Enter second number: ")
        if choice in ("4", "5") and b == 0: print("Second number cannot be zero."); continue
        result = operations[choice](a, b)
        print("Result:", f"{result:g}" + ("%" if choice == "5" else ""))

def calculate_sgpa(history):
    courses = read(COURSES)
    if not courses: print("Add courses first."); return
    total = credits = 0
    for c in courses:
        print(f'{c["code"]} - {c["name"]} ({c["credits"]} credits)')
        grade = input("Enter grade (O, A+, A, B+, B, C+, C, D, F): ").strip().upper()
        while grade not in POINTS: grade = input("Invalid grade. Try again: ").strip().upper()
        credit = int(c["credits"]); total += POINTS[grade]*credit; credits += credit
        print("Grade:", grade, "| Grade points:", POINTS[grade])
    sgpa = total/credits; semester = input("Enter semester name/number: ").strip()
    if not semester: print("Semester cannot be empty."); return
    print("Total credits:", credits, f"\nSGPA: {sgpa:.2f}")
    print("Performance:", "Excellent" if sgpa >= 9 else "Very Good" if sgpa >= 8 else "Good" if sgpa >= 7 else "Needs Improvement")
    if any(r["semester"].lower() == semester.lower() for r in history):
        if input("Semester exists. Replace record? (yes/no): ").strip().lower() != "yes": return
        history = [r for r in history if r["semester"].lower() != semester.lower()]
    history.append(dict(semester=semester, credits=credits, sgpa=f"{sgpa:.2f}")); save(history)
    print("GPA saved.")

def menu():
    while True:
        print("\n" + "="*42 + "\n               GPA CALCULATOR\n" + "="*42)
        print("1. Calculate SGPA\n2. View GPA History\n3. Calculate CGPA")
        print("4. Mini Calculator\n5. Reset GPA History\n0. Back")
        choice, history = input("Enter choice: ").strip(), read(HISTORY)
        if choice == "0": break
        elif choice == "1": calculate_sgpa(history)
        elif choice == "2":
            for r in history: print(f'{r["semester"]}: SGPA {r["sgpa"]} | Credits {r["credits"]}')
            if not history: print("No GPA records.")
        elif choice == "3":
            credits = sum(int(r["credits"]) for r in history)
            if credits: print(f'CGPA: {sum(float(r["sgpa"])*int(r["credits"]) for r in history)/credits:.2f} ({credits} total credits)')
            else: print("No GPA records.")
        elif choice == "4": calculator()
        elif choice == "5" and input("Delete all GPA records? (yes/no): ").strip().lower() == "yes":
            save([]); print("GPA history reset.")
        elif choice != "5": print("Invalid choice.")
