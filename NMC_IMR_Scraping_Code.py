import os
import pandas as  pd
# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
import time #Was using time.sleep(n), but am now using driver.implicitly_wait(n)
# import urllib.request
# import webbrowser
from selenium.webdriver.chrome.options import Options
import re

from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import math

import pickle

url = "https://www.nmc.org.in/information-desk/indian-medical-register/"

options = webdriver.ChromeOptions()
options.headless = True #Dont put headless on for some time. Once code is sorted, then do headless. 
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)

df_to_append = list()

driver.get(url)

driver.find_element_by_link_text("Year of Registration").click()

time.sleep(5)

driver.find_element_by_id("doctor_year").send_keys("2018")

time.sleep(2)

driver.find_element_by_id("doctor_year_details").click()

time.sleep(2)

entries = (driver.find_element_by_id("doct_info2_info")).text

time.sleep(2)

num_entries = int(re.findall('[0-9]+',
                             ((driver.find_element_by_xpath('//*[@id="totalRecords2"]')).text))[0])
num_pages = math.ceil(num_entries/500)

page_stopped = 1
for i in range(1, num_pages +1):
    time.sleep(2)
    current_page = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                               '//*[contains(concat( " ", @class, " " ), concat( " ", "current", " " ))]'))).text
    print("current page:", current_page)
    if int(current_page) == page_stopped:
        break
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[(@id = "doct_info2_next")]'))).click()
    time.sleep(2)
 
    
        
 
start_time = time.localtime()
for page in range(1, num_pages + 1):
    time.sleep(3)
    current_page = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, 
                                                                               '//*[contains(concat( " ", @class, " " ), concat( " ", "current", " " ))]'))).text
    print("current page:", current_page)
    for entry in range(1, 501): 
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//table[@id = "doct_info2"]/tbody/tr['+str(entry)+']/td[7]/a'))).click()
        except:
            time.sleep(5) 
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//table[@id = "doct_info2"]/tbody/tr['+str(entry)+']/td[7]/a'))).click()
        
        try:
            (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//table[@id = "doctorBiodata"]/tbody/tr[1]/td[2]'))))
        except:
            time.sleep(1)
        dfs = pd.read_html(driver.page_source)[5]
        df_to_append.append(dfs)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'modal-footer']/button[2]"))).click()
        print("page", current_page, "entry", entry, "over")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="doct_info2_next"]'))).click()
    
os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/NMC_Yearwise_Scrapped_Data")
with open('NMC_2018_Start from page 5.pkl', 'wb') as f:
    pickle.dump(df_to_append, f)

# shape_list = list()
# for df in df_to_append:
#     shape_list.append(df.shape[0])
    
# import numpy as np
# np.unique(shape_list)