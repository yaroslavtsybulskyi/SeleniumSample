from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

copyright_message = "Copyright © 2013-present Magento, Inc. All rights reserved."


@allure.feature("Magento")
@allure.story("Menu Items")
@allure.title("Test Menu Items")
def test_menu_items(browser_shop):
    for i in range(3, 9):
        btn = WebDriverWait(browser_shop, 10).until(
            EC.element_to_be_clickable((By.ID, f"ui-id-{i}"))
        )
        btn.click()

        if i == 3:
            assert (
                browser_shop.current_url
                == "https://magento.softwaretestingboard.com/what-is-new.html"
            )
        elif i == 4:
            assert (
                browser_shop.current_url
                == "https://magento.softwaretestingboard.com/women.html"
            )
        elif i == 5:
            assert (
                browser_shop.current_url
                == "https://magento.softwaretestingboard.com/men.html"
            )
        elif i == 6:
            assert (
                browser_shop.current_url
                == "https://magento.softwaretestingboard.com/gear.html"
            )
        elif i == 7:
            assert (
                browser_shop.current_url
                == "https://magento.softwaretestingboard.com/training.html"
            )
        elif i == 8:
            assert (
                browser_shop.current_url
                == "https://magento.softwaretestingboard.com/sale.html"
            )


@allure.feature("Magento")
@allure.story("What's new")
@allure.title("Test What's new page title")
def test_title_whatsnew(browser_shop):
    item = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-3"))
    )
    item.click()
    assert browser_shop.title == "What's New"


@allure.feature("Magento")
@allure.story("What's new")
@allure.title("Test What's new element")
def test_element_whatsnew(browser_shop):
    item = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-3"))
    )
    item.click()
    element = browser_shop.find_element(By.XPATH, '//*[@id="page-title-heading"]/span')
    assert element.text == "What's New"


@allure.feature("Magento")
@allure.story("Copyright Section")
@allure.title("Test Copyright Message")
def test_copyright_message(browser_shop):
    for i in range(3, 9):
        item = WebDriverWait(browser_shop, 5).until(
            EC.element_to_be_clickable((By.ID, f"ui-id-{i}"))
        )
        item.click()
        element = browser_shop.find_element(By.CLASS_NAME, "copyright")
        if i == 3:
            assert element.text.__contains__(copyright_message)
        elif i == 4:
            assert element.text.__contains__(copyright_message)
        elif i == 5:
            assert element.text.__contains__(copyright_message)
        elif i == 6:
            assert element.text.__contains__(copyright_message)
        elif i == 7:
            assert element.text.__contains__(copyright_message)
        elif i == 8:
            assert element.text.__contains__(copyright_message)


@allure.feature("Magento")
@allure.story("Women Section")
@allure.title("Test Women Section Page Title")
def test_title_women(browser_shop):
    item = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-4"))
    )
    item.click()
    assert browser_shop.title == "Women"


@allure.feature("Magento")
@allure.story("Women Section")
@allure.title("Test Women Section Element")
def test_element_women(browser_shop):
    item = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-4"))
    )
    item.click()
    element = browser_shop.find_element(By.XPATH, '//*[@id="page-title-heading"]/span')
    assert element.text == "Women"


@allure.feature("Magento")
@allure.story("Women Section")
@allure.title("Test Jackets Submenu Women Section")
def test_title_women_submenu_tops_jackets(browser_shop):
    menu = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-4"))
    )
    menu.click()
    submenu = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Tops")
    actions = ActionChains(browser_shop)
    submenu_item = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Jackets")

    actions.move_to_element(submenu)
    actions.click(submenu_item)
    actions.perform()

    assert browser_shop.title == "Jackets - Tops - Women"


@allure.feature("Magento")
@allure.story("Women Section")
@allure.title("Test Shorts Submenu Women Section")
def test_title_women_submenu_bottoms_shorts(browser_shop):
    menu = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-4"))
    )
    menu.click()
    submenu = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Bottoms")
    actions = ActionChains(browser_shop)
    submenu_item = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Shorts")

    actions.move_to_element(submenu)
    actions.click(submenu_item)
    actions.perform()

    assert browser_shop.title == "Shorts - Bottoms - Women"


@allure.feature("Magento")
@allure.story("Women Section")
@allure.title("Test Jackets Submenu Text Women Section")
def test_element_women_submenu_tops_jackets(browser_shop):
    menu = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-4"))
    )
    menu.click()
    submenu = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Tops")
    actions = ActionChains(browser_shop)
    submenu_item = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Jackets")

    actions.move_to_element(submenu)
    actions.click(submenu_item)
    actions.perform()

    element = browser_shop.find_element(
        By.XPATH, '//*[@id="narrow-by-list"]/div[8]/div[1]'
    )

    assert element.text == "ERIN RECOMMENDS"


@allure.feature("Magento")
@allure.story("Men Section")
@allure.title("Test Men Section Page Title")
def test_title_men(browser_shop):
    item = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-5"))
    )
    item.click()
    assert browser_shop.title == "Men"


@allure.feature("Magento")
@allure.story("Men Section")
@allure.title("Test Men Page Text Element")
def test_element_men(browser_shop):
    item = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-5"))
    )
    item.click()
    element = browser_shop.find_element(By.XPATH, '//*[@id="page-title-heading"]/span')
    assert element.text == "Men"


@allure.feature("Magento")
@allure.story("Men Section")
@allure.title("Test Pants Submenu Men Section")
def test_title_men_submenu_bottoms_pants(browser_shop):
    menu = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-5"))
    )
    menu.click()
    submenu = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Bottoms")
    actions = ActionChains(browser_shop)
    submenu_item = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Pants")

    actions.move_to_element(submenu)
    actions.click(submenu_item)
    actions.perform()

    assert browser_shop.title == "Pants - Bottoms - Men"


@allure.feature("Magento")
@allure.story("Men Section")
@allure.title("Test Element Men Submenu Men Section")
def test_element_men_submenu_bottoms_pants(browser_shop):
    menu = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-5"))
    )
    menu.click()
    submenu = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Bottoms")
    actions = ActionChains(browser_shop)
    submenu_item = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Pants")

    actions.move_to_element(submenu)
    actions.click(submenu_item)
    actions.perform()

    element = browser_shop.find_element(
        By.XPATH, '//*[@id="narrow-by-list"]/div[9]/div[1]'
    )

    assert element.text == "NEW"


@allure.feature("Magento")
@allure.story("Gear Section")
@allure.title("Test Gear Page Title")
def test_title_gear(browser_shop):
    item = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-6"))
    )
    item.click()
    assert browser_shop.title == "Gear"


@allure.feature("Magento")
@allure.story("Gear Section")
@allure.title("Test Element Gear Page")
def test_element_gear(browser_shop):
    item = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-6"))
    )
    item.click()
    element = browser_shop.find_element(By.XPATH, '//*[@id="page-title-heading"]/span')
    assert element.text == "Gear"


@allure.feature("Magento")
@allure.story("Gear Section")
@allure.title("Test Bags Page Title")
def test_title_gear_submenu_bags(browser_shop):
    menu = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-6"))
    )
    menu.click()
    submenu_item = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Bags")
    actions = ActionChains(browser_shop)

    actions.move_to_element(submenu_item)
    actions.click(submenu_item)
    actions.perform()

    assert browser_shop.title == "Bags - Gear"


@allure.feature("Magento")
@allure.story("Gear Section")
@allure.title("Test Element Bags Page")
def test_element_gear_submenu_bags(browser_shop):
    menu = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-6"))
    )
    menu.click()
    submenu_item = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Bags")
    actions = ActionChains(browser_shop)

    actions.move_to_element(submenu_item)
    actions.click(submenu_item)
    actions.perform()

    element = browser_shop.find_element(By.XPATH, '//*[@id="block-compare-heading"]')

    assert element.text == "Compare Products"


@allure.feature("Magento")
@allure.story("Training Section")
@allure.title("Test Training Page Title")
def test_title_training(browser_shop):
    item = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-7"))
    )
    item.click()
    assert browser_shop.title == "Training"


@allure.feature("Magento")
@allure.story("Training Section")
@allure.title("Test Element Training Page")
def test_element_training(browser_shop):
    item = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-7"))
    )
    item.click()
    element = browser_shop.find_element(By.XPATH, '//*[@id="page-title-heading"]/span')
    assert element.text == "Training"


@allure.feature("Magento")
@allure.story("Training Section")
@allure.title("Video Download Submenu")
def test_title_training_submenu_video_download(browser_shop):
    menu = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-7"))
    )
    menu.click()
    submenu_item = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Video Download")
    actions = ActionChains(browser_shop)

    actions.move_to_element(submenu_item)
    actions.click(submenu_item)
    actions.perform()

    assert browser_shop.title == "Video Download - Training"


@allure.feature("Magento")
@allure.story("Training Section")
@allure.title("Video Download Element Section")
def test_element_training_submenu_video_download(browser_shop):
    menu = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-7"))
    )
    menu.click()
    submenu_item = browser_shop.find_element(By.PARTIAL_LINK_TEXT, "Video Download")
    actions = ActionChains(browser_shop)

    actions.move_to_element(submenu_item)
    actions.click(submenu_item)
    actions.perform()

    element = browser_shop.find_element(
        By.XPATH,
        '//div[contains(text(), "We can\'t find products matching the selection.")]',
    )

    assert element.text == "We can't find products matching the selection."


@allure.feature("Magento")
@allure.story("Sale Section")
@allure.title("Test Sale Page Title")
def test_title_sale(browser_shop):
    item = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-8"))
    )
    item.click()
    assert browser_shop.title == "Sale"


@allure.feature("Magento")
@allure.story("Sale Section")
@allure.title("Test Sale Page Element")
def test_element_sale(browser_shop):
    item = WebDriverWait(browser_shop, 5).until(
        EC.element_to_be_clickable((By.ID, "ui-id-8"))
    )
    item.click()
    element = browser_shop.find_element(By.XPATH, '//*[@id="page-title-heading"]/span')
    assert element.text == "Sale"
