# Import required Selenium WebDriver modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import base driver class
from Pages.base_driver import BaseDriver
from Pages.page_signup import SignUp


class SignIn(BaseDriver):
    def __init__(self, driver):
        # Initialize parent class
        super().__init__(driver)
        self.driver = driver

        # Define element locators using IDs
        self.LNK_SIGNIN = (By.ID,'navbar-signin-button')
        self.EMAIL = (By.ID, 'auth-email')
        self.PASSWORD = (By.ID,'auth-password')
        self.BTN_SIGNIN = (By.ID, 'auth-submit-button')
        self.LNK_SIGNOUT = (By.ID,'navbar-signout-button')
        self.SIGNIN_FORM = (By.CLASS_NAME,'p-6 space-y-4')
        self.SIGNIN_SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(),'Welcome back')]")



    # Click on Sign In menu link
    def click_signin_menu(self):
        self.click_element(self.LNK_SIGNIN)

    # Input email in the email field
    def input_email(self,value):
        self.input_textbox(self.EMAIL, value)

    # Input password in the password field
    def input_password(self, value):
        self.input_textbox(self.PASSWORD,value)

    # Click the signup button to submit form
    def click_signin_button(self):
        self.click_element(self.BTN_SIGNIN)

    # Click on sign out menu option
    def click_sign_out_menu(self):
        self.click_element(self.LNK_SIGNOUT)

    def is_signout_link_present(self):
        is_visible = self.is_element_located(self.LNK_SIGNOUT)
        self.log.info(is_visible)
        return is_visible

    def is_success_message_displayed(self):
        is_visible = self.is_element_located(self.SIGNIN_SUCCESS_MESSAGE)
        self.log.info(is_visible)
        return is_visible

    def wait_until_signin_form_closes(self):
        self.wait_until_invisibility_of_an_element(self.SIGNIN_FORM)
