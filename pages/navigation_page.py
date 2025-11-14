from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class NavigationPage(BasePage):

    def go_to_home(self):
        self.open("")  # Página principal

    def go_to_checkbox(self):
        self.open("checkboxes")

    def go_to_inputs(self):
        self.open("inputs")

    def go_to_alerts(self):
        self.open("javascript_alerts")

    def get_title(self):
        return self.driver.find_element(By.TAG_NAME, "h3").text
