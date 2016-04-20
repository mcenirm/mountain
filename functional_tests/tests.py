from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class MinimalTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(MinimalTestCase, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MinimalTestCase, cls).tearDownClass()

    def test_login(self):
        self.selenium.get(self.live_server_url)
        self.assertIn('Mountain', self.selenium.title)
