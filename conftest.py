import pytest
from appium.options.android import UiAutomator2Options
from selene.support.shared import browser
from appium import webdriver
import json
from utils.attach import attach_video
from config import Settings
from dotenv import load_dotenv
from utils.path_helper import path_helper


def pytest_addoption(parser):
    parser.addoption(
        '--env',
        help='Environment for test',
        choices=['browserstack', 'local'],
        default='browserstack'
    )


@pytest.fixture(scope='session')
def set_browser(request):
    enviroment = request.config.getoption('--env')

    load_dotenv(f'.env.{enviroment}')
    settings = Settings()
    options = UiAutomator2Options()

    if enviroment == 'browserstack':
        options.load_capabilities({
            "platformName": settings.platformName,
            "platformVersion": settings.platformVersion,
            "deviceName": settings.deviceName,

            # Set URL of the application under test
            "app": settings.app,

            # Set other BrowserStack capabilities
            'bstack:options': {
                "projectName": settings.projectName,
                "buildName": settings.buildName,
                "sessionName": settings.sessionName,
                'networkLogs': settings.networkLogs,

                # Set your access credentials
                "userName": settings.userName,
                "accessKey": settings.accessKey
            }
        })

    elif enviroment == 'local':
        options.load_capabilities({
            'appium:automationName': settings.automationName,
            'appium:app': path_helper(settings.app),
            'platformName': settings.platformName,
            'appium:appWaitActivity': settings.appWaitActivity
        })

    browser.config.driver = webdriver.Remote(settings.remoteBrowser, options=options)

    yield enviroment

    if enviroment == 'browserstack':
        session_id = browser.execute_script('browserstack_executor: {"action": "getSessionDetails"}')
        video_url = json.loads(session_id)['video_url']
        attach_video(video_url)
