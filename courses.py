import csv

FILE = "data/courses.csv"

def read_courses():
    with open(FILE, newline="") as f:
        return list(csv.DictReader(f))

def menu():
    while True:
        print("\n" + "=" * 42)
        print("             COURSE MANAGEMENT")
        print("=" * 42)
        print("1. Add Course\n2. View Courses\n3. Search Course")
        print("4. Edit Course\n5. Delete Course")
        print("6. Total Registered Credits\n0. Back")
        choice = input("Enter choice: ").strip()
        rows = read_courses()

        if choice == "0":
            break
        elif choice == "1":
            entry = input("Enter course (CODE - Course Name): ").strip()
            parts = entry.split("-", 1)
            if len(parts) != 2:
                print("Use format: CSAE100 - Python Programming")
                continue
            code, name = parts[0].strip().upper(), parts[1].strip()
            letters = code.rstrip("0123456789")
            digits = code[len(letters):]
            if not letters.isalpha() or not digits.isdigit() or not name.replace(" ", "").isalpha():
                print("Use letters+numbers for code and letters for course name.")
                continue
            if any(r["code"] == code for r in rows):
                print("This course code already exists.")
                continue
            try:
                credits = int(input("Enter credits: "))
                if credits <= 0:
                    print("Credits must be positive.")
                    continue
            except ValueError:
                print("Credits must be a whole number.")
                continue
            with open(FILE, "a", newline="") as f:
                csv.writer(f).writerow([code, name, credits])
            print("Course added successfully.")

        elif choice == "2":
            if not rows:
                print("No courses added yet.")
            for r in rows:
                print(f'{r["code"]} - {r["name"]} ({r["credits"]} credits)')

        elif choice == "3":
            term = input("Enter course code or name: ").strip().lower()
            for r in rows:
                if term in r["code"].lower() or term in r["name"].lower():
                    print(f'{r["code"]} - {r["name"]} ({r["credits"]} credits)')

        elif choice == "6":
            total = sum(int(r["credits"]) for r in rows)
            print("Total registered credits:", total)

        elif choice in ("4", "5"):
            code = input("Enter course code: ").strip().upper()
            found = next((r for r in rows if r["code"] == code), None)
            if not found:
                print("Course not found.")
                continue
            if choice == "5":
                rows.remove(found)
            else:
                name = input("New course name: ").strip()
                try:
                    credits = int(input("New credits: "))
                    if not name.replace(" ", "").isalpha() or credits <= 0:
                        raise ValueError
                    found.update(name=name, credits=str(credits))
                except ValueError:
                    print("Enter a valid course name and positive whole credits.")
                    continue
            with open(FILE, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=["code", "name", "credits"])
                w.writeheader()
                w.writerows(rows)
            print("Course deleted." if choice == "5" else "Course updated.")
        else:
            print("Invalid choice.")
