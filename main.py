from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class SnackLiftAutomation:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://appbrewery.github.io/gym/")


    def login(self):
        button_navigate_login = self.driver.find_element(By.ID, "login-button")
        button_navigate_login.click()
        self.driver.implicitly_wait(3)
        field_email = self.driver.find_element(By.ID, "email-input")
        field_email.send_keys("student@test.com")
        field_password = self.driver.find_element(By.ID, "password-input")
        field_password.send_keys("password123")
        submit_button = self.driver.find_element(By.ID, "submit-button")
        submit_button.click()
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "myElementId"))
            )
            print("Element is present in the DOM.")
        except:
            print("Element is not present in the DOM within the timeout.")





if __name__ == "__main__":
    instance = SnackLiftAutomation()
    instance.login()
    instance.driver.close()

