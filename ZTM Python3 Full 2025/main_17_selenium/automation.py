# Selenium is a powerful tool for controlling web browsers through programs and performing browser automation.
# It is widely used for testing web applications, web scraping, and automating repetitive web tasks.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_experimental_option("detach", True)
# opts.add_argument("--headless=new") # Uncomment this line to run Chrome in headless mode (without GUI)


driver = webdriver.Chrome(options=opts)

driver.get("https://www.python.org")

print("Page Title:", driver.title)


# driver.quit() # Uncomment this line to close the browser after execution
