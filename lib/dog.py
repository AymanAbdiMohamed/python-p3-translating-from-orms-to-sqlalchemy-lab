from lib.models import Base, Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Engine and session factory (used in your tests)
engine = create_engine("sqlite:///dogs.db", echo=False)
Session = sessionmaker(bind=engine)


def create_table(base, engine):
    """Creates all tables in the database using the given declarative base and engine."""
    base.metadata.create_all(bind=engine)


def save(session, dog):
    """Save a Dog instance"""
    session.add(dog)
    session.commit()

def get_all(session):
    """Return all dogs"""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Return first dog matching name"""
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    """Return dog by id"""
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    """Return first dog matching both name and breed"""
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    """Update a dog's breed"""
    dog.breed = breed
    session.commit()

def update_name(session, dog, name):
    """Update a dog's name"""
    dog.name = name
    session.commit()

def delete(session, dog):
    """Delete a dog"""
    session.delete(dog)
    session.commit()
