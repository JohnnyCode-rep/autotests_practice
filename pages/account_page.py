from .main_page import MainPage
from .locators import AccountPageLocators


class AccountPage(MainPage):
    def should_be_change_password_form(self):
        assert self.is_element_present(*AccountPageLocators.CHANGE_PASSWORD_OLD_PASSWORD), "Old password input field " \
                                                                                           "is not found!"
        assert self.is_element_present(*AccountPageLocators.CHANGE_PASSWORD_NEW_PASSWORD), "New password input field " \
                                                                                           "is not found!"
        assert self.is_element_present(*AccountPageLocators.CHANGE_PASSWORD_CONFIRM_PASSWORD), "Confirm password " \
                                                                                               "input field is not " \
                                                                                               "found! "
        assert self.is_element_present(*AccountPageLocators.CHANGE_PASSWORD_BUTTON), "Change password button is not " \
                                                                                     "found "

    def password_change(self, old_password, new_password, confirm_password):
        input_old_password = self.browser.find_element(*AccountPageLocators.CHANGE_PASSWORD_OLD_PASSWORD)
        input_old_password.send_keys(old_password)
        input_new_password = self.browser.find_element(*AccountPageLocators.CHANGE_PASSWORD_NEW_PASSWORD)
        input_new_password.send_keys(new_password)
        input_confirm_password = self.browser.find_element(*AccountPageLocators.CHANGE_PASSWORD_CONFIRM_PASSWORD)
        input_confirm_password.send_keys(confirm_password)
        button = self.browser.find_element(*AccountPageLocators.CHANGE_PASSWORD_BUTTON)
        button.click()

    def should_be_password_change_message(self):
        assert self.is_element_present(*AccountPageLocators.CHANGE_PASSWORD_SUCCESS_MESSAGE), \
            "Password change message is not presented, but should be"

    def should_be_invalid_old_password_alert(self):
        assert self.is_element_present(*AccountPageLocators.INVALID_OLD_PASSWORD_ALERT), \
            "There is no message about invalid old password, but should be"

    def should_be_password_change_empty_fields_alert(self):
        assert self.is_element_present(*AccountPageLocators.OLD_PASSWORD_EMPTY_ALERT), \
            "There is no message about an empty OLD password field, but should be"
        assert self.is_element_present(*AccountPageLocators.NEW_PASSWORD_EMPTY_ALERT), \
            "There is no message about an empty NEW password field, but should be"
        assert self.is_element_present(*AccountPageLocators.CONFIRM_PASSWORD_EMPTY_ALERT), \
            "There is no message about an empty CONFIRM password field, but should be"

    def should_be_passwords_do_not_match_alert(self):
        assert self.is_element_present(*AccountPageLocators.PASSWORDS_DO_NOT_MATCH_ALERT), \
            "There is no message about the discrepancy between the new and confirmed passwords, but there should be"

    def should_be_short_new_password_alert(self):
        assert self.is_element_present(*AccountPageLocators.SHORT_NEW_PASSWORD_ALERT), \
            "There is no message about short new password, but there should be"