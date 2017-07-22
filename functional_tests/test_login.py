from .base import FunctionalTest

class LoginTest(FunctionalTest):

    def test_login_with_persona(self):
        # Edith goes to the awesome superlists site
        # and notices a "Sign in" link for the first time.
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_login').click()

        # Edith logs in with her email address
        self.browser.find_element_by_id(
            'authentication_email'  #2
        ).send_keys('edith@mockmyid.com') #3
        #self.browser.find_element_by_tag_name('button').click()

        # She can see that she is logged in
        #self.wait_for_element_with_id('logout')  #4
        #navbar = self.browser.find_element_by_css_selector('.navbar')
        #self.assertIn('edith@mockmyid.com', navbar.text)