import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables
TOKEN = str(os.getenv("TOKEN"))

