import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language. Example: --language=ru")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption('language')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    print("=" * 50)
    browser.quit()