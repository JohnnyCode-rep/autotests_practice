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
    CHECKOUT_AS_GUEST_BUTTON = (By.XPATH, "//*[@class='button-1 checkout-as-guest-button']")


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


class CategoriesPageLocators:
    ADD_TO_CART_HEALTH_BOOK = (By.XPATH, "//*[@data-productid='22']//input[@value='Add to cart']")
    SUCCESS_ADDING_TO_CART_MESSAGE = (By.XPATH, "//*[@class='bar-notification success']")


class ProductPageLocators:
    ADD_TO_CART_HEALTH_BOOK = (By.ID, "add-to-cart-button-22")
    SUCCESS_ADDING_TO_CART_MESSAGE = (By.XPATH, "//*[@class='bar-notification success']")


class CartPageLocators:
    CHECKBOX_REMOVE_FROM_CART = (By.XPATH, "//*[@name='removefromcart']")
    UPDATE_CART_BUTTON = (By.XPATH, "//*[@name='updatecart']")
    EMPTY_CART_MESSAGE = (By.XPATH, "//*[contains(text(), 'Your Shopping Cart is empty!')]")
    HEALTH_BOOK_IN_CART = (By.XPATH, "//*[@class='product']/a[@href='/health']")
    ITEM_QUANTITY_FIELD = (By.XPATH, "//*[@class='qty nobr']/input")
    PRICE_OF_ITEM = (By.XPATH, "//span[@class='product-unit-price']")
    TOTAL_PRICE = (By.XPATH, "//span[@class='product-subtotal']")
    TERMS_OF_SERVICE_CHECKBOX = (By.ID, "termsofservice")
    CHECKOUT_BUTTON = (By.ID, "checkout")


class OrderPageLocators:
    CHECKBOX_REMOVE_FROM_CART = (By.XPATH, "//*[@name='removefromcart']")
    FIRST_NAME = (By.ID, "BillingNewAddress_FirstName")
    LAST_NAME = (By.ID, "BillingNewAddress_LastName")
    EMAIL = (By.ID, "BillingNewAddress_Email")
    COUNTRY = (By.ID, "BillingNewAddress_CountryId")
    CITY = (By.ID, "BillingNewAddress_City")
    ADDRESS_1 = (By.ID, "BillingNewAddress_Address1")
    POSTAL_CODE = (By.ID, "BillingNewAddress_ZipPostalCode")
    PHONE_NUMBER = (By.ID, "BillingNewAddress_PhoneNumber")
    BILLING_ADDRESS_CONTINUE_BUTTON = (By.XPATH, "//div[@id='billing-buttons-container']/input")
    SHIPPING_ADDRESS_CONTINUE_BUTTON = (By.XPATH, "//div[@id='shipping-buttons-container']/input")
    SHIPPING_METHOD_CONTINUE_BUTTON = (By.XPATH, "//div[@id='shipping-method-buttons-container']/input")
    PAYMENT_METHOD_CONTINUE_BUTTON = (By.XPATH, "//div[@id='payment-method-buttons-container']/input")
    PAYMENT_INFO_CONTINUE_BUTTON = (By.XPATH, "//div[@id='payment-info-buttons-container']/input")
    CONFIRM_BUTTON = (By.XPATH, "//div[@id='confirm-order-buttons-container']/input")
    COMPLETE_ORDER_SECTION = (By.XPATH, "//*[@class='section order-completed']")