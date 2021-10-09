from tests.driver import Driver
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from pages.main_page import mainPage


class Home(Driver):
    def test_01(self):
        


home = Home()
home.driver.get('https://www.facebook.com')

