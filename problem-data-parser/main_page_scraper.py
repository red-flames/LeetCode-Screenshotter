from locators import ProblemPage
from locators import ProblemRow
from selenium_base import SeleniumBase

import csv
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class MainPageScraper(SeleniumBase):
    def __init__(self, waitTime=15):
        super().__init__(waitTime)
        self.csv_path = "data/problem_data.csv"

        # Load the page
        self.driver.get(ProblemPage.URL)
        self.wait.until(EC.title_is(ProblemPage.TITLE))
        time.sleep(2)

    def write_to_csv(self, row):
        with open(self.csv_path, "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(row)

    def parse_problem_div(self, row):
        title_element = row.find_element(By.XPATH, ProblemRow.TITLE_ELEMENT)
        number, name = title_element.text.split('. ')
        link = row.get_attribute('href')

        premium = row.find_elements(By.XPATH, ProblemRow.PREMIUM)
        isPremium = len(premium) > 0

        acceptanceRate = row.find_element(By.XPATH, ProblemRow.ACCEPTANCE_RATE).text
        difficulty = row.find_element(By.XPATH, ProblemRow.DIFFICULTY).text

        return [number, name, link, isPremium, acceptanceRate, difficulty]

    def get_problems_on_page(self, idx: int):
        # idx is the LeetCode question number
        row = self.get_by_xpath(ProblemPage.ROWGROUP + "/a[{idx}]".format(idx = idx))

        # [Question Number, Question Name, URL Address, "Is Premium", "Acceptance Rate"]
        parsed_row = self.parse_problem_div(row)
        self.write_to_csv(parsed_row)
