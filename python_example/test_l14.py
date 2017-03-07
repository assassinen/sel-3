__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from python_example.lib.fixture import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def test_l14(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    wait = WebDriverWait(driver, 10)

    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_css_selector(".row a").click()

    main_window = driver.current_window_handle
    links = driver.find_elements_by_css_selector(".fa.fa-external-link")

    for link in links:
        link.click()
        new_window = [i for i in driver.window_handles if i != main_window]
        wait.until(EC.new_window_is_opened(new_window))

        for window in new_window:
            driver.switch_to.window(window)
            driver.close()
        driver.switch_to.window(main_window)

