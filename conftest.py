
import pytest
from selenium import webdriver
@pytest.fixture
def driver():
    # הגדרת אפשרויות לדפדפן Chrome
    options = webdriver.ChromeOptions()
    # הפעלת Chrome ללא חלון גרפי
    options.add_argument("--headless=new")
    # הגדרות שמתאימות לסביבת CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # פתיחת הדפדפן עם האפשרויות
    driver = webdriver.Chrome(options=options)
    # העברת הדפדפן לטסט
    yield driver
    # סגירת הדפדפן בסיום
    driver.quit()