import time

import pytest
import softest

import Utils
from Pages.page_donation_women_empowerment import DonationWomenEmpowermentRegistration
from Utils.logger import Logger
from Utils import logger

from Utils.parse_yaml_file import excel_donation_womenempowerment_file, excel_donation_womenempowerment_positive_sheet_name
from Utils.excel_utils import ExcelUtils
from Utils.screenshot_utils import ScreenshotUtils
import pandas as pd
from Pages.page_signup import SignUp


@pytest.mark.usefixtures("setup")
class test_Donation_Women_Empowerment_Positive(softest.TestCase):
    @pytest.mark.sanity
    def test_donation_women_empowerment_positive(self):
        self.donationwomenempowermentregistration = DonationWomenEmpowermentRegistration(self.driver)
        self.excelutils = ExcelUtils(excel_donation_womenempowerment_file)
        dataframe = self.excelutils.load_workbook(excel_donation_womenempowerment_positive_sheet_name)
        custom_logger = Logger()
        self.log = custom_logger.get_logger()
        for i in dataframe.index:
            entry = dataframe.iloc[i]

            # Click on Donate Menu
            self.donationwomenempowermentregistration.click_donate_menu()
            # Click on Donate Now button
            self.donationwomenempowermentregistration.click_donate_now_button()
            # Input Donation Amount
            self.donationwomenempowermentregistration.input_donation_amount(str(entry['Donation_Amount']))
            # Input Full name in the name field
            self.donationwomenempowermentregistration.input_full_name(entry['Fullname'])
            # Input email in the email field
            self.donationwomenempowermentregistration.input_email(str(entry['Email']))
            # Input phone number in the Mobile field
            self.donationwomenempowermentregistration.input_phone_number(str(entry['Phone']))
            # Input Address
            self.donationwomenempowermentregistration.input_address(entry['Address'])

            # Click on Submit button
            self.donationwomenempowermentregistration.click_donate_submit_button()

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
                    self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Pass', excel_donation_womenempowerment_positive_sheet_name)
                    self.log.info(f"Expected Success Message: {expected_success_message}")
                    self.log.info(f"Actual Success Message: {actual_success_message}")
                else:
                    ScreenshotUtils.capture_screenshot(self.driver, entry['Email'])
                    self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_donation_womenempowerment_positive_sheet_name)
                    self.log.info(f"Expected Success Message: {expected_success_message}")
                    self.log.info(f"Actual Success Message: {actual_success_message}")
                    assert False, f"Expected Success Message: {expected_success_message}. Actual Success Message: {actual_success_message}. Donation Registration failed for Excel row {i + 2} and {entry['Email']}"
            except Exception as e:
                ScreenshotUtils.capture_screenshot(self.driver, entry['Email'])
                self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, 'Fail', excel_donation_womenempowerment_positive_sheet_name)
                self.log.info(f"Expected Success Message: {expected_success_message}")
                self.log.info(f"Actual Success Message: {actual_success_message}")
                assert False, f"Expected Success Message: {expected_success_message}. Actual Success Message: {actual_success_message}. Donation Registration failed for Excel row {i + 2} and {entry['Email']}"

            ScreenshotUtils.capture_screenshot(self.driver,entry['Email'])

            # Click on Browser Back button after successful donation
            self.driver.back()














