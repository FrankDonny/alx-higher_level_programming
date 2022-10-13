#!/usr/bin/python3

from relationship_city import Base, City
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker()(bind=engine)

    cities = session.query(City).order_by(City.id)
    for city in cities:
        print(f"{city.id}: {str(city.name)} -> {city.state.name}")
    session.close()
