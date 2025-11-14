from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import csv

class TablePage(BasePage):

    TABLE_ROWS = (By.CSS_SELECTOR, "#table1 tbody tr")

    def open_table(self):
        self.open("tables")

    def extract_table_data(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        data = []

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = [c.text for c in cells]
            data.append(row_data)

        return data

    def save_to_csv(self, data, filename="table_data.csv"):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Last Name", "First Name", "Email", "Due", "Website", "Action"])
            writer.writerows(data)
