from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # oldal betöltése
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html")
    time.sleep(2)

    # TC01 24 film megszámolása

    filmes = driver.find_elements_by_xpath("//div/h2")

    film_list = []

    filmes_count = 0
    for film in filmes:
        filmes_count += 1
        film_list.append(film)
    assert len(filmes) == len(film_list)

    print(f'Number of films found on the page: {filmes_count}')

    # TC02 Új film felvitele

    datas = ["Black widow", "2021", "2020", "https://www.youtube.com/watch?v=Fp9pNPdNwjI",
             "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg",
             "https://www.imdb.com/title/tt3480822/"]

    register_button = driver.find_element_by_xpath("/html/body/div[2]/div[1]/button")
    register_button.click()
    time.sleep(2)
    title = driver.find_element_by_id("nomeFilme")
    time.sleep(2)
    title.click()
    time.sleep(2)
    title.send_keys(datas[0])
    release = driver.find_element_by_id("anoLancamentoFilme")
    time.sleep(2)
    release.click()
    time.sleep(2)
    release.send_keys(datas[1])
    time.sleep(2)
    chronological_year = driver.find_element_by_id("anoCronologiaFilme")
    chronological_year.click()
    chronological_year.send_keys(datas[2])
    trailer = driver.find_element_by_id("linkTrailerFilme")
    trailer.click()
    time.sleep(2)
    trailer.send_keys(datas[3])
    image_url = driver.find_element_by_id("linkImagemFilme")
    image_url.click()
    time.sleep(2)
    image_url.send_keys(datas[4])
    film_summery = driver.find_element_by_id("linkImdbFilme")
    film_summery.click()
    time.sleep(2)
    film_summery.send_keys(datas[5])
    time.sleep(2)

    save_button = driver.find_elements_by_xpath("//div/div/fieldset/button[@onclick='salvarFilme()']")

    """tovább keresném a save gombot
    majd asserttel megnézném, hogy változott-e a filmek listájának a száma"""
finally:
    pass
    # driver.close()
