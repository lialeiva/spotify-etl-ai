import os
from dotenv import load_dotenv
from pathlib import Path

ENV = os.getenv("ENV", "local")

BASE_DIR = Path(__file__).parent

env_file = BASE_DIR / ".env.local" if ENV == "local" else BASE_DIR / ".env.production"

load_dotenv(env_file)

SCOPE="user-read-recently-played"
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI=os.getenv("SPOTIFY_REDIRECT_URI")
DB_CONNSTR=f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")