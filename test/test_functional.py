from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


class NewVisitorTest(unittest.TestCase):
    url = 'http://web:8000/'

    def setUp(self):
        selenium_hub_url = 'http://hub:4444/wd/hub'
        self.browser = webdriver.Remote(
            command_executor=selenium_hub_url,
            desired_capabilities=DesiredCapabilities.CHROME)

    def teamDown(self):
        self.browser.quit()

    def test_can_start_a_list(self):
        self.browser.get(self.url)
        self.assertEqual('To-Do list', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
