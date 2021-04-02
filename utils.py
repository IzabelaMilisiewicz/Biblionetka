from pages.base_page import BasePage
from locators import RegistrationPageLocators

class VerifyErrors(BasePage):
    def verify_visible_errors(self, number_of_errors, error_texts):
        # number_of_errors - liczba widocznych błędów
        # error_texts - lista z treściami błędów
        # np. verify_visible_errors(1, ["Nieprawidłowy e-mail"])
        # np. verify_visible_errors(2, ["Wybierz płeć", "Podaj hasło"])
        # PSEUDOKOD:
        # Wyszukaj iformacje o błędach (lista)
        error_texts = list(error_texts)
        error_messages = self.driver.find_elements(*RegistrationPageLocators.ERROR_MESSAGES_SPAN)
        # Stwórz pustą listę widocznych błędów
        visible_error_messages = []
        # Dla każdego błędu w liście informacji o błędach (for..)
        for error in error_messages:
            # Jeśli błąd jest widoczny
            if error.is_displayed():
                # Dodaj do listy widocznych błędów
                visible_error_messages.append(error)
        # Sprawdź, czy liczba widocznych błędów jest właściwa
        assert len(visible_error_messages) == number_of_errors
        # Stwórz (pustą) listę zawierającą (teksty) informacji o błędach
        error_text_fact = []
        # Przez tyle razy, ile jest widocznych błędów (for..)
        for i in range(len(visible_error_messages)):
            # Dodaj tekst błędu do listy informacji o błędach
            error_text_fact.append(visible_error_messages[i].text)
        # Porównaj obie listy z tekstami błędów: zadaną oraz faktyczną
        assert error_texts == error_text_fact