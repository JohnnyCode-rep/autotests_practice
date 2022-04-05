import pytest

from pages.account_page import AccountPage
from pages.login_page import LoginPage
from test_data.links import Links
from test_data.user import User
from pages.locators import AccountPageLocators


class TestChangePassword:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser, Links.LOGIN_PAGE_LINK)
        self.login_page.open()
        self.login_page.should_be_login_form()
        self.login_page.login_user(User.EMAIL, User.PASSWORD)
        self.login_page.should_be_authorized_user()
        self.page = AccountPage(browser, Links.ACCOUNT_INFO_PAGE)
        self.page.open()
        self.page.click_button(*AccountPageLocators.CHANGE_PASSWORD_MENU_BUTTON)
        self.page.should_be_change_password_form()

    @pytest.mark.critical_checks
    def test_user_can_change_password(self, browser):
        self.page.password_change(User.PASSWORD, User.NEW_PASSWORD, User.NEW_PASSWORD)
        self.page.should_be_password_change_message()
        self.page.click_button(*AccountPageLocators.CHANGE_PASSWORD_MENU_BUTTON)
        self.page.password_change(User.NEW_PASSWORD, User.PASSWORD, User.PASSWORD)  # Возврат исходных тестовых данных
        self.page.should_be_password_change_message()

    def test_change_password_invalid_old_password(self, browser):
        self.page.password_change(User.INVALID_PASSWORD, User.NEW_PASSWORD, User.NEW_PASSWORD)
        self.page.should_be_invalid_old_password_alert()

    def test_change_password_empty_required_fields(self, browser):
        self.page.click_button(*AccountPageLocators.CHANGE_PASSWORD_BUTTON)
        self.page.should_be_password_change_empty_fields_alert()

    def test_change_password_invalid_confirm_password(self, browser):
        self.page.password_change(User.PASSWORD, User.NEW_PASSWORD, User.INVALID_PASSWORD)
        self.page.should_be_passwords_do_not_match_alert()

    def test_change_password_short_new_password(self, browser):
        self.page.password_change(User.PASSWORD, User.SHORT_NEW_PASSWORD, User.SHORT_NEW_PASSWORD)
        self.page.should_be_short_new_password_alert()
