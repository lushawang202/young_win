#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from young_win.Page.main import Main


class App:
    _driver: WebDriver

    def start(self):
        caps = dict()
        caps["platform"] = 'Android'
        caps["deviceName"] = "QFF0219920021227"
        caps["appPackage"] = "com.dedao.juvenile"
        caps["appActivity"] = ".business.splash.SplashActivity"
        caps["automationName"] = "UiAutomator2"
        caps['autoGrantPermissions'] = True
        caps["noReset"] = "true"
        # caps['newCommandTimeout'] = 600
        caps["dontStopAppOnReset"] = True
        self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self._driver.implicitly_wait(10)
        return self

    def main(self) -> Main:
        return Main(self._driver)

    def stop(self):
        self._driver.close_app()

    def reset(self):
        self._driver.reset()

    def back(self):
        self._driver.back()
