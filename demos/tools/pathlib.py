import os
from pathlib2 import Path
from dotenv import load_dotenv

base_dir = Path(__file__).resolve()
root_path = base_dir.parents[2]
env_path = root_path / ".env"
load_dotenv(dotenv_path=env_path)

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

print(ACCESS_TOKEN)
