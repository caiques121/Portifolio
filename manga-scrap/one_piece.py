import os
import img2pdf
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import warnings

warnings.filterwarnings("ignore")

TIME_TO_WAIT = 0.8

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': r'C:\Users\p35z9yu\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\Pessoal\OP\output'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.delete_all_cookies()

driver.get("https://onepieceex.net/mangas/leitor/1010/#1")
time.sleep(TIME_TO_WAIT * 30)

try:

    driver.find_elements_by_id("smart_push_smio_not_allow")[0].click()
    time.sleep(TIME_TO_WAIT)

except:
    pass
# smart_push_smio_not_allow

continuar_rodando = True

driver.maximize_window()

while continuar_rodando == True:
    def salva_imagem(url, numero_pagina):
        import requests
        img_data = requests.get(url).content
        with open('output/' + numero_pagina + '.png', 'wb') as handler:
            handler.write(img_data)

    img = driver.find_elements_by_class_name(
        "paginamanga")[0].get_attribute("src")
    time.sleep(TIME_TO_WAIT)

    capitulo = driver.title
    capitulo = capitulo.replace(
        " | Mangá OpEx", "")

    print("Buscando o " + str(capitulo))

    salva_imagem(img, '1')

    # Como pegar o url da imagem na net
    # img = driver.find_elements_by_class_name("paginamanga")[0].get_attribute("src")

    paginas = ['2',
               '3',
               '4',
               '5',
               '6',
               '7',
               '8',
               '9',
               '10',
               '11',
               '12',
               '13',
               '14',
               '15',
               '16',
               '17',
               '18',
               '19',
               '20',
               '21',
               '22',
               '23',
               '24',
               '25',
               '26',
               '27',
               '28',
               '29',
               '30',
               '31',
               '32',
               '33',
               '34',
               '35',
               '36',
               '37',
               '38',
               '39',
               '40',
               '41',
               '42',
               '43',
               '44',
               '45',
               '46',
               '47',
               '48',
               '49',
               '50',
               '51',
               '52',
               '53',
               '54',
               '55',
               '56',
               '57',
               '58',
               '59',
               '60']

    for i in paginas:
        try:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(TIME_TO_WAIT)

            a = driver.find_elements_by_class_name(
                "pagina-" + str(i))[0].click()

            img = driver.find_elements_by_class_name(
                "paginamanga")[0].get_attribute("src")
            salva_imagem(img, str(i))

        except IndexError:
            continue

    # Cria o PDF

    def cria_pdf(capitulo):
        import glob
        list_of_files = sorted(glob.glob('output/*.png'), key=os.path.getmtime)

        with open("pdfs/" + str(capitulo) + ".pdf", "wb") as f:
            f.write(img2pdf.convert(list_of_files))

    cria_pdf(capitulo)

    time.sleep(TIME_TO_WAIT)

    from limpa_arquivos import limpaarquivos

    limpaarquivos()
    time.sleep(TIME_TO_WAIT)


    driver.find_elements_by_id("proximoModel")[0].click()
    time.sleep(TIME_TO_WAIT * 4)
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    time.sleep(TIME_TO_WAIT)
