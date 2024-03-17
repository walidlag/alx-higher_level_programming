#!/usr/bin/python3
"""List all states"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

     # Create database
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print all State objects
    for state in session.query(State).order_by(State.id):
        print(state.id, state.name, sep=": ")
        for city in state.cities:
            print("    ", city.id, city.name, sep=": ")
