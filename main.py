import csv
import os

FILES = {
    "student.csv": ["name", "enrollment", "gender", "branch", "semester"],
    "courses.csv": ["code", "name", "credits"],
    "assessments.csv": ["course", "assessment", "marks", "maximum", "date"],
    "lectures.csv": ["day", "start", "end", "name"],
    "events.csv": ["type", "name", "date", "start", "end"],
    "gpa.csv": ["semester", "credits", "sgpa"]
}

def setup():
    os.makedirs("data", exist_ok=True)
    for file, headings in FILES.items():
        path = "data/" + file
        if not os.path.exists(path):
            with open(path, "w", newline="") as f:
                csv.writer(f).writerow(headings)

def main():
    setup()
    while True:
        print("\n" + "=" * 42)
        print("          COLLEGE COURSE PLANNER")
        print("=" * 42)
        print("1. Student Profile\n2. Course Management")
        print("3. Assessment & Marks\n4. Schedule Manager")
        print("5. GPA Calculator\n0. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            import profile
            profile.menu()
        elif choice == "2":
            import courses
            courses.menu()
        elif choice == "3":
            import marks
            marks.menu()
        elif choice == "4":
            import timetable
            timetable.menu()
        elif choice == "5":
            import gpa
            gpa.menu()
        else:
            print("Please enter a valid menu number.")

if __name__ == "__main__":
    main()
