import csv

def student_profile():
    while True:
        print("\n--- STUDENT PROFILE ---")
        print("1. Add / Update profile")
        print("2. View profile")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            enrollment = input("Enrollment ID: ")
            branch = input("Branch: ")
            semester = input("Semester: ")

            with open("data/student.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "enrollment_id", "branch", "semester"])
                writer.writerow([name, enrollment, branch, semester])
            print("Profile saved.")

        elif choice == "2":
            with open("data/student.csv", "r") as file:
                rows = list(csv.reader(file))
            if len(rows) > 1:
                print("\nName:", rows[1][0])
                print("Enrollment ID:", rows[1][1])
                print("Branch:", rows[1][2])
                print("Semester:", rows[1][3])
            else:
                print("No profile saved.")

        elif choice == "0":
            break
        else:
            print("Invalid choice.")
