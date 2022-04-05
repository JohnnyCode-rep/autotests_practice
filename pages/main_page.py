from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_authorized_user(self):
        assert self.is_element_present(*MainPageLocators.ACCOUNT_ICON), "Account icon is not presented, but should be"

    def go_to_register_page_by_header_link(self):
        link = self.browser.find_element(*MainPageLocators.REGISTER_LINK)
        link.click()
        assert self.browser.current_url == "http://demowebshop.tricentis.com/register", "For some reason you are not " \
                                                                                        "on the registration page"

    def go_to_login_page_by_header_link(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        assert self.browser.current_url == "http://demowebshop.tricentis.com/login", "For some reason you are not " \
                                                                                     "on the login page"



