import os
from dotenv import load_dotenv
GITHUB_URL = "https://github.com"
load_dotenv()
TEST_GITHUB_EMAIL = os.getenv("TEST_GITHUB_EMAIL")
TEST_GITHUB_PASSWORD = os.getenv("TEST_GITHUB_PASSWORD")