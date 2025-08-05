# Import Selenium WebDriver support modules for explicit waits and expected conditions
import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utils import logger
from Utils.logger import Logger
from selenium.webdriver.common.by import By


class BaseDriver:
    """Base class that provides common WebDriver functionality"""
    
    def __init__(self,driver):
        """Initialize BaseDriver with WebDriver instance and wait configuration
        Args:
            driver: Selenium WebDriver instance
        """
        self.excelutils = None
        self.driver = driver
        # Configure explicit wait with 5 second timeout and 0.2s polling
        self.wait = WebDriverWait(driver,10,poll_frequency=0.2)
        custom_logger = Logger()
        self.log = custom_logger.get_logger()

    def click_element(self,locator):
        """Click on a web element identified by locator
        Args:
            locator: Tuple of By strategy and locator string
        """
        try:
            # Wait for element to be present and click it
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.log.info(f'Element Found {locator}')
            element.click()
            self.log.info(f'Clicked on {locator}')
        except Exception as e:
            self.log.error(f'Element Not Found {locator}')
            self.log.error(f'Exception : {e}')

    def input_textbox(self,locator,value):
        """Input text into textbox element identified by locator
        Args:
            locator: Tuple of By strategy and locator string
            value: Text to input into the textbox
        """
        try:
            # Wait for element to be present and send keys
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.log.info(f'Element Found {locator}')
            element.clear()
            element.send_keys(value)
            self.log.info(f'Input successful to {locator}')
        except Exception as e:
            self.log.error(f'Element Not Found {locator}')
            self.log.error(f'Exception : {e}')

    def input_date_control(self,locator,value):
        try:
            # Wait for element to be present and send keys
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.log.info(f'Element Found {locator}')
            self.log.info(value)
            element.send_keys(value)
            self.log.info(f'Input successful to {locator}')
        except Exception as e:
            self.log.error(f'Element Not Found {locator}')
            self.log.error(f'Exception : {e}')

    def click_radio_button(self,locator):
        try:
            # Wait for element to be present and click it
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.log.info(f'Element Found {locator}')
            if not element.is_selected():
                element.click()
                self.log.info(f'Clicked on {locator}')
        except Exception as e:
            self.log.error(f'Element Not Found {locator}')
            self.log.error(f'Exception : {e}')

    def click_checkbox(self,locator):
        try:
            # Wait for element to be present and click it
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.log.info(f'Element Found {locator}')
            if not element.is_selected():
                element.click()
                self.log.info(f'Clicked on {locator}')
        except Exception as e:
            self.log.error(f'Element Not Found {locator}')
            self.log.error(f'Exception : {e}')

    def upload_file(self,locator,file_path):
        try:
            # Wait for element to be present and click it
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.log.info(f'Element Found {locator}')
            # Path to the file you want to upload
            local_file_path = os.path.abspath(file_path)
            # Send the file path directly to the input element
            element.send_keys(local_file_path)
            self.log.info(f'File uploaded {file_path}')
        except Exception as e:
            self.log.error(f'Element Not Found {locator}')
            self.log.error(f'Exception : {e}')

    def is_element_located(self,locator):
        try:
            # Wait for element to be present
            element = self.wait.until(EC.presence_of_element_located(locator))
            if element.is_displayed():
                self.log.info(f'Element Found {locator}')
                return True
            else:
                self.log.info(f'Element NOT Found {locator}')
                return False
        except Exception as e:
            self.log.error(f'Exception: Element Not Found {locator}')
            self.log.error(f'Exception : {e}')
            return None

    def select_from_drop_down_menu(self,locator,value):
        try:
            # Wait for element to be present and click it
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.log.info(f'Element Found {locator}')
            drop_down_text = Select(element)
            drop_down_text.select_by_visible_text(value)
            self.log.info(f'Selected {value} from drop_down')
        except Exception as e:
            self.log.error(f'Element Not Found {locator}')
            self.log.error(f'Exception : {e}')

    # Check if field is empty after input
    def is_field_empty(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.get_attribute('value') == ''
        except Exception as e:
            self.log.error(f'Exception: Element Not Found {locator}')
            self.log.error(f'Exception : {e}')
            return None

    # Check if Checkbox or Radio button selected
    def is_checkbox_or_radio_button_selected(self, locator):
        try:
            element = self.driver.find_element(*locator)
            if element.is_selected:
                return True
            else:
                return False
        except Exception as e:
            self.log.error(f'Exception: Element Not Found {locator}')
            self.log.error(f'Exception : {e}')
            return None

    def wait_until_invisibility_of_an_element(self,locator):
        try:
            # Wait for element to be INVISIBLE
            element = self.wait.until(EC.invisibility_of_element(locator))
            # self.log.info(f'Element Found {element}')
        except Exception as e:
            self.log.error(f'Element Not Found {locator}')
            self.log.error(f'Exception : {e}')


    def get_element_text(self,locator):
        try:
            # Wait for element to be present
            element = self.wait.until(EC.presence_of_element_located(locator))
            element_text = element.text
            return element_text
        except Exception as e:
            self.log.error(f'Exception: Element Not Found {locator}')
            self.log.error(f'Exception : {e}')
            return None

    def browser_refresh(self):
        self.driver.refresh()

    def alert_click_ok(self):
        try:
            # First try: Wait for JavaScript alert and get its text
            # WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            self.wait.until(EC.alert_is_present())

            alert_text = self.driver.switch_to.alert.text
            self.log.info(f'Alert found: {alert_text}')
            self.driver.switch_to.alert.accept()
            self.log.info('Accepted the alert')
            self.log.info(alert_text)
            return alert_text
            
        # except:
        #     try:
        #         # Fallback: Look for HTML element containing success message
        #         success_locator = (By.XPATH, "//*[contains(text(),'Thank you for donation')]")
        #         success_message = self.get_element_text(success_locator)
        #         if success_message:
        #             self.log.info(f'Success message found in HTML: {success_message}')
        #             return success_message
        #         else:
        #             # Try broader search
        #             broader_locator = (By.XPATH, "//*[contains(text(),'Thank you') or contains(text(),'success') or contains(text(),'Success')]")
        #             broader_message = self.get_element_text(broader_locator)
        #             if broader_message:
        #                 self.log.info(f'Broader success message found: {broader_message}')
        #                 return broader_message
                        
        except Exception as e:
            self.log.error(f'Exception: Alert Dialog box not displayed - {e}')
            return None

# # If both approaches fail
            # self.log.error(f'Exception: Neither alert nor HTML success message found')
            # return None

        # alert = self.driver.switch_to.alert
        # # alert = self.wait.until(lambda d: d.switch_to.alert)
        # alert_text = alert.text
        # alert.accept()
        # self.log.info(alert_text)
        # return alert_text

    # def check_pass_or_fail(self,element):
    #     if element:
    #         result = 'Pass'
    #         self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, result)
    #         # dataframe.at[i, 'Result'] = 'Pass'
    #     else:
    #         result = 'Fail'
    #         self.excelutils.update_pass_or_fail_in_sheet(dataframe, i, result)
    #         # dataframe.at[i, 'Result'] = 'Fail'
