from sqlalchemy import create_engine
from db_conf import POSTGRES


engine = create_engine(POSTGRES)

engine.connect()

print(engine)