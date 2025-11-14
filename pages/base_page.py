from selenium import webdriver
from selenium.webdriver.edge.service import Service
from config import BASE_URL, EDGE_DRIVER_PATH

class BasePage:
    def __init__(self):
        service = Service(EDGE_DRIVER_PATH)
        self.driver = webdriver.Edge(service=service)

    def open(self, path=""):
        self.driver.get(f"{BASE_URL}/{path}")

    def close(self):
        self.driver.quit()
