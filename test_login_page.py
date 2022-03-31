import pytest
import time

from .pages.login_page import LoginPage
from .test_data.user import User
from .test_data.links import Links


@pytest.mark.critical_checks
def test_guest_can_login(browser):
    page = LoginPage(browser, Links.LOGIN_PAGE_LINK)
    page.open()
    page.should_be_login_form()
    page.login_user(User.EMAIL, User.PASSWORD)
    page.should_be_authorized_user()
    # time.sleep(5)


def test_guest_can_go_to_login_page_by_url(browser):
    page = LoginPage(browser, Links.LOGIN_PAGE_LINK)
    page.open()
    page.should_be_login_form()
    # time.sleep(5)
