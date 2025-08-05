import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

base_url = config['urls']['base_url']

excel_signin_test_data_file = config['test_data']['signin_test_data_file']
excel_signin_positive_test_data_file = config['test_data']['signin_test_data_sheet_name']


excel_signup_test_data_file = config['test_data']['signup_test_data_file']
excel_signup_positive_sheet_name = config['test_data']['signup_positive_test_data_sheet_name']
excel_signup_negative_sheet_name = config['test_data']['signup_negative_test_data_sheet_name']
excel_signup_negative_pwd_confiPwd_not_same_sheet_name = config['test_data']['signup_negative_pwd_confpwd_not_same_sheet_name']

excel_volunteer_registration_file = config['test_data']['volunteer_registration_file']
excel_volunteer_registration_positive_sheet_name = config['test_data']['volunteer_registration_positive_sheet_name']
excel_volunteer_registration_negative_sheet_name = config['test_data']['volunteer_registration_negative_sheet_name']

excel_donation_registration_file = config['test_data']['donation_registration_file']
excel_donation_registration_positive_sheet_name = config['test_data']['donation_registration_positive_sheet_name']


org_name = config['urls']['org_name']
