from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import os

class UploadPage(BasePage):

    FILE_INPUT = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    UPLOADED_MESSAGE = (By.TAG_NAME, "h3")

    def open_upload_page(self):
        self.open("upload")

    def upload_file(self, filename):
        abs_path = os.path.abspath(filename)
        self.driver.find_element(*self.FILE_INPUT).send_keys(abs_path)
        self.driver.find_element(*self.UPLOAD_BUTTON).click()

    def get_message(self):
        return self.driver.find_element(*self.UPLOADED_MESSAGE).text
