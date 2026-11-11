# # from selenium import webdriver 
# # driver.get("https://www.google.com") 
# # print(driver.title) driver.quit()
# import pytest
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait 
# from selenium.webdriver.support import expected_conditions as EC
# #     assert driver.title == "Google"
# @pytest.mark.selenium 
# def test_google_title(driver: WebDriver):
#     driver.get("https://www.google.com")
#     print(f"driver: {driver}")
#     assert driver.title == "Google"
# @pytest.mark.selenium
# def test_google_search(driver: WebDriver):
#     driver.get("https://playwright.dev/")
#     searchField = driver.find_element(By.NAME, "q")
#     # searchField = driver.find_element(By.CSS_SELECTOR, 'textarea[name="q"]')
#     searchField.send_keys("SOXL stock price")
#     # searchField.submit()
#     searchField.clear()
#     print(searchField.get_attribute("aira-label"))
#     searchField.send_keys(Keys.ENTER)
# # driver = webdriver.Chrome()
# def test_cli_button():
#     # 1. פתיחת דפדפן Chrome
#     driver = webdriver.Chrome()
#     try:
#         # 2. הקטנת החלון כדי שיופיע ההמבורגר
#         driver.set_window_size(800, 800)
#         # 3. כניסה לאתר Playwright
#         driver.get("https://playwright.dev/")
#         # 4. מציאת כפתור ההמבורגר
#         button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((
#                 By.CSS_SELECTOR,
#                 'button[aria-label="Toggle navigation bar"]'
#             ))
#         )
#         # 5. לחיצה על ההמבורגר
#         button.click()
#         # 6. מציאת CLI באמצעות XPath קצר
#         cli = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//a[contains(., 'CLI')]")
#             )
#         )
#         # 7. הדפסת הטקסט CLI
#         print(cli.text)
#         # 8. בדיקה שהטקסט הוא CLI
#         assert cli.text.strip() == "CLI"
#     finally:
#         # 9. סגירת הדפדפן
#         driver.quit()



import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# טסט 1 - בדיקת הכותרת של Google
@pytest.mark.selenium
def test_google_title(driver: WebDriver):

    # כניסה לגוגל
    driver.get("https://www.google.com/")

    # הדפסת הכותרת
    print(driver.title)

    # בדיקה שהכותרת היא Google
    assert driver.title == "Google"


# טסט 2 - חיפוש בגוגל
@pytest.mark.selenium
def test_google_search(driver: WebDriver):

    # כניסה לגוגל ולא ל-Playwright
    driver.get("https://www.google.com/")

    # המתנה לשדה החיפוש
    searchField = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.NAME, "q")
        )
    )

    # הקלדת טקסט לחיפוש
    searchField.send_keys("SOXL stock price")

    # הדפסת מאפיין הנגישות
    print(searchField.get_attribute("aria-label"))

    # לחיצה על Enter
    searchField.send_keys(Keys.ENTER)

    # המתנה שהדפדפן יעבור לדף התוצאות
    WebDriverWait(driver, 10).until(
        EC.url_contains("search")
    )

    # בדיקה שהגענו לתוצאות החיפוש
    assert "search" in driver.current_url


# טסט 3 - לחיצה על המבורגר והדפסת CLI
@pytest.mark.selenium
def test_cli_button(driver: WebDriver):

    # הקטנת החלון כדי שיופיע ההמבורגר
    driver.set_window_size(800, 800)

    # כניסה לאתר Playwright
    driver.get("https://playwright.dev/")

    # מציאת כפתור ההמבורגר
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            'button[aria-label="Toggle navigation bar"]'
        ))
    )

    # לחיצה על ההמבורגר
    button.click()

    # חיפוש קישור CLI גלוי עם XPath קצר
    cli = WebDriverWait(driver, 10).until(
        lambda d: next(
            (
                link for link in d.find_elements(
                    By.XPATH, "//a[contains(., 'CLI')]"
                )
                if link.is_displayed()
                and link.text.strip() == "CLI"
            ),
            False
        )
    )

    # הדפסת CLI
    print(cli.text)

    # בדיקה שהטקסט הוא CLI
    assert cli.text.strip() == "CLI"
