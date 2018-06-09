import sys
import time
import pytest
from .test_case_webhost import TestCaseWebHost

class TestWebHost(TestCaseWebHost):    
             
    def test_site88(self, example_fixture):
        
        # Print example pytest fixture.
        sys.stdout.write(example_fixture + '\n')
        
        # Use POM object to navigate to URL.
        pytest.webhost_page.navigate_to_url()
        
        # Send 'Hello World' input.
        pytest.webhost_page.get_textbox().send_keys('Hello World')
        
        # Wait before closing browser.
        TestCaseWebHost.wait_before_closing_browser(self)
            
    def test_google(self):
        
        # Navigate to Google home page.
        pytest.driver.get("http://www.google.com")
        
        # Wait before closing browser.
        TestCaseWebHost.wait_before_closing_browser(self)
