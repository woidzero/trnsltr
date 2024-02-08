import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config:
    DEFAULT_ABC = os.getenv("DEFAULT_ABC")
