import os
import csv

# Create the data folder and CSV files the first time the program runs.
def create_files():
    if not os.path.exists("data"):
        os.mkdir("data")

    files = {
        "student.csv": ["name", "enrollment_id", "branch", "semester"],
        "courses.csv": ["course_code", "course_name", "credits"],
        "assessments.csv": ["course_code", "name", "marks", "maximum", "date"],
        "lectures.csv": ["day", "start", "end", "name"],
        "events.csv": ["type", "name", "date", "start", "end"],
        "gpa.csv": ["semester", "credits", "sgpa"]
    }

    for filename in files:
        path = os.path.join("data", filename)
        if not os.path.exists(path):
            with open(path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(files[filename])


def main():
    create_files()

    while True:
        print("\n===== COLLEGE COURSE PLANNER =====")
        print("1. Student Profile")
        print("2. Course Management")
        print("3. Assessment and Marks")
        print("4. Timetable")
        print("5. GPA Calculator")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            import profile
            profile.student_profile()
        elif choice == "2":
            import courses
            courses.course_menu()
        elif choice == "3":
            import marks
            marks.marks_menu()
        elif choice == "4":
            import timetable
            timetable.timetable_menu()
        elif choice == "5":
            import gpa
            gpa.gpa_menu()
        elif choice == "0":
            print("Goodbye! Your data is saved.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
