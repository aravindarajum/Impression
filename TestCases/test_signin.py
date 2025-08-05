import pytest
import softest

import Utils
from Pages.page_signin import SignIn
from Utils.logger import Logger
from Utils import logger

from Utils.parse_yaml_file import excel_signup_test_data_file, excel_signin_test_data_file, \
    excel_signin_positive_test_data_file
from Utils.excel_utils import ExcelUtils
from Utils.screenshot_utils import ScreenshotUtils
import pandas as pd
from Pages.page_signup import SignUp



@pytest.mark.usefixtures("setup")
class test_SingIn(softest.TestCase):
    @pytest.mark.sanity
    def test_signup(self):
        self.signin = SignIn(self.driver)
        self.excelutils = ExcelUtils(excel_signin_test_data_file)
        dataframe = self.excelutils.load_workbook(excel_signin_positive_test_data_file)


        for i in dataframe.index:
            entry = dataframe.iloc[i]

            self.signin.click_signin_menu()
            self.signin.input_email(entry['Email'])
            self.signin.input_password(entry['Password'])
            self.signin.click_signin_button()

            # Capture Screenshot
            ScreenshotUtils.capture_screenshot(self.driver,entry['Email'])

            # Update Sign Up Excel file 'Result' column with Pass / Fail
            try:
                # Check if 'Sign Out' link present in the Menu
                is_element_present = self.signin.is_success_message_displayed()
                if is_element_present:
                    self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass', excel_signin_positive_test_data_file)

                else:
                    # Fail the test if signup was not successful
                    self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_signin_positive_test_data_file)
                    assert False, f"SignIn failed for {entry['Email']}"
            except Exception as e:
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_signin_positive_test_data_file)
                assert False, f"SignIn failed for {entry['Email']}"

            # Click Signout button
            self.signin.wait_until_signin_form_closes()
            self.signin.click_sign_out_menu()












