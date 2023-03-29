import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir("C:/Users/savas/Documents/Ashoka/Courses/Health Economics/Health Econ_Course Research/Medical Education in India/Medical Education - Tables Repo")

data = data
#Check quality of predictions 

dataEasyView = data

num_obs_list = list()
nan_percent_list = list()
correct_pred_list = list()
correct_boy_pred_list = list()
correct_girl_pred_list = list()
count_percent_oftotal_list = list()

total_bihar_gender_count = len(dataEasyView[(dataEasyView.state_medical_council == 'bihar medical council') &
                                        (dataEasyView.gender != 'not_known')])

for cutoff in range(50, 100, 1):
    a = dataEasyView[(dataEasyView.probabilty_gender > (cutoff)/100) & (dataEasyView.state_medical_council == "bihar medical council")][["predicted_gender", "gender"]]
    print(cutoff, "Total:", len(a), ";males:", len(a[a.gender == "male"]), ";females:", len(a[a.gender == "female"]))
    
    
    count_percent_oftotal_list.append((len(a)/total_bihar_gender_count) * 100)

    num_obs_list.append(len(a))
    count = 0
    nan_count = 0
    count_boy = 0
    count_girl = 0
    for i in a.index:
        if str(a['predicted_gender'][i]) == "nan" or str(a['gender'][i]) == "not_known":
            nan_count += 1
            continue
        else:
            if str(a['predicted_gender'][i]).lower() == str(a['gender'][i]).lower():
                count += 1
                if str(a['predicted_gender'][i]).lower() == "male":
                    count_boy += 1
                if str(a['predicted_gender'][i]).lower() == "female":
                    count_girl += 1
    
    # print("% of nans: ", nan_count/len(a)*100)
    nan_percent_list.append(nan_count/len(a)*100)
    # print("% of correct gender predictions", count/len(a)*100)
    correct_pred_list.append(count/len(a)*100)

    # print("% of correct boy predictions: ", count_boy/len(a[a.gender == "boy"])*100)   
    correct_boy_pred_list.append(count_boy/len(a[a.gender == "male"])*100)
    # print("% of correct girl predictions: ", count_girl/len(a[a.gender == "girl"])*100) 
    correct_girl_pred_list.append(count_girl/len(a[a.gender == "female"])*100)
    
b = pd.DataFrame(list(zip(num_obs_list, nan_percent_list, correct_pred_list,
                           correct_boy_pred_list, correct_girl_pred_list,
                           count_percent_oftotal_list)), columns = ["num_obs",
                                                                                       "nan_percent",
                                                                                       "correct_percent",
                                                                                       "corr_boy_percent",
                                                                                      "corr_girl_percent",
                                                                                      "percent_obs_included"])

                                                                                       
index_range = list(range(50, 100, 1))
b['index_range'] = index_range
b.set_index('index_range', inplace = True)



plt.plot(b['nan_percent'], label = "nan_percent", linewidth = 2)
plt.plot(b['correct_percent'], label = "correct_percent", linewidth = 2)
plt.plot(b['corr_boy_percent'], label = "corr_boy_percent", linewidth = 2)
plt.plot(b['corr_girl_percent'], label = "corr_girl_percent", linewidth = 2)
plt.plot(b['percent_obs_included'], label = 'percent_obs_included', linewidth = 2)
plt.legend()
plt.xlabel("% cutoff for gender prediction")
plt.ylabel("% correct - ")
plt.title("Bihar")
plt.savefig('Bihar quality of gender predictions.png', bbox_inches = 'tight')
plt.show()


