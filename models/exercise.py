from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

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
