# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:09:56 2022

@author: savas
"""


#Wrangle main column:
data_list = data["qualification_main"]
qual_list_to_append = list()
i = 1
for degree in list(data_list): 
        
        degree = str(degree)
        degree = degree.lower()
        
        if find_MBBS(degree) == True:
           qual_list_to_append.append("MBBS")
           pass
        
        elif find_MD(degree) == True:
           qual_list_to_append.append("MD")
           pass
        
        elif find_MS(degree) == True:
             qual_list_to_append.append("MS")
             pass
         
        elif find_diplomate_ntnl_board(degree) == True:
            qual_list_to_append.append("DNB")
            pass
        
        elif find_diploma_all(degree) == True:
             qual_list_to_append.append("Diploma")
             pass
        
        elif find_mch(degree) == True:
             qual_list_to_append.append("MCH")
             pass
        
        elif find_mrcp_mrc(degree) == True:
             qual_list_to_append.append("MRCP or MRC")
             pass
        
        elif find_fellow(degree) == True:
             qual_list_to_append.append("Fellow")
             pass
        
        elif find_public_health(degree):
             qual_list_to_append.append("Public Health")
             pass
         
        elif find_mha(degree):
            qual_list_to_append.append("MHA")
            pass
        
        elif find_lmp(degree):
            qual_list_to_append.append("LMP")
            pass
        
        elif find_lmf(degree):
            qual_list_to_append.append("LMF")
            pass
        
        elif find_lcps(degree):
            qual_list_to_append.append("LCPS")
            pass
        
        elif find_lms(degree):
            qual_list_to_append.append("LMS")
            pass
        
        elif find_lsmf(degree):
            qual_list_to_append.append("LSMF")
            pass
        
        elif find_cert_wbmf(degree):
            qual_list_to_append.append("cert_wbmf")
            pass
        
        elif find_mb(degree):
            qual_list_to_append.append("MB")
            pass
        
        elif find_lrcp(degree):
            qual_list_to_append.append("LRCP")
            pass
        
        elif find_mcps(degree):
            qual_list_to_append.append("MCPS")
            pass
        
        elif find_mmf(degree):
            qual_list_to_append.append("MMF")
            pass
        
        else: 
            qual_list_to_append.append("None")  

data["qualmain_main"] = qual_list_to_append #Add main degree columnn to dataset. 

dataEasyView = data[["qualification_main", "qualmain_main"]]