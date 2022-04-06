import pytest
import random

from pages.product_page import ProductPage
from pages.cart_page import CartPage
from test_data.links import Links
from pages.locators import ProductPageLocators
from pages.locators import CartPageLocators


class TestCart:
    @pytest.mark.critical_checks
    def test_guest_can_change_quantity_of_gods_in_cart(self, browser):
        self.page = ProductPage(browser, Links.HEALTH_BOOK_LINK)
        self.page.open()
        self.page.add_product_to_cart(*ProductPageLocators.ADD_TO_CART_HEALTH_BOOK)
        self.page.should_be_success_adding_to_cart_message()
        self.cart_page = CartPage(browser, Links.CART_PAGE_LINK)
        self.cart_page.open()
        self.cart_page.should_be_item_in_cart(*CartPageLocators.HEALTH_BOOK_IN_CART)
        self.cart_page.change_quantity_of_items_in_cart(random.randint(2, 29))
        self.cart_page.total_price_of_cart_corresponds_to_number_of_items()
        self.cart_page.remove_single_item_from_cart()  # Return of the original test data
        self.cart_page.should_be_empty_cart_message()
