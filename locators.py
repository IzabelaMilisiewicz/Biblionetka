from selenium.webdriver.common.by import By

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
    ACCEPT_PRIVACY = (By.XPATH, '//button[@class =" css-b5w9vk"]')
    SEARCH_ENGINE = (By.ID, 'ctl00_searchPhrase')
    SEARCH_BUTTON = (By.ID, 'ctl00_SearchButton')
    HOMO_DEUS = (By.XPATH, '//a[@href="book.aspx?id=505376"]')
    HOMO_DEUS_H1 = (By.TAG_NAME, '//h1')
    CATALOG = (By.XPATH, '//a[@data-target="#third"]')
    RANKINGI = (By.XPATH, '//a[@href="stats.aspx"]')
    SHOW = (By.XPATH, '//div[text()="najwyżej oceniane książki"]')
    OFTENRATED = (By.PARTIAL_LINK_TEXT, 'najczęściej oceniane książki')
    LANGUAGE = (By.XPATH, '//div[text()="wszystkie języki"]')
    CATEGORIES = (By.XPATH, '//div[text()="wszystkie gatunki i kategorie"]')
    YEAR = (By.XPATH, '//div[text()="bieżący - 2021"]')
    NONFICTION = (By.PARTIAL_LINK_TEXT, 'literatura faktu')
    BOOKCONTENT = (By.XPATH, '//div[@class="tb bookinfo__content"]')