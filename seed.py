from db import session, Base, engine
from models.user import User
from models.workout import Workout
from models.exercise import Exercise

# Drop all tables and recreate them (use with caution in production)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create sample users
user1 = User(name="Alice", age=28)
user2 = User(name="Bob", age=35)

# Create sample workouts
workout1 = Workout(name="Upper Body Blast", date="2025-06-01", user=user1)
workout2 = Workout(name="Leg Day", date="2025-06-02", user=user1)
workout3 = Workout(name="Cardio Session", date="2025-06-01", user=user2)

# Create exercises for workout1
exercise1 = Exercise(name="Push Ups", reps=15, sets=3, workout=workout1)
exercise2 = Exercise(name="Pull Ups", reps=10, sets=3, workout=workout1)

# Create exercises for workout2
exercise3 = Exercise(name="Squats", reps=20, sets=4, workout=workout2)
exercise4 = Exercise(name="Lunges", reps=12, sets=3, workout=workout2)

# Create exercises for workout3
exercise5 = Exercise(name="Jump Rope", reps=100, sets=5, workout=workout3)
exercise6 = Exercise(name="Burpees", reps=10, sets=3, workout=workout3)

# Add all records to session
session.add_all([user1, user2])
session.commit()

print("✅ Database seeded successfully!")
