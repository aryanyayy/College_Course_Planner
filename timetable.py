import csv
from datetime import datetime, timedelta

LECTURES, EVENTS = "data/lectures.csv", "data/events.csv"
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
LF, EF = ["day", "start", "end", "name"], ["type", "name", "date", "start", "end"]

def read(path):
    with open(path, newline="") as f: return list(csv.DictReader(f))

def save(path, fields, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

def valid_time(value):
    try: datetime.strptime(value, "%H:%M"); return True
    except ValueError: return False

def add_classes():
    for i, day in enumerate(DAYS, 1): print(i, day)
    pick = input("Select day (1-7): ").strip()
    if not pick.isdigit() or not 1 <= int(pick) <= 7: print("Invalid day."); return
    day, rows = DAYS[int(pick)-1], read(LECTURES)
    mode = input("1. Replace this day  2. Add classes: ").strip()
    if mode not in ("1", "2"): return
    if mode == "1": rows = [r for r in rows if r["day"] != day]
    print("Enter [START, END] Class name. Type DONE when finished.")
    while True:
        line = input("> ").strip()
        if line.upper() == "DONE": break
        try:
            times, name = line.split("]", 1); start, end = [x.strip() for x in times.strip(" [").split(",")]
            if not valid_time(start) or not valid_time(end) or start >= end or not name.strip(): raise ValueError
            rows.append(dict(day=day, start=start, end=end, name=name.strip()))
        except ValueError: print("Format: [08:20, 09:20] Digital Design Lecture")
    rows.sort(key=lambda r: (DAYS.index(r["day"]), r["start"]))
    save(LECTURES, LF, rows); print("Classes saved.")

def add_event():
    kind = input("P. Personal  O. Other: ").strip().upper()
    name, date = input("Event name: ").strip(), input("Date DD-MM-YYYY: ").strip()
    start, end = input("Start time HH:MM: ").strip(), input("End time HH:MM: ").strip()
    try:
        datetime.strptime(date, "%d-%m-%Y")
        if kind not in ("P", "O") or not name or not valid_time(start) or not valid_time(end) or start >= end: raise ValueError
        rows = read(EVENTS); rows.append(dict(type=kind, name=name, date=date, start=start, end=end))
        save(EVENTS, EF, rows); print("Event saved.")
    except ValueError: print("Invalid event details.")

def display(choice):
    today = datetime.now().date(); monday = today - timedelta(days=today.weekday())
    items = []
    for r in read(LECTURES):
        date = monday + timedelta(days=DAYS.index(r["day"]))
        if choice == "3" or (choice == "4" and date >= today) or (choice == "6" and date == today):
            items.append((date, r["start"], r["end"], r["name"], "L"))
    for r in read(EVENTS):
        date = datetime.strptime(r["date"], "%d-%m-%Y").date()
        if (choice == "3" and monday <= date <= monday+timedelta(days=6)) or (choice == "4" and date >= today) or (choice == "6" and date == today):
            items.append((date, r["start"], r["end"], r["name"], r["type"]))
    if choice == "3":
        for day in DAYS:
            date = monday + timedelta(days=DAYS.index(day)); print(f"\n{day.upper()} ({date:%d-%m-%Y})")
            for _, start, end, name, kind in sorted(x for x in items if x[0] == date): print(f"{start}-{end} {name} [{kind}]")
    else:
        if not items: print("No classes or events scheduled.")
        for date, start, end, name, kind in sorted(items): print(f"{date:%d-%m-%Y} {start}-{end} {name} [{kind}]")

def menu():
    while True:
        print("\n" + "="*42 + "\n              SCHEDULE MANAGER\n" + "="*42)
        print("1. Add Weekly Classes\n2. Add Personal / Other Event\n3. View Weekly Timetable")
        print("4. View Upcoming Schedule\n5. Reset Timetable\n6. View Today's Timetable\n0. Back")
        choice = input("Enter choice: ").strip()
        if choice == "0": break
        elif choice == "1": add_classes()
        elif choice == "2": add_event()
        elif choice in ("3", "4", "6"): display(choice)
        elif choice == "5" and input("Delete all timetable entries? (yes/no): ").strip().lower() == "yes":
            save(LECTURES, LF, []); save(EVENTS, EF, []); print("Timetable reset.")
        elif choice != "5": print("Invalid choice.")
