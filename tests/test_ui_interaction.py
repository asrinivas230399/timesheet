from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest

@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)
    elif request.param == "firefox":
        options = FirefoxOptions()
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=options)
    elif request.param == "edge":
        options = EdgeOptions()
        service = EdgeService()
        driver = webdriver.Edge(service=service, options=options)
    else:
        raise ValueError("Unsupported browser")

    yield driver
    driver.quit()

def test_styles(driver):
    driver.get("http://localhost:8000/customer/edit/1")
    form = driver.find_element(By.TAG_NAME, "form")
    assert form.is_displayed()
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    assert submit_button.is_displayed()
    assert submit_button.value_of_css_property("background-color") == "rgb(0, 121, 107)"