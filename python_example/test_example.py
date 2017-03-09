from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from python_example.fixture.fixture import driver


def test_example(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnG").click()
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))