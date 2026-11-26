# College Course Planner

A simple, terminal-based Python application for managing student details, courses, assessments, a weekly timetable, and GPA records.

## Run the project
1. Install Python 3.
2. Keep all six Python files in the same folder.
3. Open a terminal in that folder.
4. Run: `python main.py`

The `data` folder and CSV files are created automatically on first run. Keep the data folder to retain saved information.

## Files
- `main.py` — main menu and CSV setup
- `profile.py` — student profile
- `courses.py` — course management and total registered credits
- `marks.py` — assessment records, editing, deletion, course performance and upcoming assessments
- `timetable.py` — weekly classes, personal/other events, upcoming schedule and today's timetable
- `gpa.py` — SGPA, CGPA, GPA history and numeric mini calculator

## Input formats
- Course: `CSAE100 - Python Programming`
- Date: `DD-MM-YYYY`
- Time: `HH:MM` (24-hour clock)
- Course code: letters followed by digits
- Name: letters and spaces
- Integer inputs use `int(input())`; decimal inputs use `float(input())`; ordinary text uses `input()`.

## Important
The grade-point mapping is written in `gpa.py`. Confirm it against Bennett University's current official grading rules before treating the result as official.
