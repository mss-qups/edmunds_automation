from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class Driver:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def setUp(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-gpu')
        self.driver.get("https://www.edmunds.com/inventory/srp.html?inventorytype=used%2Ccpo")

    def tearDown(self):
        self.driver.close()
