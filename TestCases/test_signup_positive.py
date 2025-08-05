import pytest
import softest

import Utils
from Utils.logger import Logger
from Utils import logger

from Utils.parse_yaml_file import excel_signup_test_data_file
# from Utils.parse_yaml_file import signup_positive_test_data_sheet_name
from Utils.excel_utils import ExcelUtils
from Utils.screenshot_utils import ScreenshotUtils
import pandas as pd
from Pages.page_signup import SignUp
from Utils.parse_yaml_file import excel_signup_positive_sheet_name



@pytest.mark.usefixtures("setup")
class test_SingUp_positive(softest.TestCase):
    @pytest.mark.sanity
    def test_signup_positive(self):
        self.signup = SignUp(self.driver)
        self.excelutils = ExcelUtils(excel_signup_test_data_file)
        dataframe = self.excelutils.load_workbook(excel_signup_positive_sheet_name)


        for i in dataframe.index:
            entry = dataframe.iloc[i]

            self.signup.click_signup_menu()
            self.signup.input_full_name(entry['Fullname'])
            self.signup.input_email(entry['Email'])
            self.signup.input_phone_number(str(entry['Phone']))
            self.signup.input_password(entry['Password'])
            self.signup.input_confirm_password(entry['ConfirmPassword'])
            self.signup.click_signup_button()
            self.success_or_error_msg = entry['Message']


            # Capture Screenshot
            ScreenshotUtils.capture_screenshot(self.driver,entry['Email'])

            actual_success_message = self.signup.signup_success_message_get_text()
            expected_success_message = entry['Message']

            # Validate if acutal success message is similar to expected success message
            try:
                if actual_success_message == expected_success_message:
                    self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass', excel_signup_positive_sheet_name)
                else:
                    self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_signup_positive_sheet_name)
                    assert False, f"Signup failed for Excel row {i + 2} and {entry['Email']}"
            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_signup_positive_sheet_name)
                assert False, f"Signup failed for Excel row {i + 2} and {entry['Email']}"

            # Click Signout button
            self.signup.wait_until_signup_dialog_closes()
            ScreenshotUtils.capture_screenshot(self.driver,entry['Email'])
            self.signup.click_sign_out_menu()














