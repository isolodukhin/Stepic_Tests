from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_THE_BASKET), "Product is presented, but should not be"

    def should_be_text_about_empty_basket(self):
        message_basket_empty = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_EMPTY).text
        assert (message_basket_empty == 'Your basket is empty. Continue shopping'), "basket is not empty"
