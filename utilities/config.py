import os
from dotenv import load_dotenv
GITHUB_URL = "https://github.com"
load_dotenv()
EMAIL_GITHUB = os.getenv("TEST_USERNAME")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")