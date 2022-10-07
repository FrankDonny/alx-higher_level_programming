#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    session.query(State).filter(State.id == 1)
    for state in session.query(State).filter(State.id == 1):
        if state is None:
            pass
        else:
            print(f'{state.id}: {state.name}')
    session.close()
