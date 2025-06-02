# cli.py
from db import session
from models.user import User
from models.workout import Workout
from models.exercise import Exercise

def main_menu():
    while True:
        print("\n🏋️ Welcome to the Fitness Tracker CLI 🏋️")
        print("1. Create a new user")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_user()
        elif choice == '2':
            user = login()
            if user:
                user_menu(user)
        elif choice == '3':
            print("👋 Exiting the Fitness Tracker. Stay strong!")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(user):
    while True:
        print(f"\n🏋️ Logged in as: {user.name}")
        print("1. Log a workout")
        print("2. Add exercise to a workout")
        print("3. View my workouts")
        print("4. View exercises for a workout")
        print("5. Update my profile")
        print("6. Delete my account")
        print("7. Update a workout")
        print("8. Delete a workout")
        print("9. Update an exercise")
        print("10. Delete an exercise")
        print("11. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            log_workout(user)
        elif choice == '2':
            add_exercise(user)
        elif choice == '3':
            view_workouts(user)
        elif choice == '4':
            view_exercises(user)
        elif choice == '5':
            update_user(user)
        elif choice == '6':
            delete_user(user)
            break
        elif choice == '7':
            update_workout(user)
        elif choice == '8':
            delete_workout(user)
        elif choice == '9':
            update_exercise(user)
        elif choice == '10':
            delete_exercise(user)
        elif choice == '11':
            print("👋 Logged out.")
            break
        else:
            print("Invalid choice. Try again.")

def create_user():
    name = input("Enter user name: ")
    age = input("Enter user age: ")
    user = User(name=name, age=int(age))
    session.add(user)
    session.commit()
    print(f"✅ User '{name}' added successfully!")

def login():
    user_id = input("Enter your user ID: ")
    user = session.query(User).filter_by(id=int(user_id)).first()
    if user:
        print(f"✅ Welcome back, {user.name}!")
        return user
    else:
        print("❌ User not found.")
        return None

def log_workout(user):
    name = input("Enter workout name: ")
    date = input("Enter workout date (YYYY-MM-DD): ")
    workout = Workout(name=name, date=date, user_id=user.id)
    session.add(workout)
    session.commit()
    print(f"✅ Workout '{name}' logged.")

def add_exercise(user):
    view_workouts(user)
    workout_id = input("Enter workout ID to add exercise to: ")
    name = input("Enter exercise name: ")
    reps = input("Enter number of reps: ")
    sets = input("Enter number of sets: ")
    exercise = Exercise(name=name, reps=int(reps), sets=int(sets), workout_id=int(workout_id))
    session.add(exercise)
    session.commit()
    print(f"✅ Exercise '{name}' added.")

def view_workouts(user):
    workouts = session.query(Workout).filter_by(user_id=user.id).all()
    if workouts:
        print("\n📋 Your Workouts:")
        for w in workouts:
            print(w)
    else:
        print("❌ No workouts found.")

def view_exercises(user):
    view_workouts(user)
    workout_id = input("Enter workout ID to view exercises: ")
    exercises = session.query(Exercise).filter_by(workout_id=int(workout_id)).all()
    if exercises:
        print("\n🏋️ Exercises:")
        for e in exercises:
            print(e)
    else:
        print("❌ No exercises found.")

def update_user(user):
    name = input("Enter new name (leave blank to keep current): ")
    age = input("Enter new age (leave blank to keep current): ")
    if name:
        user.name = name
    if age:
        user.age = int(age)
    session.commit()
    print("✅ Profile updated.")

def delete_user(user):
    confirm = input("⚠️ Are you sure you want to delete your account? (yes/no): ")
    if confirm.lower() == "yes":
        session.delete(user)
        session.commit()
        print("🗑️ User deleted.")
    else:
        print("Cancelled.")

def update_workout(user):
    view_workouts(user)
    workout_id = input("Enter workout ID to update: ")
    workout = session.query(Workout).filter_by(id=int(workout_id), user_id=user.id).first()
    if workout:
        name = input("New workout name (leave blank to keep current): ")
        date = input("New workout date (leave blank to keep current): ")
        if name:
            workout.name = name
        if date:
            workout.date = date
        session.commit()
        print("✅ Workout updated.")
    else:
        print("❌ Workout not found.")

def delete_workout(user):
    view_workouts(user)
    workout_id = input("Enter workout ID to delete: ")
    workout = session.query(Workout).filter_by(id=int(workout_id), user_id=user.id).first()
    if workout:
        session.delete(workout)
        session.commit()
        print("🗑️ Workout deleted.")
    else:
        print("❌ Workout not found.")

def update_exercise(user):
    view_workouts(user)
    workout_id = input("Enter workout ID of the exercise: ")
    exercises = session.query(Exercise).filter_by(workout_id=int(workout_id)).all()
    for e in exercises:
        print(e)
    exercise_id = input("Enter exercise ID to update: ")
    exercise = session.query(Exercise).filter_by(id=int(exercise_id)).first()
    if exercise:
        name = input("New name (leave blank to keep current): ")
        reps = input("New reps (leave blank to keep current): ")
        sets = input("New sets (leave blank to keep current): ")
        if name:
            exercise.name = name
        if reps:
            exercise.reps = int(reps)
        if sets:
            exercise.sets = int(sets)
        session.commit()
        print("✅ Exercise updated.")
    else:
        print("❌ Exercise not found.")

def delete_exercise(user):
    view_workouts(user)
    workout_id = input("Enter workout ID of the exercise: ")
    exercises = session.query(Exercise).filter_by(workout_id=int(workout_id)).all()
    for e in exercises:
        print(e)
    exercise_id = input("Enter exercise ID to delete: ")
    exercise = session.query(Exercise).filter_by(id=int(exercise_id)).first()
    if exercise:
        session.delete(exercise)
        session.commit()
        print("🗑️ Exercise deleted.")
    else:
        print("❌ Exercise not found.")

if __name__ == "__main__":
    main_menu()
