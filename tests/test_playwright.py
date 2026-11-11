import pytest
from selenium.webdriver.common.by import By 
def test_play_wright_page(driver):
    driver.get("https://playwright.dev/")
    myElement = driver.find_element(By.TAG_NAME,"h1")
    print(f"my element: {myElement}")
    myElements = driver.find_elements(By.TAG_NAME,"h1")
    print(f"my element: {myElements[0]}")