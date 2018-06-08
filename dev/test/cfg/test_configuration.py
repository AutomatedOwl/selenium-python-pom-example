from selenium import webdriver
from sys import platform
import os

class TestConfiguration:
    
    def get_driver(self):
        if platform == "linux" or platform == "linux2":
            return webdriver.Chrome(
                os.path.join(os.getcwd(),
                    "driver","executable","chromedriver"))
        elif platform == "win32":
            return webdriver.Chrome(
                os.path.join(os.getcwd(),
                    "driver","executable","chromedriver.exe"))
