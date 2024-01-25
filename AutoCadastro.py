# Importar as bibliotecas
import os
import pyautogui
import time
import pandas as pd

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # site fornecido pelo curso de python da hashtag

# Inserir um delay
pyautogui.PAUSE = 0.5

# Entrar no site
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2) # tempo para carregar o website

# Realizar o login no sistema
pyautogui.click(x=472, y=381)
pyautogui.write("email@email.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("enter")

# Importar a base de dados
tabela = pd.read_csv("produtos.csv")

# Cadastrar itens até acabar a base de dados
for linha in tabela.index:
    pyautogui.PAUSE = 0.2
    pyautogui.click(x=411, y=275)
    pyautogui.click(x=411, y=275)
    pyautogui.PAUSE = 0.5
    # codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(obs)
    else:
        pyautogui.press("backspace")
    pyautogui.press("tab")

    pyautogui.scroll(5000)
