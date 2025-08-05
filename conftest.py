import os
import time

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import DesiredCapabilities


from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Utils.parse_yaml_file import base_url
from Utils.parse_yaml_file import org_name
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptInsecureCerts'] = True

@pytest.fixture(scope='class')
def setup(request, browser, get_url):
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.maximize_window()
    driver.get(get_url)
    request.cls.driver = driver

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--url')
    parser.addoption('--headless')


@pytest.fixture(scope="session",autouse=True)
def browser(request):
    """Get browser name from command line"""
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def headless(request):
    """Get headless mode from command line"""
    return request.config.getoption("--headless")

@pytest.fixture(scope="class")
def get_url(request):
    """Get base URL from command line"""
    return request.config.getoption("--url")
    # """Get URL from command line or config file"""
    # url = request.config.getoption("--url")
    # if not url:
    #     import yaml
    #     with open("config.yaml", "r") as f:
    #         config = yaml.safe_load(f)
    #         url = config["base_url"]
    # return url

def pytest_html_report_title(report):
    report.title = org_name + " Test Report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results"""
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url(base_url))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            if hasattr(item, 'instance') and hasattr(item.instance, 'driver') and item.config.option.htmlpath:
                try:
                    report_directory = os.path.dirname(item.config.option.htmlpath)
                    file_name = str(int(round(time.time() * 1000))) + ".png"
                    destinationFile = os.path.join(report_directory, file_name)
                    item.instance.driver.save_screenshot(destinationFile)
                    html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extras.append(pytest_html.extras.html(html))
                except Exception as e:
                    print(f"Screenshot capture failed: {e}")
        report.extras = extras

