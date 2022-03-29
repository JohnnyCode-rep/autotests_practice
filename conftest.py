import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--headless', action='store', default=None,
                     help="Enter --headless to run in the background mode")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    headless_mode = request.config.getoption("headless")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        if headless_mode:
            options = ChromeOptions()
            options.headless = True
            browser = webdriver.Chrome(options=options)
        else:
            browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        if headless_mode:
            options = FirefoxOptions()
            options.add_argument("-headless")
            browser = webdriver.Firefox(options=options)
        else:
            browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
