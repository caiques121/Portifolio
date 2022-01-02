from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import warnings
from cria_pdf import cria_pdf
import re

warnings.filterwarnings("ignore")

TIME_TO_WAIT = 0.8

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': r'C:\Users\p35z9yu\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\Pessoal\OP\output'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.delete_all_cookies()

print("Carregando a Página")
driver.get("https://leitor.net/manga/berserk/14159/capitulo--16#/!page0")

all_running = True

while all_running == True:
    time.sleep(TIME_TO_WAIT * 5)

    print("Clicando no banner da idade")
    driver.find_elements_by_class_name("eighteen-but")[0].click()

    def salva_imagem(url, numero_pagina):
        import requests
        img_data = requests.get(url).content
        with open('output/' + numero_pagina + '.png', 'wb') as handler:
            handler.write(img_data)

    time.sleep(TIME_TO_WAIT)

    print("Pegando a pagina 1")
    elements = driver.find_elements_by_class_name("manga-image")

    for i in elements:
        image = i.find_element_by_tag_name("img")
        img_src = image.get_attribute("src")

    print("Salvando a página 1")
    salva_imagem(img_src, "1")

    print("Passando para a próxima página")
    # Muda de Página
    from selenium.webdriver.common.keys import Keys
    webdriver.ActionChains(driver).send_keys(Keys.RIGHT).perform()

    continuar_rodando = True

    pagina = 1

    while continuar_rodando == True:

        b = driver.current_url

        if re.search("#comments", b):
            print("Chegamos ao fim do capitulo")
            continuar_rodando = False
            pass

        elements = driver.find_elements_by_class_name("manga-image")
        for i in elements:
            image = i.find_element_by_tag_name("img")
            img_src = image.get_attribute("src")

        salva_imagem(img_src, str(pagina + 1))
        pagina = pagina + 1
        webdriver.ActionChains(driver).send_keys(Keys.RIGHT).perform()

    print("Criando o PDF do capitulo")
    capitulo = driver.title
    capitulo = capitulo.replace(
        " por Kousen", "")

    print("Salvando o mangá " + str(capitulo))

    cria_pdf(capitulo)
    from limpa_arquivos import limpaarquivos
    limpaarquivos()
    time.sleep(TIME_TO_WAIT * 3)

    driver.find_elements_by_class_name("chapter-next")[0].click()
