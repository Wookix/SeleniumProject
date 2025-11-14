from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import os
import time

class DownloadPage(BasePage):

    FILE_LINKS = (By.CSS_SELECTOR, ".example a")  # Solo archivos

    def open_download_page(self):
        self.open("download")

    def click_first_file(self):
        files = self.driver.find_elements(*self.FILE_LINKS)
        file_element = files[0]        # Primer archivo real
        filename = file_element.text
        file_element.click()
        return filename

    def file_exists_in_downloads(self, filename):
        downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        return os.path.isfile(os.path.join(downloads, filename))

