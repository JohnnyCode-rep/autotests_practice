from .main_page import MainPage
from .locators import LoginPageLocators


class LoginPage(MainPage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Email input field is not found"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Password input field is not found"
        assert self.is_element_present(*LoginPageLocators.REMEMBER_ME_CHECKBOX), "Checkbox 'Remember me' is not found"
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_BUTTON), "Forgot password button is not found"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not found"

    def login_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        input_password.send_keys(password)
        remember_me_checkbox = self.browser.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX)
        remember_me_checkbox.click()
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
