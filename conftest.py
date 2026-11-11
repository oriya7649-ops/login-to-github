import pytest
from selenium import webdriver
import os
@pytest.fixture
def driver():
    # optinot=webdriver.ChromeOptions()
    # optinot.add_argument("--headlees")
    driver = webdriver.Chrome()
    # print(f"driver:{driver}")
    yield driver
    driver.quit()