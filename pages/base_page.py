from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.ACCOUNT_ICON), "Account icon is not presented, but should be"

    def go_to_register_page(self):
        link = self.browser.find_element(*BasePageLocators.REGISTER_LINK)
        link.click()
        assert self.browser.current_url == "http://demowebshop.tricentis.com/register", "For some reason you are not " \
                                                                                        "on the registration page"
