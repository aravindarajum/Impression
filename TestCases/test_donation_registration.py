import time

import pytest
import softest

from Pages.page_donation_registration import DonationRegistration
from Utils.logger import Logger

from Utils.parse_yaml_file import excel_signup_test_data_file, excel_volunteer_registration_file, \
    excel_volunteer_registration_positive_sheet_name, excel_donation_registration_file, \
    excel_donation_registration_positive_sheet_name
# from Utils.parse_yaml_file import signup_positive_test_data_sheet_name
from Utils.excel_utils import ExcelUtils
from Utils.screenshot_utils import ScreenshotUtils




@pytest.mark.usefixtures("setup")
class test_Donation_Registration_Positive(softest.TestCase):
    @pytest.mark.sanity
    def test_donation_registration_positive(self):
        self.donationregistration = DonationRegistration(self.driver)
        self.excelutils = ExcelUtils(excel_donation_registration_file)
        dataframe = self.excelutils.load_workbook(excel_donation_registration_positive_sheet_name)
        custom_logger = Logger()
        self.log = custom_logger.get_logger()
        for i in dataframe.index:
            entry = dataframe.iloc[i]

            # Click on Donate Menu
            self.donationregistration.click_donate_menu()
            # Click on Donate Now button
            self.donationregistration.click_donate_now_button()
            # Input Donation Amount
            self.donationregistration.input_donation_amount(str(entry['Donation_Amount']))
            # Input Full name in the name field
            self.donationregistration.input_full_name(entry['Fullname'])
            # Input email in the email field
            self.donationregistration.input_email(str(entry['Email']))
            # Input phone number in the Mobile field
            self.donationregistration.input_phone_number(str(entry['Phone']))
            # Input Address
            self.donationregistration.input_address(entry['Address'])

            # Click on Submit button
            self.donationregistration.click_donate_submit_button()

            time.sleep(2)

            # Capture Screenshot
            actual_success_message = self.driver.switch_to.alert.text

            expected_success_message = entry['Message']
            self.log.info(f"Expected Success Message: {expected_success_message}")
            self.log.info(f"Actual Success Message: {actual_success_message}")
            # Validate if Alert actual message = alert expected message
            try:
                if expected_success_message == actual_success_message:
                    ScreenshotUtils.capture_screenshot(self.driver, entry['Email'])
                    self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass', excel_donation_registration_positive_sheet_name)
                    self.log.info(f"Expected Success Message: {expected_success_message}")
                    self.log.info(f"Actual Success Message: {actual_success_message}")
                else:
                    ScreenshotUtils.capture_screenshot(self.driver, entry['Email'])
                    self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_donation_registration_positive_sheet_name)
                    self.log.info(f"Expected Success Message: {expected_success_message}")
                    self.log.info(f"Actual Success Message: {actual_success_message}")
                    assert False, f"Expected Success Message: {expected_success_message}. Actual Success Message: {actual_success_message}. Donation Registration failed for Excel row {i + 2} and {entry['Email']}"
            except Exception as e:
                ScreenshotUtils.capture_screenshot(self.driver, entry['Email'])
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_donation_registration_positive_sheet_name)
                self.log.info(f"Expected Success Message: {expected_success_message}")
                self.log.info(f"Actual Success Message: {actual_success_message}")
                assert False, f"Expected Success Message: {expected_success_message}. Actual Success Message: {actual_success_message}. Donation Registration failed for Excel row {i + 2} and {entry['Email']}"
                # assert False, f"Donation Registration failed for Excel row {i + 2} and {entry['Email']}"


            ScreenshotUtils.capture_screenshot(self.driver,entry['Email'])

            # Click on Browser Back button after successful donation
            self.driver.back()














