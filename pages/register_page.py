from .main_page import MainPage
from .locators import RegisterPageLocators


class RegisterPage(MainPage):
    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FIRST_NAME), "First name input field is not " \
                                                                                   "found! "
        assert self.is_element_present(*RegisterPageLocators.REGISTER_LAST_NAME), "Last name input field is not " \
                                                                                  "found! "
        assert self.is_element_present(*RegisterPageLocators.REGISTER_EMAIL), "Email input field is not found"
        assert self.is_element_present(*RegisterPageLocators.REGISTER_PASSWORD), "Password input field is not found"
        assert self.is_element_present(*RegisterPageLocators.REGISTER_CONFIRM_PASSWORD), "Confirm password input " \
                                                                                         "field is not found "
        assert self.is_element_present(*RegisterPageLocators.REGISTER_BUTTON), "Register button is not found"

    def register_new_user(self, first_name, last_name, email, password):
        gender_male_radiobutton = self.browser.find_element(*RegisterPageLocators.REGISTER_GENDER_MALE)
        gender_male_radiobutton.click()
        input_first_name = self.browser.find_element(*RegisterPageLocators.REGISTER_FIRST_NAME)
        input_first_name.send_keys(first_name)
        input_last_name = self.browser.find_element(*RegisterPageLocators.REGISTER_LAST_NAME)
        input_last_name.send_keys(last_name)
        input_email = self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD)
        input_password.send_keys(password)
        input_confirm_password = self.browser.find_element(*RegisterPageLocators.REGISTER_CONFIRM_PASSWORD)
        input_confirm_password.send_keys(password)
        register_button = self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_success_register_message(self):
        assert self.is_element_present(*RegisterPageLocators.SUCCESS_REGISTER_MESSAGE), \
            "Success register message is not presented, but should be"
