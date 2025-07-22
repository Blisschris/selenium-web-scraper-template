# 🔧 Selenium Web Scraper Template

This project is a reusable Python Selenium scraper that can be customized to automate and extract data from **any website**.

## 🚀 Features

- Automates Chrome with Selenium
- Waits for elements using `WebDriverWait`
- Example interaction with search input and results
- Customizable for any target site

## 📁 Files

- `scraper_template.py` — main script
- `requirements.txt` — install dependencies
- `README.md` — usage guide

## 🛠️ Setup

1. Install Python and Chrome
2. Download matching [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/)
3. Install Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Update `chrome_path` in the script with your local ChromeDriver path
5. Run:
   ```bash
   python scraper_template.py
   ```

## ✏️ Customize

- Change the `url`
- Update the `By.XPATH` or `By.NAME` selectors
- Replace the interaction logic to match your target site

## ✅ Example Use Cases

- Price scraping
- Search automation
- Product data extraction
- Form testing
