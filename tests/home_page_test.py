import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage

from time import sleep

book = "Homo Deus"

class HomePageTest(BaseTest):
    """
    Test strony głównej
    """

    def setUp(self):
        print("setUp z BasePageTest")
        super().setUp()
        hp = HomePage(self.driver)
        hp.accept_privacy_btn()

    @unittest.skip("Skipped")
    def test_search_engine(self):
        hp = HomePage(self.driver)
        hp.search_book(book)
        assert "Homo deus: Krótka historia jutra • Harari Noah Yuval • książka - recenzje, opisy, opinie » BiblioNETka.pl" in self.driver.title

    def test_ranking(self):
        hp = HomePage(self.driver)
        hp.check_ranking()
   

    sleep(10)
    if __name__ == "__main__":
        unittest.main(verbosity=2)