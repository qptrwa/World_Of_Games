import sys
from selenium import webdriver


Chrome_driver = '/Users/micha/PycharmProjects/WOW/chromedriver'

def test_scores_service(url):
    driver = webdriver.Chrome(Chrome_driver)
    driver.get(url)
    try:
        elem = driver.find_element_by_id("score")
        scoreToInt = int(elem.text)
        if 1 <= scoreToInt <= 1000:
            return True
    except ValueError:
        return False
    return False

def main_function():
    my_url = "http://0.0.0.0:8000/"
    if test_scores_service(my_url):
        sys.exit(0)
    else:
        sys.exit(-1)

main_function()