from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")
    EMAIL = (By.XPATH, "//*[@id='id_registration-email']")
    PASSWORD = (By.XPATH, "//*[@id='id_registration-password1']")
    PASSWORD_CONFIRM = (By.XPATH, "//*[@id='id_registration-password2']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert alert-success  fade in']")


class ProductPageLocators():
    ADD_BASKET = (By.XPATH, "//*[@id='add_to_basket_form']")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span[@class = 'btn-group']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PRODUCT_IN_THE_BASKET = (By.XPATH, "//form[@id='basket_formset']")
    MESSAGE_BASKET_EMPTY = (By.XPATH, "//div[@id='content_inner']")



