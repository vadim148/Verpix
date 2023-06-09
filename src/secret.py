from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")