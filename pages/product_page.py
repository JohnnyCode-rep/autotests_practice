from .main_page import MainPage
from .locators import ProductPageLocators


class ProductPage(MainPage):
    def add_product_to_basket(self, how, what):
        add_to_cart_button = self.browser.find_element(how, what)
        add_to_cart_button.click()

    def should_be_success_adding_to_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADDING_TO_CART_MESSAGE), \
            "Success adding to cart message is not presented, but should be"
