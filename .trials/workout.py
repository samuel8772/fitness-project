from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationships
    user = relationship('User', back_populates='workouts')
    exercises = relationship('Exercise', back_populates='workout')

    def __repr__(self):
        return f"<Workout(id={self.id}, name='{self.name}', date='{self.date}')>"
