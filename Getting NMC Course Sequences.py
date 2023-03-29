# Course sequence frequency: Currently Testing Phase
import re
import collections
import numpy as np
data = data

degree = "MBBS"
print(len(data[(data.qualmain_main == degree)]),
len(data[(data.addnQual1_main == degree)]),
len(data[(data.addnQual2_main == degree)]),
len(data[(data.addnQual3_main == degree)]))

# dataEasyView = data[data.year_of_info == 2015]
dataEasyView.reset_index(inplace = True, drop = True)
dataEasyView = data
loop_start = np.min(dataEasyView.index) #subsetting data to dataEasyView keeps the index, so we need to 
#find the index start and end. 
loop_end = np.max(dataEasyView.index)

count = 0
main_addn1_seq_list = list()
for i in range(loop_start, loop_end + 1):       
    # print(i)
    if str(dataEasyView['qual_year_addtional_1'][i]) == 'nan' or str(dataEasyView['qual_year_main'][i]) == 'nan': 
        main_addn1_seq_list.append('no year ' + str(dataEasyView['qualmain_main'][i] +', ' +  str(dataEasyView['addnQual1_main'][i])))
        if dataEasyView['addnQual1_main'][i] == 'MD':
           count += 1
        continue
    
    elif (dataEasyView['qual_year_addtional_1'][i] > dataEasyView['qual_year_main'][i]):
        string1 = str(dataEasyView['qualmain_main'][i])
        string2 = str(dataEasyView['addnQual1_main'][i])
        string = string1 + ', ' + string2
        main_addn1_seq_list.append(string)
        if dataEasyView['addnQual1_main'][i] == 'MD':
           count += 1
        continue
    
    elif dataEasyView['qual_year_addtional_1'][i] <= dataEasyView['qual_year_main'][i]:
        main_addn1_seq_list.append('year error')
        if dataEasyView['addnQual1_main'][i] == 'MD':
           count += 1
        continue
    
dataEasyView = pd.DataFrame(dict(collections.Counter(main_addn1_seq_list)).items())
#Check how many degrees there are:
def find_degree(degree):
    print(len(dataEasyView[dataEasyView.addnQual1_main == degree]))
find_degree("MD")
find_degree("MS")
find_degree("Diploma")
find_degree("DNB")    


dataEasyView['main_addn1_seq'] = main_addn1_seq_list
np.unique(main_addn1_seq_list)
dataEasyView.groupby(['main_addn1_seq'])['main_addn1_seq'].count()


addn1_addn2_seq_list = list()
for i in range(loop_start, loop_end + 1):        
    if str(dataEasyView['qual_year_addtional_1'][i]) == 'nan' or str(dataEasyView['qual_year_addtional_2'][i]) == 'nan': 
        addn1_addn2_seq_list.append(np.nan)
        continue
    
    elif (dataEasyView['qual_year_addtional_2'][i] > dataEasyView['qual_year_addtional_1'][i]):
        string1 = str(dataEasyView['addnQual1_main'][i])
        string2 = str(dataEasyView['addnQual2_main'][i])
        string = string1 + ', ' + string2
        addn1_addn2_seq_list.append(string)
        continue
    
    elif dataEasyView['qual_year_addtional_2'][i] <= dataEasyView['qual_year_addtional_1'][i]:
        addn1_addn2_seq_list.append('year error')
        continue

collections.Counter(addn1_addn2_seq_list)

# dataEasyView['addn1_addn2_seq'] = addn1_addn2_seq_list
# np.unique(addn1_addn2_seq_list)
# dataEasyView.groupby(['addn1_addn2_seq'])['addn1_addn2_seq'].count()



main_addn1_addn2_seq_list = list()
for i in range(loop_start, loop_end + 1):  
    string1 = str(dataEasyView['main_addn1_seq'][i])
    try:
        string2 = str(dataEasyView['addn1_addn2_seq'][i]).split(', ')[1]
        string = string1 + ', ' + string2
        main_addn1_addn2_seq_list.append(string)
    except:
        string = string1 + ', ' + string2
        main_addn1_addn2_seq_list.append(string)

collections.Counter(main_addn1_addn2_seq_list)
# dataEasyView['main_addn1_addn2_seq'] = main_addn1_addn2_seq_list
# test = dataEasyView.groupby(['main_addn1_addn2_seq'])['main_addn1_addn2_seq'].count()
### Idea list: Course sequence frequency? 

test_seq_list = list()
for i in range(loop_start, loop_end + 1):        
    string1 = str(dataEasyView['qualmain_main'][i])
    string2 = str(dataEasyView['addnQual1_main'][i])
    string3 = str(dataEasyView['addnQual2_main'][i])
    string = string1 + ', ' + string2 + ', ' + string3
    test_seq_list.append(string)

dict_course_seq = dict(collections.Counter(test_seq_list))
seq_list = list()
seq_num_list = list()
for i in dict_course_seq:
    seq_list.append(i)
    seq_num_list.append(dict_course_seq[i])
    print(i, dict_course_seq[i])

df = pd.DataFrame(list(zip(seq_list, seq_num_list)),
                columns =['course_sequence', 'number'])

df['cleaned_course_sequence'] = ''
for i in range(0, len(df)):
    if re.search("MD, None, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MD, None"
    
    elif re.search("MD, Diploma, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MD, Diploma"
        
    elif re.search("MD, MD, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MD, MD"
        
    elif re.search("MD, MS, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MD, MS"
        
    elif re.search("MD, DNB, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MD, DNB"

    elif re.search("MD, Fellow, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MD, Fellow"        

    elif re.search("Diploma, None, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, Diploma, None"  
        
    elif re.search("DNB, None, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, DNB, None"          
        
    elif re.search("MD, DM, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MD, DM"          
        
    elif re.search("None, MS, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MS, Fellow"         
        
    elif re.search("MD, None, DNB", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MD, DNB"             
        
    elif re.search("MCH, None, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MS, MCH"         
        
    elif re.search("DNB, MCH, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, DNB, MCH"  
        
    elif re.search("MS, None, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MS, None" 
        
    elif re.search("MBBS, MCH, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MS, MCH" 
        
    elif re.search("MBBS, DM, DNB", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MD, DM, DNB" 

    elif re.search("MBBS, DM, Diploma", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MD, DM, Diploma" 
        
    elif re.search("MBBS, DM, MD", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MD, DM" 
        
    elif re.search("MBBS, DM, None", df['course_sequence'][i]):
        df['cleaned_course_sequence'][i] = "MBBS, MD, DM" 
        
    else: 
        df['cleaned_course_sequence'][i] = df['course_sequence'][i]

test = pd.DataFrame(df.groupby(df['cleaned_course_sequence'])['number'].sum())
        

#Gender wise sequence
test_seq_list = list()
for i in range(loop_start, loop_end + 1):        
    string1 = str(dataEasyView['qualmain_main'][i])
    string2 = str(dataEasyView['addnQual1_main'][i])
    string3 = str(dataEasyView['addnQual2_main'][i])
    string = string1 + ', ' + string2 + ', ' + string3
    test_seq_list.append(string)
   

dataEasyView["course_sequence"] = test_seq_list 
dataEasyView = df

test = pd.DataFrame(dataEasyView[dataEasyView.state_medical_council == "bihar"].groupby(['cleaned_course_sequence', 'gender'])['cleaned_course_sequence'].count())

