__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from python_example.fixture.fixture import driver
from python_example.fixture.random_string import random_string


def set_general(driver, name):
    driver.find_element_by_name("status").click()
    driver.find_element_by_name("name[en]").send_keys(name)
    driver.find_element_by_name("code").send_keys("1296")
    driver.find_element_by_css_selector("[value='1-1']").click()
    driver.find_element_by_name("quantity").clear()
    driver.find_element_by_name("quantity").send_keys("1")
    path = os.path.abspath(r"img/DSC_0007_43.jpg")
    driver.find_element_by_name("new_images[]").send_keys(path)
    date_from = datetime.date.today()
    driver.find_element_by_name("date_valid_from").send_keys(date_from.strftime('%Y-%m-%d'))
    date_to = datetime.date.today() + datetime.timedelta(days=15)
    driver.find_element_by_name("date_valid_to").send_keys(date_to.strftime('%Y-%m-%d'))
    driver.find_element_by_css_selector("[href='#tab-information']").click()


def set_information(driver):
    Select(driver.find_element_by_name("manufacturer_id")).select_by_visible_text("ACME Corp.")
    driver.find_element_by_name("keywords").send_keys("keywords")
    driver.find_element_by_name("short_description[en]").send_keys("short_description")
    driver.find_element_by_name("description[en]").send_keys("description<br>description<br>description")
    driver.find_element_by_name("head_title[en]").send_keys("head_title")
    driver.find_element_by_name("meta_description[en]").send_keys("meta_description")
    driver.find_element_by_css_selector("[href='#tab-prices']").click()


def set_prices(driver):
    driver.find_element_by_name("purchase_price").clear()
    driver.find_element_by_name("purchase_price").send_keys("1")
    Select(driver.find_element_by_name("purchase_price_currency_code")).select_by_value("USD")
    driver.find_element_by_name("gross_prices[USD]").clear()
    driver.find_element_by_name("gross_prices[USD]").send_keys("10")
    driver.find_element_by_name("gross_prices[EUR]").clear()
    driver.find_element_by_name("gross_prices[EUR]").send_keys("10")
    driver.find_element_by_xpath("//button[@name='save']").click()


def check_product(driver, name):
    driver.find_element_by_link_text(name).click()
    driver.find_element_by_name("delete").click()
    Alert(driver).accept()


def test_l12(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    wait = WebDriverWait(driver, 10)

    driver.find_element_by_css_selector("[href$='/admin/?app=catalog&doc=catalog']").click()
    driver.find_element_by_css_selector("[href$='/admin/?category_id=0&app=catalog&doc=edit_product']").click()

    name = random_string("", 10)

    set_general(driver, name)
    set_information(driver)
    set_prices(driver)
    check_product(driver, name)

