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


