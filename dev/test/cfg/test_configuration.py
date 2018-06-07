from selenium import webdriver
import os

class TestConfiguration:
    
    def get_driver(self):
        return webdriver.Chrome(
            os.getcwd() + '/driver/executable/chromedriver')