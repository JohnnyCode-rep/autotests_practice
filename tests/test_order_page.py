import pytest

from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage
from test_data.links import Links
from pages.locators import ProductPageLocators
from pages.locators import CartPageLocators
from pages.locators import LoginPageLocators
from pages.locators import OrderPageLocators
from test_data.user import User


class TestOrder:
    @pytest.mark.critical_checks
    def test_guest_can_make_an_order(self, browser):
        self.page = ProductPage(browser, Links.HEALTH_BOOK_LINK)
        self.page.open()
        self.page.add_product_to_cart(*ProductPageLocators.ADD_TO_CART_HEALTH_BOOK)
        self.page.should_be_success_adding_to_cart_message()
        self.cart_page = CartPage(browser, Links.CART_PAGE_LINK)
        self.cart_page.open()
        self.cart_page.should_be_item_in_cart(*CartPageLocators.HEALTH_BOOK_IN_CART)
        self.cart_page.click_button(*CartPageLocators.TERMS_OF_SERVICE_CHECKBOX)
        self.cart_page.click_button(*CartPageLocators.CHECKOUT_BUTTON)
        self.cart_page.click_button(*LoginPageLocators.CHECKOUT_AS_GUEST_BUTTON)
        self.order_page = OrderPage(browser, browser.current_url)
        self.order_page.open()
        self.order_page.fill_billing_address(User.FIRST_NAME, User.LAST_NAME, User.EMAIL, User.COUNTRY, User.CITY,
                                             User.ADDRESS, User.POSTAL_CODE, User.PHONE_NUMBER)
        self.order_page.click_button(*OrderPageLocators.SHIPPING_ADDRESS_CONTINUE_BUTTON)
        self.order_page.click_button(*OrderPageLocators.SHIPPING_METHOD_CONTINUE_BUTTON)
        self.order_page.click_button(*OrderPageLocators.PAYMENT_METHOD_CONTINUE_BUTTON)
        self.order_page.click_button(*OrderPageLocators.PAYMENT_INFO_CONTINUE_BUTTON)
        self.order_page.click_button(*OrderPageLocators.CONFIRM_BUTTON)
        self.order_page.should_be_complete_order_section()
