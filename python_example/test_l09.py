__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from python_example.fixture.fixture import driver


def test_l09_1(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    wait = WebDriverWait(driver, 10)
    #driver.implicitly_wait(10)

    countries = [i.text for i in driver.find_elements_by_css_selector("tr.row a:not([title])")]
    assert (countries == sorted(countries))

    not_zero_zones = [i.text for i in driver.find_elements_by_css_selector("td:nth-child(6)")]
    not_zero_zones_indexs = [not_zero_zones.index(i) for i in not_zero_zones if i != '0']

    for not_zero_zones_index in not_zero_zones_indexs:
        country = driver.find_elements_by_css_selector("td:nth-child(5)>a")
        country[not_zero_zones_index].click()
        zones = [i.get_attribute("textContent") for i in driver.find_elements_by_css_selector("#table-zones tr>td:nth-child(3)") if i.get_attribute("textContent") != ""]
        assert (zones == sorted(zones))
        driver.back()


def test_l09_2(driver):
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    #wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)

    zones_number = len(driver.find_elements_by_css_selector("tr.row"))

    while zones_number:
        zones_number -= 1
        country = driver.find_elements_by_css_selector("td:nth-child(3)>a")
        country[zones_number].click()
        zones = [i.get_attribute("textContent") for i in driver.find_elements_by_css_selector("td:nth-child(3)>select option[selected]")]
        assert (zones == sorted(zones))
        driver.back()
