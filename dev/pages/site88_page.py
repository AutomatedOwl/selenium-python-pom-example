from selenium import webdriver

SITE_URL = 'https://testjs2.000webhostapp.com/'

class Site88Page:
            
    def __init__(self, driver):
        self.driver = driver
        
    def navigate_to_url(self):
        self.driver.get(SITE_URL)
        
    def get_textbox(self):
        return self.driver.find_element_by_class_name('form-control')
