import os
from dotenv import load_dotenv
GITHUB_URL = "https://github.com"
load_dotenv()
GITHUB_TEST_EMAIL = os.getenv("GITHUB_TEST_EMAIL")
GITHUB_TEST_PASSWORD = os.getenv("GITHUB_TEST_PASSWORD")