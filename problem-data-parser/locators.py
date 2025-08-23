class ProblemPage:
    URL =  "https://leetcode.com/problemset/"
    TITLE = "Problems - LeetCode"

    ROWGROUP = "//a[@id='1']/parent::div"

class ProblemRow:
    TITLE_ELEMENT = "./div/div[2]/div[1]/div/div"
    PREMIUM = "./div/div[1]/div/*[local-name() = 'svg']"
    ACCEPTANCE_RATE = "./div/div[2]/div[2]"
    DIFFICULTY = "./div/div[2]/p"
