from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # oldal betöltése
    driver.get(" https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html ")
    time.sleep(2)