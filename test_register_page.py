import pytest
import time
import names

from .pages.main_page import MainPage
from .pages.register_page import RegisterPage
from .test_data.links import Links


class TestRegisterFunctions:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = Links.MAIN_PAGE_LINK
        self.page = MainPage(browser, self.link)
        self.page.open()
        # time.sleep(5)

    @pytest.mark.critical_checks
    def test_guest_can_register(self, browser):
        self.page.go_to_register_page_by_header_link()
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


def test_guest_can_go_to_register_page_by_url(browser):
    page = RegisterPage(browser, Links.REGISTER_PAGE_LINK)
    page.open()
    page.should_be_register_form()
    # time.sleep(5)
