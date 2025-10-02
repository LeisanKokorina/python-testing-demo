import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    options = Options()
    #options.add_argument("--headless=new")  # remove if you want to watch
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1400, 900)
    yield driver
    driver.quit()

def test_unilu_master_search(browser):
    wait = WebDriverWait(browser, 15)

    # 1. Open Uni.lu
    browser.get("https://www.uni.lu/en/")

    # 2. Decline cookies (if shown)
    try:
        decline = wait.until(EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyButtonDecline")))
        decline.click()
    except Exception:
        pass

    # 3. Check home page title
    assert browser.title.strip().startswith("Home - University of Luxembourg")

    # 4. Click search button (id="search-page")
    search_button = wait.until(EC.element_to_be_clickable((By.ID, "???")))
    search_button.click()

    # 5. Enter search query into search bar
    search_input = wait.until(EC.visibility_of_element_located((By.NAME, "???"))) # search field
    search_input.send_keys("???")
    search_input.send_keys(Keys.ENTER)

    # 6. Click the first relevant result
    first_result = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, "a.search-result__link"
    )))
    first_result.click()

    # 7. Assert the destination page title
    wait.until(EC.title_contains("???"))
    assert "????" in browser.title
