import os
import uuid
from datetime import datetime

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

def return_env_value(key: str) -> str:
	return os.environ[key]

def upload_file_name_formatter() -> str:
	dummy_uuid = uuid.uuid4()
	timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
	return f"{dummy_uuid}_{timestamp}"



