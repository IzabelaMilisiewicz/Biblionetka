from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators

from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    Strona logowania
    """
    def click_register_btn(self):
        # KLiknięcie w przycisk Rejestracja
        # Tworzenie instancji klasy WebDriverWait
        wait = WebDriverWait(self.driver, 60)
        # Wywołanie metody until na obiekcie WebDriverWait
        # W efekcie otrzymamy element (jeśli warunek wystąpi)
        element = wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_BTN))
        element.click()