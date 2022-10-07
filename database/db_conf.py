import os
from dotenv import load_dotenv

load_dotenv()

DBUSER = os.getenv('POSTGRES_USER')
DBPASS = os.getenv('POSTGRES_PASSWORD')
DB = os.getenv('POSTGRES_DB')

POSTGRES = f"postgresql+psycopg2://{DBUSER}:{DBPASS}@localhost/{DB}"
