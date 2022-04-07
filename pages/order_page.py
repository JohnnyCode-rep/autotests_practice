from .main_page import MainPage
from .locators import OrderPageLocators
from selenium.webdriver.support.ui import Select


class OrderPage(MainPage):
    def fill_billing_address(self, first_name, last_name, email, country, city, address, postal_code, phone_number):
        input_first_name = self.browser.find_element(*OrderPageLocators.FIRST_NAME)
        input_first_name.send_keys(first_name)
        input_last_name = self.browser.find_element(*OrderPageLocators.LAST_NAME)
        input_last_name.send_keys(last_name)
        input_email = self.browser.find_element(*OrderPageLocators.EMAIL)
        input_email.send_keys(email)
        select = Select(self.browser.find_element(*OrderPageLocators.COUNTRY))
        select.select_by_visible_text(country)
        input_city = self.browser.find_element(*OrderPageLocators.CITY)
        input_city.send_keys(city)
        input_address = self.browser.find_element(*OrderPageLocators.ADDRESS_1)
        input_address.send_keys(address)
        input_postal_code = self.browser.find_element(*OrderPageLocators.POSTAL_CODE)
        input_postal_code.send_keys(postal_code)
        input_phone_number = self.browser.find_element(*OrderPageLocators.PHONE_NUMBER)
        input_phone_number.send_keys(phone_number)
        self.click_button(*OrderPageLocators.BILLING_ADDRESS_CONTINUE_BUTTON)

    def should_be_complete_order_section(self):
        assert self.is_element_present(*OrderPageLocators.COMPLETE_ORDER_SECTION), \
            "Complete order section is not presented, but it should be"
