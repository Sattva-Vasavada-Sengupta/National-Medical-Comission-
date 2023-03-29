import os
import pandas as pd
import pickle  

from collections import Counter 

os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/UpdatedDataFiles")
with open("UpdatedData_3_2012-2018.pkl", 'rb') as f:
    data = pickle.load(f)
    
#%%% #Number of records degree wise

lst1 = list(data['qualmain_main'])
lst2 = list(data['addnQual1_main'])
lst3 = list(data['addnQual2_main'])
lst4 = list(data['addnQual3_main'])

lst = lst1 + lst2 + lst3 + lst4

df = pd.DataFrame(dict(Counter(lst)).items())
df.columns = ['degree', 'count']
df = df.sort_values(by = 'count', ascending = False)
df.reset_index(drop = True, inplace = True)

df = df.loc[df.degree != 'None']

# os.chdir("C:/Users/savas/Documents/Ashoka/Courses/Health Economics/Health Econ_Course Research/Medical Education in India/Medical Education - Tables Repo")
# df.to_csv("count of records degree wise.csv")

#%%% #predicted gender wise differnece in degrees

dataEasyView = data.dropna(subset = ['predicted_gender'])

df1 = dataEasyView[['qualmain_main', 'predicted_gender']]
df1.columns = ['qualification', 'predicted_gender']

df2 = dataEasyView[['addnQual1_main', 'predicted_gender']]
df2.columns = ['qualification', 'predicted_gender']

df3 = dataEasyView[['addnQual2_main', 'predicted_gender']]
df3.columns = ['qualification', 'predicted_gender']

df4 = dataEasyView[['addnQual3_main', 'predicted_gender']]
df4.columns = ['qualification', 'predicted_gender']

df = df1.append(df2)
df = df.append(df3)
df = df.append(df4)

df.groupby(['qualification', 'predicted_gender'])['predicted_gender'].count()


#%%% #Number of records year wise and degree wise. 

df1 = data[['qualmain_main', 'qual_year_main']]
df1.columns = ['qualification', 'year']

df2 = data[['addnQual1_main', 'qual_year_addtional_1']]
df2.columns = ['qualification', 'year']

df3 = data[['addnQual2_main', 'qual_year_addtional_2']]
df3.columns = ['qualification', 'year']

df4 = data[['addnQual3_main', 'qual_year_addtional_3']]
df4.columns = ['qualification', 'year']

df = pd.DataFrame()

df = pd.concat([df, df1], axis = 0)
df = pd.concat([df, df2], axis = 0)
df = pd.concat([df, df3], axis = 0)
df = pd.concat([df, df4], axis = 0)

df = pd.DataFrame(df.groupby(['year', 'qualification'])['qualification'].count())
df.columns = ['count']
df.reset_index(inplace = True)

df = pd.pivot_table(df, index = 'year', 
               columns = 'qualification', aggfunc = sum, fill_value = 0)
df.columns = df.columns.get_level_values(1)

df = df[['MBBS', 'MD', 'MS', 'DNB', 'Diploma', 'MCH']]
df = df[(df.index > 2005) & (df.index < 2019)]

os.chdir("C:/Users/savas/Documents/Ashoka/Courses/Health Economics/Health Econ_Course Research/Medical Education in India/Medical Education - Tables Repo")
df.to_csv('count of records by year and qualification.csv')


#%%% #Numeber of records by State Medical Council 



df = pd.DataFrame(dict(Counter(data['state_medical_council'])).items())
df.columns = ['state medical council', 'count']
df = df.sort_values(by = 'count', ascending = False)

os.chdir("C:/Users/savas/Documents/Ashoka/Courses/Health Economics/Health Econ_Course Research/Medical Education in India/Medical Education - Tables Repo")
df.to_csv('count of records by state medical council.csv')

#%%% #Number of records by state medical council and degree wise


df1 = data[['qualmain_main', 'state_medical_council']]
df1.columns = ['qualification', 'state_medical_council']

df2 = data[['addnQual1_main', 'state_medical_council']]
df2.columns = ['qualification', 'state_medical_council']

df3 = data[['addnQual2_main', 'state_medical_council']]
df3.columns = ['qualification', 'state_medical_council']

df4 = data[['addnQual3_main', 'state_medical_council']]
df4.columns = ['qualification', 'state_medical_council']

df = pd.DataFrame()

df = pd.concat([df, df1], axis = 0)
df = pd.concat([df, df2], axis = 0)
df = pd.concat([df, df3], axis = 0)
df = pd.concat([df, df4], axis = 0)

df = pd.DataFrame(df.groupby(['state_medical_council', 'qualification'])['qualification'].count())
df.columns = ['count']
df.reset_index(inplace = True)

df = pd.pivot_table(df, index = 'state_medical_council', 
               columns = 'qualification', aggfunc = sum, fill_value = 0)
df.columns = df.columns.get_level_values(1)

df = df[['MBBS', 'MD', 'MS', 'DNB', 'Diploma', 'MCH']]

os.chdir("C:/Users/savas/Documents/Ashoka/Courses/Health Economics/Health Econ_Course Research/Medical Education in India/Medical Education - Tables Repo")
df.to_csv('count of records by state medical council and qualification.csv')


from fuzzywuzzy import fuzz

os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/Other Data for Merging")
census2011st = pd.read_csv('census2011_with_state_numbers.csv')

df.reset_index(drop = False, inplace = True)

#match above df with census state names. 
# fuzz_state_match_list = list()
# for state in df['state_medical_council']:
#     temp = 0
#     for state_census in census2011st['State name']:
#         fuzz_ratio = fuzz.ratio(state, state_census)
#         if fuzz_ratio > temp:
#             fuzz_state_match = state_census
#             temp = fuzz_ratio
            
#     fuzz_state_match_list.append(fuzz_state_match)
    
# df['census_state_names_match'] = fuzz_state_match_list


df.loc[df['state_medical_council'] == 'jammu & kashmir medical council',
         'state_medical_council'] = 'jammu and kashmir medical council'
df.loc[df['state_medical_council'] == 'orissa council of medical registration', 
         'state_medical_council'] = 'orissa medical council'
df.loc[df['state_medical_council'] == 'travancore cochin medical council, trivandrum',
         'state_medical_council'] = 'kerala medical council'
df.loc[df['state_medical_council'] == 'delhi medical council',
         'state_medical_council'] = 'nct of delhi medical council'
df.loc[df['state_medical_council'] == 'himanchal pradesh medical council',
         'state_medical_council'] = 'himachal pradesh medical council'
df.loc[df['state_medical_council'] == 'chattisgarh medical council',
         'state_medical_council'] = 'chhattisgarh medical council'

df['state_ext_medical_council'] = df['state_medical_council'].str.replace(' medical council', '')

df1 = pd.merge(df, census2011st, how = 'inner', left_on = 'state_ext_medical_council', 
              right_on = 'State name')

df1.drop_duplicates('state_medical_council', inplace = True)

df1 = df1[['state_medical_council', 'state_ext_medical_council', 'MBBS', 'MD', 'MS', 'DNB', 'Diploma', 'MCH', 
            'state_Population', 'state_Literate']]

df1['mbbs_pc'] = (df1['MBBS'] / df1['state_Population']) * 1000
df1['md_pc'] = (df1['MD'] / df1['state_Population']) * 1000
df1['ms_pc'] = (df1['MS'] / df1['state_Population']) * 1000
df1['dnb_pc'] = (df1['DNB'] / df1['state_Population']) * 1000
df1['diploma_pc'] = (df1['Diploma'] / df1['state_Population']) * 1000
df1['mch_pc'] = (df1['MCH'] / df1['state_Population']) * 1000

df1['post_grad_pc'] = df1['md_pc'] + df1['ms_pc'] + df1['dnb_pc'] + df1['diploma_pc'] + df1['mch_pc']


df2 = df1[['mbbs_pc', 'md_pc', 'ms_pc', 'dnb_pc', 'diploma_pc', 'mch_pc', 
     'post_grad_pc']].describe()

os.chdir("C:/Users/savas/Documents/Ashoka/Courses/Health Economics/Health Econ_Course Research/Medical Education in India/Medical Education - Tables Repo")
df2.to_csv('per-capita_registered doctors by degree.csv')

#%%% #Average age of completion of degrees

df1 = data[['qualmain_main', 'age_qualification_main']]
df1.columns = ['qualification', 'age at qualification']

df2 = data[['addnQual1_main', 'age_qualification_addtional_1']]
df2.columns = ['qualification', 'age at qualification']

df3 = data[['addnQual2_main', 'age_qualification_addtional_2']]
df3.columns = ['qualification', 'age at qualification']

df4 = data[['addnQual3_main', 'age_qualification_addtional_3']]
df4.columns = ['qualification', 'age at qualification']

df = pd.DataFrame()

df = pd.concat([df, df1], axis = 0)
df = pd.concat([df, df2], axis = 0)
df = pd.concat([df, df3], axis = 0)
df = pd.concat([df, df4], axis = 0)

df = pd.DataFrame(df.groupby(['qualification'])['age at qualification'].mean())
df.columns = ['age at qualification']
df.reset_index(inplace = True)

#get count of each degree so that we know how much of a possible error there can be. Large count
#implies smaller error. 
lst1 = list(data['qualmain_main'])
lst2 = list(data['addnQual1_main'])
lst3 = list(data['addnQual2_main'])
lst4 = list(data['addnQual3_main'])

lst = lst1 + lst2 + lst3 + lst4

df1 = pd.DataFrame(dict(Counter(lst)).items())
df1.columns = ['qualification', 'count']

df2 = pd.merge(df, df1, on = 'qualification')
df2 = df2.sort_values(by = 'age at qualification', ascending = True)
df2 = df2.loc[df2.qualification != 'None']
df2.reset_index(drop = True, inplace = True)

os.chdir("C:/Users/savas/Documents/Ashoka/Courses/Health Economics/Health Econ_Course Research/Medical Education in India/Medical Education - Tables Repo")
df2.to_csv('age of completion of degree.csv')

#%%%

#summary stats by degree. 

df1 = data[['qualmain_main', 'age_qualification_main']]
df1.columns = ['qualification', 'age at qualification']

df2 = data[['addnQual1_main', 'age_qualification_addtional_1']]
df2.columns = ['qualification', 'age at qualification']

df3 = data[['addnQual2_main', 'age_qualification_addtional_2']]
df3.columns = ['qualification', 'age at qualification']

df4 = data[['addnQual3_main', 'age_qualification_addtional_3']]
df4.columns = ['qualification', 'age at qualification']

df = pd.DataFrame()

df = pd.concat([df, df1], axis = 0)
df = pd.concat([df, df2], axis = 0)
df = pd.concat([df, df3], axis = 0)
df = pd.concat([df, df4], axis = 0)

df1 = pd.DataFrame(df.groupby(['qualification'])['age at qualification'].mean())
df1.reset_index(drop = False, inplace = True)
df1.columns = ['qualification', 'mean']

df2 = pd.DataFrame(df.groupby(['qualification'])['age at qualification'].std())
df2.reset_index(drop = False, inplace = True)
df2.columns = ['qualification', 'std dev']

df3 = pd.DataFrame(df.groupby(['qualification'])['age at qualification'].quantile(0.25))
df3.reset_index(drop = False, inplace = True)
df3.columns = ['qualification', '25th percentile']

df4 = pd.DataFrame(df.groupby(['qualification'])['age at qualification'].quantile(0.5))
df4.reset_index(drop = False, inplace = True)
df4.columns = ['qualification', '50th percentile']

df5 = pd.DataFrame(df.groupby(['qualification'])['age at qualification'].quantile(0.75))
df5.reset_index(drop = False, inplace = True)
df5.columns = ['qualification', '75th percentile']

df6 = pd.DataFrame(df.groupby(['qualification'])['age at qualification'].min())
df6.reset_index(drop = False, inplace = True)
df6.columns = ['qualification', 'minimum']

df7 = pd.DataFrame(df.groupby(['qualification'])['age at qualification'].max())
df7.reset_index(drop = False, inplace = True)
df7.columns = ['qualification', 'maximum']

dfs = [df1, df2, df3, df4, df5, df6, df7]

import functools as ft
df_final = ft.reduce(lambda left, right: pd.merge(left, right, on='qualification'), dfs)
df_final = df_final.sort_values(by = 'mean', ascending = True)
df_final = df_final.loc[df_final.qualification != 'None']
df_final.reset_index(drop = True, inplace = True)

os.chdir("C:/Users/savas/Documents/Ashoka/Courses/Health Economics/Health Econ_Course Research/Medical Education in India/Medical Education - Tables Repo")
df_final.to_csv('age of completion by degree summary stats.csv')



#%%% #Count of observations with son/of or daughter/of or Miss or Mrs. etc. 

df = pd.DataFrame(data.groupby(["state_medical_council", "gender"])['gender'].count())
df.columns = ['count']

df.reset_index(inplace = True)

df = df.pivot_table(index = 'state_medical_council', 
                    columns = 'gender', aggfunc= sum, fill_value=0)

df.columns = df.columns.get_level_values(1)

df.sort_values(by = 'female', inplace = True, ascending = False)

os.chdir("C:/Users/savas/Documents/Ashoka/Courses/Health Economics/Health Econ_Course Research/Medical Education in India/Medical Education - Tables Repo")
df.to_csv('count of observations with gender identification.csv')

#%%% Pincode availbility by state medical council. 

df = pd.DataFrame(data.groupby(['state_medical_council', 'pincode_availability'])['pincode_availability'].count())
df.columns = ['count']
df.reset_index(inplace = True)


df = df.pivot_table(df, index = 'state_medical_council', 
                columns = 'pincode_availability')
df.columns = df.columns.get_level_values(1)


df['pincode available %'] = (df['available'] / (df['available'] + df['not_available']))*100

df.to_csv('pincode availabiliy by state medical council.csv')

#%%% Getting quality of NMC Gender Predictions

os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/Code")
exec(open('Getting Quality of NMC Gender Predictions.py').read())

#%%% 




