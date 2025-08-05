import pytest
import softest

import Utils
from Utils.logger import Logger
from Utils import logger

from Utils.parse_yaml_file import excel_signup_test_data_file, excel_signup_negative_pwd_confiPwd_not_same_sheet_name
# from Utils.parse_yaml_file import signup_positive_test_data_sheet_name
from Utils.excel_utils import ExcelUtils
from Utils.screenshot_utils import ScreenshotUtils
import pandas as pd
from Pages.page_signup import SignUp
from Utils.parse_yaml_file import excel_signup_negative_sheet_name



@pytest.mark.usefixtures("setup")
class test_SingUp_negative(softest.TestCase):
    @pytest.mark.sanity
    def test_signup_negative(self):
        self.signup = SignUp(self.driver)
        self.excelutils = ExcelUtils(excel_signup_test_data_file)
        dataframe = self.excelutils.load_workbook(excel_signup_negative_sheet_name)

        for i in dataframe.index:
            entry = dataframe.iloc[i]

            self.signup.click_signup_menu()
            self.signup.input_full_name(entry['Fullname']) if pd.notna(entry['Fullname']) else ''
            self.signup.input_email(entry['Email']) if pd.notna(entry['Email']) else ''
            self.signup.input_phone_number(int(entry['Phone'])) if pd.notna(entry['Phone']) else ''
            self.signup.input_password(entry['Password']) if pd.notna(entry['Password']) else ''
            # self.signup.input_confirm_password(entry['ConfirmPassword']) if pd.notna(entry['ConfirmPassword']) else ''
            self.signup.click_signup_button()

            # Check if Fullname field is empty. If empty check if the error message displayed
            try:
                is_name_field_empty = self.signup.is_signup_form_name_field_empty()
                if is_name_field_empty:
                    is_name_error_msg_displayed = self.signup.is_name_required_error_message_present()
                    if is_name_error_msg_displayed:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass', excel_signup_negative_sheet_name)
            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_signup_negative_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"


            # Check if Email field is empty. If empty check if the error message displayed
            try:
                is_email_field_empty = self.signup.is_signup_form_email_field_empty()
                if is_email_field_empty:
                    is_email_error_msg_displayed = self.signup.is_email_required_error_message_present()
                    if is_email_error_msg_displayed:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass',
                                                                     excel_signup_negative_sheet_name)
            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                                     excel_signup_negative_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"

            # Check if Phone Number field is empty. If empty check if the error message displayed
            try:
                is_phone_number_field_empty = self.signup.is_signup_form_phone_number_field_empty()
                if is_phone_number_field_empty:
                    is_phone_number_error_msg_displayed = self.signup.is_phone_number_required_error_message_present()
                    if is_phone_number_error_msg_displayed:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass',
                                                                     excel_signup_negative_sheet_name)
            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_signup_negative_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"

            # Check if Password field is empty. If empty check if the error message displayed
            try:
                is_password_field_empty = self.signup.is_signup_form_password_field_empty()
                if is_password_field_empty:
                    is_password_error_msg_displayed = self.signup.is_password_required_error_message_present()
                    if is_password_error_msg_displayed:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass',
                                                                     excel_signup_negative_sheet_name)
                    else:
                        self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                                     excel_signup_negative_sheet_name)
                        assert False, f"Name error message not displayed for Excel row {i + 2}"

            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                             excel_signup_negative_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"


            ScreenshotUtils.capture_screenshot(self.driver,entry['Email'])
            # Refresh browser
            self.signup.browser_refresh()

    @pytest.mark.sanity
    def test_signup_negative_pwd_confPwd_not_same(self):
        self.signup = SignUp(self.driver)
        self.excelutils = ExcelUtils(excel_signup_test_data_file)
        dataframe = self.excelutils.load_workbook(excel_signup_negative_pwd_confiPwd_not_same_sheet_name)

        for i in dataframe.index:
            entry = dataframe.iloc[i]

            self.signup.click_signup_menu()
            self.signup.input_full_name(entry['Fullname'])
            self.signup.input_email(entry['Email'])
            self.signup.input_phone_number(int(entry['Phone']))
            self.signup.input_password(entry['Password'])
            self.signup.input_confirm_password(entry['ConfirmPassword'])
            self.signup.click_signup_button()

            try:
                is_password_not_same_error_msg_displayed = self.signup.is_confirm_password_required_error_message_present()
                if is_password_not_same_error_msg_displayed:
                    self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass',
                                                                 excel_signup_negative_pwd_confiPwd_not_same_sheet_name)
                else:
                    self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                                 excel_signup_negative_pwd_confiPwd_not_same_sheet_name)
                    assert False, f"Name error message not displayed for Excel row {i + 2}"

            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail',
                                                             excel_signup_negative_pwd_confiPwd_not_same_sheet_name)
                assert False, f"Name error message not displayed for Excel row {i + 2}"















