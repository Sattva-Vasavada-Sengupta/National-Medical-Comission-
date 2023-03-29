# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:14:34 2022

@author: savas
"""
data = data
import re 


#Get year of qualification of all degrees attained AND Age of completion of degrees
degree_endingterm_list = ['main', 'addtional_1', 'addtional_2' ,'addtional_3']

for end_term in degree_endingterm_list:
    
    print(end_term)
    # # Replace nans with np.nan
    # for i in range(0,len(data)):
    #     if str(data['year_qualification_'+end_term][i]) == 'nan':
    #         data['year_qualification_'+end_term][i] = np.nan
    
    # column = data['year_qualification_'+end_term]         
    # print('nan replacement over')
            
    #Get cleaned qualification years of degree
    qual_year_cleaned_list = list()  
    for date in list(data['year_qualification_'+end_term]):  
        if str(date) == 'nan':
            qual_year_cleaned_list.append(date) #If nan, then just impute nan in the list.
        else:
            try:
                qual_year_cleaned_list.append(date.split("-", 1)[1]) #If date like AUG-2020, then get '2020'
            except:
                qual_year_cleaned_list.append(date) #If not, then just append date
                
    print("list 1 over")
    
    qual_year_cleaned_list_2 = list() #Clean the list above. 
    for date in qual_year_cleaned_list:
        date = str(date)
        if date == 'nan':
            qual_year_cleaned_list_2.append(date) #nan
            
        elif re.search("\.", date):
            try:
                int((date.split('.',1)[0]))
                qual_year_cleaned_list_2.append(date.split('.',1)[0]) #Get all 2015.0 to only 2015
            except:
                qual_year_cleaned_list_2.append(np.nan)      
        
        elif re.search("^ ", date):        
            qual_year_cleaned_list_2.append(re.sub("^ ", "", date))       
        
        else:
            try:
                int(date)
                qual_year_cleaned_list_2.append(date) #If date cannot be converted to an integer, say it is
                #'2015}", then go to except and convert it to a nan. 
            except:
                qual_year_cleaned_list_2.append(np.nan)
                
    print("list 2 over")
                
    
    qual_year_cleaned_list_3 = list()
    for date in qual_year_cleaned_list_2:
        if str(date) == 'nan':
            qual_year_cleaned_list_3.append(np.nan)
            continue
            
        if int(date) <= 1900 or int(date) >= 2030:
            qual_year_cleaned_list_3.append(np.nan)
            continue
        
        else:
            qual_year_cleaned_list_3.append(int(date))
            continue

    print(set(qual_year_cleaned_list_3))

    data["qual_year_"+end_term] = qual_year_cleaned_list_3
    
    print("list 3 over")
    degree_age = list()
    
    for i in range(0, len(data)):
        if str(dob_list[i]) == 'nan' or str(qual_year_cleaned_list_3[i]) == 'nan':
            degree_age.append(np.nan)
        
        else:
            age = (qual_year_cleaned_list_3[i]) - (dob_list[i])
            degree_age.append(age)
            
    print("ilst 4 over")
    
    data["age_qualification_"+end_term] = degree_age
    
dataEasyView = data[["year_qualification_main", "qual_year_main",
                     "year_qualification_addtional_1", "qual_year_addtional_1", 
                     "year_qualification_addtional_2", "qual_year_addtional_2", 
                     "year_qualification_addtional_3", "qual_year_addtional_3"]]

dataEasyView = data[["date_of_birth_year", "year_qualification_main", "age_qualification_main"]]
dataEasyView = data[["date_of_birth_year", "year_qualification_addtional_1", "age_qualification_addtional_1"]]
dataEasyView = data[["date_of_birth_year", "year_qualification_addtional_2", "age_qualification_addtional_2"]]
dataEasyView = data[["date_of_birth_year", "year_qualification_addtional_3", "age_qualification_addtional_3"]]
