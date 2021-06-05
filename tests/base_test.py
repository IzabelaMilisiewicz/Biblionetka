import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):
    """
    Klasa bazowa każdego testu
    """
    def setUp(self):
        print("setUp z BaseTest")
        # self.options = Options()
        # self.options.add_argument('--headless')
        # self.driver = webdriver.Chrome(options=self.options)
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.biblionetka.pl/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()