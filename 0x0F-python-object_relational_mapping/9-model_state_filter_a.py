#!/usr/bin/python3
"""
    Write a script that lists all State objects
    from the database hbtn_0e_6_usa if its exists
"""
if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    arg = sys.argv

    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'
                .format(arg[1], arg[2], arg[3]),
                pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    res = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .order_by(State.id).all()
        )

    for state in res:
        print("{}: {}".format(state.id, state.name))

    session.close()
