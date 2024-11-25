from pages.base_page import BasePage

class LoginPage(BasePage):

    LOCATORS = {
        "uname": "username",
        "pwd": "password", 
        "submit_btn": ".orangehrm-login-button"
    }

    def  __init__(self, page, config_data):
        self.username = config_data['username']
        self.password = config_data['password']
        super().__init__(page, config_data['hostname'])

    def navigate_login (self):
        self.navigate("")

    def enter_username (self):
        self.fill_input(self.LOCATORS['uname'],self.username)

    def enter_password (self):
        self.fill_input(self.LOCATORS['pwd'], self.password)
    
    def click_login (self):
        self.click_element(self.LOCATORS['submit_btn'])

    def authenticate (self):
        self.enter_username()
        self.enter_password()
        self.click_login()
