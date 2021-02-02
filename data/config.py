import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables
TOKEN = str(os.getenv("TOKEN"))

POSTGRES_HOST = "localhost"
POSTGRES_PORT = 5432
POSTGRES_PASSWORD = str(os.getenv("POSTGRES_PASSWORD"))
POSTGRES_USER = str(os.getenv("POSTGRES_USER"))
POSTGRES_DB = str(os.getenv("POSTGRES_DB"))
POSTGRES_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
