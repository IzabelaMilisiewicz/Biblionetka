class BasePage():
    """
    Klasa bazowa dla każdej strony
    """
    def __init__(self, driver):
        print("Metoda inicjalizacyjna z BasePage")
        self.driver = driver
        self._verify_page()  #kazda strona będzie sie na początku weryfikowała, żeby sprawdzic automatycznie tytuł strony, albo czy są np obrazki
    # metoda prywatna ma na początku podkreslnik
    def _verify_page(self):
        print("Weryfikacja z BasePage")