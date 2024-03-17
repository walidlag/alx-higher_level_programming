#!/usr/bin/python3
"""List all states"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()
    instance = session.query(State).filter(State.name == (sys.argv[4],))

    # Check if the state exists; if found, print its ID, otherwise print "Not found"
    try:
        print(instance[0].id)
    except IndexError:
        print("Not found")
