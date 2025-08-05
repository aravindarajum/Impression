# Import required Selenium WebDriver modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import base driver class
from Pages.base_driver import BaseDriver

class SignUp(BaseDriver):
    def __init__(self, driver):
        # Initialize parent class
        super().__init__(driver)
        self.driver = driver

        # Define element locators using IDs
        self.LNK_SIGNUP = (By.ID,'navbar-signup-button')
        self.FULL_NAME = (By.ID,'auth-name')
        self.EMAIL = (By.ID, 'auth-email')
        self.PHONE_NUMBER = (By.ID,'auth-phone')
        self.PASSWORD = (By.ID, 'auth-password')
        self.CONFIRM_PASSWORD = (By.ID,'auth-confirm-password')
        self.BTN_SIGNUP = (By.ID,'auth-submit-button')
        self.LNK_SIGNOUT = (By.ID,'navbar-signout-button')
        self.SIGNUP_SUCCESS_MESSAGE = (By.XPATH,"//*[(text()='Account created successfully! Welcome to Impression.')]")

        # Sign Up Form Error Messages - Form Elements
        self.NAME_REQUIRED = (By.XPATH,"//p[text()='Name is required']")
        self.EMAIL_REQUIRED = (By.XPATH,"//p[text()='Email is required']")
        self.PHONE_NUMBER_REQUIRED = (By.XPATH,"//p[text()='Phone number is required']")
        self.PASSWORD_IS_REQUIRED = (By.XPATH,"//p[text()='Password is required']")
        self.CONFIRM_PASSWORD_IS_REQUIRED = (By.XPATH,"//p[text()='Passwords do not match']")

    # Click on signup menu link
    def click_signup_menu(self):
        self.click_element(self.LNK_SIGNUP)

    # Input full name in the name field
    def input_full_name(self,value):
        self.input_textbox(self.FULL_NAME, value)

    # Input email in the email field
    def input_email(self,value):
        self.input_textbox(self.EMAIL, value)

    # Input phone number in the phone field
    def input_phone_number(self, value):
        self.input_textbox(self.PHONE_NUMBER,value)

    # Input password in the password field
    def input_password(self, value):
        self.input_textbox(self.PASSWORD,value)

    # Input password confirmation
    def input_confirm_password(self,value):
        self.input_textbox(self.CONFIRM_PASSWORD,value)

    # Click the signup button to submit form
    def click_signup_button(self):
        self.click_element(self.BTN_SIGNUP)

    # Click on sign out menu option
    def click_sign_out_menu(self):
        self.click_element(self.LNK_SIGNOUT)

    def is_signup_success_message_displayed(self):
        is_visible = self.is_element_located(self.SIGNUP_SUCCESS_MESSAGE)
        self.log.info(is_visible)
        return is_visible

    def signup_success_message_get_text(self):
        return self.get_element_text(self.SIGNUP_SUCCESS_MESSAGE)

    def is_signout_link_present(self):
        is_visible = self.is_element_located(self.LNK_SIGNOUT)
        self.log.info(is_visible)
        return is_visible

    def wait_until_signup_dialog_closes(self):
        self.wait_until_invisibility_of_an_element(self.LNK_SIGNOUT)

    # Methods to check errors msgs if empty values entered in the SignUp form fields (for negative test cases)
    def is_signup_form_name_field_empty(self,):
        is_name_empty = self.is_field_empty(self.FULL_NAME)
        self.log.info(f'Is Name field Empty{is_name_empty}')
        return is_name_empty
    def is_signup_form_email_field_empty(self,):
        is_email_empty = self.is_field_empty(self.EMAIL)
        self.log.info(f'Is Email field Empty{is_email_empty}')
        return is_email_empty
    def is_signup_form_phone_number_field_empty(self,):
        is_phone_number_empty = self.is_field_empty(self.PHONE_NUMBER)
        self.log.info(f'Is Phone Number field Empty{is_phone_number_empty}')
        return is_phone_number_empty
    def is_signup_form_password_field_empty(self,):
        is_password_empty = self.is_field_empty(self.PASSWORD)
        self.log.info(f'Is Password field Empty{is_password_empty}')
        return is_password_empty
    def is_signup_form_confirm_password_field_empty(self,):
        is_confirm_password_empty = self.is_field_empty(self.CONFIRM_PASSWORD)
        self.log.info(f'Is Confirm Password field Empty{is_confirm_password_empty}')
        return is_confirm_password_empty

    #     Methods to check Sign Up form error messages
    def is_name_required_error_message_present(self):
        is_name_visible = self.is_element_located(self.NAME_REQUIRED)
        self.log.info(f"Is Name error Message Dispalyed {is_name_visible}")
        return is_name_visible
    def is_email_required_error_message_present(self):
        is_email_visible = self.is_element_located(self.EMAIL_REQUIRED)
        self.log.info(f"Is Email error Message Dispalyed {is_email_visible}")
        return is_email_visible
    def is_phone_number_required_error_message_present(self):
        is_phone_number_visible = self.is_element_located(self.PHONE_NUMBER_REQUIRED)
        self.log.info(f"Is Phone Number error Message Dispalyed {is_phone_number_visible}")
        return is_phone_number_visible
    def is_password_required_error_message_present(self):
        is_password_visible = self.is_element_located(self.PASSWORD_IS_REQUIRED)
        self.log.info(f"Is Password error Message Dispalyed {is_password_visible}")
        return is_password_visible
    def is_confirm_password_required_error_message_present(self):
        is_confirm_password_visible = self.is_element_located(self.CONFIRM_PASSWORD_IS_REQUIRED)
        self.log.info(f"Is Confirm Password error Message Dispalyed {is_confirm_password_visible}")
        return is_confirm_password_visible
