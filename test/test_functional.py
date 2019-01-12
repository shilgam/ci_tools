from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


class TestStringMethods(unittest.TestCase):

    def test_firefox_site(self):
        firefox = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)

        firefox.get('https://www.google.com')
        assert 'Google' in firefox.title
        firefox.quit()

    def test_chrome_browser(self):
        chrome = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        chrome.get('https://www.google.com')
        assert 'Google' in chrome.title
        chrome.quit()


if __name__ == '__main__':
    unittest.main()
