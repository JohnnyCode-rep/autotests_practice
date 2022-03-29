from selenium.webdriver.common.by import By


class BasePageLocators:
    ACCOUNT_ICON = (By.XPATH, "//div[@class='header-links-wrapper']//*[@class='account']")
    REGISTER_LINK = (By.XPATH, "//*[@class='ico-register']")


class RegisterPageLocators:
    REGISTER_FIRST_NAME = (By.ID, "FirstName")
    REGISTER_LAST_NAME = (By.ID, "LastName")
    REGISTER_EMAIL = (By.ID, "Email")
    REGISTER_PASSWORD = (By.ID, "Password")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
    SUCCESS_REGISTER_MESSAGE = (By.XPATH, "//*[@class='result']")
