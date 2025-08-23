from main_page_scraper import MainPageScraper

import os
import time

from selenium.webdriver.common.by import By

def runProblemDataScraper():
    scraper = MainPageScraper()
    idx = 1

    num_of_problem = scraper.driver.find_element(By.XPATH, "//a[@href='/progress/']/div/div[2]").text
    num_of_problem = num_of_problem.split(" ")
    num_of_problem = num_of_problem[0][num_of_problem[0].find("/") + 1:]

    try:
        os.remove(scraper.csv_path)
        print(f"File '{scraper.csv_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"Error: File '{scraper.csv_path}' not found.")

    # Add 1 for the daily problem in the first row
    while idx <= int(num_of_problem) + 1:
        scraper.get_problems_on_page(idx)
        idx +=1




if __name__ == "__main__":
    runProblemDataScraper()
