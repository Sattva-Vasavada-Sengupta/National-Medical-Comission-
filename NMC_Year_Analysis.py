import os
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import collections
import difflib
import pickle

#%%%
    
#%%%

#assume cutoff is 90% - check age of qualification from MBBS 

dataEasyView = data[(data.probabilty_gender > 0.9) &
                    (data.age_qualification_main > 20)]

dataEasyView.groupby(["state_medical_council", "predicted_gender"])['predicted_gender'].count()

dataEasyView[dataEasyView.qualmain_main == "MBBS"].groupby(["state_medical_council" ,
                                                            "predicted_gender"])['age_qualification_main'].mean()
                       

test = dataEasyView[dataEasyView.qualmain_main == "MBBS"].groupby(["state_medical_council" ,
                                                            "predicted_gender", 
                                                            "qual_year_main"])['age_qualification_main'].mean().reset_index()
 
def make_gender_mbbs_age_plot(state):
    plt.plot(test[(test.predicted_gender == "boy") &
                  (test.state_medical_council == state)]['qual_year_main'], 
             test[(test.predicted_gender == "boy") &
                  (test.state_medical_council == state)]['age_qualification_main'], label = "male")
    plt.plot(test[(test.predicted_gender == "girl") &
                  (test.state_medical_council == state)]['qual_year_main'], 
             test[(test.predicted_gender == "girl") &
                  (test.state_medical_council == state)]['age_qualification_main'], label = "female")
    plt.xlabel("Year")
    plt.ylabel("Age of Qualification, MBBS")
    plt.legend()
    plt.title("Gender Wise Age of Qualification, MBBS " +state)
    plt.xlim(2010, 2020)
    plt.show()
    
make_gender_mbbs_age_plot("karnataka medical council")
make_gender_mbbs_age_plot("telangana medical council")
make_gender_mbbs_age_plot("uttar pradesh medical council")



#=============================================================================
#%%%

#Summary Tables: Average age of completion of degrees - for all years (qual_year_main)

print(data[(data.age_qualification_main <= 80) &
     (data.age_qualification_main >= 17)][["qualmain_main", "age_qualification_main"]].groupby('qualmain_main').mean())


print(data[(data.age_qualification_addtional_1 <= 80) &
     (data.age_qualification_addtional_1 >= 17)][["addnQual1_main",
                                           "age_qualification_addtional_1"]].groupby('addnQual1_main').mean())

print(data[(data.age_qualification_addtional_2 <= 80) &
     (data.age_qualification_addtional_2 >= 17)][["addnQual2_main",
                                           "age_qualification_addtional_2"]].groupby('addnQual2_main').mean())

print(data[(data.age_qualification_addtional_3 <= 80) &
     (data.age_qualification_addtional_3 >= 17)][["addnQual3_main",
                                           "age_qualification_addtional_3"]].groupby('addnQual3_main').mean())


#=============================================================================
#%%%
     
# Individual level age differnece in going from MBBS to other degrees                                                
data["diff_addn1_main"] = data['age_qualification_addtional_1'] - data['age_qualification_main']

a1 = (data[(data.qualmain_main == "MBBS") & 
     (data.age_qualification_main <= 80) & (data.age_qualification_main >= 17) &
     (data.age_qualification_addtional_1 <= 80) & (data.age_qualification_addtional_1 >= 17)].groupby("addnQual1_main")['diff_addn1_main'].mean())
a2 = (data[(data.qualmain_main == "MBBS") & 
     (data.age_qualification_main <= 80) & (data.age_qualification_main >= 17) &
     (data.age_qualification_addtional_1 <= 80) & (data.age_qualification_addtional_1 >= 17)].groupby("addnQual1_main")['diff_addn1_main'].count())
print(pd.merge(a1, a2, left_index = True, right_index = True).rename(columns = {'diff_addn1_main_x': 'Time b/w MBBS and: ',
                                                                                        'diff_addn1_main_y': 'count'}))




len(data[(data.qualmain_main == "MBBS") & (data.addnQual1_main == "MS")])

#Individual level age difference in going from first additional degree to second additional degree
data["diff_addn2_addn1"] = data['age_qualification_addtional_2'] - data['age_qualification_addtional_1']

a1 = (data[(data.age_qualification_addtional_1 <= 80) & (data.age_qualification_addtional_1 >= 17) &
     (data.age_qualification_addtional_2 <= 80) & (data.age_qualification_addtional_2 >= 17)].groupby(
         ["addnQual1_main", "addnQual2_main"])['diff_addn2_addn1'].mean())

a2 =  (data[(data.age_qualification_addtional_1 <= 80) & (data.age_qualification_addtional_1 >= 17) &
     (data.age_qualification_addtional_2 <= 80) & (data.age_qualification_addtional_2 >= 17)].groupby(
         ["addnQual1_main", "addnQual2_main"])['diff_addn2_addn1'].count())
         
print(pd.merge(a1, a2, left_index = True, right_index = True)  )      
        
         
len(data[(data.addnQual1_main == "MD") & (data.addnQual2_main == "DM")])


#=============================================================================
#%%%

#Age of qualification MBBS grouped by state medical council registration. 
print(data[(data.age_qualification_main <= 80) & (data.age_qualification_main >= 17) &
     (data.qualmain_main == "MBBS")].groupby("state_medical_council")['state_medical_council', 'age_qualification_main'].mean().sort_values(by = 'age_qualification_main'))



#=============================================================================
#%%%

#Age of qualification of MBBS grouped by year of graduation from MBBS
data_qual_age_MBBS = data[(data.age_qualification_main <= 80) & (data.age_qualification_main >= 17) &
     (data.qualmain_main == "MBBS")].groupby("qual_year_main")['qual_year_main', 'age_qualification_main'].mean()

test = pd.DataFrame(data[(data.age_qualification_main <= 80) & (data.age_qualification_main >= 17) &
     (data.qualmain_main == "MBBS")]['qual_year_main'].value_counts())
test['year'] = list(test.index)



plt.scatter(data_qual_age_MBBS['qual_year_main'], data_qual_age_MBBS['age_qualification_main'])
plt.xlim(2000, 2018)
plt.show()

dataEasyView = data[(data.qual_year_main > 2015)]


#=============================================================================
#%%%

#Look at MBBS age of graduation by gender for Bihar

a1 = data[(data.age_qualification_main <= 80) & (data.age_qualification_main >= 17) &
     (data.qualmain_main == "MBBS") &
     (data.state_medical_council == 'bihar')].groupby(["gender", 'qual_year_main'])['age_qualification_main'].mean()


                                                                                    
a2 = (data[(data.age_qualification_main <= 80) & (data.age_qualification_main >= 17) &
     (data.qualmain_main == "MBBS") &
     (data.state_medical_council == 'bihar')].groupby(["gender", 'qual_year_main'])['age_qualification_main'].count())
                                                                                    
dataEasyView = pd.merge(a1, a2, how = 'inner', left_index = True, right_index = True)                                                                        

dataEasyView.reset_index(inplace = True)
dataEasyView = dataEasyView[(dataEasyView.qual_year_main > 2011) &
                            (dataEasyView.qual_year_main <= 2018)]
dataEasyView.rename(columns = {'age_qualification_main_y': 'count'}, inplace = True)
     
print(dataEasyView)



plt.plot(dataEasyView[dataEasyView.gender == "boy"]['qual_year_main'], 
         dataEasyView[dataEasyView.gender == 'boy']['age_qualification_main_x'], label = "male")
plt.plot(dataEasyView[dataEasyView.gender == "girl"]['qual_year_main'], 
         dataEasyView[dataEasyView.gender == 'girl']['age_qualification_main_x'], label =  "female")
plt.xlabel("Year")
plt.ylabel("Age of Qualification, MBBS")
plt.legend()
plt.title("Bihar: Gender Wise Age of Qualification, MBBS")
plt.show()


#=============================================================================
#%%%

#Statewise trends in age of qualification (state obtained from pincode)

def make_statewise_degree_table(degree):
    
    if str(degree) == "MBBS":
        a1 = data[(data.age_qualification_main <= 80) & (data.age_qualification_main >= 17) &
                  (data.qualmain_main == "MBBS")].groupby("StateName")['StateName', 'age_qualification_main'].mean().sort_values(by = 'age_qualification_main')
        a2 = pd.DataFrame(data[(data.age_qualification_main <= 80) & (data.age_qualification_main >= 17) &
             (data.qualmain_main == "MBBS")].groupby("StateName")['age_qualification_main'].count().sort_values())
        print(pd.merge(a1, a2, left_index = True, right_index = True).rename(columns = {'age_qualification_main_y': 'count',
                                                                                        'age_qualification_main_x': 'MBBS graduation age'}).sort_values(by = 'MBBS graduation age'))

        
    if degree != "MBBS": 
        a1 = data[(data.age_qualification_main <= 80) & (data.age_qualification_main >= 17) &
                  (data.addnQual1_main == degree)].groupby("StateName")['StateName', 'age_qualification_addtional_1'].mean().sort_values(by = 'age_qualification_addtional_1')
        a2 = data[(data.age_qualification_main <= 80) & (data.age_qualification_main >= 17) &
             (data.addnQual1_main == degree)].groupby("StateName")['age_qualification_addtional_1'].count().sort_values()
        print(pd.merge(a1, a2, left_index = True, right_index = True).rename(columns = {'age_qualification_addtional_1_y': 'count',
                                                                                        'age_qualification_addtional_1_x': degree}).sort_values(by = degree))

make_statewise_degree_table("MBBS")
make_statewise_degree_table("MD")
make_statewise_degree_table("MS")
make_statewise_degree_table("Diploma")
make_statewise_degree_table("DNB")


#=============================================================================
#%%%


a1 = (data[(data.qualmain_main == "MBBS") & 
     (data.age_qualification_main <= 80) & 
     (data.age_qualification_main >= 17) &
     (data.age_qualification_addtional_1 <= 80) &
     (data.age_qualification_addtional_1 >= 17) &
     (data.diff_addn1_main >= 3) &
     (data.probabilty_gender >= 0.9)].groupby([ "StateName", "predicted_gender",
                                                          "addnQual1_main"])['diff_addn1_main'].mean())


a2 = (data[(data.qualmain_main == "MBBS") & 
     (data.age_qualification_main <= 80) & 
     (data.age_qualification_main >= 17) &
     (data.age_qualification_addtional_1 <= 80) &
     (data.age_qualification_addtional_1 >= 17) &
     (data.diff_addn1_main >= 3)&
     (data.probabilty_gender >= 0.9)].groupby(['StateName', "predicted_gender",
                                           "addnQual1_main"])['diff_addn1_main'].count())

test = (pd.merge(a1, a2, left_index = True, right_index = True)).rename(columns = {'diff_addn1_main_x': 'time gap b/w mbbs and degree qualification',
                                                                                   'diff_addn1_main_y': 'count'})
test.reset_index(inplace = True)


dataEasyView = test[test.addnQual1_main == "MD"].sort_values(by = "time gap b/w mbbs and degree qualification")


dataEasyView = data[(data.StateName == "Tripura") &
                    (data.addnQual1_main == "MD")][['name_x', 'qualmain_main',
                                                    'addnQual1_main',
                                                    'date_of_birth_year', 'qual_year_main',
                                                    'age_qualification_main',
                                                    'qual_year_addtional_1',
                                                    'age_qualification_addtional_1', 
                                                    'addnQual2_main', 'addnQual3_main',
                                                    'diff_addn1_main']]
                                                    
                                                    
len(data[data.addnQual1_main == "DNB"])


#=============================================================================
#%%%


