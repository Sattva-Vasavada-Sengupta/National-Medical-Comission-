import os
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import collections
from collections import Counter
import difflib
import pickle
import pgeocode #For calculating distance between pincodes. 
from fuzzywuzzy import fuzz
import time
from nameparser import HumanName
import probablepeople
from guess_indian_gender import IndianGenderPredictor

#=============================================================================
#%%% Combining all available datasets from 2012-2018. 

os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/NMC_Yearwise_Scrapped_Data")
year_list = list(map(str, list(range(1957, 2019, 1))))
year_list.remove("1958")
year_list.remove("1959")

data = pd.DataFrame()
for year in year_list:
    data_year = pd.read_csv("NMC_"+year+".csv")
    data_year = data_year.drop_duplicates(subset = ['name', 'father_name', 'permanent_address'], keep = 'first')
    print(year, len(data_year))
    data = pd.concat([data, data_year], axis = 0)

# data = pd.read_csv("NMC_2018.csv")
data.drop(["Unnamed: 0"], axis = 1, inplace = True)
data.columns

data_index_list = list(range(0, len(data)))

index = pd.Index(data_index_list)
data = data.set_index(index)


# test = (data[data.duplicated(keep = False)])
#=============================================================================
#%%% Defining functions to see if a doctor did an MD or a MS or something else. 

os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/Code")
exec(open('Getting NMC Degrees - MBBS, MD, etc.py').read())


#=============================================================================
#%%% Getting list of cleaned qualifications using the fuctions defined in the above cell. 

os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/Code")
exec(open('Getting Cleaned Qualification List.py').read())
    
#=============================================================================
#%%% Wrangling the main degree column (mostly MBBS, but some MD, MS too)

os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/Code")
exec(open('Getting the NMC main degree column wrangled.py').read())

#=============================================================================
#%%%

#delete this file as soon as you are done with cleaing the degrees. Best not to have too many temp files around. 
# os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/UpdatedDataFiles")
# data.to_csv("nmc_onlydegreewrangled.csv")

# os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/UpdatedDataFiles")
# data = pd.read_csv("nmc_onlydegreewrangled.csv")
#data changed to data1 in case for some reason I manage to uncomment and run this code. 
#seems correct now. Will now comment this code so that I don't run it accidentaly. 


#%%%

#checking function
def c(column):
    data[column]
    return Counter(data[column])

def dip_checking():
    return data[(data.qualmain_main != "Diploma") & (data.addnQual1_main != "Diploma") &
                        (data.addnQual2_main != "Diploma") & (data.addnQual3_main != "Diploma") &
                        (data.pg_degree_1 == "Diploma")]

def ug_checking():
    return Counter(data.ug_degree)

#=============================================================================
#%%% Creating final degree columns.Currently not being used. 

data['ug_degree'] = ''
data['ug_degree_imputed'] = 0 #0 if qualmain_main is MBBS, 1 if qualmain_main is MD, MS. We impute MBBS for
#observations with MD, MS because they must've done MBBS before, obviously. 

data['pg_degree_1'] = ''
data['pg_degree_1_imputed'] = 0 

data['pg_degree_2'] = ''
data['pg_degree_2_imputed'] = 0

data['pg_degree_3'] = ''
data['pg_degree_3_imputed'] = 0

data['pg_degree_unsorted_1'] = ''
data['pg_degree_unsorted_1_imputed'] = 0

data['pg_degree_unsorted_2'] = ''
data['pg_degree_unsorted_2_imputed'] = 0

data['ugdeg_mapfrom'] = ''
data['pgdeg1_mapfrom'] = ''
data['pgdeg2_mapfrom'] = ''
data['pgdeg3_mapfrom'] = ''
data['pgdeg1_unsorted_mapfrom'] = ''
data['pgdeg2_unsorted_mapfrom'] = ''

data['not_recog_ugdeg'] = 0
data['foreign_ugdeg'] = 0

#Convert all old undergraduate degrees into MBBS degrees. THis preserves their qulification as an undergrad
#These degrees also have not_recog_deg = 1
old_ug_deg_list = ['LMP', 'LMS', 'LMF', 'cert_wbmf', 'LCPS', 'LSMF', 'MB', 'MMF']
for degree in old_ug_deg_list: 
    data.loc[(data['qualmain_main'] == degree), 'not_recog_ugdeg'] = 1
    data.loc[(data['qualmain_main'] == degree), 'qualmain_main'] = 'MBBS'

    data.loc[(data['addnQual1_main'] == degree), 'not_recog_ugdeg'] = 1
    data.loc[(data['addnQual1_main'] == degree), 'addnQual1_main'] = 'MBBS'
    
    data.loc[(data['addnQual2_main'] == degree), 'not_recog_ugdeg'] = 1
    data.loc[(data['addnQual2_main'] == degree), 'addnQual2_main'] = 'MBBS'
    
    data.loc[(data['addnQual3_main'] == degree), 'not_recog_ugdeg'] = 1
    data.loc[(data['addnQual3_main'] == degree), 'addnQual3_main'] = 'MBBS'

foreign_deg_list = ['LRCP']
for degree in foreign_deg_list: 
    data.loc[(data['qualmain_main'] == degree), 'foreign_ugdeg'] = 1
    data.loc[(data['qualmain_main'] == degree), 'qualmain_main'] = 'MBBS'

    data.loc[(data['addnQual1_main'] == degree), 'foreign_ugdeg'] = 1
    data.loc[(data['addnQual1_main'] == degree), 'addnQual1_main'] = 'MBBS'
    
    data.loc[(data['addnQual2_main'] == degree), 'foreign_ugdeg'] = 1
    data.loc[(data['addnQual2_main'] == degree), 'addnQual2_main'] = 'MBBS'
    
    data.loc[(data['addnQual3_main'] == degree), 'foreign_ugdeg'] = 1
    data.loc[(data['addnQual3_main'] == degree), 'addnQual3_main'] = 'MBBS'
#ug degree column
data.loc[(data['qualmain_main'] == 'None'), 'ug_degree'] = 'None' #none remains none, but will be changed 
# data.loc[(data['qualmain_main'] == 'None'), 'ugdeg_mapfrom'] = 0 #none remains none, but will be changed 
#later if a pg degree has MBBS written in it. 
ug_checking() #43883 None, which matches with tab qualmain_main number of Nones. 

#if qualmain_main is MBBS, then put ug_degree as MBBS
data.loc[(data['qualmain_main'] == 'MBBS'), 'ug_degree'] = 'MBBS'
data.loc[(data['qualmain_main'] == 'MBBS'), 'ugdeg_mapfrom'] = 0 #ug degree mapped from column "0" - qualmain_main
# ug_checking() #1,10,393: same as tab qualmain_main


#if qualmain_main is any other ug degree other than MBBS, then put ug_degree = that degree
data.loc[(data['qualmain_main'] != 'MBBS') & 
          (data['qualmain_main'] != 'None'), 'ug_degree'] = 'MBBS' #for all obesrvations that are not MBBS 
          #and not "None", that is, MD MS etc, these people must've done an MBBS from somewhere, obviously.
data.loc[(data['qualmain_main'] != 'MBBS') & 
          (data['qualmain_main'] != 'None'), 'ugdeg_mapfrom'] = 0.1
data.loc[(data['qualmain_main'] != 'MBBS') & 
          (data['qualmain_main'] != 'None'), 'ug_degree_imputed'] = 1  #we put 1 for such imputed observations
#because we do not want to include them when working with university of graduation, because we will end
#up considering university of (say) MD for a university for MBBS, which is obviously wrong. 

# ug_checking() #correct. number of PG degrees in qualmain_main: 27,958. Correct: 1103393 + 27958 = 1131351

#For pg degrees that have MBBS in them: 
data.loc[(data['addnQual1_main'] == 'MBBS') &
         (data['qualmain_main'] != "MBBS"), 'ug_degree'] = 'MBBS'
data.loc[(data['addnQual1_main'] == 'MBBS'), 'ugdeg_mapfrom'] = 1 

# ug_checking() #MBBS now: 1133482, diff from above: 2131. There were 2212 MBBSs in addnqual1_main. Where 
#did the 81 MBBSs go? There are 81 less mbbs's getting transffered. Does this mean that for 81 obervations
#ug_degree already had MBBS, and thus only 2131 new MBBSs got added? 

data.loc[(data['addnQual2_main'] == 'MBBS') &
         (data['qualmain_main'] != "MBBS"), 'ug_degree'] = 'MBBS'
data.loc[(data['addnQual2_main'] == 'MBBS'), 'ugdeg_mapfrom'] = 2

# ug_checking() #MBBSs now: 1133569, diff from above: 87. 

data.loc[(data['addnQual3_main'] == 'MBBS') &
         (data['qualmain_main'] != "MBBS"), 'ug_degree'] = 'MBBS'
data.loc[(data['addnQual3_main'] == 'MBBS'), 'ugdeg_mapfrom'] = 3

# ug_checking() #1133574 MBBSs. 
#2223 more MBBS's added: addnqual1_main has 2212 MBBSs, addnqual2_main has 125, addnqual3_main has 6. 
#total is 2343. 

#for all observaions where qualmain_main is none and addnqual 1,2,3 have a PG degree (neither None nor MBBS),
#put ug_degree as MBBS by imputing. 
data.loc[(data.qualmain_main == "None") &
         ((data.addnQual1_main != "None") & (data.addnQual1_main != "MBBS")) |
         ((data.addnQual2_main != "None") & (data.addnQual2_main != "MBBS")) | 
         ((data.addnQual3_main != "None") & (data.addnQual3_main != "MBBS")),
         'ug_degree'] = "MBBS"
data.loc[(data.qualmain_main == "None") &
         ((data.addnQual1_main != "None") & (data.addnQual1_main != "MBBS")) |
         ((data.addnQual2_main != "None") & (data.addnQual2_main != "MBBS")) | 
         ((data.addnQual3_main != "None") & (data.addnQual3_main != "MBBS")),
         'ug_degree_imputed'] = 1
data.loc[(data.qualmain_main == "None") &
         ((data.addnQual1_main != "None") & (data.addnQual1_main != "MBBS")) |
         ((data.addnQual2_main != "None") & (data.addnQual2_main != "MBBS")) | 
         ((data.addnQual3_main != "None") & (data.addnQual3_main != "MBBS")),
         'ugdeg_mapfrom'] = 0.1

# ug_checking() #Final: 1134527. 

#-------------------

#pg degree column 1: addnQual1_main
data.loc[(data['addnQual1_main'] == 'None'), 'pg_degree_1'] = 'None' #none remains none.
# data.loc[(data['addnQual1_main'] == 'None'), 'pgdeg1_mapfrom'] = 1 #none remains none.

  
#now for all pg degrees in addnQual1_main, put pg_degree_1 = that degree
for degree in list(set(data.addnQual1_main) - {'MBBS', 'None'}):
    data.loc[(data['addnQual1_main'] == degree), 'pg_degree_1'] = degree 
    data.loc[(data['addnQual1_main'] == degree), 'pgdeg1_mapfrom'] = 1


# a = dip_checking()

#impute all MD MS etc in qualmain_main to pg_degree_1
for degree in list(set(data.qualmain_main) - {'MBBS', 'None'}):
    data.loc[(data['qualmain_main'] == degree), 'pg_degree_1'] = degree 
    data.loc[(data['qualmain_main'] == degree), 'pg_degree_1_imputed'] = 1
    data.loc[(data['qualmain_main'] == degree), 'pgdeg1_mapfrom'] = 0
# a = dip_checking()


#what about observations with PG degrees in qualmain_main (not MBBS, not None) and a PG degree in 
#addnQual1_main? Then simply replacing pg_degree_1 initially with addnqual1_main and then replacing that
#with qualmain_main would only result in the qualmain_main obervation being recorded. There are 828 such 
#observations. We thus create another column to store such obs. The observations in addnqual1_main are 
#stored in pg_degree4 list, with a column in the dataframe called pg_degree_unsorted_1.
pg_degree4_list = list()
for degree, degree_addn1 in zip(list(data.qualmain_main), list(data.addnQual1_main)):
    if degree == "MBBS" or degree == "None":
        pg_degree4_list.append("None")
        continue
    else:
        if degree_addn1 == "MBBS" or degree_addn1 == "None":
            pg_degree4_list.append(np.nan)
            continue
        else:
            pg_degree4_list.append(degree_addn1)

data['pg_degree_unsorted_1'] = pg_degree4_list
data.loc[(data.pg_degree_unsorted_1 != "None") &
         (data.pg_degree_unsorted_1 != ""), "pgdeg1_unsorted_mapfrom"] = 1 #observations come from addnqual1_main
data.loc[(data.pg_degree_unsorted_1 != "None") , "pg_degree_unsorted_1_imputed"] = 1

#for all addnQual2_main degrees that are neither none nor MBBS, but addnQual1_main is, 
#put pgdegree1 = that degree
for degree in list(set(data.addnQual2_main) - {'MBBS', 'None'}):
    data.loc[(data['addnQual2_main'] == degree) &
              ((data['addnQual1_main'] == "None") |
              (data['addnQual1_main'] == "MBBS")) &
              ((data.pg_degree_1 == "") |
               (data.pg_degree_1 == "None")), 'pg_degree_1'] = degree #pg_degree1 condition added because 
    #there were observations where addnqual1_main was MBBS and thus the PG degree in addnqual2_main 
    #was being mapped to pg_degree_1 where there was already a degree there before, from qualmain_main. 
    data.loc[(data['addnQual2_main'] == degree) &
              ((data['addnQual1_main'] == "None")|
              (data['addnQual1_main'] == "MBBS"))&
              ((data.pg_degree_1 == "") |
               (data.pg_degree_1 == "None")), 'pg_degree_1_imputed'] = 1 
    data.loc[(data['addnQual2_main'] == degree) &
              ((data['addnQual1_main'] == "None") |
              (data['addnQual1_main'] == "MBBS"))&
              ((data.pg_degree_1 == "") |
               (data.pg_degree_1 == "None")), 'pgdeg1_mapfrom'] = 2 

# a = dip_checking()


#now suppose there is a PG degree in qualmain_main, "None" in addnqual1_main, and another PG degree in addnqual2_main. 
#if we replace pg_degree_1 with those addnqual2_main degrees, then the origanl qualmain_main PG degrees 
#will get wiped out. 
pg_degree5_list = list()
for degree_m, degree_1, degree_2 in zip(list(data.qualmain_main), list(data.addnQual1_main), list(data.addnQual2_main)):
    if degree_m == "MBBS" or degree_m == "None": #filter out PG degrees
        pg_degree5_list.append("None")
        continue
    else: #now degree_m is a PG degee
        if degree_1 == "None": #get addnqual1_main degrees that are none.  
            if degree_2 != "None": #get addnqual2_main degrees that are not none
                pg_degree5_list.append(degree_m) #get the wiped out qualmain_main PG degree. 
            else:
                pg_degree5_list.append("None")
        else: 
            pg_degree5_list.append("None")
            continue
        

data['pg_degree_unsorted_2'] = pg_degree5_list
data.loc[(data.pg_degree_unsorted_2 != "None") &
         (data.pg_degree_unsorted_2 != ""), 'pgdeg2_unsorted_mapfrom'] = 2
data.loc[data.pg_degree_unsorted_2 != "None", 'pg_degree_unsorted_2_imputed'] == 1
# br qualmain_main addnqual1_main addnqual2_main  if qualmain_main != "MBBS" & qualmain_main != "None" & addnqual1_main == "None" & addnqual2_main != "None"        
# print(Counter(pg_degree5_list))
#the counter should return the same list of observations as the STATA br command above. 

#for all addnQual3_main degrees that are not None or MBBS but addnQual1_main and 2 is, put pgdegree1 = that degree
for degree in list(set(data.addnQual3_main) - {'MBBS', 'None'}):
    data.loc[(data['addnQual3_main'] == degree) &
              (data['addnQual2_main'] == "None") &
              (data['addnQual1_main'] == "None"), 'pg_degree_1'] = degree 
    data.loc[(data['addnQual3_main'] == degree) &
              (data['addnQual2_main'] == "None") &
              (data['addnQual1_main'] == "None"), 'pg_degree_1_imputed'] = 1
    data.loc[(data['addnQual3_main'] == degree) &
              (data['addnQual2_main'] == "None") &
              (data['addnQual1_main'] == "None"), 'pgdeg1_mapfrom'] = 3
    
#a = dip_checking()


#There are no observations that have a PG degree in qualmain_main, but none in addnqual1_main and 
#addnqual2_main but then have a PG degree in addnqual3_main. Hene, we do not fear wiping out these 
#observations in pg_degree_1 which origianlly had qualmain_main PG degree but would be replaced by 
#addnqual3_main PG degree. Check in STATA: 
#br qualmain_main addnqual1_main addnqual2_main addnqual3_main if qualmain_main != "MBBS" & qualmain_main != "None" & addnqual1_main == "None" & addnqual2_main == "None" & addnqual3_main != "None"
    
#pg degree column 2: addnQual2_main
data.loc[(data['addnQual2_main'] == 'None'), 'pg_degree_2'] = 'None' #none remains none.
# data.loc[(data['addnQual2_main'] == 'None'), 'pgdeg2_mapfrom'] = 2 #none remains none.

#for all degrees in addnQual2_main that are not MBBS or None, put pgdegree2 = that degree.
for degree in list(set(data.addnQual2_main) - {'MBBS', 'None'}):
    data.loc[(data['addnQual2_main'] == degree), 'pg_degree_2'] = degree 
    data.loc[(data['addnQual2_main'] == degree), 'pgdeg2_mapfrom'] = 2 
    
#for all addnQual3_main degrees that are not MBBS or None, but addnQual2_main is, put pgdegree2 = that degree
for degree in list(set(data.addnQual3_main) - {'MBBS', 'None'}):
    data.loc[(data['addnQual3_main'] == degree) &
              ((data['addnQual2_main'] == "None") |
              (data['addnQual2_main'] == "MBBS")), 'pg_degree_2'] = degree 
    data.loc[(data['addnQual3_main'] == degree) &
              ((data['addnQual2_main'] == "None") |
              (data['addnQual2_main'] == "MBBS")), 'pg_degree_2_imputed'] = 1 
    data.loc[(data['addnQual3_main'] == degree) &
              ((data['addnQual2_main'] == "None") |
              (data['addnQual2_main'] == "MBBS")), 'pgdeg2_mapfrom'] = 3
    
#for pg degree column 3: addnQual3_main
data.loc[(data['addnQual3_main'] == 'None'), 'pg_degree_3'] = 'None' #none remains none.
# data.loc[(data['addnQual3_main'] == 'None'), 'pgdeg3_mapfrom'] = 3 #none remains none.

#for all degrees in addnQual3_main that are not MBBS or None, put pgdegree3 = that degree.
for degree in list(set(data.addnQual2_main) - {'MBBS', 'None'}):
    data.loc[(data['addnQual3_main'] == degree), 'pg_degree_3'] = degree 
    data.loc[(data['addnQual3_main'] == degree), 'pgdeg3_mapfrom'] = 3 


#%%%
os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/UpdatedDataFiles")

dataEasyView = data[['addnQual1_main', 'addnQual2_main', 'addnQual3_main', 'qualmain_main',
                    'ug_degree', 'ug_degree_imputed', 'pg_degree_1', 'pg_degree_1_imputed',
                    'pg_degree_2', 'pg_degree_2_imputed', 'pg_degree_3',
                    'pg_degree_3_imputed', 'pg_degree_unsorted_1',
                    'pg_degree_unsorted_1_imputed', 'pg_degree_unsorted_2',
                    'pg_degree_unsorted_2_imputed', 'ugdeg_mapfrom', 'pgdeg1_mapfrom',
                    'pgdeg2_mapfrom', 'pgdeg3_mapfrom', 'pgdeg1_unsorted_mapfrom',
                    'pgdeg2_unsorted_mapfrom', 'not_recog_ugdeg', 'foreign_ugdeg']]
dataEasyView.to_csv("nmc_testingdegreecleaning.csv")



#=============================================================================
#%%%

#Check stuff here: 
checking_list = list(data['qualification_addtional_3'])
cleanedSet =  [y.lower() for y in set([x for x in checking_list if str(x) != 'nan'])] 
for degree in cleanedSet:
    if re.search("adm", degree):
        print(re.search("adm", degree), degree) 
        
    # elif re.search("^diplomate", degree):
    #     print(re.search("^diplomate", degree), degree) 

#=============================================================================   
#%%%
##Check what degrees are included in none.       
#column names: qualification_main, qualification_addtional_
checking_list = list(data['qualification_main'])
# cleanedSet =  [y.lower() for y in set([x for x in checking_list if str(x) != 'nan'])] 

count = 0
unaccounted_degrees_list = list()
for degree in checking_list:
    
    degree = str(degree).lower()
    if str(degree) == 'nan': 
        continue
    
    elif find_MBBS(degree) == True:
        continue
        
    elif find_MD(degree) == True:
        continue
    
    elif find_MS(degree) == True:
        continue
        
    elif find_DM(degree) == True:
        continue
    
    elif find_diplomate_ntnl_board(degree) == True:
        continue
    
    elif find_diploma_all(degree) == True:
        continue
    
    elif find_mch(degree) == True:
        continue
    
    elif find_mrcp_mrc(degree) == True:
        continue
    
    elif find_fellow(degree) == True:
        continue
    
    elif find_public_health(degree) ==  True:
        continue
    
    elif find_mha(degree) == True:
        continue
    
    elif find_lmp(degree) == True:
        continue
    
    elif find_lmf(degree) == True: 
        continue
    
    elif find_lcps(degree) == True: 
        continue
    
    elif find_lms(degree) == True: 
        continue
    
    elif find_lsmf(degree) == True: 
        continue
    
    elif find_cert_wbmf(degree) == True: 
        continue
    
    elif find_mb(degree) == True: 
        continue
    
    elif find_lrcp(degree) == True: 
        continue
    
    elif find_mcps(degree) == True: 
        continue
    
    elif find_mmf(degree) == True: 
        continue
    
      
    else: 
        count += 1
        # print(degree)
        unaccounted_degrees_list.append(degree)

# (unaccounted_degrees_list.sort())
# for degree in unaccounted_degrees_list:
#     print(degree)

dataEasyView = pd.DataFrame(dict(Counter(unaccounted_degrees_list)).items())
print(count)
#=============================================================================    
#%%%

#Get date of births
dob_list = list()
for i in range(0, len(data)):
    if str(data['date_of_birth'][i]) == 'nan':
        dob_list.append(np.nan)
    else:
        try:
            dob_list.append(int((data['date_of_birth'][i]).split("/",2)[2]))
            
        except: 
            dob_list.append(int((data['date_of_birth'][i]).split("-",2)[2]))

data["date_of_birth_year"] = dob_list
dataEasyView = data[["date_of_birth", "date_of_birth_year"]]

len(dataEasyView) #3,20,803
(dataEasyView['date_of_birth_year']).isna().sum() #3371
#=============================================================================    
#%%%

os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/Code")
exec(open('Getting cleaned year of qualification and age of completion of degrees.py').read())


#=============================================================================
#%%% #get cleaned year of qualification: for ug degree

ug_degree_year_list = list()

#ug_year
count = 0
for degree_ug, qualmain_date, deg_mapfrom, addn1_date, addn2_date, addn3_date in zip(list(data['ug_degree']),
                                                  list(data['qual_year_main']), 
                                                  list(data['ugdeg_mapfrom']), 
                                                  list(data['qual_year_addtional_1']),
                                                  list(data['qual_year_addtional_2']),
                                                  list(data['qual_year_addtional_3'])):

    if deg_mapfrom == 0:
        ug_degree_year_list.append(qualmain_date)
    elif deg_mapfrom == 1:
        ug_degree_year_list.append(addn1_date)
    elif deg_mapfrom == 2:
        ug_degree_year_list.append(addn2_date)
    elif deg_mapfrom == 3:
        ug_degree_year_list.append(addn3_date)
    else:
        ug_degree_year_list.append(np.nan)
    
data['ug_degree_year'] = ug_degree_year_list
    

#=============================================================================
#%%%
#This is the old dataset. Do not go ahead with the old dataset. 
import os
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import collections
import difflib
import pickle
from collections import Counter 

#Commented to stop accidental running. 


# os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/UpdatedDataFiles")
# with open("UpdatedData2012-2018.pkl", 'rb') as f:
#     data = pickle.load(f)
    


#=============================================================================
#%%%
#getting state medical council. We only need to take all medical council as lower. 
checking_list = data["medical_council"]
cleanedSet = cleanedSet =  [y.lower() for y in set([x for x in checking_list if str(x) != 'nan'])]
print(cleanedSet)

dataEasyView = data[["medical_council", "permanent_address"]]

data['state_medical_council'] = data['medical_council'].str.lower()

data.loc[data['state_medical_council'] == 'jammu & kashmir medical council',
         'state_medical_council'] = 'jammu and kashmir medical council'
data.loc[data['state_medical_council'] == 'orissa council of medical registration', 
         'state_medical_council'] = 'orissa medical council'
data.loc[data['state_medical_council'] == 'travancore cochin medical council, trivandrum',
         'state_medical_council'] = 'kerala medical council'
data.loc[data['state_medical_council'] == 'delhi medical council',
         'state_medical_council'] = 'nct of delhi medical council'
data.loc[data['state_medical_council'] == 'himanchal pradesh medical council',
         'state_medical_council'] = 'himachal pradesh medical council'
data.loc[data['state_medical_council'] == 'chattisgarh medical council',
         'state_medical_council'] = 'chhattisgarh medical council'
data.loc[data['state_medical_council'] == 'madras medical council',
          'state_medical_council'] = 'tamil nadu medical council'
data.loc[data['state_medical_council'] == 'bombay medical council',
          'state_medical_council'] = 'maharashtra medical council'
data.loc[data['state_medical_council'] == 'hyderabad medical council',
          'state_medical_council'] = 'telangana state medical council'
data.loc[data['state_medical_council'] == 'vidharba medical council',
          'state_medical_council'] = 'maharashtra medical council'
data.loc[data['state_medical_council'] == 'mahakoshal medical council',
          'state_medical_council'] = 'madhya pradesh medical council'
data.loc[data['state_medical_council'] == 'bhopal medical council',
          'state_medical_council'] = 'madhya pradesh medical council'
data.loc[data['state_medical_council'] == 'mysore medical council',
          'state_medical_council'] = 'karnataka medical council'

# test3.loc[test3['StateName'] == 'Chattisgarh', 'StateName'] = 'CHHATTISGARH'

print(Counter(data['state_medical_council'] ))

#=============================================================================
#%%%
#Identifying prefixes:
print(set(data.state_medical_council))
#Rajasthan - wife of: W/O - many names with the type: firstname, surname
#nagaland: not done
#maniur: not done
#Medical council of india: 
#uttarakhand - nothing
dataEasyView = data[data.state_medical_council == 'medical council of india']



#%%%

#Get son/of or daugther/of for observations that have s/o and d/o
count = 0
gender_list= list()
for name in data['father_name']:
    name = str(name)
    name = name.lower()
    if re.search("s\/o", name):
        gender_list.append("male")
        count += 1
        continue
        
    elif re.search("d\/o", name):
        gender_list.append("female")
        count += 1
        continue
        
    elif re.search("\(miss\)", name):
        gender_list.append("female")
        count += 1
        continue
    
    elif re.search("w\/o", name):
        gender_list.append("female")
        count += 1
        continue
        
    else: 
        gender_list.append("not_known")

print("Num of obsernations with s/o or d/o:", count)
data["gender"] = gender_list        



#=============================================================================
#%%%

#Delete this as soon as you extract the gender data. This is only a temporary checkpoint
##so that I can run this code on another PC in the computer lab. 

# dataEasyView = data[['name', 'father_name']]

# os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/UpdatedDataFiles")
# with open('NMC name and father name data for gender scraping.pkl', 'wb') as f:
#     pickle.dump(dataEasyView, f)

#=============================================================================
#%%% #define function to remove common elements from two lists. set differnce works, but it changes order. 
#order is important for the HumanName function from nameparser to work. 

def remove_common(list1, list2):
    for i in list1[:]:
        if i in list2:
            list1.remove(i)
            
    return list1

#=============================================================================
#%%% #Get first names to extract gender by predicting.

#Try extracting first name from full name. Idea: fullname - father name = first name. 

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
        if str(name) == "nan" or str(father_name) == "nan":
            appending_list.append(np.nan)
        else: 
            appending_list.append(remove_common(name.split(" "), father_name.split(" "))) #function 
            #defined above. 

dataEasyView['name_subtraction'] = appending_list
test = dataEasyView[['name', 'father_name', 'name_subtraction']]

count = 0
for first_name in dataEasyView['name_subtraction']:
    if str(first_name) != "nan":
        if len(first_name) == 1 :
            count += 1
        
print(count)


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

name_index_df = pd.DataFrame(list(zip(one_word_name_list, index_list)), columns =['name', 'index_col']) 


#=============================================================================
#%%% using nameparser to get first names. 
first_name_subtract_list = list()

#test is a df that has the name, father name, and the subtraction of father name from name. 
for name_subtraction in list(test.name_subtraction):
    
    if str(name_subtraction) == "nan":
        first_name_subtract_list.append(np.nan)
    
    elif len(name_subtraction) == 1 and str(name_subtraction) != "nan":
        first_name_subtract_list.append(list(name_subtraction)[0])
        
    elif len(name_subtraction) != 1 and str(name_subtraction) != "nan":
        first_name_subtract_list.append(np.nan)
           
test['first_name_subtract'] = first_name_subtract_list

#I first nameparser on names only. We will later do it on substractd names to make it more accurate. 
print("nameparser-ing now")
nameparser_list = list()
for name in list(test.name):
    if str(name) != "nan":
        name = name.lower()
    nameparser_list.append(HumanName(str(name)).first)
    
probablepeople_list = list()
count = 0
for name in list(test.name):
    if str(name) != "nan":
        name = name.lower()
    try: 
        probablepeople_list.append(probablepeople.parse(str(name))[0][0])
    except:
        probablepeople_list.append(np.nan)
        count += 1
        
test['first_name_probablepeople'] = probablepeople_list
        
    
test['first_name_nameparser'] = nameparser_list
test1 = test[test.name_subtraction.str.len() == 1]
print("nameparser accuracy with name as input: ",
      len(test1[test1.first_name_subtract == test1.first_name_nameparser])/len(test1))

print("probablepeople accuracy with name as input: ",
      len(test1[test1.first_name_subtract == test1.first_name_probablepeople])/len(test1))

#what is the above print printing? 
#I first assume that observations with name subtraction == 1 has their "true" first name. 
#Then, I do nameparser on the name column, and compare accuracy with the observations where I could 
#observe their true first name. 
#This would be invalid if the nameparcer has a different probablity of predicting first name for 
#observations where name minus father name yields the first name. This does not seem very likely. 

#we only observe an accuracy rate of 64.3%. This means that only 64.3% of the nameparser first names 
#were the true first names. 

#look at observations where first name subtraction is not equal to first name by nameparser. 
test2 = test1[test1.first_name_subtract != test1.first_name_nameparser]

#=============================================================================
#%%%

#now we run nameparser on a name that has the name_subtraction elements. 
#for this, we first convert name_subtraction into a sentence. 
def sentence_from_list(lst):
    sentence = ""
    if str(lst) == "nan":
        sentence = ""
        
    else:
        for word in lst:
            sentence = sentence + " " + word
     
    return sentence.strip()
       
test['first_name_cleaned'] = test['name_subtraction'].map(sentence_from_list)

print("nameparser-ing now")
nameparser_list = list()
for name in list(test.first_name_cleaned):
    if str(name) != "nan":
        name = name.lower()
    nameparser_list.append(HumanName(str(name)).first)
    
test['first_name_cleaned_nameparser'] = nameparser_list
test1 = test[test.name_subtraction.str.len() == 1]
print("nameparser accuracy with cleaned name as input: ",
      len(test1[test1.first_name_subtract == test1.first_name_cleaned_nameparser])/len(test1))

#What are we doing above? 
#I basically run the nameparser on the subtracted names: this is because the nameparsor was wronly 
#attributing the first name to the fathers name, which is not what we want. 

#=============================================================================
#%%%

#use indian gender names library to predict gender. 
print("indian gender name library prediction")
gender_predict_lib_list = list()
i = IndianGenderPredictor()

test1 = test[test.name_subtraction.str.len() == 1]

for name in list(test1.name_subtraction):
    if str(name) != "nan":
        name = name[0].lower()
        gender_predict_lib_list.append(i.predict(name = name))
    else:
        gender_predict_lib_list.append(np.nan)

test1['gender_lib_predict'] = gender_predict_lib_list

test1['gender_lib_predict'].describe()
test1.groupby('gender_lib_predict')['gender_lib_predict'].count()

#%%%
            
#Gender wise analysis (after getting gender data from website)
os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/NMC_Yearwise_Scrapped_Data")

with open("GenderData_1957-2018.pkl", 'rb') as f:
    gender_website_data = pickle.load(f)
    

appending_df = pd.DataFrame()

for df in gender_website_data:
    appending_df = pd.concat([appending_df, df], axis = 0)    

appending_df.columns = ['name', 'predicted_gender', 'probabilty_gender']
appending_df.drop_duplicates(inplace = True)
appending_df.reset_index(inplace = True)

#Run above code block before merging this. 
result_df = pd.merge(name_index_df, appending_df, how = "inner", on = 'name')

dataEasyView = data
dataEasyView['index_col'] = data.index

dataEasyView = pd.merge(dataEasyView, result_df, how = "left", on = "index_col")
dataEasyView['gender'] = dataEasyView['gender'].str.lower()
dataEasyView['predicted_gender'] = dataEasyView['predicted_gender'].str.lower()

dataEasyView.groupby(["medical_council", "gender"])['gender'].count()

dataEasyView.groupby(["medical_council", "predicted_gender"])['predicted_gender'].count()
data = dataEasyView

data = data.replace(to_replace = "boy", value = "male")
data = data.replace(to_replace = "girl", value = "female")

#=============================================================================
#%%%
#Pin code in address
count = 0
pincode_list = list()
pincode_available_list = list()
for address in data['permanent_address']:
    address = str(address)
    
    if re.search("\d{6}", address):
        pincode = int(re.search("\d{6}", address).group(0))
        pincode_list.append(pincode)
        pincode_available_list.append('available')
        count += 1
        
    else: 
        pincode_list.append('not available')
        pincode_available_list.append("not_available")
        
print(count)

data["pincode"] = pincode_list
data['pincode_availability'] = pincode_available_list

#=============================================================================
#%%%

#This section is done. Do not run it again. 

#Fuzzy matching districts. 

#first see how many duplicate permanent addresses. 
# dataEasyView = data[data.duplicated('permanent_address', keep = False)]
# print(len(dataEasyView))


# #importing census district level 
# os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/NMC_Yearwise_Scrapped_Data")
# census2011 = pd.read_csv("india-districts-census-2011.csv")
# census2011['State name'] = census2011['State name'].str.lower()
# census2011['District name'] = census2011['District name'].str.lower()

# print(set(census2011['State name']))

# #fuzzy match state medical councils with state names in census. 
# predicted_state_list = list()
# state_medical_council_list = list(set(data['state_medical_council']))
# for state_medical_council in state_medical_council_list:
#     temp = 0
    
#     if str(state_medical_council) == 'nan':
#         predicted_state_list.append(np.nan)
#         continue
    
#     state_medical_council = re.sub("medical council", "", state_medical_council)
    
#     for state_census in set(census2011['State name']):
#         fuzz_ratio = fuzz.ratio(state_medical_council, state_census)
        
#         if fuzz_ratio > temp:
#             temp = fuzz_ratio
            
#             predicted_state = state_census
        
#     predicted_state_list.append(predicted_state)
    
# dataEasyView = pd.DataFrame(list(zip(state_medical_council_list, predicted_state_list)),
#              columns =['state_medical_council', 'state_of_state_medical_council']) 

# dataEasyView['state_of_state_medical_council'].loc[dataEasyView.state_medical_council == 'telangana state medical council'] = 'andhra pradesh'
# dataEasyView['state_of_state_medical_council'].loc[dataEasyView.state_medical_council == 'medical council of india'] = 'not a state'

# # data = pd.merge(data, dataEasyView, on = 'state_medical_council', how = 'inner')

# #first find district from fuzzy match. Then match with pincode. 

# word_list_match_list = list()
# word_list_match_list_2 = list()

# state_district_match_list = list()
# country_district_match_list = list()

# fuzz_ratio_state_list = list()
# fuzz_ratio_country_list = list()

# permanent_address_loop_list = list()

# count = 1

# master_df = pd.DataFrame(data.groupby(['state_medical_council', 
#                                   'state_of_state_medical_council'])['state_of_state_medical_council'].count())
# master_df.columns = ['count']
# master_df.reset_index(inplace = True)

# data.sort_values(by = 'state_medical_council', inplace = True)
# master_df.sort_values(by = 'state_medical_council', inplace = True)

# print(time.ctime())
# for state_medical_council, state_census in zip(master_df['state_medical_council'], master_df['state_of_state_medical_council']):
    
#     df_nmc_smc = data[data.state_medical_council == state_medical_council]
#     df_census2011 = census2011[census2011['State name'] == state_census]
#     print(state_medical_council, len(df_nmc_smc), state_census, len(df_census2011))
    
#     for perm_add in df_nmc_smc['permanent_address']:
        
#         permanent_address_loop_list.append(perm_add)

#         if str(perm_add) == 'nan':
#             continue
        
#         #for specific state
#         max_element_list = list()
#         max_element_index_list = list()
        
#         #for whole country
#         max_element_list_2 = list()
#         max_element_index_list_2 = list()

#         perm_add = re.sub("\-", " ", perm_add)
#         perm_add = re.sub("\.", " ", perm_add)
#         perm_add = re.sub("\;", " ", perm_add)
#         perm_add = re.sub("\,", " ", perm_add)
#         perm_add = re.sub("\:", " ", perm_add)

#         word_list = [word.lower() for word in perm_add.split()]
        
#         if len(word_list) == 0:
#             word_list = ['abcdef']
#         #first try with state of the state medical council. 
        
#         # if state_medical_council == 'medical council of india':
            
#         for census_dist in df_census2011['District name']:
            
#             def fuzzy_ratio(word):
#                 return fuzz.ratio(census_dist, word)
            
#             output_list = list(map(fuzzy_ratio, word_list))
            
#             #max element - given a census district and a permanent address, how muh was the highest fuzzy
#             #match from words in the permanent address. This is a fuzzy match number. 
#             max_element_list.append(np.max(output_list))
            
#             #what was the index of that max element? This will allow us to find the word the district matched to.
#             max_element_index_list.append(output_list.index(np.max(output_list)))
            
#             #for a given district if we find a word with fuzzy match 100, then stop this loop. That is the 
#             #district we want. 
#             if np.max(output_list) == 100:
#                 break
            
#         if state_medical_council != 'medical council of india': 
#             #fuzzy match ratio:
#             fuzz_ratio_state_list.append(np.max(max_element_list))
#             #above, we take the max of the max element list. This allows us to get the highest match from the list
#             #of district wise highest matches. Note that this is all for one permanent address. 
            
#             #index of max element from max element list  
#             index_max_element = max_element_list.index(np.max(max_element_list))
        
#             #get word from word list that was matched with district
#             word_list_match = word_list[max_element_index_list[index_max_element]]
        
#             #get district that was matched. 
#             state_district_match = list(df_census2011['District name'])[index_max_element]
            
#             word_list_match_list.append(word_list_match)
#             state_district_match_list.append(state_district_match)
        
#         else: #append np.nan to each row if we are doing medical council of india. 
#             #fuzzy match ratio:
#             fuzz_ratio_state_list.append(np.nan)
#             #above, we take the max of the max element list. This allows us to get the highest match from the list
#             #of district wise highest matches. Note that this is all for one permanent address. 
            
#             #index of max element from max element list  
#             # index_max_element = max_element_list.index(np.max(max_element_list))
        
#             #get word from word list that was matched with district
#             # word_list_match = word_list[max_element_index_list[index_max_element]]
        
#             #get district that was matched. 
#             # state_district_match = list(df_census2011['District name'])[index_max_element]
            
#             word_list_match_list.append(np.nan)
#             state_district_match_list.append(np.nan)
        
#         #now, for all districts in India, fuzzy find. 
#         for census_dist in census2011['District name']:
            
#             def fuzzy_ratio(word):
#                 return fuzz.ratio(census_dist, word)
            
#             output_list_2 = list(map(fuzzy_ratio, word_list))
            
#             max_element_list_2.append(np.max(output_list_2))
#             max_element_index_list_2.append(output_list_2.index(np.max(output_list_2)))
            
#             if np.max(output_list_2) == 100:
#                 break
            
            
#         #fuzzy match ratio:
#         fuzz_ratio_country_list.append(np.max(max_element_list_2))
        
#         #index of max element from max element list  
#         index_max_element_2 = max_element_list_2.index(np.max(max_element_list_2))
    
#         #get word from word list that was matched with district
#         word_list_match_2 = word_list[max_element_index_list_2[index_max_element_2]]
    
#         #get district that was matched. 
#         country_district_match = list(census2011['District name'])[index_max_element_2]
        
#         word_list_match_list_2.append(word_list_match_2)
#         country_district_match_list.append(country_district_match)
        
#         count += 1
#         if (count%1000) == 0:
#             print(count)
        
# country_data_add_list = list(data['permanent_address'])
# country_data_add_list = [x for x in country_data_add_list if str(x) != 'nan']

# dataEasyView = pd.DataFrame(list(zip(country_data_add_list, 
#                                      word_list_match_list, 
#                                      state_district_match_list,
#                                      fuzz_ratio_state_list, 
#                                      word_list_match_list_2,
#                                      country_district_match_list, 
#                                      fuzz_ratio_country_list)),
#                             columns =['permanent_address',
#                                       'perm_add_dist', 
#                                       'smc_identified_dist',
#                                       'fuzz_ratio_state',
#                                       'perm_add_dist_country_match', 
#                                       'country_dist', 
#                                       'fuzz_ratio_country'])


# print(len(dataEasyView[dataEasyView.fuzz_ratio_state == 100]))
# print(len(dataEasyView[dataEasyView.fuzz_ratio_country == 100]))

# dataEasyView.drop_duplicates(['permanent_address'], inplace = True)
# dataEasyView.to_csv("nmc_permadd_district_fuzzy_match.csv")

# #now read the above to_csv'd file again to merge: 
    

# data = pd.merge(data, dataEasyView, on = 'permanent_address', how = 'left')

# print('done')
# # test1 = test.iloc[:1000]
# test2 = test1[test1.duplicated()]
# test3 = test.drop_duplicates('permanent_address')



# test.groupby('state_medical_council')['fuzz_ratio_state'].mean()
#%%%

#above code was run, and districts were mathed. We call the dataframe here: 
os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/NMC_Yearwise_Scrapped_Data")
dataEasyView = pd.read_csv("nmc_permadd_district_fuzzy_match.csv")

data = pd.merge(data, dataEasyView, on = 'permanent_address', how = 'left')


#%%%
#Number of observations where fuzz ratio match is 100 or pincode is available
test = ((data[(data.fuzz_ratio_state == 100) | (data.fuzz_ratio_country == 100) | (data.pincode_availability == 'available')]))

data['dist_available'] = 0
data.loc[data.fuzz_ratio_state == 100, 'dist_available'] = 1
data.loc[data.fuzz_ratio_country == 100, 'dist_available'] = 1
data.loc[data.pincode_availability == 'available', 'dist_available'] = 1

data.groupby('state_medical_council')['dist_available'].mean()


#=============================================================================
#%%%

#Pincode merging
data.pincode
dataEasyView = data

os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry")
pincode_registry = pd.read_csv("Pincode Directory.csv", encoding = "latin1")
pincode_registry.rename(columns = {'Pincode': 'pincode'}, inplace = True)

test = pd.merge(dataEasyView, pincode_registry, how = 'left', on = 'pincode')
test.drop_duplicates(subset = ['name_x', 'father_name', 'date_of_birth', 
                                          'year_of_info', 'registration_number', 
                                          'date_of_registration'], inplace = True)

len(test) - sum(test.duplicated(subset = ['name_x', 'father_name', 'date_of_birth', 
                                          'year_of_info', 'registration_number', 
                                          'date_of_registration']))

data = test    

dataEasyView = data.groupby("pincode_availability")

#=============================================================================
#%%%

#Here lay the massive code to get specialisation names. I have now saved the code
#in a seperate file, and that seprate file is run by the code below. 

#=============================================================================
#%%%
#Running Specialisations file.

#nothing being added to the dataset yet - no new columns created. 
os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/Code")
exec(open('Getting NMC Specialisations Code.py').read())


#=============================================================================
#%%% Government or private. Match MBBS university list to universities in data. 

# mbbs_universities_data = pd.read_csv("MBBS College List.csv")    

# mbbs_uni_master = mbbs_universities_data['University Name']
# mbbs_uni_master = [x.lower() for x in mbbs_uni_master]

# dataEasyView = data[data.year_of_info == 2015]
# mbbs_uni_data = dataEasyView['university_qualification_main']

# def common_members(a,b):
#     a_set = set(a)
#     b_set = set(b)
    
#     if a_set & b_set:
#         print(a_set & b_set)
        
#     else:
#         print("no common elements")

# cleanedSet = set(mbbs_uni_data)
# for uni in cleanedSet:
#     try:
#         uni = uni.lower()
#         if re.search("^u\.", uni):
#             pass
#             # print(uni)
#     except: 
#         print("non str uni:", uni)

# cleaned_uni_name_list = list()
# for uni in cleanedSet:
#     print(uni)
#     uni_name_input = input("Enter Uni Name: ")
#     try:
#         if int(uni_name_input) == 000:
#             break
#     except:
#         cleaned_uni_name_list.append(uni_name_input)
#         if str(uni_name_input).lower() in mbbs_uni_master:
#             print("yes")
#         else:
#             print("no")
    


#============================================================================
#%%%
#Run course sequences file. 

#currently we are not adding this to the data, so no need to run this while creating the 
#merged final data file. 
            
os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/Code")
exec(open('Getting NMC Course Sequences.py').read())

#=============================================================================
#%%% Getting gender division

os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/Code")
exec(open('Getting Quality of NMC Gender Predictions.py').read())

#=============================================================================
#%%%

#This section cannot run now. We have made the necceasry changes, and re-running
#this section will cause errors. TO accidently stop this code from running, it has been
#converted to comments. 

#87 districts are yet to be merged. This section will be reopned when time comes. 

#Update 24-11-22: Section closed. No longer do we need this while creating our data. 

# import numpy as np
# from fuzzywuzzy import fuzz

# #merging data with census district level demographic data
# os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/Other Data for Merging")
# census2011 = pd.read_csv("india-districts-census-2011.csv")

# census2011['District name'] = census2011['District name'].str.lower()
 
# #District is in pincode dir, and District name is in Census 2011
# data['District'] = data['District'].str.lower()

# test = pd.merge(data, census2011, how = 'left', left_on = 'District', right_on = 'District name')
# test2 = test[['District', 'District name']]

# test1 = test[test['District'] == test['District name']]
# test1 = test1[['District', 'District name']]
test = data


test3 = test[(test['final_district'].notnull()) & (test['District name'].isnull())]
test3 = test3[['StateName', 'State name', 'final_district', 'District name']]
test3 = test3.drop_duplicates('final_district')
# print(set(test3.District))
# print(len(set(test3.District)))


# print(set(census2011['State name']))

# test3.loc[test3['StateName'] == 'Chattisgarh', 'StateName'] = 'CHHATTISGARH'
# test3.loc[test3['StateName'] == 'Andaman and Nico.In.', 'StateName'] = 'ANDAMAN AND NICOBAR ISLANDS'
# test3.loc[test3['StateName'] == 'Telangana', 'StateName'] = ''
# test3.loc[test3['StateName'] == 'Megalaya', 'StateName'] = 'MEGHALAYA'
# test3.loc[test3['StateName'] == '', 'StateName'] = ''


# for state in list(set(test3['StateName'])):
#     print(state, len(census2011[census2011['State name'].str.lower() == state.lower()]))



# #find closest match from Census2011 for each unmatched district in the merge above. 
# final_dist_name_list = list()
# for district, state in zip(test3['District'], test3['StateName']):  
                                               
#     temp = 0
#     for census_dist in census2011['District name']:
        
#         fuzz_ratio = fuzz.ratio(district, census_dist)
        
#         if fuzz_ratio > temp:
            
#             final_dist_name = census_dist
#             temp = fuzz_ratio

#     final_dist_name_list.append(final_dist_name)
    
# test3['fuzzymatch_dist'] = final_dist_name_list

# test3['correct_fuzz'] = 0

# x = int(input('name?'))

# for district, fuzzymatch_dist, index in zip(test3['District'], 
#                                             test3['fuzzymatch_dist'],
#                                             list(test3.index)):
#     if index > 29746:
#         print(district, fuzzymatch_dist)
#         correct = input("correct? 1 if yes, 0 if no")
#         test3.loc[test3['District'] == district, 'correct_fuzz'] = int(correct)

#%%%

#Look at predictions and save them. 

# test4 = test3[test3.correct_fuzz == 0]
# test5 = test3[test3.correct_fuzz == 1]

# test4.to_csv('incorrect_fuzz_matched_districts.csv')
# test5.to_csv('correct_fuzz_matched_districts.csv')

#%%%

#making clean census2011 district column. 

census2011['District name'] = census2011['District name'].str.lower()
census2011['State name'] = census2011['State name'].str.lower()
test4 = pd.read_csv('incorrect_fuzz_matched_districts.csv')
test5 = pd.read_csv('correct_fuzz_matched_districts.csv')

test5 = test5[test5.fuzzymatch_dist != 'kurnool']

    
for district, fuzzy_match_dist in zip(test5['District'], test5['fuzzymatch_dist']):
    data.loc[data['District'] == district, 'District'] = fuzzy_match_dist
print('test5 fuzz match over')

test4.sort_values('District', inplace = True)
distchangecensus2011 = {'Sri Potti Sriramulu Nellore': 'nellore',
                        'Y.S.R.': 'kadapa',
                        'Sivasagar': 'sibsagar',
                        'Dima Hasao': 'dima hasso - north cachar hill',
                        'Central': 'central delhi',
                        'South West': 'south west delhi',
                        'South': 'south delhi',
                        'West': 'west delhi',
                        'East': 'east delhi',
                        'North West': 'north west delhi',
                        'North': 'north delhi',
                        'North East': 'north east delhi',
                        'Dohad': 'dahod',
                        'ahmedabad city': 'ahmadabad',
                        'Leh(Ladakh)': 'leh',
                        'Purbi Singhbhum': 'east singhbhum',
                        'Pashchimi Singhbhum': 'west singhbhum',
                        'Gulbarga': 'kalaburagi',
                        'Bangalore': 'bengaluru',
                        'Belgaum': 'belagavi',
                        'Khargone (West Nimar)': 'khargone',
                        'Khandwa (East Nimar)': 'khandwa',
                        'Bid': 'beed',
                        'Subarnapur': 'sonapur',
                        'Sahibzada Ajit Singh Nagar': 'mohali',
                        'Rupnagar': 'ropar',
                        'Dhaulpur': 'dholpur',
                        'East District': 'east sikkim',
                        'West District': 'west sikkim',
                        'South District': 'south sikkim',
                        'Thoothukkudi': 'tuticorin',
                        'West Tripura': 'agartala',
                        'Mahamaya Nagar': 'hathras',
                        'Jyotiba Phule Nagar': 'amroha',
                        'Garhwal': 'pauri garhwal',
                        'Maldah': 'malda',
                        'Paschim Medinipur': 'west midnapore',
                        'Purba Medinipur': 'east midnapore',
                        'Dakshin Dinajpur': 'south dinajpur',
                        'Uttar Dinajpur': 'north dinajpur',
                        'Central': 'central delhi',  
                        'East District': 'east sikkim',
                        'North  District': 'north sikkim'}

for key in distchangecensus2011:
    print(key, ",", distchangecensus2011[key])
    census2011.loc[census2011['District name'] == key.lower(), 'District name'] = distchangecensus2011[key]

#districts in pincode dir and thus main data that need to be changed because these are
#new districts formed after census 2011. 
distchange_in_data = {'hindupur': 'ananthapur', 
                  'kovvur': 'nellore', 
                  'surajpur': 'surguja', 
                  'bemetara': 'durg',
                  'balod': 'durg',
                  'ahmedabad city': 'ahmadabad',
                  'balod bazer': 'raipur',
                  'jagdalpur': 'bastar',
                  'kanker': 'bastar',
                  'mungeli': 'bilaspur', 
                  'gariaband': 'raipur', 
                  'kawardha': 'kabeerdham', 
                  'dantewada': 'dakshin bastar dantewada',
                  'aravalli': 'sabar kantha',
                  'gir somnath': 'junagadh', 
                  'chhotaudepur': 'rajkot',
                  'devbhoomi dwerka': 'jamnagar',
                  'athani': 'belagavi',
                  'bailhongal': 'belagavi',
                  'hubballi': 'dharwad', 
                  'agar malwa': 'shajapur', 
                  'palghar': 'Thane',
                  'malegaon': 'Nashik', 
                  'fazilka': 'Firozpur', 
                  'nawanshahr': 'Shahid Bhagat Singh Nagar', 
                  'pathankot': 'Gurdaspur',
                  'hapur': 'ghaziabad',
                  'West Tripura': 'agartala', 
                  'bangalore': 'bengaluru', 
                  'lahul  spiti': 'lahul and spiti', 
                  'tura': 'west garo hills', 
                  'rupnagar': 'ropar'}

for key in distchange_in_data:
    print(key, ",", distchange_in_data[key])
    data.loc[data['District'] == key.lower(), 'District'] = distchange_in_data[key]
    
#change fuzzy matched census district names
data['smc_identified_dist_clean'] = data['smc_identified_dist']
data['country_dist_clean'] = data['country_dist']

for key in distchangecensus2011:
    print(key, ",", distchangecensus2011[key])
    data.loc[data['smc_identified_dist'] == key.lower(), 'smc_identified_dist_clean'] = distchangecensus2011[key]
    data.loc[data['country_dist'] == key.lower(), 'country_dist_clean'] = distchangecensus2011[key]
 
    

#%%%

#final district name to be merged on columns
data['final_district'] = ''

df1 = data[data.pincode_availability == "available"]
df1['final_district'] = df1['District']

df2 = data[(data.pincode_availability == 'not_available') & (data.fuzz_ratio_state == 100) &
           (data.fuzz_ratio_country != 100)]
df2['final_district'] = df2['smc_identified_dist_clean']

df3 = data[(data.pincode_availability == 'not_available') & 
           (data.fuzz_ratio_country == 100) &
           (data.fuzz_ratio_state != 100)]
df3['final_district'] = df3['country_dist_clean']

df4 = data[(data.pincode_availability == 'not_available') & 
           (data.fuzz_ratio_country == 100) &
           (data.fuzz_ratio_state == 100)]
df4['final_district'] = df4['smc_identified_dist_clean']

df5 = data[(data.pincode_availability == 'not_available') & 
           (data.fuzz_ratio_country != 100) &
           (data.fuzz_ratio_state != 100)]
df5['final_district'] = 'unknown'

df = pd.concat([df1, df2], axis = 0)
df = pd.concat([df, df3], axis = 0)
df = pd.concat([df, df4], axis = 0)
df = pd.concat([df, df5], axis = 0)

data = df



# test1 = data[data.final_district == '']
    
#%%% Manuallay cleaning this stupid ass ddata



#%%%
#Merge districts by name, after cleaning district names above. 

#around 95 districts still remain to be merged. It will happen soon. 

# #District is in pincode dir, and District name is in Census 2011
data['District'] = data['District'].str.lower()
data['final_district'] = data['final_district'].str.lower()

census2011['District name'] = census2011['District name'].str.lower()

data = pd.merge(data, census2011, how = 'left', left_on = 'final_district', right_on = 'District name')

data = (test.drop_duplicates(subset = ['name_x', 'father_name', 'date_of_birth', 
                                          'year_of_info', 'registration_number', 
                                          'date_of_registration', 'permanent_address']))


#%%%

#Make census state population column. 

#we need to aggregate information state wise from the census 2011 data. 
#For all columns, we need to create new variables. See on how to create variabels by loops below. 
# for x in range(0, 9):
#     globals()['list%s' % x] = list()

# #Read census data
# os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/Other Data for Merging")
# census2011 = pd.read_csv("india-districts-census-2011.csv")
# census2011['District name'] = census2011['District name'].str.lower()
# census2011['State name'] = census2011['State name'].str.lower()

# for var in list(census2011.columns)[3:]:
#     df = pd.DataFrame(census2011.groupby('State name')[var].sum())
#     df.columns = ['state_' + str(df.columns[0])]
#     df.reset_index(drop = False, inplace = True)
    
#     census2011 = pd.merge(census2011, df, on = 'State name')
    
# os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/Other Data for Merging")
# census2011.to_csv('census2011_with_state_numbers.csv')



#%%%
#Read data for 2012-2018 with age and date of birth calculated. This was done because
#the code took waaay too much time to run for the above block. Note that this block will
#have to be updated as and when I update my data by including more years. 

# os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/UpdatedDataFiles")
# with open('UpdatedData2012-2018.pkl', 'wb') as f:
#     pickle.dump(data, f)


#Un-comment and run code below to avoid accidently saving data that was being prepred midway. 
#there is a copy file saved too, incaes we accidentaly dump data that was not fully prepared. 

# os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/UpdatedDataFiles")
# with open('UpdatedData_2_2012-2018.pkl', 'wb') as f:
#     pickle.dump(data, f)


    
#%%%
    
#Remove outliers from data - age of qualification of degree. 
test = data

qualification_number_list = ['age_qualification_main',
                        'age_qualification_addtional_1',
                        'age_qualification_addtional_2',
                        'age_qualification_addtional_3']

# for qualification_number in qualification_number_list:
test = test.loc[(test.age_qualification_main >= 17) | (test['age_qualification_main'].isnull())]
test = test.loc[(test.age_qualification_main <= 50) | (test['age_qualification_main'].isnull())]

test = test.loc[(test.age_qualification_addtional_1 >= 17) | (test['age_qualification_addtional_1'].isnull())]
test = test.loc[(test.age_qualification_addtional_1 <= 50) | (test['age_qualification_addtional_1'].isnull())]

test = test.loc[(test.age_qualification_addtional_2 >= 17) | (test['age_qualification_addtional_2'].isnull())]
test = test.loc[(test.age_qualification_addtional_2 <= 80) | (test['age_qualification_addtional_2'].isnull())]

test = test.loc[(test.age_qualification_addtional_3 >= 17) | (test['age_qualification_addtional_3'].isnull())]
test = test.loc[(test.age_qualification_addtional_3 <= 80) | (test['age_qualification_addtional_3'].isnull())]

data = test

#%%%


os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/UpdatedDataFiles")
data.to_csv('NMC_PG_Specialization_data.csv')
    
#%%%

