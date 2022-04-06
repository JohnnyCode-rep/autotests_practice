from .main_page import MainPage
from .locators import CartPageLocators
from selenium.webdriver.common.by import By


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

    def change_quantity_of_items_in_cart(self, number):
        item_quantity = self.browser.find_element(*CartPageLocators.ITEM_QUANTITY_FIELD)
        item_quantity.clear()
        item_quantity.send_keys(number)
        button = self.browser.find_element(*CartPageLocators.UPDATE_CART_BUTTON)
        button.click()
        assert self.is_element_present(By.XPATH, f"//*[@class='qty nobr']/input[@value='{number}']"), \
            "The quantity of the item in the basket does not match the entered value"

    def total_price_of_cart_corresponds_to_number_of_items(self):
        price_of_item = self.browser.find_element(*CartPageLocators.PRICE_OF_ITEM)
        total_price = self.browser.find_element(*CartPageLocators.TOTAL_PRICE)
        item_quantity = int(float(total_price.text) / float(price_of_item.text))
        assert self.is_element_present(By.XPATH, f"//*[@class='qty nobr']/input[@value='{item_quantity}']"), \
            "The quantity of the item in the basket does not match the entered value"

