#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# run under vp-env
#

# Download xml file from b3, unzip, read and parse xml, create tsv file to store results

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from webdriver_manager.chrome import ChromeDriverManager

import os
from os import listdir
from os.path import isfile
import os.path
import re
import time
import datetime
import urllib
from datetime import datetime, timedelta
from lxml import html, etree
from urllib.parse import  urlparse, parse_qs
import requests
import subprocess
from pyvirtualdisplay import Display
import zipfile
from settings import pathZip


def getB3Xml():
  ''' Download zip file from b3 '''
  
  url = 'https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/pesquisa-por-pregao/'
  
  # start webdriver and navegate to the webpage
  display = Display(visible=1, size=(800, 800))  
  display.start()
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.get( url )
  
  # wait until element to click is loaded
  wait = WebDriverWait(driver, 10)
  xp = '//input[@id="botao-download"]'
  confirm = wait.until(EC.element_to_be_clickable((By.XPATH, xp)))
  
  # find list
  xp = '//table/tbody/tr/td/input[@type="checkbox"]'
  e = driver.find_elements_by_xpath( xp )
  
  # let's hope b3 does not change this table because we are selecting
  # the selection box by location
  #print(len(e))
  e[4].click()
  
  # click download button
  xp = '//input[@id="botao-download"]'
  e = driver.find_element_by_xpath( xp )
  e.click()
  
  # WAIT THE DOWNLOAD TO FINISH
  
  file_path = pathZip + 'pesquisa-pregao.zip'
  
  tries = 1
  while not os.path.exists(file_path):
    time.sleep(1)
    tries += 1
    if tries > 180:
      break

  if isfile(file_path):
    pass
  else:
    raise ValueError("%s isn't a file!" % file_path)
  
  #time.sleep(5)
  

def unzipFile():
  ''' unzip files and delete original zip files '''
  
  # extract first file
  with zipfile.ZipFile(pathZip + "pesquisa-pregao.zip","r") as zip_ref:
    zip_ref.extractall(pathZip + 'b3')
  # find extracted zip file name
  for f in listdir(pathZip + 'b3'):  
    if isfile(pathZip + 'b3/' + f):
      # extract second file to xml directory
      with zipfile.ZipFile(pathZip + 'b3/' + f,"r") as zip_ref:
        zip_ref.extractall(pathZip + 'b3/xml')
      # delete second zip file
      os.remove(pathZip + 'b3/' + f)
  
  # delete first zip file
  os.remove(pathZip + "pesquisa-pregao.zip")
  
  

if __name__ == "__main__":
  getB3Xml()
  unzipFile()
