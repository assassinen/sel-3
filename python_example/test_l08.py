__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    driver = webdriver.Firefox()
    request.addfinalizer(driver.quit)
    return driver


def test_l08(driver):
    driver.get("http://localhost/litecart/")
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("li.product")

    popular_products = driver.find_elements_by_css_selector("li.product")

    for popular_product in popular_products:
        stickers = popular_product.find_elements_by_css_selector(".sticker")
        assert (len(stickers) == 1)

