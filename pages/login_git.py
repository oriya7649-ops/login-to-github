from playwright.sync_api import Locator, Page
from pages.Base_page import BasePage
from utilities import config
import re
class LoginPage(BasePage):
    PATH = config.GITHUB_URL
    def __init__(self, page: Page):
        super().__init__(page)
    #י יש 2 אפשריות להגדיר אובייקט או פנציה שמבצעת את הלחיצה או פונקציה שרק מיבאה את האוביקט  
    def SignInButton(self) -> Locator:
        return self.page.get_by_role("link", name="Sign in")
    
    def clickOnSingin(self) -> None:
        self.page.get_by_role("link", name="Sign in").click()
       
    def waitForLoginPageLoad(self):
        self.page.wait_for_url("**/login**")
    def emailField(self):
       return self.page.get_by_role("textbox", name="Username or email address")
    def PasswordField(self):
       return self.page.get_by_role("textbox", name="Password")   
    def singInWithCredent(self)->Locator:
        return self.page.get_by_role("button", name="Sign in", exact=True)
        