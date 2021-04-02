from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators import RegistrationPageLocators

class RegistrationPage(BasePage):
    """
    Strona rejestracji
    """
    def _verify_page(self):
        print("Weryfikacja RegistartionPage")
        # Tutaj będziemy weryfikować stronę
        wait = WebDriverWait(self.driver, 60)
        # Wywołanie metody until na obiekcie WebDriverWait
        # W efekcie otrzymamy element (jeśli warunek wystąpi)
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.LOGIN_INPUT))


    # Wpisanie imienia
    def fill_login(self, name):
        # Wyszukac input imienia
        element = self.driver.find_element(*RegistrationPageLocators.LOGIN_INPUT)
        # Wpisac w ten input to imię (name)
        element.send_keys(name)

    # Wpisanie hasła
    def fill_password(self, password):
        # Wyszukać input hasła
        element = self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        # Wpisać w ten input hasło (password)
        element.send_keys(password)

    # Potwierdzenie wpisanego hasła
    def confirm_password(self, password):
        element = self.driver.find_element(*RegistrationPageLocators.CONFIM_PASSWORD)
        # Wpisać w ten input hasło (password)
        element.send_keys(password)

    # Wpisanie e-maila
    def fill_email(self, wpisywany_email):
        self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(wpisywany_email)

    # Potwierdzanie e-maila
    def confirm_email(self, wpisywany_email):
        self.driver.find_element(*RegistrationPageLocators.CONFIRM_EMAIL).send_keys(wpisywany_email)

    # Podanie roku urodzenia
    def fill_birth_year(self, birth_year):
        self.driver.find_element(*RegistrationPageLocators.BIRTH_YEAR).send_keys(birth_year)

    # Wybór płci
    def choose_gender_female(self):
        # Wybierz kobietę
        self.driver.find_element(*RegistrationPageLocators.GENDER_FEMALE).click()