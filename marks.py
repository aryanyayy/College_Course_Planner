import csv

def marks_menu():
    while True:
        print("\n--- ASSESSMENT AND MARKS ---")
        print("1. Add assessment")
        print("2. View assessments")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            code = input("Course code: ").upper()
            name = input("Assessment name (Quiz/Viva/Project etc.): ")
            marks = input("Marks obtained: ")
            maximum = input("Maximum marks: ")
            date = input("Date (DD-MM-YYYY): ")

            with open("data/assessments.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([code, name, marks, maximum, date])
            print("Assessment saved.")

        elif choice == "2":
            with open("data/assessments.csv", "r") as file:
                rows = list(csv.reader(file))
            print("\nASSESSMENT RECORDS")
            for row in rows[1:]:
                print(row[0], "|", row[1], "|", row[2], "/", row[3], "|", row[4])
            if len(rows) == 1:
                print("No assessments saved.")

        elif choice == "0":
            break
        else:
            print("Invalid choice.")
