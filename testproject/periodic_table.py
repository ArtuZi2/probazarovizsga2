from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # oldal betöltése
    driver.get(" https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html ")
    time.sleep(2)
    # TC01 adatok beolvasás

    with open('data.txt', encoding='utf-8') as csvtable:
        csvreader = csv.reader(csvtable, delimiter=',')
        for row in csvreader:
            print(row)

    """lis = []
    period_elements = driver.find_elements_by_xpath("//div/ul/li")
    for elem in period_elements:
        lis.append(elem)
        print()"""

# nehéz feladat még nekem, több idő kellene rá. de valahogyan végigmennék az elemeken(data-pos) talán for ciklussal,
# megnézném, hány elemből áll, majd assertel megnézném, hány elemből áll a data.txt fájl.
#vagy összehasonlítanám, hogy megegyeznek-e a nevek.

finally:
    pass
    # driver.close()
