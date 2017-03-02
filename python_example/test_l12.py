__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from python_example.lib.fixture import driver
from selenium.webdriver.support.wait import WebDriverWait
from python_example.lib.random_string import random_string


def test_l12(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    wait = WebDriverWait(driver, 10)

