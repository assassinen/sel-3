__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    driver = webdriver.Firefox()
    #driver = webdriver.Chrome()
    #driver = webdriver.Ie()
    request.addfinalizer(driver.quit)
    return driver


def is_correct_name(driver):
    name_from_main_page = driver.find_element_by_css_selector("#box-campaigns .name").text
    driver.find_element_by_css_selector("#box-campaigns a").click()
    name_from_product_page = driver.find_element_by_css_selector("h1.title").text
    assert (name_from_main_page == name_from_product_page)
    driver.back()


def is_correct_price(driver, type_price):
    price_from_main_page = driver.find_element_by_css_selector("#box-campaigns " + type_price).text
    driver.find_element_by_css_selector("#box-campaigns a").click()
    price_from_product_page = driver.find_element_by_css_selector(type_price).text
    assert (price_from_main_page == price_from_product_page)
    driver.back()


def is_correct_prices_style(driver, list, value):
    if value == "color":
        assert driver.find_element_by_css_selector(list[0][0]).value_of_css_property(value) == list[0][1]
        assert driver.find_element_by_css_selector(list[1][0]).value_of_css_property(value) == list[1][1]
    elif value == "font-size":
        font_regular = float(driver.find_element_by_css_selector(list[0][0]).value_of_css_property(value)[0:-2])
        font_campaign = float(driver.find_element_by_css_selector(list[1][0]).value_of_css_property(value)[0:-2])
        assert font_regular < font_campaign
    else:
        assert False


def test_l10(driver):
    driver.get("http://localhost/litecart/")
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("li.product")

    is_correct_name(driver)
    is_correct_price(driver, ".regular-price")
    is_correct_price(driver, ".campaign-price")

    color_price_list = [
        [
            ["#box-campaigns s.regular-price", "rgba(119, 119, 119, 1)"],
            ["#box-campaigns strong.campaign-price", "rgba(204, 0, 0, 1)"],
        ], [
            ["s.regular-price", "rgba(102, 102, 102, 1)"],
            ["strong.campaign-price", "rgba(204, 0, 0, 1)"]
        ]
    ]

    for i in color_price_list[0:1]:
        is_correct_prices_style(driver, i, "color")
        is_correct_prices_style(driver, i, "font-size")

    driver.find_element_by_css_selector("#box-campaigns a").click()
    for i in color_price_list[1:]:
        is_correct_prices_style(driver, i, "color")
        is_correct_prices_style(driver, i, "font-size")
    driver.back()



