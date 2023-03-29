import os
import pandas as pd    
import numpy as np
import time
# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver

import re
from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import math

import pickle


#=============================================================================
#%%%

dataEasyView = data #[data.year_of_info == 2015]
dataEasyView = dataEasyView.reset_index(drop = True)

loop_start = np.min(dataEasyView.index) 
loop_end = np.max(dataEasyView.index)


appending_list = list()


#Subtract father name from child name to get child first name. 
for i in range(loop_start, loop_end + 1):
    if str(dataEasyView["name"][i]) == "nan" or str(dataEasyView["father_name"][i]) == "nan":
        appending_list.append(np.nan)
        continue
        
    else:    
        name = re.sub("dr\. ", "", dataEasyView['name'][i].lower())
        name = re.sub("\,", "", name)
        father_name = re.sub("dr\.", "", dataEasyView['father_name'][i].lower())
        appending_list.append(set(name.split(" ")) - 
                               set(father_name.split(" ")))

dataEasyView['name_subtraction'] = appending_list
test = dataEasyView[['name', 'father_name', 'name_subtraction']]

count = 0
for first_name in dataEasyView['name_subtraction']:
    if str(first_name) != "nan":
        if len(first_name) == 1 :
            count += 1
        
print(count)

#%%%

one_word_name_list = list()
index_list = list()

for i in range(0, len(dataEasyView['name_subtraction'])):
    name = dataEasyView['name_subtraction'][i]
    if str(name) == "nan":
        continue
    
    if str(name) != "nan" and len(name) == 1:
        try:
            name = re.search("[A-Za-z]+", str(name)).group(0).lower()
            one_word_name_list.append(name)
            index_list.append(i)
        except:
            continue

    
    if str(name) != "nan" and len(name) != 1:
        continue

test = pd.DataFrame(list(zip(one_word_name_list, index_list)), columns =['name', 'index_col']) 

result = [] 
[result.append(x) for x in one_word_name_list if x not in result] 

ten_words_list = list()
temp = list()
count = 1
for name in result:
    if count <= 10:
        temp.append(name)
        count += 1
    else:
        count = 2
        ten_words_list.append(temp)
        temp = list()
        temp.append(name)

count = 0      
for words_list in ten_words_list:
    try:
        if len(set(words_list)) != 10:
            count += 1
            a = words_list
    except: 
        continue
print(count)
            

string_list = list()
for i in range(0, len(ten_words_list)):
    string = ""
    count = 1
    test_list = ten_words_list[i]
    for name in test_list:
        if count == 1:
            string = string + str(name)
            count += 1
            
        else:
            string = string + ", " + str(name)
            
    string_list.append(string)




#=============================================================================
#%%%

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time #Was using time.sleep(n), but am now using driver.implicitly_wait(n)
# import urllib.request
# import webbrowser
from selenium.webdriver.chrome.options import Options
import re

from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.support import expected_conditions as EC

import logging
import pickle


df_to_append = list()

url = "https://www.boyorgirl.xyz/"

options = webdriver.ChromeOptions()
options.headless = True 
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)

driver.get(url)
count = 1
string_list_updated = string_list[0:]
for string in string_list_updated:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[(@id = "reset-button")]'))).click()
    
    text_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[(@id = "names")]')))
    time.sleep(1)
    text_field.send_keys(string)
    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[(@id = "submit-button")]'))).click()
    
    time.sleep(1)
    try:
        df = pd.read_html(driver.page_source)[0][1:11]
    except: 
        time.sleep(3)
        text_field.send_keys(string)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[(@id = "submit-button")]'))).click()
        df = pd.read_html(driver.page_source)[0][1:11]
        
    df_to_append.append(df)
    print(count)
    count += 1
    
os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/NMC_Yearwise_Scrapped_Data")
with open('GenderData_1978-2018.pkl', 'wb') as f:
    pickle.dump(df_to_append, f)
    
#=============================================================================
#%%% 

#Test merging code. it is correct. 


# appending_df = pd.DataFrame()

# for df in df_to_append:
#     appending_df = pd.concat([appending_df, df], axis = 0)    

# appending_df.columns = ['name', 'predicted_gender', 'probabilty_gender']
# appending_df.reset_index(inplace = True)


# result_df = pd.merge(test, appending_df, how = "inner", on = 'name')
