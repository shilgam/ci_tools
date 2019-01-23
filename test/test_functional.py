from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


class TestStringMethods(unittest.TestCase):
    url = 'http://web:8000/'
    selenium_hub_url = 'http://hub:4444/wd/hub'

    def test_site_firefox(self):
        self.base_test_suite(DesiredCapabilities.FIREFOX)

    def test_site_chome(self):
        self.base_test_suite(DesiredCapabilities.CHROME)

    def base_test_suite(self, browser_desired_caps):
        browser = webdriver.Remote(
            command_executor=self.selenium_hub_url,
            desired_capabilities=browser_desired_caps)

        browser.get(self.url)
        self.assertEqual(browser.title, 'Welcome to Django')
        browser.quit()
