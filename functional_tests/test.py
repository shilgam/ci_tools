import socket
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):
    # Set host to externally accessible web server address
    host = socket.gethostbyname(socket.gethostname())

    def setUp(self):
        selenium_hub_url = 'http://hub:4444/wd/hub'
        self.browser = webdriver.Remote(
            command_executor=selenium_hub_url,
            desired_capabilities=DesiredCapabilities.CHROME)

    def teamDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)

        # page title and header
        self.assertEqual('To-Do list', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # user is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # type into a text box
        inputbox.send_keys('Buy peacock feathers')

        # when user hits enter, the page updates, and now entered item
        # appears in the list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting user to add another item.
        # she enters one more item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # User wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique url for her.
        # User visits that URL - her to-do list is still there.
