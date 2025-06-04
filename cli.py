from models.my_models import User, Workout, Exercise, session
import getpass
import bcrypt

def main_menu():
    while True:
        print("\nWelcome to the Fitness Tracker CLI")
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
            print("Exiting the Fitness Tracker. Stay strong!")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(user):
    while True:
        print(f"\nLogged in as: {user.name}")
        print("1. Add a workout")
        print("2. Add exercise to a workout")
        print("3. View my workouts")
        print("4. View exercises for a workout")
        print("5. Update my profile")
        print("6. Delete my account")
        print("7. Update a workout")
        print("8. Delete a workout")
        print("9. Update an exercise")
        print("10. Delete an exercise")
        print("11. View profile")
        print("12. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_workout(user)
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
            print(f"Name: {user.name}, Age: {user.age}, Email: {user.email}")
        elif choice == '11':
            print("Logged out.")
            break
        else:
            print("Invalid choice. Try again.")

def create_user():
    name = input("Enter user name: ")
    age = input("Enter user age: ")
    email = input("Enter user email: ")
    password = getpass.getpass("Enter user password: ")

    if password == "" or email == "":
        print("Password or Email cannot be empty")
        return
    
    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    user = User(name=name, age=int(age), email=email, password=password_hash.decode("utf-8"))
    session.add(user)
    session.commit()
    print(f"User '{name}' added successfully!")

def login():
    user_email = input("Enter your user email: ")
    user_password = getpass.getpass("Enter your user password: ")
    user = session.query(User).filter_by(email=user_email).first()
    if user and bcrypt.checkpw(user_password.encode("utf-8"),user.password.encode("utf-8")):
        print("Login Successfully")
        return user
    else:
        print("Invalid email or password.")
        return None

def add_workout(user):
    name = input("Enter Workout name: ")
    sets = input("Enter duration: ")
    exercise = Workout(activity=name, duration=int(sets), user=user)
    session.add(exercise)
    session.commit()
    print(f"Workout '{name}' added.")

def add_exercise(user):
    view_workouts(user)
    

    # First, list user's workouts to choose from
    workouts = session.query(Workout).filter_by(user_id=user.id).all()
    if not workouts:
        print("You have no workouts. Please log a workout first.")
        return
    
    print("\nYour Workouts:")
    for workout in workouts:
        print(f"ID: {workout.id} - Activity: {workout.activity}, Duration: {workout.duration} minutes")
    
    workout_id = input("Enter the ID of the workout to add an exercise to: ")
    workout = session.query(Workout).filter_by(id=int(workout_id), user_id=user.id).first()

    if not workout:
        print("Workout not found or does not belong to you.")
        return
    
    name = input("Enter exercise name: ")
    reps = input("Enter number of reps: ")
    sets = input("Enter number of sets: ")

    # Validate inputs
    try:
        reps = int(reps)
        sets = int(sets)
    except ValueError:
        print("Reps and sets must be numbers.")
        return

    # Create the Exercise and link it to the workout
    exercise = Exercise(name=name, reps=reps, sets=sets, workout=workout)
    session.add(exercise)
    session.commit()
    print(f"Exercise '{name}' added to workout '{workout.activity}'.")


def view_workouts(user):
    workouts = session.query(Workout).filter_by(user_id=user.id).all()
    if workouts:
        print("\nYour Workouts:")
        for w in workouts:
            print(f"Workout ID: {w.id}, Name: {w.activity}, Duration: {w.duration} minutes")
    else:
        print("No workouts found.")

def view_exercises(user):
    view_workouts(user)
    workout_id = input("Enter workout ID to view exercises: ")
    exercises = session.query(Exercise).filter_by(workout_id=int(workout_id)).all()
    if exercises:
        print("\n🏋️ Exercises:")
        for e in exercises:
            print(f"Exercise ID: {e.id}\n Name: {e.name}\n Reps: {e.reps}\n Sets: {e.sets}")
    else:
        print("No exercises found.")

def update_user(user):
    name = input("Enter new name (leave blank to keep current): ")
    age = input("Enter new age (leave blank to keep current): ")
    if name:
        user.name = name
    if age:
        user.age = int(age)
    session.commit()
    print("Profile updated.")

def delete_user(user):
    confirm = input("Are you sure you want to delete your account? (yes/no): ")
    if confirm.lower() == "yes":
        session.delete(user)
        session.commit()
        print("User deleted.")
    else:
        print("Cancelled.")

def update_workout(user):
    view_workouts(user)
    workout_id = input("Enter workout ID to update: ")
    workout = session.query(Workout).filter_by(id=int(workout_id), user_id=user.id).first()
    if workout:
        name = input("New workout name (leave blank to keep current): ")
        duration = input("New workout duration (leave blank to keep current): ")
        if name:
            workout.activity = name
        if duration:
            workout.duration = duration
        session.commit()
        print("Workout updated.")
    else:
        print("Workout not found.")

def delete_workout(user):
    view_workouts(user)
    workout_id = input("Enter workout ID to delete: ")
    workout = session.query(Workout).filter_by(id=int(workout_id), user_id=user.id).first()
    if workout:
        session.delete(workout)
        session.commit()
        print("Workout deleted.")
    else:
        print("Workout not found.")

def update_exercise(user):
    view_workouts(user)
    workout_id = input("Enter workout ID of the exercise: ")
    exercises = session.query(Exercise).filter_by(workout_id=int(workout_id)).all()
    for e in exercises:
        print(f"Exercise ID: {e.id}, Name: {e.name}, Reps: {e.reps}, Sets: {e.sets}")
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
        print("Exercise updated.")
    else:
        print("Exercise not found.")

def delete_exercise(user):
    view_workouts(user)
    workout_id = input("Enter workout ID of the exercise: ")
    exercises = session.query(Exercise).filter_by(workout_id=int(workout_id)).all()
    for e in exercises:
        print(f"Exercise ID: {e.id}, Name: {e.name}, Reps: {e.reps}, Sets: {e.sets}")
    exercise_id = input("Enter exercise ID to delete: ")
    exercise = session.query(Exercise).filter_by(id=int(exercise_id)).first()
    if exercise:
        session.delete(exercise)
        session.commit()
        print("Exercise deleted.")
    else:
        print("Exercise not found.")

if __name__ == "__main__":
    main_menu()
