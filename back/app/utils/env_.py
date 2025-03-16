from dotenv import load_dotenv
import os

load_dotenv()

class Env:
    database_uri = os.getenv("DATABASE_URI")
    async_mode = os.getenv("ASYNC_MODE")