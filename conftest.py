import pytest
from selenium import webdriver

from src.my_api import My_Api


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()

    driver.get("https://www.google.com/")
    yield driver
    driver.close()


URL = "https://the-internet.herokuapp.com/floating_menu#home"


@pytest.fixture()
def incognito():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)

    yield driver

    driver.quit()


@pytest.fixture()
def headless():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)

    yield driver

    driver.quit()


@pytest.fixture()
def headless_incognito():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)

    yield driver

    driver.quit()


@pytest.fixture()
def browser_shop():
    driver = webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com/")

    yield driver

    driver.quit()


@pytest.fixture()
def behance_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.behance.net/gallery/18988225/B-Yoga-Website")

    yield driver

    driver.quit()


@pytest.fixture()
def delassus_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://delassus.com/en/")

    yield driver

    driver.quit()


@pytest.fixture()
def my_api():
    return My_Api()
