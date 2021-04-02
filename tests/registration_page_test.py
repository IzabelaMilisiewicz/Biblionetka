import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from time import sleep
from test_data import TestData
from ddt import ddt, data, unpack
from utils import VerifyErrors

@ddt
class RegistrationPageTest(BaseTest, TestData):
    """
    Test strony Rejestracji
    """
    def setUp(self):
        print("setUp z RegistrationPageTest")
        # Wywołanie metody setUp z klasy nadrzędnej (BaseTest)
        super().setUp()
        # Kliknięcie zaloguj
        # Stworzenie instancji klasy HomePage (hp)
        hp = HomePage(self.driver)
        hp.accept_privacy_btn()
        # Użycie metody click_zaloguj_btn zawartej w obiekcie hp klasy HomePage
        hp.click_zaloguj_btn()
        # Kliknięcie Rejestracja na stronie Logowania
        # Stworzenie instancji klasy LoginPage (lp)
        lp = LoginPage(self.driver)
        # Użycie metody click_register_btn zawartej w obiekcie lp klasy LoginPage
        lp.click_register_btn()

    # @unittest.skip("Pomijam")
    @data(*TestData.get_data("excel_data.csv"))
    @unpack
    def test_wrong_password_during_confirmation(self, email, password):
        # Stworzenie instancji klasy RegistrationPage (rp)
        rp = RegistrationPage(self.driver)
        td = TestData()
        ut = VerifyErrors(self.driver)
        rp.fill_login(td.username)
        rp.fill_password(td.password)
        rp.confirm_password("3")
        rp.fill_email(email)
        # UWAGA TEST!
        ut.verify_visible_errors(1, ["Hasło i potwierdzenie hasła muszą być takie same."])

    @unittest.skip("Pomijam")
    def test_incorrect_email(self):
        rp = RegistrationPage(self.driver)
        td = TestData()
        ut = VerifyErrors(self.driver)
        rp.fill_login(td.username)
        rp.fill_password(td.valid_password)
        rp.confirm_password(td.valid_password)
        rp.fill_email(td.invalid_email)
        rp.confirm_email(" ")
        ut.verify_visible_errors(1, ["Podaj prawidłowy adres email!"])

    @unittest.skip("Pomijam")
    def test_incorrect_birth_year(self):
        rp = RegistrationPage(self.driver)
        td = TestData()
        ut = VerifyErrors(self.driver)
        rp.fill_login(td.username)
        rp.fill_password(td.password)
        rp.confirm_password(td.password)
        rp.fill_email(td.valid_email)
        rp.confirm_email(td.valid_email)
        rp.fill_birth_year("18")
        rp.choose_gender_female()
        ut.verify_visible_errors(1, ["* Niepoprawny rok urodzenia"])

    sleep(10)
    if __name__ == "__main__":
        unittest.main(verbosity=2)