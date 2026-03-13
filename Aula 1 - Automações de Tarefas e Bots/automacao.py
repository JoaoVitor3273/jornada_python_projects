#primeiro projeto:
    #passo 1 :entrar no sistema da empresa
    #passo 2 :fazer login
    #passo 3: abrir base de dados
    #passo 4: cadastar um produto
    #passo 5: repetir até acabar a lista

#baixar pyautogui para automatizar o pc
# pip install pyautogui no terminal
import pyautogui
import time
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 0.5

#passo 1 :entrar no sistema da empresa
#abrir navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

#passo 2 :fazer login
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3) 
#clicar no link
pyautogui.click(x=975, y=361)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") #passa pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab") #passa pro botão
pyautogui.press("enter")
time.sleep(3)

#passo 3: abrir base de dados
#baixar pandas pra base de dados e openxl para conseguir uxar exel
#pip install pandas openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv") #declara a variavel tabela para que o código consiga ler
print(tabela)

for linha in tabela.index:
    #passo 4: cadastar um produto
    pyautogui.click(x=936, y=243)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")



