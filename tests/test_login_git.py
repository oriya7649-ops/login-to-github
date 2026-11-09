from playwright.sync_api import Page, expect
from pages.login_git import LoginPage
from utilities.config import TEST_GITHUB_EMAIL,TEST_GITHUB_PASSWORD

def test_sign_in_to_gmail(page: Page):
    signInPage = LoginPage(page)
    signInPage.open()
    page.pause()
    assert TEST_GITHUB_EMAIL is not None
    assert TEST_GITHUB_PASSWORD is not None
    signInPage.clickOnSingin()
    signInPage.waitForLoginPageLoad()
    # signInPage.SignInButton().click()
    #signInPage.page.wait_for_url("**/login**")
    signInPage.emailField().fill(TEST_GITHUB_EMAIL)
    signInPage.PasswordField().fill(TEST_GITHUB_PASSWORD)
    expect(signInPage.singInWithCredent()).to_be_visible()
    signInPage.singInWithCredent().click()
    
    page.pause()