import pytest
import time
import names

from .pages.base_page import BasePage
from .pages.register_page import RegisterPage

BASE_LINK = "http://demowebshop.tricentis.com/"


@pytest.mark.critical_checks
class TestAccountFunctions:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = BASE_LINK
        self.page = BasePage(browser, self.link)
        self.page.open()
        # time.sleep(5)

    def test_guest_can_register(self, browser):
        self.page.go_to_register_page()
        self.page = RegisterPage(browser, browser.current_url)
        self.page.open()
        self.page.should_be_register_form()
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        email = str(time.time()) + "@examplemail.org"
        password = str(time.time()) + "test"
        self.page.register_new_user(first_name, last_name, email, password)
        self.page.should_be_success_register_message()
        self.page.should_be_authorized_user()
        # time.sleep(5)
