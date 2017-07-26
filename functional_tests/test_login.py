from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

class LoginTest(FunctionalTest):

    def test_login_with_persona(self):
        # Edith goes to the awesome superlists site
        # and notices a "Sign in" link for the first time.
        # Edith logs in with her email address
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_login').send_keys('edith@mockmyid.com')
        self.browser.find_element_by_id('id_login').send_keys(Keys.ENTER)


        # She can see that she is logged in
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('edith@mockmyid.com', navbar.text)