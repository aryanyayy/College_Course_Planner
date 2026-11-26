import csv
from datetime import datetime

FILE, COURSES = "data/assessments.csv", "data/courses.csv"
FIELDS = ["course", "assessment", "marks", "maximum", "date"]

def read(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))

def save(rows):
    with open(FILE, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

def choose_course():
    courses = read(COURSES)
    if not courses:
        print("Add courses first.")
        return None
    for i, c in enumerate(courses, 1):
        print(f'{i}. {c["code"]} - {c["name"]}')
    pick = input("Select course number: ").strip()
    return courses[int(pick)-1] if pick.isdigit() and 1 <= int(pick) <= len(courses) else None

def assessment_details(old=None):
    name = input("Assessment name: ").strip()
    try:
        marks = float(input("Marks obtained: "))
        maximum = float(input("Maximum marks: "))
        date = input("Date DD-MM-YYYY: ").strip()
        datetime.strptime(date, "%d-%m-%Y")
        if not name or maximum <= 0 or not 0 <= marks <= maximum:
            raise ValueError
        return dict(assessment=name, marks=marks, maximum=maximum, date=date)
    except ValueError:
        print("Enter a name, valid marks and date.")
        return None

def show(rows):
    for i, r in enumerate(rows, 1):
        print(f'{i}. {r["course"]} | {r["assessment"]}: {r["marks"]}/{r["maximum"]} | {r["date"]}')

def menu():
    while True:
        print("\n" + "=" * 42 + "\n       ASSESSMENT & MARKS TRACKER\n" + "=" * 42)
        print("1. Add Assessment\n2. View All Assessments\n3. Course Performance")
        print("4. Edit Assessment\n5. Delete Assessment\n6. Upcoming Assessments\n0. Back")
        choice, rows = input("Enter choice: ").strip(), read(FILE)
        if choice == "0": break
        if choice == "1":
            course = choose_course()
            details = assessment_details() if course else None
            if course and details:
                rows.append(dict(course=course["code"], **details)); save(rows)
                print("Assessment saved.")
            elif not course: print("Invalid course selection.")
        elif choice in ("2", "3"):
            course = choose_course() if choice == "3" else None
            if choice == "3" and not course: continue
            shown = [r for r in rows if choice == "2" or r["course"] == course["code"]]
            show(shown)
            if choice == "3":
                got = sum(float(r["marks"]) for r in shown)
                total = sum(float(r["maximum"]) for r in shown)
                print(f"Total: {got:g}/{total:g}")
                print(f"Percentage: {got/total*100:.1f}%" if total else "No records.")
            elif not shown: print("No assessments found.")
        elif choice == "6":
            upcoming = [r for r in rows if datetime.strptime(r["date"], "%d-%m-%Y").date() >= datetime.now().date()]
            for r in sorted(upcoming, key=lambda x: datetime.strptime(x["date"], "%d-%m-%Y")):
                print(f'{r["date"]} | {r["course"]} | {r["assessment"]}')
            if not upcoming: print("No upcoming assessments.")
        elif choice in ("4", "5"):
            if not rows: print("No assessments found."); continue
            show(rows); pick = input("Select record number: ").strip()
            if not pick.isdigit() or not 1 <= int(pick) <= len(rows):
                print("Invalid record."); continue
            index = int(pick)-1
            if choice == "5": rows.pop(index)
            else:
                details = assessment_details(rows[index])
                if not details: continue
                rows[index].update(details)
            save(rows); print("Assessment deleted." if choice == "5" else "Assessment updated.")
        else: print("Invalid choice.")
