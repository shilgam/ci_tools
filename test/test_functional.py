from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


class TestStringMethods(unittest.TestCase):
    url = 'http://web:8000/'

    def test_firefox_site(self):
        firefox = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)

        firefox.get(self.url)
        self.assertEqual(firefox.title, 'Welcome to Django')
        firefox.quit()

    def test_chrome_browser(self):
        chrome = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        chrome.get(self.url)
        self.assertEqual(chrome.title, 'Welcome to Django')
        chrome.quit()


if __name__ == '__main__':
    unittest.main()
