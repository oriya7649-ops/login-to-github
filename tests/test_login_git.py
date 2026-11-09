from playwright.sync_api import Page, expect
from pages.login_git import LoginPage
from utilities.config import GITHUB_TEST_EMAIL,GITHUB_TEST_PASSWORD

def test_sign_in_to_gmail(page: Page):
    signInPage = LoginPage(page)
    signInPage.open()
    page.pause()
    assert GITHUB_TEST_EMAIL is not None
    assert GITHUB_TEST_PASSWORD is not None
    signInPage.clickOnSingin()
    signInPage.waitForLoginPageLoad()
    # signInPage.SignInButton().click()
    #signInPage.page.wait_for_url("**/login**")
    signInPage.emailField().fill(GITHUB_TEST_EMAIL)
    signInPage.PasswordField().fill(GITHUB_TEST_PASSWORD)
    expect(signInPage.singInWithCredent()).to_be_visible()
    signInPage.singInWithCredent().click()
    
    page.pause()