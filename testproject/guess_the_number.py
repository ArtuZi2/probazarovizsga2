from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # oldal betöltése
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html")
    time.sleep(2)

    # TC01 Helyes szám megkeresése
    number = driver.find_element_by_xpath("/html/body/div/div[2]/input")
    random_number_list = [1, 100]
    random_number = random.randint(1, 100)
    number.send_keys(random_number)
    guess_button = driver.find_element_by_xpath("//div/span/button")
    guess_button.click()
    guess_info = driver.find_element_by_xpath("/html/body/div/p")

    for i in random_number_list:
        if guess_info.text == "Guess higher.":
            continue
        number.clear
        time.sleep(2)
        number.send_keys(random_number)
        guess_button.click()
        time.sleep(2)
    for i in random_number_list:
        if guess_info.text == "Guess lower.":
            continue
        number.clear()
        time.sleep(2)
        number.send_keys(random_number)
        guess_button.click()

    # azt hiszem, nem jó az irány, de nehéznek találom a feladatot. még valahogy azt is bele kellene írnom,
    # hogy ha alacsonyabb a szám, akkor adjon  hozzá egyet addig, amíg jó nem lesz, illetve,
    # ha magasabb, akkor vegyen el belőle egyet. a windowgame házi feladatot gondoltam egyébként hasonlónak.

    """mytable = driver.find_elements_by_xpath("//*[@id='button']/tbody/tr")
    print(mytable)

    for row in mytable.find_elements_by_css_selector('tr'):
        for cell in row.find_elements_by_tag_name('td'):
            print(cell.text)

    all_rows = driver.find_element_by_xpath("//*[@id='button']/tbody/tr").click()"""

finally:
    pass
    # driver.close()
