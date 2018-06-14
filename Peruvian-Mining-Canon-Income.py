# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 09:05:58 2017
Last modified on June 2018

@author: ndominguez
"""

import time
import os
import sys
import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromedriver = 'C:/Users/ndominguez/OneDrive/Executables/chromedriver'
b = webdriver.Chrome(chromedriver)

################################################ CANON BUDGET 2007-2013 ################################################

### 2007-2011
for k in range(2007, 2012):
    print(str(k))
    b.get("http://apps5.mineco.gob.pe/transparencia/Navegador/default.aspx?y=" + str(k) + "&ap=ActProy")
    frame = b.find_element_by_xpath('//*[@id="frame0"]')
    b.switch_to.frame(frame)

    nivel_gobierno = b.find_element_by_name("ctl00$CPH1$BtnTipoGobierno")
    nivel_gobierno.click()

    gobierno_local = b.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr[2]")
    gobierno_local.click()

    departamentos = b.find_element_by_name("ctl00$CPH1$BtnDepartamento")
    departamentos.click()

    list_ccdd = [4, 7, 12, 13, 14, 15, 16, 20]  # 8 regiones [4, 7, 12, 13, 14, 15, 16, 20]

    for i in list_ccdd:
        departamento = b.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr[" + str(i) + "]/td[2]").text
        print(departamento)
        b.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr[" + str(i) + "]").click()

        b.find_element_by_xpath('//*[@id="ctl00_CPH1_BtnProvincia"]').click()

        b.find_element_by_xpath('//*[@id="ctl00_CPH1_RptData_ctl01_TD0"]/input').click()  # elegir la primera provincia

        b.find_element_by_name("ctl00$CPH1$BtnMunicipalidad").click()

        distritos = b.find_elements_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr")

        count = 1
        for distrito1 in distritos:
            distrito1.click()
            #print (count)
            count = count + 1

        for l in range(1, count):
            distrito = b.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr[" + str(l) + "]")
            distrito2 = ''.join([i for i in distrito.text if not i.isdigit()])
            distrito2 = re.sub('[-:,.]', '', distrito2)
            print(distrito2.strip())
            distrito.click()

            b.find_element_by_xpath('//*[@id="ctl00_CPH1_BtnFuenteAgregada"]').click() # Boton Fuentes
            time.sleep(1.5)

            recursos=b.find_elements_by_xpath('//*[@id="PnlData"]/table[2]/tbody/tr')
            a = 0
            for x in recursos:
                a = a + 1
            #print(a)

            b.find_element_by_xpath('//*[@id="ctl00_CPH1_RptData_ctl0' + str(a) + '_TD0"]/input').click()  # 5. Recursos Determinados

            b.find_element_by_xpath('//*[@id="ctl00_CPH1_BtnRubro"]').click()  # Boton Rubros
            time.sleep(1.5)

            canon = b.find_elements_by_xpath('//*[@id="PnlData"]/table[2]/tbody/tr')
            c = 0
            for y in canon:
                c = c + 1
            # print(c)

            b.find_element_by_xpath('//*[@id="ctl00_CPH1_RptData_ctl0' + str(c) + '_TD0"]/input').click()  # 18. Canon

            b.find_element_by_xpath('//*[@id="ctl00_CPH1_BtnTipoRecurso"]').click()  # Boton Tipos Recurso
            time.sleep(1.5)

            descargar = b.find_element_by_xpath("/html/body/form/div[4]/div[2]/table/tbody/tr/td[1]/a[2]")
            descargar.click()
            time.sleep(1.5)

            volver_ccdi = b.find_element_by_xpath('//*[@id="ctl00_CPH1_RptHistory_ctl05_TD0"]')
            volver_ccdi.click()
            time.sleep(1.5)

        volver_ccdd = b.find_element_by_xpath('//*[@id="ctl00_CPH1_RptHistory_ctl03_TD0"]')
        volver_ccdd.click()
        time.sleep(1)

### 2012-2013
for k in range(2012, 2014):
    print(str(k))
    b.get("http://apps5.mineco.gob.pe/transparencia/Navegador/default.aspx?y=" + str(k) + "&ap=ActProy")
    frame = b.find_element_by_xpath('//*[@id="frame0"]')
    b.switch_to.frame(frame)

    nivel_gobierno = b.find_element_by_name("ctl00$CPH1$BtnTipoGobierno")
    nivel_gobierno.click()

    gobierno_local = b.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr[2]")
    gobierno_local.click()

    gobierno_sublocal = b.find_element_by_xpath('//*[@id="ctl00_CPH1_BtnSubTipoGobierno"]')
    gobierno_sublocal.click()

    munis = b.find_element_by_xpath('//*[@id="ctl00_CPH1_RptData_ctl01_TD0"]/input')
    munis.click()

    departamentos = b.find_element_by_name("ctl00$CPH1$BtnDepartamento")
    departamentos.click()

    list_ccdd = [4, 7, 12, 13, 14, 15, 16, 20]  # 8 regiones [4, 7, 12, 13, 14, 15, 16, 20]

    for i in list_ccdd:
        departamento = b.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr[" + str(i) + "]/td[2]").text
        print(departamento)
        b.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr[" + str(i) + "]").click()

        b.find_element_by_xpath('//*[@id="ctl00_CPH1_BtnProvincia"]').click()

        b.find_element_by_xpath('//*[@id="ctl00_CPH1_RptData_ctl01_TD0"]/input').click()  # elegir la primera provincia

        b.find_element_by_name("ctl00$CPH1$BtnMunicipalidad").click()

        distritos = b.find_elements_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr")

        count = 1
        for distrito1 in distritos:
            distrito1.click()
            #print (count)
            count = count + 1

        for l in range(1, count):
            distrito = b.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[3]/div/table[2]/tbody/tr[" + str(l) + "]")
            distrito2 = ''.join([i for i in distrito.text if not i.isdigit()])
            distrito2 = re.sub('[-:,.]', '', distrito2)
            print(distrito2.strip())
            distrito.click()

            b.find_element_by_xpath('//*[@id="ctl00_CPH1_BtnFuenteAgregada"]').click() # Boton Fuentes
            time.sleep(1.5)

            recursos=b.find_elements_by_xpath('//*[@id="PnlData"]/table[2]/tbody/tr')
            a = 0
            for x in recursos:
                a = a + 1
            #print(a)

            b.find_element_by_xpath('//*[@id="ctl00_CPH1_RptData_ctl0' + str(a) + '_TD0"]/input').click()  # 5. Recursos Determinados

            b.find_element_by_xpath('//*[@id="ctl00_CPH1_BtnRubro"]').click()  # Boton Rubros
            time.sleep(1.5)

            canon = b.find_elements_by_xpath('//*[@id="PnlData"]/table[2]/tbody/tr')
            c = 0
            for y in canon:
                c = c + 1
            # print(c)

            b.find_element_by_xpath('//*[@id="ctl00_CPH1_RptData_ctl0' + str(c) + '_TD0"]/input').click()  # 18. Canon

            b.find_element_by_xpath('//*[@id="ctl00_CPH1_BtnTipoRecurso"]').click()  # Boton Tipos Recurso
            time.sleep(1.5)

            descargar = b.find_element_by_xpath("/html/body/form/div[4]/div[2]/table/tbody/tr/td[1]/a[2]")
            descargar.click()
            time.sleep(1.5)

            volver_ccdi = b.find_element_by_xpath('//*[@id="ctl00_CPH1_RptHistory_ctl06_TD0"]')
            volver_ccdi.click()
            time.sleep(1.5)

        volver_ccdd = b.find_element_by_xpath('//*[@id="ctl00_CPH1_RptHistory_ctl04_TD0"]')
        volver_ccdd.click()
        time.sleep(1)
