
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class SeleniumBase:
    def __init__(self, waitTime):
        options = Options()

        # options.add_argument("--headless")

        self.driver = WebDriver(options=options)
        self.wait = WebDriverWait(self.driver, waitTime)

    def get_by_xpath(self, xpath):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(15)

        return self.driver.find_element(By.XPATH, xpath)
