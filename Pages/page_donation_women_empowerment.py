# Import required Selenium WebDriver modules
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import base driver class
from Pages.base_driver import BaseDriver
from datetime import datetime


class DonationWomenEmpowermentRegistration(BaseDriver):
    def __init__(self, driver):
        # Initialize parent class
        super().__init__(driver)
        self.driver = driver
        self.value = None
        # Define element locators using IDs
        self.LNK_DONATE = (By.ID, 'nav-donate')
        self.BTN_DONATE = (By.ID, 'donate-cause-3')
        self.TXT_DONATION_AMOUNT =(By.ID,'donation-amount')
        self.DONOR_FULLNAME = (By.ID, 'donor-name')
        self.DONOR_EMAIL = (By.ID,'donor-email')
        self.DONOR_PHONE = (By.ID, 'donor-phone')
        self.DONOR_ADDRESS = (By.ID, 'donor-address')
        self.BTN_DONATION_SUBMIT = (By.ID, 'donation-submit-button')
        self.ALERT_DIALOG_TEXT_MESSAGE = f"Thank you for your donation of ₹{self.value} for Education for All! Razorpay integration would be implemented here. Sign up for an account to track your donations."
  

    # Click on Donate menu link
    def click_donate_menu(self):
        self.click_element(self.LNK_DONATE)

    # Click on Register Now button
    def click_donate_now_button(self):
        self.click_element(self.BTN_DONATE)

    # Input Donation Amount
    def input_donation_amount(self, value):
        self.input_textbox(self.TXT_DONATION_AMOUNT, value)

    # Input full name in the name field
    def input_full_name(self,value):
        self.input_textbox(self.DONOR_FULLNAME, value)

    # Input phone number in the phone field
    def input_phone_number(self, value):
        self.input_textbox(self.DONOR_PHONE, value)

    # Input email in the email field
    def input_email(self,value):
        self.input_textbox(self.DONOR_EMAIL, value)

    # Input Address
    def input_address(self,value):
        self.input_textbox(self.DONOR_ADDRESS,value)

    # Click on Donate menu link
    def click_donate_submit_button(self):
        self.click_element(self.BTN_DONATION_SUBMIT)

    def set_donation_amount_to_value_variable(self,amount):
        self.value = amount
        return self.TXT_DONATION_AMOUNT

   
