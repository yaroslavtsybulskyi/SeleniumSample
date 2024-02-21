import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Behance")
@allure.story("Behance Tests")
@allure.title("Behance Yoga Page Tests")
def test_behance_page(behance_browser):
    assert behance_browser.title == "Behance"
    time.sleep(1)
    assert behance_browser.title == "B Yoga Website :: Behance"

    element = behance_browser.find_element(
        By.XPATH, '//*[@id="project-modules"]/section[1]/div[1]/div'
    )
    assert element.is_displayed()

    behance_button = behance_browser.find_element(
        By.CLASS_NAME, "PrimaryNav-logoWrap-gf0"
    )
    behance_button.click()

    WebDriverWait(behance_browser, 10).until(EC.url_to_be("https://www.behance.net/"))

    opened_link = behance_browser.current_url
    assert opened_link == "https://www.behance.net/"
    time.sleep(2)
    behance_browser.back()

    behance_browser.maximize_window()

    search_box = WebDriverWait(behance_browser, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/div/div[1]/nav/div/div[2]/div[3]/div/div[1]/form/label/input',
            )
        )
    )

    assert search_box.is_displayed()

    behance_browser.minimize_window()
    assert not search_box.is_displayed()

    target_element = behance_browser.find_element(
        By.CLASS_NAME, "Project-projectName-n_3"
    )
    behance_browser.execute_script("arguments[0].scrollIntoView(true);", target_element)
    assert target_element.text == "B Yoga Website"

    time.sleep(2)

    images = behance_browser.find_elements(By.TAG_NAME, "img")
    assert len(images) > 0

    footer = behance_browser.find_element(By.TAG_NAME, "footer")
    assert footer.is_displayed(), "Footer is not displayed on the page"

    login_button = behance_browser.find_element(
        By.XPATH, '//*[@id="app"]/div/div/div[1]/nav/div/div[2]/div[6]/ul/li[1]/button'
    )
    assert login_button.text == "Log In"
    assert login_button.is_displayed()

    signup_button = behance_browser.find_element(
        By.XPATH, '//*[@id="app"]/div/div/div[1]/nav/div/div[2]/div[6]/ul/li[2]/button'
    )
    assert signup_button.text == "Sign Up"
    assert signup_button.is_displayed()

    share_label = behance_browser.find_element(
        By.XPATH, "//label[contains(text(), 'Share')]"
    )
    assert share_label.text == "Share"
    assert share_label.is_displayed()
