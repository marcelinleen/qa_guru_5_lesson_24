import pydantic
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):

    #  Appium settings
    platformName: str = None
    platformVersion: str = None
    deviceName: Optional[str] = None
    app: str = None
    appWaitActivity: Optional[str] = None
    automationName: Optional[str] = None

    # BrowserStack settings
    projectName: Optional[str] = None
    buildName: Optional[str] = None
    sessionName: Optional[str] = None
    networkLogs: Optional[bool] = False

    # BrowserStack conditionals
    userName: Optional[str] = None
    accessKey: Optional[str] = None

    remoteBrowser: str = None

    class Config:
        fields = {
            'platformName': 'platformName',
            'platformVersion': 'platformVersion',
            'deviceName': 'deviceName',
            'app': 'app',
            'appWaitActivity': 'appWaitActivity',
            'automationName': 'automationName',
            'projectName': 'projectName',
            'buildName':'buildName',
            'sessionName': 'sessionName',
            'networkLogs': 'networkLogs',
            'userName': 'userName',
            'accessKey': 'accessKey',
            'remoteBrowser': 'remoteBrowser'
        }
