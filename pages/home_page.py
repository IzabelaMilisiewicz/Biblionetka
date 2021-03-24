# importowanie wlaśnej biblioteki z innego pliku
from pages.base_page import BasePage
from locators import HomePageLocators
# teraz pobieramy exclipit wait, zawsze te 2 linie pobieramy w parzee
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    """
    Strona domowa
    """

    def accept_privacy_btn(self):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.presence_of_element_located(HomePageLocators.ACCEPT_PRIVACY)).click()

    def click_zaloguj_btn(self):
        # Tworzenie instancji klasy WebDriverWait
        wait = WebDriverWait(self.driver, 60)
        # Wywołanie metody until na obiekcie WebDriverWait
        # W efekcie otrzymamy element (jeśli warunek wystąpi)
        element = wait.until(EC.element_to_be_clickable(HomePageLocators.ZALOGUJ_BTN))
        # element = self.driver.find_element(*HomePageLocators.ZALOGUJ_BTN)
        element.click()

    def _verify_page(self):
        print("Weryfikacja HomePage")
        assert "BiblioNETka.pl » książki - recenzje, opisy, opinie" in self.driver.title

    def search_book(self, book):
        element = self.driver.find_element(*HomePageLocators.SEARCH_ENGINE)
        element.send_keys(book)
        self.driver.find_element(*HomePageLocators.SEARCH_BUTTON).click()
        self.driver.find_element(*HomePageLocators.HOMO_DEUS).click()

    def book_assertion(self):
        search_result = self.driver.find_element(*HomePageLocators.HOMO_DEUS_H1)
        print(search_result)

    def check_catalog(self):
        self.driver.find_element(*HomePageLocators.CATALOG)
        self.driver.find_element(*HomePageLocators.RANKINGI).click()

    def choose_results(self):
        self.driver.find_element(*HomePageLocators.SHOW).click()

    def choose_often_rated(self):
        self.driver.find_element(*HomePageLocators.OFTENRATED).click()

    def choose_categories(self):
        self.driver.find_element(*HomePageLocators.CATEGORIES).click()

    def non_fiction(self):
        self.driver.find_element(*HomePageLocators.NONFICTION).click()

    def book_content_visible(self):
        self.driver.find_element(*HomePageLocators.BOOKCONTENT).is_displayed()









