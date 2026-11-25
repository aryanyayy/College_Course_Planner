# College Course Planner — Simple Version

## Run
Open this folder in VS Code and run:

    python main.py

Only `main.py` needs to be run. It imports the other component files.

## Python files
- `main.py` — main menu and creates CSV files
- `profile.py` — student profile
- `courses.py` — course list
- `marks.py` — assessments and marks
- `timetable.py` — L, P and O schedule entries; Monday to Sunday
- `gpa.py` — SGPA, GPA history and CGPA

There are no separate helper or storage files.

## CSV location
On the first run, `main.py` creates a folder named `data` beside the Python files. It creates these files inside it:
- student.csv
- courses.csv
- assessments.csv
- lectures.csv
- events.csv
- gpa.csv

CSV records are saved when entered. Keep the `data` folder with the Python files.

## L timetable format
Select a day (Monday=1 through Sunday=7), then enter:

    [08:20, 09:20] Digital Design Lecture
    [10:30, 11:20] Calculus Tutorial
    DONE

P and O events are added with a date and time.

## GPA
The grade-point mapping is in `gpa.py`. Check the current official university scale before relying on the result.
