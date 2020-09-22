#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import allure
from appium.webdriver.common.mobileby import MobileBy


def handle_black(func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        _black_list = [(MobileBy.XPATH, "//*[@resource-id='com.dedao.juvenile:id/iv_close']"),
                       (MobileBy.XPATH, "//*[@resource-id='com.dedao.juvenile:id/ivClose']")
                       ]
        error_num = 1
        error_max = 3

        from young_win.Page.base_page import BasePage
        instance: BasePage = args[0]
        while True:
            try:
                logging.info('Running ' + func.__name__ + '\n args: \n' + repr(args[1:]) + repr(kwargs))
                element = func(*args, **kwargs)
                error_num = 0
                instance._driver.implicitly_wait(10)
                return element
            except Exception as e:
                instance.screenshot('tmp.png')
                with open('tmp.png', 'rb') as f:
                    content = f.read()
                allure.attach(content, attachment_type=allure.attachment_type.PNG)
                logging.error('elements not found, handle black list')

                if error_num > error_max:
                    raise e
                instance._driver.implicitly_wait(1)
                _black_try = 0
                for ele in _black_list:
                    elements = instance.finds(*ele)
                    if len(elements) > 0:
                        elements[0].click()
                        break
                    if len(elements) == 0:
                        _black_try += 1
                if _black_try == len(_black_list):
                    raise e
                error_num += 1

    return wrapper
