import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def browser():
    options = Options()
    # options.add_argument("--headless=new")  # enable headless mode if needed
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1400, 900)
    #driver.implicitly_wait(10)  #  apply implicit wait globally
    yield driver
    driver.quit()

def test_unilu_master_search(browser):
    # 1. Open Uni.lu
    browser.get("https://www.uni.lu/en/")

    # 2. Decline cookies (if shown)
    try:
        browser.find_element(By.ID, "CybotCookiebotDialogBodyButtonDecline").click()
    except:
        pass  # cookie banner not shown

    # 3. Check home page title
    assert browser.title.strip().startswith("Home - University of Luxembourg")

    # 4. Click search button
    browser.find_element(By.ID, "search-page").click()

    # 5. Search for the program
    search_input = browser.find_element(By.NAME, "search-box")
    search_input.send_keys("Master in Information and Computer Sciences")
    search_input.send_keys(Keys.ENTER)

    # 6. Click the first search result
    browser.find_element(By.CSS_SELECTOR, "a.search-result__link").click()

    # 7. Check the title of the resulting page
    assert "Master in Information and Computer Sciences - FSTM" in browser.title
