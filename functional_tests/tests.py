from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_visit_site(self):
        # user opens the web site
        self.browser.get(self.live_server_url)
        current_url = self.browser.current_url

        # the page loads and sees the title
        self.assertIn('Jon Redeker', self.browser.title)


class PollsVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_visit_polls(self):
        # user opens the polls home
        self.browser.get(self.live_server_url)
        current_url = self.browser.current_url

