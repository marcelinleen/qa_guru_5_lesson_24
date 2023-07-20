import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from utils.assert_helper import page_texts
from selene import be
import pytest


def test_find_article_android_9(set_browser):

    if set_browser == 'local':
        pytest.skip("unsupported configuration")

    article = 'Taylor Swift'

    # ACT
    with allure.step('Make a search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).send_keys(article)

    with allure.step('Open the article'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_container')).click()

    # ASSERT

    with allure.step('Check the opened page'):
        text_elements = browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))
        assert article in page_texts(text_elements)


def test_find_article_android_11(set_browser):

    if set_browser == 'browserstack':
        pytest.skip("unsupported configuration")

    with allure.step('Click on the first article on the main page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_featured_article_card_content_container')).click()

    with allure.step('Assert that article is opened'):
        browser.element((AppiumBy.CLASS_NAME, 'android.view.View')).should(be.visible)
