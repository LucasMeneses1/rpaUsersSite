#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random

df = pd.read_excel('users.xlsx')

# Criando listas dodos dados dos usuarios
aux1 = ['curso_html', 'curso_css', 'curso_javascript', 'curso_python', 'curso_sql', 'curso_java']
cursos_aux = []
usuarios = []
emails = []
senhas = []
titulos = []
posts = []
fotos = []
cursos = []
aux2 = [usuarios, emails, senhas, titulos, posts, fotos, cursos]

for item in df['cursos']:
    cursos_aux.append(item)

for n in cursos_aux:
    l = []
    for i in range(n):
        l.append(random.choice(aux1))
    cursos.append(l)
    
for i, col in enumerate(df):
    for item in df[col]:
        if col == 'cursos':
            break
        aux2[i].append(item)
        
        
# Criando o navegador
driver = webdriver.Chrome()
driver.maximize_window() 
driver.get('https://comunidadedev.herokuapp.com/')


# Criando um novo usuario
driver.execute_script('window.open();')
site = driver.window_handles[0]
aux = driver.window_handles[1]
driver.switch_to.window(site)

for i in range(len(usuarios)):
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul[2]/li[2]/a/span').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(usuarios[i])
    driver.find_element(By.ID, 'em').send_keys(emails[i])
    driver.find_element(By.ID, 'pw').send_keys(senhas[i])
    driver.find_element(By.ID, 'confirmacao').send_keys(senhas[i])
    driver.find_element(By.ID, 'botao_submit_criarconta').click()
    time.sleep(2)
    
    driver.find_element(By.XPATH, '//*[@id="foto_perfil"]').send_keys(fotos[i])   
    
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(4)
    
    for curso in cursos[i]:
        driver.find_element(By.ID, curso).click()

    driver.find_element(By.ID, 'botao_submit_editarperfil').click()
    
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul[2]/li[1]/a/span').click()
    
    driver.find_element(By.ID, 'titulo').send_keys(titulos[i])
    driver.find_element(By.ID, 'corpo').send_keys(posts[i])
    
    driver.find_element(By.ID, 'botao_submit_post').click()
    
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul[2]/li[3]/a/span').click()
    time.sleep(2)

