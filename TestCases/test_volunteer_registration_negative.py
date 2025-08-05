import pytest
import softest

import Utils
from Pages.page_volunteer_registraion import VolunteerRegistration
from Utils.logger import Logger
from Utils import logger

from Utils.parse_yaml_file import excel_signup_test_data_file, excel_signup_negative_pwd_confiPwd_not_same_sheet_name, \
    excel_volunteer_registration_file, excel_volunteer_registration_negative_sheet_name
# from Utils.parse_yaml_file import signup_positive_test_data_sheet_name
from Utils.excel_utils import ExcelUtils
from Utils.screenshot_utils import ScreenshotUtils
import pandas as pd
from Pages.page_signup import SignUp
from Utils.parse_yaml_file import excel_signup_negative_sheet_name



@pytest.mark.usefixtures("setup")
class test_Volunteer_Registration_negative(softest.TestCase):
    @pytest.mark.sanity
    def test_volunteer_registration_negative(self):
        self.volunteerregistration = VolunteerRegistration(self.driver)
        self.excelutils = ExcelUtils(excel_volunteer_registration_file)
        dataframe = self.excelutils.load_workbook(excel_volunteer_registration_negative_sheet_name)
        custom_logger = Logger()
        self.log = custom_logger.get_logger()

        for i in dataframe.index:
            entry = dataframe.iloc[i]
            self.volunteerregistration.click_volunteer_menu()
            self.volunteerregistration.click_register_now_button()

            self.volunteerregistration.input_full_name(entry['Fullname']) if pd.notna(entry['Fullname']) else ''
            self.volunteerregistration.input_phone_number(int(entry['Mobile'])) if pd.notna(entry['Mobile']) else ''
            self.volunteerregistration.input_email(entry['Email']) if pd.notna(entry['Email']) else ''
            self.volunteerregistration.input_date_of_birth(entry['Date of Birth']) if pd.notna(entry['Date of Birth']) else ''
            self.volunteerregistration.input_address(entry['Address']) if pd.notna(entry['Address']) else ''
            self.volunteerregistration.select_city(entry['City']) if pd.notna(entry['City']) else ''
            self.volunteerregistration.select_state(entry['State']) if pd.notna(entry['State']) else ''
            self.volunteerregistration.select_gender(entry['Gender']) if pd.notna(entry['Gender']) else ''
            self.volunteerregistration.click_areas_of_interests(entry['Areas_of_Interest']) if pd.notna(entry['Areas_of_Interest']) else ''

            self.volunteerregistration.click_submit_application_button()

# -----------------------------------------------------------------------------------------------------------------------------------------
            # Check if Fullname field is empty. If empty check if the error message displayed
            try:
                is_name_field_empty = self.volunteerregistration.is_volunteer_form_name_field_empty()
                if is_name_field_empty:
                    is_name_error_msg_displayed = self.volunteerregistration.is_name_required_error_message_present()
                    if is_name_error_msg_displayed:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass', excel_volunteer_registration_negative_sheet_name)
            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_volunteer_registration_negative_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"

# -----------------------------------------------------------------------------------------------------------------------------------------
            # Check if Phone Number field is empty. If empty check if the error message displayed
            try:
                is_mobile_number_field_empty = self.volunteerregistration.is_volunteer_form_phone_number_field_empty()
                if is_mobile_number_field_empty:
                    is_mobile_number_error_msg_displayed = self.volunteerregistration.is_mobile_number_required_error_message_present()
                    if is_mobile_number_error_msg_displayed:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass',
                                                                     excel_volunteer_registration_negative_sheet_name)
            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_volunteer_registration_negative_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"

# -----------------------------------------------------------------------------------------------------------------------------------------
            # Check if Email field is empty. If empty check if the error message displayed
            try:
                is_volunteer_email_field_empty = self.volunteerregistration.is_volunteer_form_email_field_empty()
                if is_volunteer_email_field_empty:
                    is_volunteer_email_error_msg_displayed = self.volunteerregistration.is_email_required_error_message_present()
                    if is_volunteer_email_error_msg_displayed:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass',
                                                                     excel_volunteer_registration_negative_sheet_name)
                    else:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                                     excel_volunteer_registration_negative_sheet_name)
                        assert False, f"Name error message not displayed for Excel row {i + 2}"
            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                                     excel_volunteer_registration_negative_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"

# -----------------------------------------------------------------------------------------------------------------------------------------
            # Check if Date of Birth field is empty. If empty check if the error message displayed
            try:
                is_date_of_birth_field_empty = self.volunteerregistration.is_date_of_birth_form_field_empty()
                if is_date_of_birth_field_empty:
                    is_date_of_birth_error_msg_displayed = self.volunteerregistration.is_date_of_birth_required_error_message_present()
                    if is_date_of_birth_error_msg_displayed:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass',
                                                                     excel_volunteer_registration_negative_sheet_name)
                    else:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                                     excel_volunteer_registration_negative_sheet_name)
                        assert False, f"Name error message not displayed for Excel row {i + 2}"

            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                             excel_volunteer_registration_negative_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"
# -----------------------------------------------------------------------------------------------------------------------------------------
            # Check if Address field is empty. If empty check if the error message displayed
            try:
                is_address_field_empty = self.volunteerregistration.is_address_form_field_empty()
                if is_address_field_empty:
                    is_address_error_msg_displayed = self.volunteerregistration.is_address_required_error_message_present()
                    if is_address_error_msg_displayed:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass',
                                                                     excel_volunteer_registration_negative_sheet_name)
                    else:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                                     excel_volunteer_registration_negative_sheet_name)
                        assert False, f"Name error message not displayed for Excel row {i + 2}"

            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                             excel_volunteer_registration_negative_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"
# -----------------------------------------------------------------------------------------------------------------------------------------
            # Check if City field is empty. If empty check if the error message displayed
            try:
                is_city_field_empty = self.volunteerregistration.is_city_form_field_empty()
                if is_city_field_empty:
                    is_city_error_msg_displayed = self.volunteerregistration.is_city_required_error_message_present()
                    if is_city_error_msg_displayed:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass',
                                                                     excel_volunteer_registration_negative_sheet_name)
                    else:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                                     excel_volunteer_registration_negative_sheet_name)
                        assert False, f"Name error message not displayed for Excel row {i + 2}"

            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                             excel_volunteer_registration_negative_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"
# -----------------------------------------------------------------------------------------------------------------------------------------
            # Check if State field is empty. If empty check if the error message displayed
            try:
                is_state_field_empty = self.volunteerregistration.is_state_form_field_empty()
                if is_state_field_empty:
                    is_state_error_msg_displayed = self.volunteerregistration.is_state_required_error_message_present()
                    if is_state_error_msg_displayed:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass',
                                                                     excel_volunteer_registration_negative_sheet_name)
                    else:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                                     excel_volunteer_registration_negative_sheet_name)
                        assert False, f"Name error message not displayed for Excel row {i + 2}"

            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                             excel_volunteer_registration_negative_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"
# -----------------------------------------------------------------------------------------------------------------------------------------
            # Check if Gender field is empty. If empty check if the error message displayed
            try:
                is_gender_field_selected = self.volunteerregistration.is_gender_form_field_selected()
                if is_gender_field_selected:
                    is_gender_error_msg_displayed = self.volunteerregistration.is_gender_required_error_message_present()
                    if is_gender_error_msg_displayed:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass',
                                                                     excel_volunteer_registration_negative_sheet_name)
                    else:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                                     excel_volunteer_registration_negative_sheet_name)
                        assert False, f"Name error message not displayed for Excel row {i + 2}"

            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                             excel_volunteer_registration_negative_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"
# -----------------------------------------------------------------------------------------------------------------------------------------
            # Check if Areas of Interest field is empty. If empty check if the error message displayed
            try:
                is_areas_of_interest_fields_selected = self.volunteerregistration.is_areas_of_interest_form_fields_selected()
                if is_areas_of_interest_fields_selected:
                    is_areas_of_interest_error_msg_displayed = self.volunteerregistration.is_areas_of_interested_error_message_present()
                    if is_areas_of_interest_error_msg_displayed:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass',
                                                                     excel_volunteer_registration_negative_sheet_name)
                    else:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                                     excel_volunteer_registration_negative_sheet_name)
                        assert False, f"Name error message not displayed for Excel row {i + 2}"

            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                             excel_volunteer_registration_negative_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"
        # -----------------------------------------------------------------------------------------------------------------------------------------

            ScreenshotUtils.capture_screenshot(self.driver,entry['Email'])
            # Refresh browser
            self.driver.back()
    #
    # @pytest.mark.sanity
    # def test_signup_negative_pwd_confPwd_not_same(self):
    #     self.signup = SignUp(self.driver)
    #     self.excelutils = ExcelUtils(excel_signup_test_data_file)
    #     dataframe = self.excelutils.load_workbook(excel_signup_negative_pwd_confiPwd_not_same_sheet_name)
    #
    #     for i in dataframe.index:
    #         entry = dataframe.iloc[i]
    #
    #         self.signup.click_signup_menu()
    #         self.signup.input_full_name(entry['Fullname'])
    #         self.signup.input_email(entry['Email'])
    #         self.signup.input_phone_number(int(entry['Phone']))
    #         self.signup.input_password(entry['Password'])
    #         self.signup.input_confirm_password(entry['ConfirmPassword'])
    #         self.signup.click_signup_button()
    #
    #         try:
    #             is_password_not_same_error_msg_displayed = self.signup.is_confirm_password_required_error_message_present()
    #             if is_password_not_same_error_msg_displayed:
    #                 self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass',
    #                                                              excel_signup_negative_pwd_confiPwd_not_same_sheet_name)
    #             else:
    #                 self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
    #                                                              excel_signup_negative_pwd_confiPwd_not_same_sheet_name)
    #                 assert False, f"Name error message not displayed for Excel row {i + 2}"
    #
    #         except Exception as e:
    #             self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
    #                                                          excel_signup_negative_pwd_confiPwd_not_same_sheet_name)
    #             assert False, f"Name error message not displayed for Excel row {i + 2}"
    #
    #
    #
    #
    #










