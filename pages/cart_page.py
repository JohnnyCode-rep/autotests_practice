from .main_page import MainPage
from .locators import CartPageLocators


class CartPage(MainPage):
    def should_be_item_in_cart(self, how, what):
        assert self.is_element_present(how, what), \
            "Item is not in the cart, but it should be"

    def remove_single_item_from_cart(self):
        checkbox = self.browser.find_element(*CartPageLocators.CHECKBOX_REMOVE_FROM_CART)
        checkbox.click()
        button = self.browser.find_element(*CartPageLocators.UPDATE_CART_BUTTON)
        button.click()

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE), \
            "Empty cart message is not presented, but it should be"


