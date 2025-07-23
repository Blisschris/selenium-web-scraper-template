import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === Setup ChromeDriver path ===
chrome_path = "/path/to/your/chromedriver"  # Replace with your actual path
service = Service(executable_path=chrome_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

# === Target website (example: Google Search) ===
url = "https://www.google.com"
driver.get(url)
time.sleep(2)

# === Perform search and collect result titles ===
search_query = "Selenium Python"
results = []

try:
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys(search_query)
    time.sleep(1)

    search_box.submit()  # Better than clicking the button
    time.sleep(2)

    # Extract search result titles (e.g., <h3>)
    titles = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "h3")))
    for title in titles:
        text = title.text.strip()
        if text:
            results.append([text])

except Exception as e:
    print(f"⚠️ Error: {e}")

# === Save to CSV file ===
csv_path = "search_results.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Search Result Titles"])
    writer.writerows(results)

print(f"✅ Saved results to {csv_path}")

driver.quit()
