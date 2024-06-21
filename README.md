# Automatização no Guardião Digital
Neste repositório há uma automação para subir documentos em uma plataforma de Armazenamento, utilizando as bibliotecas selenium e pyautogui

### Funcionalidade
Primeiramente o robô lê os arquivos com extensão .PDF que se encontram na pasta, em seguida abre a janela da Guardião no navegador. Em seguida, lê um arquivo .venv onde ficam armazenadas as credenciais do usuários, por fim utiliza os nomes caputados dos arquivos para realizar as consultas no sistema um por vez, selecinar ou criar a pasta de destino dos aquivos e fazer o upload do arquivo do loop atual na mesma. 

### Como utilizei as bibliotecas
- Utilizando o Selenium para fazer toda a parte de interação com o navegador como identificar os textos e botões das páginas.
- Já o Pyautogui utilizei para fazer a interação com o Explorer no momento de selecionar o arquivo e fazer seu upload para a plataforma
