# config.py
import os
from dotenv import load_dotenv

load_dotenv()

DHL_API_KEY = os.getenv("DHL_API_KEY")
BASE_URL = os.getenv("BASE_URL")
DHL_SECRET = os.getenv("DHL_API_SECRET")