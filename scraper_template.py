import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === Setup ChromeDriver path ===
chrome_path = "/path/to/your/chromedriver"
service = Service(executable_path=chrome_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

# === Target URL (example) ===
url = "https://example.com"
driver.get(url)
time.sleep(2)

# === Sample interaction: Search box ===
try:
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys("Selenium Python")
    time.sleep(1)

    search_button = driver.find_element(By.NAME, "btnK")
    search_button.click()
    time.sleep(2)

    results = driver.find_elements(By.TAG_NAME, "h3")
    for r in results:
        print(r.text)

except Exception as e:
    print(f"⚠️ Error: {e}")

driver.quit()
