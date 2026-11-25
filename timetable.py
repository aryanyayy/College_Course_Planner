import csv
from datetime import datetime, date, timedelta

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]


def add_lecture():
    print("\nChoose a day:")
    for i in range(7):
        print(i + 1, "-", DAYS[i])

    day_number = int(input("Enter day number (1-7): "))
    day = DAYS[day_number - 1]

    print("Enter the day's classes in this format:")
    print("[START TIME, END TIME] Class name")
    print("Example: [08:20, 09:20] Digital Design Lecture")
    print("Type DONE when finished.")

    entries = []
    while True:
        line = input("> ")
        if line.upper() == "DONE":
            break
        try:
            times, name = line.split("]", 1)
            times = times.replace("[", "").split(",")
            start = datetime.strptime(times[0].strip(), "%H:%M").strftime("%H:%M")
            end = datetime.strptime(times[1].strip(), "%H:%M").strftime("%H:%M")
            if end <= start or name.strip() == "":
                print("Check the times and class name.")
            else:
                entries.append([day, start, end, name.strip()])
        except:
            print("Wrong format. Example: [08:20, 09:20] Digital Design Lecture")

    if entries:
        print("1. Replace this day's old classes")
        print("2. Add these to existing classes")
        option = input("Choose: ")

        with open("data/lectures.csv", "r") as file:
            rows = list(csv.reader(file))

        if option == "1":
            rows = [rows[0]] + [row for row in rows[1:] if row[0] != day]

        rows.extend(entries)
        rows[1:] = sorted(rows[1:], key=lambda row: (DAYS.index(row[0]), row[1]))

        with open("data/lectures.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(day, "schedule saved.")


def add_personal_other():
    kind = input("Enter P for Personal or O for Other: ").upper()
    if kind not in ["P", "O"]:
        print("Choose P or O.")
        return

    name = input("Event name: ")
    event_date = input("Date (DD-MM-YYYY): ")
    start = input("Start time (HH:MM): ")
    end = input("End time (HH:MM): ")

    try:
        start_time = datetime.strptime(start, "%H:%M").time()
        end_time = datetime.strptime(end, "%H:%M").time()
        datetime.strptime(event_date, "%d-%m-%Y")
        if end_time <= start_time:
            print("End time must be after start time.")
            return
    except ValueError:
        print("Invalid date or time.")
        return

    with open("data/events.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([kind, name, event_date, start, end])
    print("Event saved.")


def view_week():
    with open("data/lectures.csv", "r") as file:
        lectures = list(csv.reader(file))
    with open("data/events.csv", "r") as file:
        events = list(csv.reader(file))

    today = date.today()
    monday = today - timedelta(days=today.weekday())

    for i in range(7):
        day = DAYS[i]
        date_for_day = monday + timedelta(days=i)
        print("\n" + day.upper())
        day_entries = []

        for row in lectures[1:]:
            if row[0] == day:
                day_entries.append([row[1], row[2], row[3] + " [L]"])

        for row in events[1:]:
            try:
                event_day = datetime.strptime(row[2], "%d-%m-%Y").date()
                if event_day == date_for_day:
                    day_entries.append([row[3], row[4], row[1] + " [" + row[0] + "]"])
            except ValueError:
                pass

        day_entries.sort(key=lambda x: x[0])
        if not day_entries:
            print("No entries.")
        for entry in day_entries:
            print(entry[0], "-", entry[1], entry[2])


def view_chronological():
    now = datetime.now()
    all_entries = []

    with open("data/events.csv", "r") as file:
        events = list(csv.reader(file))

    for row in events[1:]:
        try:
            event_date = datetime.strptime(row[3], "%d-%m-%Y").date()
            start = datetime.strptime(row[3], "%H:%M").time()
            end = datetime.strptime(row[4], "%H:%M").time()
            start_dt = datetime.combine(event_date, start)
            end_dt = datetime.combine(event_date, end)
            if end_dt >= now:
                all_entries.append([start_dt, end_dt, row[1] + " [" + row[0] + "]"])
        except ValueError:
            pass

    with open("data/lectures.csv", "r") as file:
        lectures = list(csv.reader(file))

    today = date.today()
    for row in lectures[1:]:
        day_number = DAYS.index(row[0])
        days_ahead = (day_number - today.weekday()) % 7
        next_day = today + timedelta(days=days_ahead)
        start = datetime.strptime(row[1], "%H:%M").time()
        end = datetime.strptime(row[2], "%H:%M").time()
        start_dt = datetime.combine(next_day, start)
        end_dt = datetime.combine(next_day, end)
        if end_dt < now:
            next_day = next_day + timedelta(days=7)
            start_dt = datetime.combine(next_day, start)
            end_dt = datetime.combine(next_day, end)
        all_entries.append([start_dt, end_dt, row[3] + " [L]"])

    all_entries.sort(key=lambda x: x[0])
    print("\nCURRENT AND UPCOMING EVENTS")
    if not all_entries:
        print("No upcoming entries.")
    for entry in all_entries:
        print(entry[0].strftime("%d-%m-%Y"), "|",
              entry[0].strftime("%H:%M"), "-", entry[1].strftime("%H:%M"),
              "|", entry[2])


def reset_timetable():
    answer = input("Delete all timetable entries? (y/n): ").lower()
    if answer == "y":
        for filename, header in [
            ("data/lectures.csv", ["day", "start", "end", "name"]),
            ("data/events.csv", ["type", "name", "date", "start", "end"])
        ]:
            with open(filename, "w", newline="") as file:
                csv.writer(file).writerow(header)
        print("Timetable cleared.")


def timetable_menu():
    while True:
        print("\n--- TIMETABLE ---")
        print("1. Enter L (Lecture/Lab/Tutorial) schedule")
        print("2. Add P (Personal) or O (Other) event")
        print("3. View weekly timetable")
        print("4. View chronological list")
        print("5. Reset timetable")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            add_lecture()
        elif choice == "2":
            add_personal_other()
        elif choice == "3":
            view_week()
        elif choice == "4":
            view_chronological()
        elif choice == "5":
            reset_timetable()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
