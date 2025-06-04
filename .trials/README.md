# 🏋️ Fitness Tracker CLI App

A simple yet powerful Python CLI application for tracking workouts, exercises, and user fitness profiles. Built using SQLAlchemy and SQLite as part of the Moringa/Flatiron Phase 3 Project.

---

## 📌 Features

- 👤 Create and manage user profiles
- 🔐 User login with personalized dashboard
- 🏋️ Log workouts with name and date
- 🏃 Add exercises to workouts with reps and sets
- 🔁 View, update, and delete users, workouts, and exercises
- 💾 Data persisted using SQLAlchemy ORM with SQLite

---

## 🛠️ Technologies Used

- Python 3
- SQLAlchemy ORM
- SQLite (via `sqlite3`)
- Rich CLI interface with user-friendly prompts

---

## 🧱 Project Structure

```bash
.
├── cli.py                # Main CLI interface
├── db.py                 # Database setup and session
├── models/
│   ├── __init__.py
│   ├── user.py           # User model
│   ├── workout.py        # Workout model
│   └── exercise.py       # Exercise model
├── Pipfile               # Pipenv dependencies
└── README.md             # Project documentation
