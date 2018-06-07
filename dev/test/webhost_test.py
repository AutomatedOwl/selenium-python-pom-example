import sys
import pytest
import time
from .cfg.test_configuration import TestConfiguration
from ..pages.site88_page import Site88Page

config = TestConfiguration()

def pytest_namespace():
    return {'webhost_page': None}
    return {'driver': None}

@pytest.fixture
def example_fixture():
    return 'test_fixture'
    
class TestClass():

    def setup_method(self, method):
        sys.stdout.write('\n' + 'setting up selenium test..\n')
        pytest.driver = config.get_driver()
        pytest.webhost_page = Site88Page(pytest.driver)
    
    def teardown_method(self, method):
        sys.stdout.write('\n' + 'tearing down selenium test..')
        pytest.driver.quit()

    def test_site88(self, example_fixture):
        sys.stdout.write(example_fixture + '\n')
        pytest.webhost_page.navigate_to_url()
        pytest.webhost_page.get_textbox().send_keys('Hello World')
        time.sleep(5)
    
    def test_google(self):
        pytest.driver.get("http://www.google.com")
        time.sleep(5)
