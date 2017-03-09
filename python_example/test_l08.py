__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from python_example.fixture.fixture import driver


def test_l08(driver):
    driver.get("http://localhost/litecart/")
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("li.product")

    popular_products = driver.find_elements_by_css_selector("li.product")

    for popular_product in popular_products:
        stickers = popular_product.find_elements_by_css_selector(".sticker")
        assert (len(stickers) == 1)

