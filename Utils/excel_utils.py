import pandas as pd

from Utils.logger import Logger


class ExcelUtils:
    def __init__(self,file_path):
        self.file_path = file_path
        custom_logger = Logger()
        self.log = custom_logger.get_logger()

    def load_workbook(self, Sheet_Name = None):
        try:
            if Sheet_Name:
                return pd.read_excel(self.file_path, sheet_name=Sheet_Name)
            else:
                return pd.read_excel(self.file_path)
        except FileNotFoundError as e:
            self.log.error(f"Error: File '{self.file_path}' not found.")
            self.log.error(f"Exception:  '{e}'")
            return None
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            return None

    def update_pass_or_fail_in_sheet(self, dataframe, i, pass_or_fail, sheet_name=None):
        try:
            result = 'Pass' if pass_or_fail == 'Pass' else 'Fail'
            
            # Read all sheets from the Excel file
            all_sheets = pd.read_excel(self.file_path, sheet_name=None)
            
            # Update the specific sheet
            target_sheet = sheet_name if sheet_name else list(all_sheets.keys())[0]
            all_sheets[target_sheet]['Result'] = all_sheets[target_sheet]['Result'].astype('object')
            all_sheets[target_sheet].at[i, 'Result'] = result
            
            # Write back all sheets
            with pd.ExcelWriter(self.file_path, engine='openpyxl') as writer:
                for sheet, data in all_sheets.items():
                    data.to_excel(writer, sheet_name=sheet, index=False)
            
            return None
        except Exception as e:
            print(f"An error occurred while updating result: {e}")
            return None



    # Update Test Data Excel file with Pass / Fail
    # def update_pass_or_fail_in_sheet(self,dataframe, i, is_element_present):
    #     try:
    #         if is_element_present:
    #             result = 'Pass'
    #         else:
    #             result = 'Fail'
    #
    #         dataframe['Result'] = dataframe['Result'].astype('object')
    #         dataframe.at[i, 'Result'] = result
    #         dataframe.to_excel(self.file_path, index=False)
    #         return None
    #     except Exception as e:
    #         print(f"An error occurred while updating result: {e}")
    #         return None




