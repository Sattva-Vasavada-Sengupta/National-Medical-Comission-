data = data

for qualification_number in [1,2,3]:
    
    data_list = list(data['qualification_addtional_'+str(qualification_number)])
    addn_qual_x_list = list()
    
    for degree in data_list: 
        
        degree = str(degree)
        degree = degree.lower()
        
        if find_MBBS(degree) == True:
            addn_qual_x_list.append("MBBS")
            continue
        
        if find_MD(degree) == True:
            addn_qual_x_list.append("MD")
            continue
        
        elif find_MS(degree) == True:
            addn_qual_x_list.append("MS")
            continue
        
        elif find_diplomate_ntnl_board(degree) == True:
            addn_qual_x_list.append("DNB")
            continue             

        elif find_diploma_all(degree) == True:
            addn_qual_x_list.append("Diploma")
            continue
        
        
        elif find_DM(degree) == True:
            addn_qual_x_list.append("DM")
            continue
        
        elif find_mch(degree) == True:
            addn_qual_x_list.append("MCH")
            continue
        
        elif find_mrcp_mrc(degree) == True:
            addn_qual_x_list.append("MRCP or MRC")
            continue
        
        elif find_fellow(degree) == True:
            addn_qual_x_list.append("Fellow")
            continue
        
        elif find_public_health(degree):
            addn_qual_x_list.append("Public Health")
            continue
        
        elif find_mha(degree):
            addn_qual_x_list.append("MHA")
            
        elif find_lmp(degree) == True:
            addn_qual_x_list.append("LMP")
            continue
        
        elif find_lmf(degree) == True: 
            addn_qual_x_list.append("LMF")
            continue
        
        elif find_lcps(degree) == True: 
            addn_qual_x_list.append("LCPS")
            continue
        
        elif find_lms(degree) == True: 
            addn_qual_x_list.append("LMS")
            continue
        
        elif find_lsmf(degree) == True: 
            addn_qual_x_list.append("LSMF")
            continue
        
        elif find_cert_wbmf(degree) == True: 
            addn_qual_x_list.append("cert_wbmf")
            continue
        
        elif find_mb(degree) == True: 
            addn_qual_x_list.append("MB")
            continue
        
        elif find_lrcp(degree) == True: 
            addn_qual_x_list.append("LRCP")
            continue
        
        elif find_mcps(degree) == True: 
            addn_qual_x_list.append("MCPS")
            continue
        
        elif find_mmf(degree) == True: 
            addn_qual_x_list.append("MMF")
            continue
               
        else: 
            addn_qual_x_list.append("None")
            continue
    
    print(qualification_number)
    
    data['addnQual'+str(qualification_number)+'_main'] = addn_qual_x_list  

