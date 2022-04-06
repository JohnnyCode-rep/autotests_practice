import pytest

from pages.categories_page import CategoriesPage
from pages.cart_page import CartPage
from test_data.links import Links
from pages.locators import CategoriesPageLocators
from pages.locators import CartPageLocators


class TestAddProduct:
    @pytest.mark.critical_checks
    def test_guest_can_add_product_to_basket_from_category_page(self, browser):
        self.page = CategoriesPage(browser, Links.BOOKS_CATEGORY_LINK)
        self.page.open()
        self.page.add_product_to_basket(*CategoriesPageLocators.ADD_TO_CART_HEALTH_BOOK)
        self.page.should_be_success_adding_to_cart_message()
        self.cart_page = CartPage(browser, Links.CART_PAGE_LINK)
        self.cart_page.open()
        self.cart_page.should_be_item_in_cart(*CartPageLocators.HEALTH_BOOK_IN_CART)
        self.cart_page.remove_single_item_from_cart()  # Return of the original test data
        self.cart_page.should_be_empty_cart_message()
