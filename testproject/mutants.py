from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    #oldal betöltése
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html")
    time.sleep(2)


    character_count = 0
    character_list = []
    characters_name = driver.find_elements_by_xpath("//div/ul/li")
    for character in characters_name:
        character_count += 1
        character_list.append(character)
        print(character.text)
    driver.find_element_by_xpath("/html/body/div/label[2]").click()
    time.sleep(2)
    for character in characters_name:
        character_count += 1
        character_list.append(character)
        print(character.text)
    driver.find_element_by_xpath("/html/body/div/label[3]").click()
    time.sleep(2)
    for character in characters_name:
        character_count += 1
        character_list.append(character)
        print(character.text)
    driver.find_element_by_xpath("/html/body/div/label[4]").click()
    time.sleep(2)
    for character in characters_name:
        character_count += 1
        character_list.append(character)
        print(character.text)
    print(len(character_list))


characters_xpath = driver.find_elements_by_xpath("//div/ul/li" and "")





finally:
    pass
    #driver.close()