import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Set up argument parser
parser = argparse.ArgumentParser(description='Upload a file to YNAB CSV converter.')
parser.add_argument('file_path', type=str, help='The path to the file to be uploaded')
parser.add_argument('download_dir', type=str, help='The directory to where the file will be downloaded')
parser.add_argument('--start_row', type=str, help='The row number where the data starts')
parser.add_argument('--date_col_name', type=str, help='The column name for the date')
parser.add_argument('--payee_col_name', type=str, help='The column name for the payee')
parser.add_argument('--memo_col_name', type=str, help='The column name for the memo')
parser.add_argument('--outflow_col_name', type=str, help='The column name for the outflow')
parser.add_argument('--inflow_col_name', type=str, help='The column name for the inflow')
args = parser.parse_args()

file_path        = args.file_path
download_dir     = args.download_dir
start_row        = args.start_row
date_col_name    = args.date_col_name
payee_col_name   = args.payee_col_name
memo_col_name    = args.memo_col_name
outflow_col_name = args.outflow_col_name
inflow_col_name  = args.inflow_col_name

print(f"File path: {file_path}")
print(f"Download dir: {download_dir}")
print(f"Start row: {start_row}")
print(f"Date column name: {date_col_name}")
print(f"Payee column name: {payee_col_name}")
print(f"Memo column name: {memo_col_name}")
print(f"Outflow column name: {outflow_col_name}")
print(f"Inflow column name: {inflow_col_name}")

# Set up the WebDriver (assuming Chrome)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")

prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

# When testing create a new instance of the browser without the options argument to see the browser
driver = webdriver.Chrome(options=chrome_options)

def setupFirstPage():
    # Wait until the "Input File Config" button is clickable and click it
    input_file_config_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Input file config']"))
    )
    input_file_config_button.click()

    # Wait for the "Encoding" input field to be visible and interactable
    encoding_dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='encoding']"))
    )
    select_encoding = Select(encoding_dropdown)
    select_encoding.select_by_visible_text("ISO-8859-1")

    # Wait for the "Start at Row" input field to be visible and interactable
    start_at_row_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='start_row']"))
    )
    start_at_row_input.clear()
    start_at_row_input.send_keys(start_row)
    
    # Add file to "Or choose" button
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'file'))
    )
    file_input.send_keys(file_path)

def setupSecondPage():
    # DATE
    date = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='id-Date']"))
    )
    date = Select(date)
    date.select_by_visible_text(date_col_name)
    
    # Payee
    payee = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='id-Payee']"))
    )
    payee = Select(payee)
    payee.select_by_visible_text(payee_col_name)

    # Memo
    memo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='id-Memo']"))
    )
    memo = Select(memo)
    memo.select_by_visible_text(memo_col_name)

    # Outflow
    outflow = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='id-Outflow']"))
    )
    outflow = Select(outflow)
    outflow.select_by_visible_text(outflow_col_name)

    # Inflow
    inflow = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='id-Inflow']"))
    )
    inflow = Select(inflow)
    inflow.select_by_visible_text(inflow_col_name)

    return

def downloadFile():
    download_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="btn btn-success" and @ng-click="downloadFile()"]'))
    )
    download_button.click()
    print("File downloaded successfully")


try:
    # Open the website
    driver.get("https://aniav.github.io/ynab-csv/")

    setupFirstPage()
    setupSecondPage()
    downloadFile()

    # When testing uncomment this to see browser state at end
    # import time
    # time.sleep(50)

finally:
    # Close the browser
    driver.quit()