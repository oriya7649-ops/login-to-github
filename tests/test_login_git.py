from playwright.sync_api import Page, expect
from pages.login_git import LoginPage
from utilities.config import EMAIL_GITHUB,TEST_PASSWORD

def test_sign_in_to_gmail(page: Page):
    signInPage = LoginPage(page)
    signInPage.open()
    page.pause()
    assert EMAIL_GITHUB is not None
    assert TEST_PASSWORD is not None
    signInPage.clickOnSingin()
    signInPage.waitForLoginPageLoad()
    # signInPage.SignInButton().click()
    #signInPage.page.wait_for_url("**/login**")
    signInPage.emailField().fill(EMAIL_GITHUB)
    signInPage.PasswordField().fill(TEST_PASSWORD)
    expect(signInPage.singInWithCredent()).to_be_visible()
    signInPage.singInWithCredent().click()
    
    page.pause()