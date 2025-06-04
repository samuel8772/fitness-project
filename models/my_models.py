from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///fitness_tracker.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # One user has many workouts
    workouts = relationship('Workout', back_populates='user', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', age={self.age})>"

class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    activity = Column(String)
    duration = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='workouts')
    exercises = relationship('Exercise', back_populates='workout', cascade="all, delete-orphan")

class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    reps = Column(Integer)
    sets = Column(Integer)

    workout_id = Column(Integer, ForeignKey('workouts.id'))

    # Relationship
    workout = relationship('Workout', back_populates='exercises')

    def __repr__(self):
        return f"<Exercise(id={self.id}, name='{self.name}', reps={self.reps}, sets={self.sets})>"

# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)