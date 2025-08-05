# Import required Selenium WebDriver modules
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import base driver class
from Pages.base_driver import BaseDriver
from datetime import datetime


class VolunteerRegistration(BaseDriver):
    def __init__(self, driver):
        # Initialize parent class
        super().__init__(driver)
        self.driver = driver
        self.value = None
        # Define element locators using IDs
        self.LNK_VOLUNTEER = (By.ID, 'nav-volunteer')
        self.VOLUNTEER_COMMUNITY_OUTREACH_REGISTER = (By.ID, 'volunteer-register-community-outreach')
        self.VOLUNTEER_FULLNAME = (By.ID, 'volunteer-name')
        self.VOLUNTEER_MOBILE = (By.ID, 'volunteer-mobile')
        self.VOLUNTEER_EMAIL = (By.ID, 'volunteer-email')
        self.DATE_OF_BIRTH = (By.ID, 'volunteer-date-of-birth')
        self.VOLUNTEER_ADDRESS = (By.ID, 'volunteer-address')
        self.VOLUNTEER_CITY = (By.ID, 'volunteer-city')
        self.VOLUNTEER_STATE = (By.ID, 'volunteer-state')
        self.VOLUNTEER_GENDER_FEMALE = (By.ID, 'volunteer-gender-female')
        self.VOLUNTEER_GENDER = (By.XPATH, f"//input[@name='gender' and @value='{self.value}']")
        self.VOLUNTEER_GENDER_MALE = (By.ID, 'volunteer-gender-male')
        self.VOLUNTEER_AREA_OF_INTEREST = (By.XPATH,f"//input[@type='checkbox' and @id='volunteer-interest-{self.value}']")
        self.VOLUNTEER_AREA_OF_INTEREST_HEALTH = (By.ID, 'volunteer-interest-health')
        self.VOLUNTEER_AREA_OF_INTEREST_EDUCATION = (By.ID, 'volunteer-interest-education')
        self.VOLUNTEER_AREA_OF_INTEREST_AGRICULTURE = (By.ID, 'volunteer-interest-agriculture')
        self.VOLUNTEER_AREA_OF_INTEREST_YOUTH_PROGRAMS = (By.ID, 'volunteer-interest-youth-programs')
        self.VOLUNTEER_AREA_OF_INTEREST_WOMEN_EMPOWERMENT = (By.ID, 'volunteer-interest-women-empowerment')
        self.VOLUNTEER_PROFILE_PICTURE = (By.CSS_SELECTOR, "input[type='file']")
        self.VOLUNTEER_SUBMIT = (By.ID, 'volunteer-submit')
        self.VOLUNTEER_REGISTRATION_SUCCESS_MESSAGE = (By.XPATH,"//h2[contains(text(),'Registration Successful!')]")
        self.BUTTON_BACK_TO_VOLUNTEER_PAGE = (By.ID,'volunteer-back-to-page')

    #  Registration Form Error Message
        self.FULLNAME_ERROR_MSG =  (By.XPATH,"//p[contains(text(),'Name is required')]")
        self.MOBILE_NUMBER_ERROR_MSG = (By.XPATH,"//p[contains(text(),'Mobile number is required')]")
        self.EMAIL_ADDRESS_ERROR_MSG = (By.XPATH,"//p[contains(text(),'Email is required')]")
        self.DATE_OF_BIRTH_ERROR_MSG = (By.XPATH,"//p[contains(text(),'Date of birth is required')]")
        self.ADDRESS_ERROR_MSG = (By.XPATH,"//p[contains(text(),'Address is required')]")
        self.GENDER_ERROR_MSG = (By.XPATH,"//p[contains(text(),'Gender is required')]")
        self.CITY_ERROR_MSG = (By.XPATH, "//p[contains(text(),'City is required')]")
        self.STATE_ERROR_MSG = (By.XPATH, "//p[contains(text(),'State is required')]")
        self.AREA_OF_INTEREST_ERROR_MSG = (By.XPATH, "//p[contains(text(),'Please select at least one area of interest')]")



    # Click on Volunteer menu link
    def click_volunteer_menu(self):
        self.click_element(self.LNK_VOLUNTEER)

    # Click on Register Now button
    def click_register_now_button(self):
        self.click_element(self.VOLUNTEER_COMMUNITY_OUTREACH_REGISTER)

    # Input full name in the name field
    def input_full_name(self,value):
        self.input_textbox(self.VOLUNTEER_FULLNAME, value)

    # Input phone number in the phone field
    def input_phone_number(self, value):
        self.input_textbox(self.VOLUNTEER_MOBILE, value)

    # Input email in the email field
    def input_email(self,value):
        self.input_textbox(self.VOLUNTEER_EMAIL, value)

    # Input Date of Birth
    def input_date_of_birth(self, value):
        self.input_textbox(self.DATE_OF_BIRTH,value)

    # Input Address
    def input_address(self,value):
        self.input_textbox(self.VOLUNTEER_ADDRESS,value)

    # Select City from dropdown
    def select_city(self, value):
        self.select_from_drop_down_menu(self.VOLUNTEER_CITY, value)


    # Select State from dropdown
    def select_state(self, value):
        self.select_from_drop_down_menu(self.VOLUNTEER_STATE, value)

    # Click Male or Female radio button
    # def select_gender(self,value):
    #     if value == 'Female':
    #         By.ID, f'volunteer-gender-{value}'
    #         self.click_element(self.VOLUNTEER_GENDER_FEMALE)
    #     else:
    #         self.click_element(self.VOLUNTEER_GENDER_MALE
    #
    # # Click Male or Female radio button - Reconstructing the Radio button ID along 'value'
    def select_gender(self,value):
            self.value = value
            self.VOLUNTEER_GENDER = (By.XPATH, f"//input[@name='gender' and @value='{self.value}']")
            self.click_radio_button(self.VOLUNTEER_GENDER)
            # self.VOLUNTEER_GENDER = (By.ID, f'volunteer-gender-{self.value}')


    # Click Areas of Interest radio button
    def click_areas_of_interests(self, value):
        self.value = value
        areas_of_interests = value.split(',')
        self.log.info(areas_of_interests)
        for each_interest in areas_of_interests:
            self.log.info(each_interest)
            # --------------------------------------------------------------
            # each_interest_lower_case = (each_interest.lower()).strip()
            # self.VOLUNTEER_AREA_OF_INTEREST = (By.XPATH,
            #                                    f"//input[@type='checkbox' and @id='volunteer-interest-{each_interest_lower_case}']")
            # self.click_checkbox(self.VOLUNTEER_AREA_OF_INTEREST)
            # --------------------------------------------------------------

            if each_interest == 'Health':
                self.click_element(self.VOLUNTEER_AREA_OF_INTEREST_HEALTH)
            elif each_interest == 'Education':
                self.click_element(self.VOLUNTEER_AREA_OF_INTEREST_EDUCATION)
            elif each_interest == 'Agriculture':
                self.click_element(self.VOLUNTEER_AREA_OF_INTEREST_AGRICULTURE)
            elif each_interest == 'Youth Programs':
                self.click_element(self.VOLUNTEER_AREA_OF_INTEREST_YOUTH_PROGRAMS)
            else:
                self.click_element(self.VOLUNTEER_AREA_OF_INTEREST_WOMEN_EMPOWERMENT)

    # Upload profile picture
    def click_choose_file(self,file_path):
        self.upload_file(self.VOLUNTEER_PROFILE_PICTURE,file_path)

        # self.click_element(self.VOLUNTEER_PROFILE_PICTURE)

    # Click on Submit Application button
    def click_submit_application_button(self):
        self.click_element(self.VOLUNTEER_SUBMIT)

    def is_volunteer_registration_success_message_displayed(self):
        is_visible = self.is_element_located(self.VOLUNTEER_REGISTRATION_SUCCESS_MESSAGE)
        success_message = self.get_element_text(self.VOLUNTEER_REGISTRATION_SUCCESS_MESSAGE)
        self.log.info(is_visible)
        return success_message

    def click_back_to_volunteer_button(self):
        self.click_element(self.BUTTON_BACK_TO_VOLUNTEER_PAGE)

    # Methods to if empty values entered in the SignUp form fields (for negative test cases)
    def is_volunteer_form_name_field_empty(self):
        is_name_empty = self.is_field_empty(self.VOLUNTEER_FULLNAME)
        self.log.info(f'Is Name field Empty {is_name_empty}')
        return is_name_empty
    def is_volunteer_form_phone_number_field_empty(self):
        is_mobile_number_empty = self.is_field_empty(self.VOLUNTEER_MOBILE)
        self.log.info(f'Is Phone Number field Empty {is_mobile_number_empty}')
        return is_mobile_number_empty
    def is_volunteer_form_email_field_empty(self):
        is_email_empty = self.is_field_empty(self.VOLUNTEER_EMAIL)
        self.log.info(f'Is Email field Empty {is_email_empty}')
        return is_email_empty
    def is_date_of_birth_form_field_empty(self):
        is_date_of_birth_empty = self.is_field_empty(self.DATE_OF_BIRTH)
        self.log.info(f'Is Date of Birth field Empty {is_date_of_birth_empty}')
        return is_date_of_birth_empty
    def is_address_form_field_empty(self):
        is_address_empty = self.is_field_empty(self.VOLUNTEER_ADDRESS)
        self.log.info(f'Is Address field Empty {is_address_empty}')
        return is_address_empty
    def is_city_form_field_empty(self):
        is_city_empty = self.is_field_empty(self.VOLUNTEER_CITY)
        self.log.info(f'Is City field Empty {is_city_empty}')
        return is_city_empty
    def is_state_form_field_empty(self):
        is_state_empty = self.is_field_empty(self.VOLUNTEER_STATE)
        self.log.info(f'Is State field Empty {is_state_empty}')
        return is_state_empty
    def is_gender_form_field_selected(self):
        is_gender_selected = self.is_checkbox_or_radio_button_selected(self.VOLUNTEER_GENDER_MALE)
        is_gender_selected = self.is_checkbox_or_radio_button_selected(self.VOLUNTEER_GENDER_FEMALE)
        self.log.info(f'Is Gender NOT empty {is_gender_selected}')
        if is_gender_selected:
            return False
        else:
            return True
    def is_areas_of_interest_form_fields_selected(self):
        is_areas_of_interest_selected = self.is_checkbox_or_radio_button_selected(self.VOLUNTEER_AREA_OF_INTEREST_HEALTH)
        is_areas_of_interest_selected = self.is_checkbox_or_radio_button_selected(self.VOLUNTEER_AREA_OF_INTEREST_EDUCATION)
        is_areas_of_interest_selected = self.is_checkbox_or_radio_button_selected(self.VOLUNTEER_AREA_OF_INTEREST_AGRICULTURE)
        is_areas_of_interest_selected = self.is_checkbox_or_radio_button_selected(self.VOLUNTEER_AREA_OF_INTEREST_YOUTH_PROGRAMS)
        is_areas_of_interest_selected = self.is_checkbox_or_radio_button_selected(self.VOLUNTEER_AREA_OF_INTEREST_WOMEN_EMPOWERMENT)
        self.log.info(f'Are Areas of Interested fields NOT selected {is_areas_of_interest_selected}')
        if is_areas_of_interest_selected:
            return False
        else:
            return True


    #
    #     Methods to check Sign Up form error messages
    def is_name_required_error_message_present(self):
        is_name_visible = self.is_element_located(self.FULLNAME_ERROR_MSG)
        self.log.info(f"Is Name error Message Dispalyed {is_name_visible}")
        return is_name_visible
    def is_email_required_error_message_present(self):
        is_email_visible = self.is_element_located(self.EMAIL_ADDRESS_ERROR_MSG)
        self.log.info(f"Is Email error Message Dispalyed {is_email_visible}")
        return is_email_visible
    def is_mobile_number_required_error_message_present(self):
        is_mobile_number_visible = self.is_element_located(self.VOLUNTEER_MOBILE)
        self.log.info(f"Is Mobile Number error Message Dispalyed {is_mobile_number_visible}")
        return is_mobile_number_visible
    def is_date_of_birth_required_error_message_present(self):
        is_date_of_birth_visible = self.is_element_located(self.DATE_OF_BIRTH_ERROR_MSG)
        self.log.info(f"Is Date of Birth error Message Dispalyed {is_date_of_birth_visible}")
        return is_date_of_birth_visible
    def is_address_required_error_message_present(self):
        is_address_visible = self.is_element_located(self.ADDRESS_ERROR_MSG)
        self.log.info(f"Is Address error Message Dispalyed {is_address_visible}")
        return is_address_visible
    def is_city_required_error_message_present(self):
        is_city_visible = self.is_element_located(self.CITY_ERROR_MSG)
        self.log.info(f"Is City error Message Dispalyed {is_city_visible}")
        return is_city_visible
    def is_state_required_error_message_present(self):
        is_state_visible = self.is_element_located(self.STATE_ERROR_MSG)
        self.log.info(f"Is State error Message Dispalyed {is_state_visible}")
        return is_state_visible
    def is_gender_required_error_message_present(self):
        is_gender_visible = self.is_element_located(self.GENDER_ERROR_MSG)
        self.log.info(f"Is Gender error Message Dispalyed {is_gender_visible}")
        return is_gender_visible
    def is_areas_of_interested_error_message_present(self):
        is_areas_of_interested_visible = self.is_element_located(self.AREA_OF_INTEREST_ERROR_MSG)
        self.log.info(f"Is Gender error Message Dispalyed {is_areas_of_interested_visible}")
        return is_areas_of_interested_visible
