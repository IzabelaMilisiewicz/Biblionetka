from selenium.webdriver.common.by import By

class HomePageLocators():
    """
    Lokatory strony głównej
    """
    ZALOGUJ_BTN = (By.XPATH, "//div[@class='down__item login__menu__item']")

class LoginPageLocators():
    """
    Lokatory strony logowania
    """
    REGISTER_BTN = (By.XPATH, '//a[@class="btn__red btn__submit"]')

class RegistrationPageLocators():
    """
    Lokatory strony rejestracji
    """
    LOGIN_INPUT = (By.NAME, 'ctl00$MCP$CUW$CreateUserStepContainer$UserName')
    PASSWORD_INPUT = (By.NAME, 'ctl00$MCP$CUW$CreateUserStepContainer$Password')
    CONFIM_PASSWORD = (By.NAME, 'ctl00$MCP$CUW$CreateUserStepContainer$ConfirmPassword')
    EMAIL_INPUT = (By.NAME, 'ctl00$MCP$CUW$CreateUserStepContainer$Email')
    CONFIRM_EMAIL = (By.NAME, 'ctl00$MCP$CUW$CreateUserStepContainer$Email2')
    BIRTH_YEAR = (By.NAME, 'ctl00$MCP$CUW$CreateUserStepContainer$BirthYear')
    GENDER_FEMALE = (By.XPATH, '//input[@id ="ctl00_MCP_CUW_CreateUserStepContainer_Sex_0"]')
    GENDER_MALE = (By.XPATH, '//input[@id ="ctl00_MCP_CUW_CreateUserStepContainer_Sex_1"]')
    ERROR_MESSAGES_SPAN = (By.XPATH, '//span[@class="err nomore"]/span')

class HomePageLocators():
    """
    Lokatory strony głównej
    """
    ZALOGUJ_BTN = (By.XPATH, '//div[@class="down__item login__menu__item"]')
    ACCEPT_PRIVACY = (By.XPATH, '//button[@class =" css-3xxwnt"]')
    SEARCH_ENGINE = (By.ID, 'ctl00_searchPhrase')
    SEARCH_BUTTON = (By.ID, 'ctl00_SearchButton')
    READ_MORE_HOMO_DEUS = (By.XPATH, '//a[@href="book.aspx?id=505376"]')