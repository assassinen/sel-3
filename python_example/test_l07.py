__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from python_example.lib.fixture import driver


def test_l07(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    wait = WebDriverWait(driver, 10)

    menu_number = len(driver.find_elements_by_css_selector("ul#box-apps-menu > li"))

    while menu_number:
        menu_number -= 1
        menu_items = driver.find_elements_by_css_selector("ul#box-apps-menu > li")
        menu_items[menu_number].click()
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        submenu_number = len(driver.find_elements_by_css_selector(".docs>li>a"))
        while submenu_number:
            submenu_number -= 1
            submenu_items = driver.find_elements_by_css_selector(".docs>li>a")
            submenu_items[submenu_number].click()
            element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

            aaa = EC.number_of_windows_to_be(1)

