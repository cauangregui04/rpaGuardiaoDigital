from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import pyautogui
import os

cwd = os.getcwd()
path = cwd + "\\"
i = 0

caminhos = [os.path.join(path, nome) for nome in os.listdir(path)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
pdfs = [arq for arq in arquivos if arq.endswith(".pdf")]
pdfs = list(map(lambda x: x.replace(path, ""), pdfs))

servico = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
prefs = {
    "download.prompt_for_download": True,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": False,
    "profile.default_content_setting_values.notifications": 2,
}

options.add_experimental_option("prefs", prefs)
navegador = webdriver.Chrome(service=servico, options=options)

navegador.get("https://cedoc.guardiao.digital/#/login/company")
navegador.maximize_window()

with open("venv.txt", "r") as arquivo:
    texto = arquivo.readlines()
usu = texto[0].split("/n")[0]
pas = texto[0].split("/n")[1]

time.sleep(2)
navegador.find_element(
    "xpath",
    "/html/body/app-root/gd-login/div/div[3]/gd-company/div/div/div/div/form/div[1]/div/input",
).send_keys("rni")
navegador.find_element(
    "xpath",
    "/html/body/app-root/gd-login/div/div[3]/gd-company/div/div/div/div/form/button",
).click()
time.sleep(1)
navegador.find_element(
    "xpath",
    "/html/body/app-root/gd-login/div/div[3]/gd-user-password/div/form/div/div[1]/input",
).send_keys(usu)
navegador.find_element(
    "xpath",
    "/html/body/app-root/gd-login/div/div[3]/gd-user-password/div/form/div/div[2]/input",
).send_keys(pas)
navegador.find_element(
    "xpath", "/html/body/app-root/gd-login/div/div[3]/gd-user-password/div/form/button"
).click()
time.sleep(1)
navegador.find_element(
    "xpath", "/html/body/app-root/gd-login/div/div[1]/button"
).click()
time.sleep(5)
ActionChains(navegador).send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
time.sleep(2)


def rpaGed():
    navegador.find_element(
        "xpath",
        "/html/body/app-root/gd-ged/main/section/div/gd-pesquisa/div/div[1]/div[2]/gd-simple-search/div/div[1]/div/div[2]/input",
    ).clear()
    navegador.find_element(
        "xpath",
        "/html/body/app-root/gd-ged/main/section/div/gd-pesquisa/div/div[1]/div[2]/gd-simple-search/div/div[1]/div/div[2]/input",
    ).send_keys(pdfs[i].split("-")[0] + "-" + pdfs[i].split("-")[1])
    ActionChains(navegador).send_keys(Keys.ENTER).perform()
    time.sleep(2)

    try:
        clickable = navegador.find_element(
            "xpath", "// span[contains(text(),'MALA DIRETA')]"
        )
        ActionChains(navegador).double_click(clickable).perform()
        msg = "Importado para o GED"

    except:
        navegador.find_element(
            "xpath", "/html/body/app-root/gd-ged/main/div/div[2]"
        ).click()
        time.sleep(2)
        iframe = navegador.find_element(
            "xpath", "// div[contains(text(),' MALA DIRETA ')]"
        )
        ActionChains(navegador).scroll_to_element(iframe).double_click(iframe).perform()
        pdfs2 = pdfs[i].split("-")
        time.sleep(2)
        navegador.find_element(
            "xpath",
            "/html/body/app-root/gd-ged/main/section/div/gd-documentos/div/gd-document/div/div[1]/div/gd-document-form/form/gd-box-form[4]/div/gd-smart-select/ng-select/div/div/div[2]/input",
        ).send_keys(pdfs2[0])
        time.sleep(2)
        ActionChains(navegador).send_keys(Keys.ENTER).perform()
        time.sleep(1)
        navegador.find_element(
            "xpath",
            "/html/body/app-root/gd-ged/main/section/div/gd-documentos/div/gd-document/div/div[1]/div/gd-document-form/form/gd-document-form-dynamic/gd-box-form[2]/div/gd-input-text/div/div/input",
        ).send_keys(pdfs2[1])
        time.sleep(2)
        navegador.find_element(
            "xpath",
            "/html/body/app-root/gd-ged/main/section/div/gd-documentos/div/gd-document/div/div[1]/gd-box/div/gd-button[2]/button",
        ).click()
        msg = "Criado a pasta e importado para o GED"

    time.sleep(6)
    iframe = navegador.find_element(
        "xpath", "// span[contains(text(),' AR/Telegrama/Protocolo ')]"
    )
    ActionChains(navegador).scroll_to_element(iframe).click(iframe).perform()
    time.sleep(1)
    navegador.find_element(
        "xpath",
        "/html/body/app-root/gd-ged/main/section/div/gd-documentos/div/gd-document/div/div[3]/gd-document-files-folders/div/gd-box/div/gd-button[2]/button/i",
    ).click()
    time.sleep(2)
    navegador.find_element(
        "xpath",
        "/html/body/app-root/smart-modal/div[1]/div/div/div[2]/gd-document-insert-file/form/div[2]/div/label",
    ).click()
    time.sleep(2)
    pyautogui.write(path + pdfs[i])
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    # save
    navegador.find_element(
        "xpath",
        "/html/body/app-root/smart-modal/div[1]/div/div/div[2]/gd-document-insert-file/div[2]/gd-button[3]/button",
    ).click()

    time.sleep(9)
    ActionChains(navegador) \
        .key_down(Keys.LEFT_CONTROL) \
        .send_keys("q") \
        .key_up(Keys.LEFT_CONTROL) \
        .perform()

    time.sleep(1)

    ActionChains(navegador) \
        .key_down(Keys.LEFT_CONTROL) \
        .send_keys("q") \
        .key_up(Keys.LEFT_CONTROL) \
        .perform()

    print(f"{pdfs[i]} foi {msg}")
    time.sleep(1)

while i < len(pdfs):
    try:
        rpaGed()
        print(f"Documento {i + 1} de {len(pdfs)} concluído")
        i += 1
    except:
        print(f"Processo parou no documento {i + 1} de {len(pdfs)}")
        break

input("=============== PROCESSO FINALIZADO ===============")
