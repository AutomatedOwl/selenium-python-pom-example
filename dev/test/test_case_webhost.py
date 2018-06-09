import sys
import time
import pytest
from .cfg.test_configuration import TestConfiguration
from ..pages.site88_page import Site88Page
    
config = TestConfiguration()

class TestCaseWebHost():
        
    def pytest_namespace(self):
        return {'webhost_page': None}
        return {'driver': None}
    
    @pytest.fixture
    def example_fixture(self):
        return 'test_fixture'

    def wait_before_closing_browser(self):
        time.sleep(5)
    
    def setup_method(self, method):
        sys.stdout.write('\n' + 'setting up selenium test..\n')
        pytest.driver = config.get_driver()
        pytest.webhost_page = Site88Page(pytest.driver)
    
    def teardown_method(self, method):
        sys.stdout.write('\n' + 'tearing down selenium test..')
        pytest.driver.quit()
