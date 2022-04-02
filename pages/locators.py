from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_ICON = (By.XPATH, "//div[@class='header-links-wrapper']//*[@class='account']")
    REGISTER_LINK = (By.XPATH, "//*[@class='ico-register']")
    LOGIN_LINK = (By.XPATH, "//*[@class='ico-login']")


class RegisterPageLocators:
    REGISTER_GENDER_MALE = (By.ID, "gender-male")
    REGISTER_GENDER_FEMALE = (By.ID, "gender-female")
    REGISTER_FIRST_NAME = (By.ID, "FirstName")
    REGISTER_LAST_NAME = (By.ID, "LastName")
    REGISTER_EMAIL = (By.ID, "Email")
    REGISTER_PASSWORD = (By.ID, "Password")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
    SUCCESS_REGISTER_MESSAGE = (By.XPATH, "//*[@class='result']")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "Email")
    LOGIN_PASSWORD = (By.ID, "Password")
    REMEMBER_ME_CHECKBOX = (By.ID, "RememberMe")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//*[@class='forgot-password']")
    LOGIN_BUTTON = (By.XPATH, "//*[@class='button-1 login-button']")


class AccountPageLocators:
    CHANGE_PASSWORD_MENU_BUTTON = (By.XPATH, "//*[@href='/customer/changepassword']")
    CHANGE_PASSWORD_OLD_PASSWORD = (By.ID, "OldPassword")
    CHANGE_PASSWORD_NEW_PASSWORD = (By.ID, "NewPassword")
    CHANGE_PASSWORD_CONFIRM_PASSWORD = (By.ID, "ConfirmNewPassword")
    CHANGE_PASSWORD_BUTTON = (By.XPATH, "//*[@class='button-1 change-password-button']")
    CHANGE_PASSWORD_SUCCESS_MESSAGE = (By.XPATH, "//*[@class='result']")
    OLD_PASSWORD_EMPTY_ALERT = (By.XPATH, "//*[@class='field-validation-error'][@data-valmsg-for='OldPassword']")
    NEW_PASSWORD_EMPTY_ALERT = (By.XPATH, "//*[@class='field-validation-error'][@data-valmsg-for='NewPassword']")
    CONFIRM_PASSWORD_EMPTY_ALERT = (By.XPATH, "//*[@class='field-validation-error']["
                                              "@data-valmsg-for='ConfirmNewPassword']")
    INVALID_OLD_PASSWORD_ALERT = (By.XPATH, "//*[@class='validation-summary-errors']")
    PASSWORDS_DO_NOT_MATCH_ALERT = (By.XPATH, "//*[text()='The new password and confirmation password do not match.']")
    SHORT_NEW_PASSWORD_ALERT = (By.XPATH, "// *[text() = 'The password should have at least 6 characters.']")
