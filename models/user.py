from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    # One user has many workouts
    workouts = relationship('Workout', back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', age={self.age})>"
