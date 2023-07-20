import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene import be
import pytest


def test_complete_onboarding(set_browser):

    if set_browser == 'browserstack':
        pytest.skip("unsupported configuration")

    # ACT
    
    with allure.step('Go to the second page of onboarding'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Go to the third page of onboarding'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Go to the fourth page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Accept the data checking'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).click()

    # ASSERT
    with allure.step('Check the main page is displayed'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')).should(be.visible)



