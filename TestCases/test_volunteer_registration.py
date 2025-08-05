import pytest
import softest

import Utils
from Pages.page_volunteer_registraion import VolunteerRegistration
from Utils.logger import Logger
from Utils import logger

from Utils.parse_yaml_file import excel_signup_test_data_file, excel_volunteer_registration_file, \
    excel_volunteer_registration_positive_sheet_name
# from Utils.parse_yaml_file import signup_positive_test_data_sheet_name
from Utils.excel_utils import ExcelUtils
from Utils.screenshot_utils import ScreenshotUtils
import pandas as pd
from Pages.page_signup import SignUp
from Utils.parse_yaml_file import excel_signup_positive_sheet_name



@pytest.mark.usefixtures("setup")
class test_Volunteer_Registration_Positive(softest.TestCase):
    @pytest.mark.sanity
    def test_volunteer_registration_positive(self):
        self.volunteerregistration = VolunteerRegistration(self.driver)
        self.excelutils = ExcelUtils(excel_volunteer_registration_file)
        dataframe = self.excelutils.load_workbook(excel_volunteer_registration_positive_sheet_name)
        custom_logger = Logger()
        self.log = custom_logger.get_logger()
        for i in dataframe.index:
            entry = dataframe.iloc[i]

            # Click on Volunteer Menu
            self.volunteerregistration.click_volunteer_menu()
            # Click on Register Now button
            self.volunteerregistration.click_register_now_button()
            # Input full name in the name field
            self.volunteerregistration.input_full_name(entry['Fullname'])
            # Input phone number in the Mobile field
            self.volunteerregistration.input_phone_number(str(entry['Mobile']))
            # Input email in the email field
            self.volunteerregistration.input_email(str(entry['Email']))
            # Input Date of Birth
            self.volunteerregistration.input_date_of_birth(str(entry['Date of Birth']))
            ScreenshotUtils.capture_screenshot(self.driver,entry['Email'])
            # Input Address
            self.volunteerregistration.input_address(entry['Address'])
            # Select City from dropdown
            self.volunteerregistration.select_city(entry['City'])
            # Select State from dropdown
            self.volunteerregistration.select_state(entry['State'])
            # Click Male or Female radio button
            self.volunteerregistration.select_gender(entry['Gender'])
            # Click Areas of Interest radio button
            self.volunteerregistration.click_areas_of_interests(entry['Areas_of_Interest'])
            # Upload profile picture
            self.volunteerregistration.click_choose_file(entry['Profile_Picture'])
            # Click on Submit button
            self.volunteerregistration.click_submit_application_button()

            self.success_or_error_msg = entry['Message']


            # Capture Screenshot
            ScreenshotUtils.capture_screenshot(self.driver,entry['Email'])

            actual_success_message = self.volunteerregistration.is_volunteer_registration_success_message_displayed()
            expected_success_message = entry['Message']
            self.log.info(f"Expected Success Message: {expected_success_message}")
            self.log.info(f"Actual Success Message: {actual_success_message}")
            # Validate if acutal success message is similar to expected success message
            try:
                if actual_success_message == expected_success_message:
                    self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass', excel_volunteer_registration_positive_sheet_name)
                else:
                    self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_volunteer_registration_positive_sheet_name)
                    assert False, f"Volunteer Registration failed for Excel row {i + 2} and {entry['Email']}"
            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_volunteer_registration_positive_sheet_name)
                assert False, f"Volunteer Registration failed for Excel row {i + 2} and {entry['Email']}"


            ScreenshotUtils.capture_screenshot(self.driver,entry['Email'])

            # Click on Back to Volunteer button after successful registration
            self.volunteerregistration.click_back_to_volunteer_button()














