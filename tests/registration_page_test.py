import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from time import sleep
from utils import MyUtils


# # DANE TESTOWE
# fake = Faker("es_ES")
# simple_profile = fake.simple_profile()
# username = simple_profile["username"]
#
# os.chdir("/home/tester/PycharmProjects/Biblionetka/")
# workbook = openpyxl.load_workbook("accounts.xlsx")
# sheet = workbook["Arkusz1"]
# password = sheet["B2"].value
#
# valid_password = "qwerty123"
# valid_email = "iza@wp.pl"
# invalid_email = "qwerty.pl"


class RegistrationPageTest(BaseTest):
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
    def test_wrong_password_during_confirmation(self):
        # Stworzenie instancji klasy RegistrationPage (rp)
        rp = RegistrationPage(self.driver)
        ut = MyUtils()
        rp.fill_login(ut.username)
        rp.fill_password(ut.valid_password)
        rp.confirm_password("3")
        rp.fill_email(" ")
        # UWAGA TEST!
        rp.verify_visible_errors(1, ["Hasło i potwierdzenie hasła muszą być takie same."])

    @unittest.skip("Pomijam")
    def test_incorrect_email(self):
        rp = RegistrationPage(self.driver)
        ut = MyUtils()
        rp.fill_login(ut.username)
        rp.fill_password(ut.valid_password)
        rp.confirm_password(ut.valid_password)
        rp.fill_email(ut.invalid_email)
        rp.confirm_email(" ")
        rp.verify_visible_errors(1, ["Podaj prawidłowy adres email!"])

    @unittest.skip("Pomijam")
    def test_incorrect_birth_year(self):
        rp = RegistrationPage(self.driver)
        ut = MyUtils()
        rp.fill_login(ut.username)
        rp.fill_password(ut.password)
        rp.confirm_password(ut.password)
        rp.fill_email(ut.valid_email)
        rp.confirm_email(ut.valid_email)
        rp.fill_birth_year("18")
        rp.choose_gender_female()
        rp.verify_visible_errors(1, ["* Niepoprawny rok urodzenia"])

    sleep(10)
    if __name__ == "__main__":
        unittest.main(verbosity=2)