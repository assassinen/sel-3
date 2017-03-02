__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import Select
from python_example.lib.random_string import random_string
from python_example.lib.fixture import driver


def test_l11(driver):
    account_info = dict(
        firstname = random_string("", 10),
        lastname = random_string("", 10),
        address1 = random_string("", 10),
        postcode = "12345",
        city = random_string("", 10),
        email = random_string("", 10) + "@selenium.org",
        phone = "+79991234567",
        password = "123321",
        confirmed_password = "123321"
    )

    driver.get("http://localhost/litecart/")
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("tr:last-of-type").click()

    for key, item in account_info.items():
        driver.find_element_by_name(key).send_keys(item)

    Select(driver.find_element_by_name("country_code")).select_by_value("US")
    Select(driver.find_element_by_css_selector("select[name = zone_code]")).select_by_value("CA")
    driver.find_element_by_name("create_account").click()

    driver.find_element_by_css_selector("#box-account li:last-of-type a").click()

    driver.find_element_by_name("email").send_keys(account_info["email"])
    driver.find_element_by_name("password").send_keys(account_info["password"])
    driver.find_element_by_name("login").click()
    driver.find_element_by_css_selector("[href$='/logout']").click()

