from selenium.webdriver.common.by import By
import allure


@allure.feature("Herokuapp Website")
@allure.story("Incognito Mode")
@allure.title("Test Incognito Mode")
def test_title_incognito(incognito):
    assert incognito.title == "The Internet"


@allure.feature("Herokuapp Website")
@allure.story("Headless Mode")
@allure.title("Test Headless Mode")
def test_title_headless(headless):
    assert headless.title == "The Internet"


@allure.feature("Herokuapp Website")
@allure.story("Headless Incognito Mode")
@allure.title("Test Headless Incognito Mode")
def test_title_headless_incognito(headless_incognito):
    assert headless_incognito.title == "The Internet"


@allure.feature("Herokuapp Website")
@allure.story("Incognito Mode")
@allure.title("Test Buttons with Incognito Mode")
def test_button_clicks_incognito(incognito):
    for i in range(1, 5):
        btn = incognito.find_element(By.XPATH, f'//*[@id="menu"]/ul/li[{i}]/a')
        btn.click()

        if i == 1:
            assert incognito.current_url == "https://the-internet.herokuapp.com/floating_menu#home"
        elif i == 2:
            assert incognito.current_url == "https://the-internet.herokuapp.com/floating_menu#news"
        elif i == 3:
            assert incognito.current_url == "https://the-internet.herokuapp.com/floating_menu#contact"
        elif i == 4:
            assert incognito.current_url == "https://the-internet.herokuapp.com/floating_menu#about"


@allure.feature("Herokuapp Website")
@allure.story("Headless Mode")
@allure.title("Test Buttons with Headless Mode")
def test_button_clicks_headless(headless):
    for i in range(1, 5):
        btn = headless.find_element(By.XPATH, f'//*[@id="menu"]/ul/li[{i}]/a')
        btn.click()

        if i == 1:
            assert headless.current_url == "https://the-internet.herokuapp.com/floating_menu#home"
        elif i == 2:
            assert headless.current_url == "https://the-internet.herokuapp.com/floating_menu#news"
        elif i == 3:
            assert headless.current_url == "https://the-internet.herokuapp.com/floating_menu#contact"
        elif i == 4:
            assert headless.current_url == "https://the-internet.herokuapp.com/floating_menu#about"


@allure.feature("Herokuapp Website")
@allure.story("Headless Incognito Mode")
@allure.title("Test Buttons with Headless Incognito Mode")
def test_button_clicks_headless_incognito(headless_incognito):
    for i in range(1, 5):
        btn = headless_incognito.find_element(By.XPATH, f'//*[@id="menu"]/ul/li[{i}]/a')
        btn.click()

        if i == 1:
            assert headless_incognito.current_url == "https://the-internet.herokuapp.com/floating_menu#home"
        elif i == 2:
            assert headless_incognito.current_url == "https://the-internet.herokuapp.com/floating_menu#news"
        elif i == 3:
            assert headless_incognito.current_url == "https://the-internet.herokuapp.com/floating_menu#contact"
        elif i == 4:
            assert headless_incognito.current_url == "https://the-internet.herokuapp.com/floating_menu#about"


@allure.feature("Herokuapp Website")
@allure.story("Incognito Mode")
@allure.title("Test Floating menu with Incognito Mode")
def test_floating_menu_incognito(incognito):
    floating_menu = incognito.find_element(By.XPATH, '//*[@id="content"]/div/h3')
    assert floating_menu.text == "Floating Menu"


@allure.feature("Herokuapp Website")
@allure.story("Headless Mode")
@allure.title("Test Floating menu with Headless Mode")
def test_floating_menu_headless(headless):
    floating_menu = headless.find_element(By.XPATH, '//*[@id="content"]/div/h3')
    assert floating_menu.text == "Floating Menu"


@allure.feature("Herokuapp Website")
@allure.story("Headless Incognito Mode")
@allure.title("Test Floating menu with Headless Incognito Mode")
def test_floating_menu_headless_incognito(headless_incognito):
    floating_menu = headless_incognito.find_element(By.XPATH, '//*[@id="content"]/div/h3')
    assert floating_menu.text == "Floating Menu"


@allure.feature("Herokuapp Website")
@allure.story("Incognito Mode")
@allure.title("Test Powered by with Incognito Mode")
def test_powered_by_incognito(incognito):
    powered_by = incognito.find_element(By.XPATH, '//*[@id="page-footer"]/div/div')
    assert powered_by.text == "Powered by Elemental Selenium"


@allure.feature("Herokuapp Website")
@allure.story("Headless Mode")
@allure.title("Test Powered by with Headless Mode")
def test_powered_by_headless(headless):
    powered_by = headless.find_element(By.XPATH, '//*[@id="page-footer"]/div/div')
    assert powered_by.text == "Powered by Elemental Selenium"


@allure.feature("Herokuapp Website")
@allure.story("Headless Incognito Mode")
@allure.title("Test Powered by with Headless Incognito Mode")
def test_powered_by_headless_incognito(headless_incognito):
    powered_by = headless_incognito.find_element(By.XPATH, '//*[@id="page-footer"]/div/div')
    assert powered_by.text == "Powered by Elemental Selenium"


@allure.feature("Herokuapp Website")
@allure.story("Incognito Mode")
@allure.title("Test Menu with Incognito Mode")
def test_menu_is_displayed_incognito(incognito):
    for i in range(1, 5):
        btn = incognito.find_element(By.XPATH, f'//*[@id="menu"]/ul/li[{i}]/a')
        btn.click()

        if i == 1:
            assert incognito.find_element(By.ID, 'menu').is_displayed()
        elif i == 2:
            assert incognito.find_element(By.ID, 'menu').is_displayed()
        elif i == 3:
            assert incognito.find_element(By.ID, 'menu').is_displayed()
        elif i == 4:
            assert incognito.find_element(By.ID, 'menu').is_displayed()


@allure.feature("Herokuapp Website")
@allure.story("Headless Mode")
@allure.title("Test Menu with Headless Mode")
def test_menu_is_displayed_headless(headless):
    for i in range(1, 5):
        btn = headless.find_element(By.XPATH, f'//*[@id="menu"]/ul/li[{i}]/a')
        btn.click()

        if i == 1:
            assert headless.find_element(By.ID, 'menu').is_displayed()
        elif i == 2:
            assert headless.find_element(By.ID, 'menu').is_displayed()
        elif i == 3:
            assert headless.find_element(By.ID, 'menu').is_displayed()
        elif i == 4:
            assert headless.find_element(By.ID, 'menu').is_displayed()


@allure.feature("Herokuapp Website")
@allure.story("Headless_Incognito Mode")
@allure.title("Test Menu with Headless Incognito Mode")
def test_menu_is_displayed_headless_incognito(headless_incognito):
    for i in range(1, 5):
        btn = headless_incognito.find_element(By.XPATH, f'//*[@id="menu"]/ul/li[{i}]/a')
        btn.click()

        if i == 1:
            assert headless_incognito.find_element(By.ID, 'menu').is_displayed()
        elif i == 2:
            assert headless_incognito.find_element(By.ID, 'menu').is_displayed()
        elif i == 3:
            assert headless_incognito.find_element(By.ID, 'menu').is_displayed()
        elif i == 4:
            assert headless_incognito.find_element(By.ID, 'menu').is_displayed()
