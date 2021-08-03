from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time, datetime
from selenium.webdriver.support.select import Select
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # oldal betöltése
    driver.get(" https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")
    time.sleep(2)

    #TC01 formanyomtatvány tesztelése
    select_legordul = driver.find_element_by_name("bf_totalGuests")
    sel = Select(select_legordul)
    time.sleep(2)
    sel.select_by_index(1)
    time.sleep(2)
    next_button = driver.find_element_by_xpath("//form/div/div/ul/li/button")
    next_button.click()
    time.sleep(2)
    date = driver.find_element_by_name("bf_date")
    date.send_keys("2021.08.20. 13:00")
    time_of_day = driver.find_element_by_name("bf_time")
    sel2 = Select(time_of_day)
    sel2.select_by_index(1)
    hours = driver.find_element_by_name("bf_hours")
    sel3 = Select(hours)
    sel3.select_by_index(2)
    next2_button = driver.find_element_by_xpath("//*[@id='step2']/ul/li[4]/button")
    next2_button.click()
    time.sleep(2)
    full_name = driver.find_element_by_name("bf_fullname")
    full_name.send_keys("Zita Mazurka")
    email = driver.find_element_by_name("bf_email")
    email.send_keys("lifeisheavy@gmail.com")
    reques = driver.find_element_by_xpath("//*[@id='step3']/ul/li[4]/button")
    reques.click()
    time.sleep(2)

#TC2 Válasz ellenőrzése

    """szoveg = driver.find_elements_by_xpath("//*[@id='booking-form']/h2")
    print(szoveg.text)

    message = "Your message was sent successfully. Thanks! We'll be in touch as soon as we can," \
              "which is usually like lightning (Unless we're sailing or eating tacos!)."
    assert message == szoveg"""

#TC3 Email validáció

    driver.get(" https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")
    time.sleep(2)

    select_legordul = driver.find_element_by_name("bf_totalGuests")
    sel = Select(select_legordul)
    time.sleep(2)
    sel.select_by_index(1)
    time.sleep(2)
    next_button = driver.find_element_by_xpath("//form/div/div/ul/li/button")
    next_button.click()
    time.sleep(2)
    date = driver.find_element_by_name("bf_date")
    date.send_keys("2021.08.20. 13:00")
    time_of_day = driver.find_element_by_name("bf_time")
    sel2 = Select(time_of_day)
    sel2.select_by_index(1)
    hours = driver.find_element_by_name("bf_hours")
    sel3 = Select(hours)
    sel3.select_by_index(2)
    next2_button = driver.find_element_by_xpath("//*[@id='step2']/ul/li[4]/button")
    next2_button.click()
    time.sleep(2)
    full_name = driver.find_element_by_name("bf_fullname")
    full_name.send_keys("Zita Mazurka")
    email = driver.find_element_by_name("bf_email")
    email.send_keys("lifeisheavy")
    reques = driver.find_element_by_xpath("//*[@id='step3']/ul/li[4]/button")
    reques.click()
    time.sleep(2)

    message = driver.find_element_by_id("bf_email-error")
    valid = "Please enter a valid email address."
    assert message is not None
    assert message.text == valid.upper()


finally:
    pass
    driver.close()
