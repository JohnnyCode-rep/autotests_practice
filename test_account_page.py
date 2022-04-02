import pytest
import time

from .pages.account_page import AccountPage
from .pages.login_page import LoginPage
from .test_data.links import Links
from .test_data.user import User
from .pages.locators import AccountPageLocators


class TestAccountFunctions:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, Links.LOGIN_PAGE_LINK)
        self.page.open()
        self.page.should_be_login_form()
        self.page.login_user(User.EMAIL, User.PASSWORD)
        self.page.should_be_authorized_user()
        # time.sleep(5)

    @pytest.mark.critical_checks
    def test_user_can_change_password(self, browser):
        self.page = AccountPage(browser, Links.ACCOUNT_INFO_PAGE)
        self.page.open()
        change_password_menu = browser.find_element(*AccountPageLocators.CHANGE_PASSWORD_MENU_BUTTON)
        change_password_menu.click()
        self.page.should_be_change_password_form()
        self.page.password_change(User.PASSWORD, User.NEW_PASSWORD, User.NEW_PASSWORD)
        self.page.should_be_password_change_message()
        change_password_menu = browser.find_element(*AccountPageLocators.CHANGE_PASSWORD_MENU_BUTTON)
        change_password_menu.click()
        self.page.password_change(User.NEW_PASSWORD, User.PASSWORD, User.PASSWORD)  # Возврат исходных тестовых данных
        self.page.should_be_password_change_message()
        # time.sleep(5)

    def test_change_password_invalid_old_password(self, browser):
        self.page = AccountPage(browser, Links.ACCOUNT_INFO_PAGE)
        self.page.open()
        change_password_menu = browser.find_element(*AccountPageLocators.CHANGE_PASSWORD_MENU_BUTTON)
        change_password_menu.click()
        self.page.should_be_change_password_form()
        self.page.password_change(User.INVALID_PASSWORD, User.NEW_PASSWORD, User.NEW_PASSWORD)
        self.page.should_be_invalid_old_password_alert()
        # time.sleep(5)

    def test_change_password_empty_required_fields(self, browser):
        self.page = AccountPage(browser, Links.ACCOUNT_INFO_PAGE)
        self.page.open()
        change_password_menu = browser.find_element(*AccountPageLocators.CHANGE_PASSWORD_MENU_BUTTON)
        change_password_menu.click()
        self.page.should_be_change_password_form()
        button = browser.find_element(*AccountPageLocators.CHANGE_PASSWORD_BUTTON)
        button.click()
        self.page.should_be_password_change_empty_fields_alert()
        # time.sleep(5)

    def test_change_password_invalid_confirm_password(self, browser):
        self.page = AccountPage(browser, Links.ACCOUNT_INFO_PAGE)
        self.page.open()
        change_password_menu = browser.find_element(*AccountPageLocators.CHANGE_PASSWORD_MENU_BUTTON)
        change_password_menu.click()
        self.page.should_be_change_password_form()
        self.page.password_change(User.PASSWORD, User.NEW_PASSWORD, User.INVALID_PASSWORD)
        self.page.should_be_passwords_do_not_match_alert()
        # time.sleep(5)

    def test_change_password_short_new_password(self, browser):
        self.page = AccountPage(browser, Links.ACCOUNT_INFO_PAGE)
        self.page.open()
        change_password_menu = browser.find_element(*AccountPageLocators.CHANGE_PASSWORD_MENU_BUTTON)
        change_password_menu.click()
        self.page.should_be_change_password_form()
        self.page.password_change(User.PASSWORD, User.SHORT_NEW_PASSWORD, User.SHORT_NEW_PASSWORD)
        self.page.should_be_short_new_password_alert()
        time.sleep(5)