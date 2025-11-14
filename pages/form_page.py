from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class FormPage(BasePage):

    NUMBER_INPUT = (By.TAG_NAME, "input")
    DROPDOWN = (By.ID, "dropdown")

    def open_inputs(self):
        self.open("inputs")

    def open_dropdown(self):
        self.open("dropdown")

    def enter_number(self, value):
        field = self.driver.find_element(*self.NUMBER_INPUT)
        field.clear()
        field.send_keys(str(value))

    def get_number_value(self):
        return self.driver.find_element(*self.NUMBER_INPUT).get_attribute("value")

    def select_dropdown_option(self, option_value):
        dropdown = Select(self.driver.find_element(*self.DROPDOWN))
        dropdown.select_by_value(option_value)

    def get_selected_dropdown_text(self):
        dropdown = Select(self.driver.find_element(*self.DROPDOWN))
        return dropdown.first_selected_option.text
