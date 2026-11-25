import csv

# Check these grade points against the university's current official rules.
GRADE_POINTS = {
    "O": 10, "A+": 10, "A": 9, "B+": 8, "B": 7,
    "C+": 6, "C": 5, "D": 4, "F": 0
}


def gpa_menu():
    while True:
        print("\n--- GPA CALCULATOR ---")
        print("1. Calculate and save semester GPA")
        print("2. View GPA history")
        print("3. Calculate CGPA")
        print("4. Reset GPA history")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            with open("data/courses.csv", "r") as file:
                courses = list(csv.reader(file))

            if len(courses) == 1:
                print("Add courses first.")
                continue

            semester = input("Semester number: ")
            total_points = 0
            total_credits = 0

            for course in courses[1:]:
                print("\n", course[1], "-", course[2], "credits")
                grade = input("Enter final grade: ").upper()

                if grade not in GRADE_POINTS:
                    print("Invalid grade. This course was not counted.")
                    continue

                credits = float(course[2])
                total_points += credits * GRADE_POINTS[grade]
                total_credits += credits

            if total_credits == 0:
                print("No valid grades entered.")
                continue

            sgpa = total_points / total_credits
            print("SGPA:", round(sgpa, 2))

            save = input("Save this semester GPA? (y/n): ").lower()
            if save == "y":
                with open("data/gpa.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([semester, total_credits, round(sgpa, 2)])
                print("GPA saved.")

        elif choice == "2":
            with open("data/gpa.csv", "r") as file:
                rows = list(csv.reader(file))
            print("\nSEMESTER GPA HISTORY")
            for row in rows[1:]:
                print("Semester", row[0], "| Credits:", row[1], "| SGPA:", row[2])
            if len(rows) == 1:
                print("No GPA records.")

        elif choice == "3":
            with open("data/gpa.csv", "r") as file:
                rows = list(csv.reader(file))
            points = 0
            credits_total = 0
            for row in rows[1:]:
                credits = float(row[1])
                sgpa = float(row[2])
                points += credits * sgpa
                credits_total += credits
            if credits_total == 0:
                print("No GPA records.")
            else:
                print("CGPA:", round(points / credits_total, 2))

        elif choice == "4":
            if input("Delete all GPA history? (y/n): ").lower() == "y":
                with open("data/gpa.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["semester", "credits", "sgpa"])
                print("GPA history cleared.")

        elif choice == "0":
            break
        else:
            print("Invalid choice.")
