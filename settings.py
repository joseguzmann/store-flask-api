import os
from dotenv import load_dotenv

load_dotenv()

# Setting for redis queues

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
QUEUES = ["emails", "default"]
