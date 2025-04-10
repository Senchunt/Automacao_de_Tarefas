# Passo a passo do código (A LÓGICA DO PROGRAMAÇÃO - Lógica de Programação)
    # Comandos básicos:
    # pyautogui.click --> clicar em algum lugar
    # pyautogui.write --> escrever um texto
    # pyautogui.press --> pressionar uma tecla
    # pyautogui.hotkey --> pressionar várias teclas ao mesmo tempo (combinação de teclas ex: Ctrl + C)
    # pyautogui.screenshot --> tirar um print da tela
    # pyautogui.locateOnScreen --> localizar uma imagem na tela (ex: um botão, uma imagem, etc)

import pyautogui as gui
import time # Importar a biblioteca de tempo (para fazer pausas entre os comandos)
gui.PAUSE = 0.5 # Pausa de 1 segundo entre cada comando (entre TODOS os comandos)
# Passo 1: Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o Chrome
gui.press("win")
gui.write("Google Chrome")
gui.press("enter")
# Digitar o Site
gui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
gui.press("enter")
# espera 3 segundos
time.sleep(5) # Espera o site carregar (somente naquele lugar (localmente aplicado))

gui.click(x=422, y=407) # Clica no campo de email (coordenadas do mouse)gui.write("pythonimpressionador@gmail.com")
gui.write("meuprimeiroemail@gmail.com") # Pressiona a tecla enter (apenas para o campo de email)
gui.press("tab")
gui.write("minhasenhasupersecreta")
#apertar o botão Login
gui.press("tab")
gui.press("enter")
time.sleep(5)

# Passo 3: Importar a base de dados: https://dlp.hashtagtreinamentos.com/python/intensivao/loja.csv
import pandas

tabela = pandas.read_csv("produtos.csv") #criar uma variável com o nome TABELA
print(tabela) #imprimir a tabela

# Passo 4: Cadastrar um produto

for linha in tabela.index: # Para cada linha da tabela (cada produto) REPETIR
    gui.click(x=395, y=296)

# para apagar textos existentes no campo de texto
    gui.hotkey("ctrl", "a") # pressionar as teclas CTRL + A (selecionar todo o campo de texto)
    gui.press("backspace") # pressionar a tecla BACKSPACE (apagar tudo o que foi escrito)

    codigo = tabela.loc[linha, "codigo"] # Pegar o código do produto da linha atual
    gui.write(codigo) # Preencher o código do produto
    gui.press("tab")

    marca = str(tabela.loc[linha, "marca"]) # Pegar a marca do produto da linha atual
    gui.write(marca) # Preencher a marca do produto
    gui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"]) # Pegar o tipo do produto da linha atual
    gui.write(tipo) # Preencher o tipo do produto
    gui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"]) # Pegar a categoria do produto da linha atual. str é uma STRING = TEXTO
    gui.write(categoria) # Preencher a categoria do produto
    gui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"]) # Pegar o preço unitário do produto da linha atual
    gui.write(preco_unitario) # Preencher o preço unitário do produto
    gui.press("tab")

    custo = str(tabela.loc[linha, "custo"]) # Pegar o custo do produto da linha atual
    gui.write(custo) # Preencher o custo do produto
    gui.press("tab")  

    obs = str(tabela.loc[linha, "obs"])  # Pegar a observação do produto da linha atual
    if obs != "nan":
        gui.write(obs) # Preencher a observação do produto

    gui.press("tab") # ir para o botão ENVIAR
    gui.press("enter") # clicar no botão ENVIAR

    gui.scroll(10000)     # rolar a tela para CIMA (sobe tudo)
