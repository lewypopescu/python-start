# Selenium is a powerful tool for controlling web browsers through programs and performing browser automation.
# It is widely used for testing web applications, web scraping, and automating repetitive web tasks.


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

opts = Options()
# keep Chrome open after the script
opts.add_experimental_option("detach", True)
# opts.add_argument("--headless=new")          # uncomment to run without UI

driver = webdriver.Chrome(options=opts)
driver.maximize_window()
wait = WebDriverWait(driver, 30)


def go_home():
    driver.get("https://www.qaplayground.com/practice")
    wait.until(EC.title_contains("QA Playground"))
    print("[HOME] Opened QA Playground.")


def open_section(link_text: str):
    el = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
    el.click()


try:
    go_home()

    # 1 INPUT, Edit
    open_section("Edit")
    print("[INPUT] Page opened.")

    movie = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input[placeholder="Enter hollywood movie name"]')
    ))
    movie.clear()
    movie.send_keys("Interstellar")
    assert movie.get_attribute("value") == "Interstellar"
    print("[INPUT] Movie typed and verified.")

    clear_me = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input[value="QA PlayGround Clear Me"]')
    ))
    clear_me.clear()
    assert (clear_me.get_attribute("value") or "") == ""
    print("[INPUT] Clear action verified.")

    disabled = driver.find_element(By.CSS_SELECTOR, 'input[disabled]')
    assert disabled.get_attribute("disabled") is not None

    readonly = driver.find_element(By.CSS_SELECTOR, 'input[readonly]')
    assert readonly.get_attribute("readonly") is not None
    print("[INPUT] Disabled and readonly verified.")

    driver.back()
    wait.until(EC.title_contains("Practice"))

    # 2 SELECT, Select By
    open_section("Select By")
    print("[SELECT] Page opened.")

    select_el = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "select"))
    )
    sel = Select(select_el)

    options = [o.text.strip() for o in sel.options]
    print("[SELECT] Options found:", options)

    matched = False
    for o in sel.options:
        if o.text.strip().lower() == "option 2":
            o.click()
            matched = True
            print("[SELECT] 'Option 2' selected.")
            break

    if not matched:
        sel.select_by_index(1)
        print("[SELECT] Fallback: selected option by index 1.")

    driver.back()
    wait.until(EC.title_contains("Practice"))

    # 3 BUTTON, Click
    open_section("Click")
    print("[BUTTON] Page opened.")

    btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Find my color')]"))
    )
    btn.click()
    print("[BUTTON] 'Find my color?' button clicked.")

    # Go back to home (Practice) page
    driver.back()
    wait.until(EC.title_contains("Practice"))
    print("[HOME] Returned to Practice page successfully.")

    print("✅ Test flow completed successfully.")

except TimeoutException as e:
    print(f"❌ Timeout while waiting for an element: {e}")

# finally:
#     driver.quit() # Uncomment to close the browser after script ends
