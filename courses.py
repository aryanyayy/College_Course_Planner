import csv

def course_menu():
    while True:
        print("\n--- COURSE MANAGEMENT ---")
        print("1. Add course")
        print("2. View courses")
        print("3. Delete course")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            code = input("Course code: ").upper()
            name = input("Course name: ")
            credits = input("Credits: ")

            with open("data/courses.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([code, name, credits])
            print("Course added.")

        elif choice == "2":
            with open("data/courses.csv", "r") as file:
                rows = list(csv.reader(file))
            print("\nCOURSES")
            for row in rows[1:]:
                print(row[0], "-", row[1], "| Credits:", row[2])
            if len(rows) == 1:
                print("No courses added.")

        elif choice == "3":
            code = input("Enter course code to delete: ").upper()
            with open("data/courses.csv", "r") as file:
                rows = list(csv.reader(file))
            new_rows = [rows[0]]
            for row in rows[1:]:
                if row[0].upper() != code:
                    new_rows.append(row)
            with open("data/courses.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(new_rows)
            print("If the course existed, it has been deleted.")

        elif choice == "0":
            break
        else:
            print("Invalid choice.")
