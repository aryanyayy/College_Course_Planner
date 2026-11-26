import csv

FILE = "data/student.csv"

def menu():
    while True:
        print("\n" + "=" * 42)
        print("             STUDENT PROFILE")
        print("=" * 42)
        print("|  1. Create / Update Profile           |")
        print("|  2. View Profile                      |")
        print("|  0. Back to Main Menu                 |")
        print("=" * 42)
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Full name: ").strip()
            while not name.replace(" ", "").isalpha():
                print("Enter letters only.")
                name = input("Full name: ").strip()
            enrollment = input("Enrollment ID: ").strip()
            print("1. Male  2. Female  3. Other  4. Prefer not to say")
            gender = input("Select gender: ").strip()
            while gender not in ["1", "2", "3", "4"]:
                gender = input("Choose 1-4: ").strip()
            genders = ["Male", "Female", "Other", "Prefer not to say"]
            branch = input("Branch / Degree: ").strip()
            try:
                semester = int(input("Current semester: "))
                while semester < 1 or semester > 8:
                    semester = int(input("Enter semester 1-8: "))
            except ValueError:
                print("Semester must be a whole number.")
                continue
            with open(FILE, "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["name", "enrollment", "gender", "branch", "semester"])
                w.writerow([name, enrollment, genders[int(gender)-1], branch, semester])
            print("+" * 42 + "\nPROFILE SAVED SUCCESSFULLY\n" + "+" * 42)

        elif choice == "2":
            with open(FILE, newline="") as f:
                profile = next(csv.DictReader(f), None)
            if profile:
                print("\n" + "=" * 42)
                print("              YOUR PROFILE")
                print("=" * 42)
                for key, value in profile.items():
                    print("|", key.title().ljust(12), ":", value)
                print("=" * 42)
            else:
                print("No profile found. Create one first.")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
