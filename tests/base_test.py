import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    """
    Klasa bazowa każdego testu
    """
    def setUp(self):
        print("setUp z BaseTest")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.biblionetka.pl/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()