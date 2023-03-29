import re
data = data

#getting specialisations of MD DNB etc. 
checking_list = data[data.addnQual1_main == "MD"]['qualification_addtional_1']
cleanedSet = set(checking_list)

def find_MD_ObsGyne(degree):
    if re.search("obst", degree):
        return True
    
    elif re.search("gynae", degree):
        return True
    
    elif re.search("gyana", degree):
        return True
    
    elif re.search("obg", degree):
        return True

    elif re.search("o\.b\.g", degree):
        return True
 
def find_MD_Radio_Diagnosis(degree):
    if re.search("diag", degree):
        return True
    
    elif re.search("radiogiagnosis", degree):
        return True
    
    elif re.search("diaag", degree):
        return True
    
    elif re.search("r \& d", degree):
        return True
    
    elif re.search("rad\. dign\.", degree):
        return True

def find_MD_Physiology(degree):
    if re.search("physi", degree):
        return True

    elif re.search("pshy", degree):
        return True
    
    elif re.search("psysio", degree):
        return True
    
def find_MD_GenMed(degree):
    if re.search("general", degree):
        return True
    
    elif re.search("gen\. m", degree):
        return True
    
    elif re.search("gen\.m", degree):
        return True

    elif re.search("genl", degree):
        return True
    
    elif re.search("gen ", degree):
        return True
    
    elif re.search("gener", degree):
        return True
    
    elif re.search("gen\-m", degree):
        return True

    elif re.search("\(medicine\)", degree):
        return True
    
    elif re.search("\( medicine\)", degree):
        return True
    
    elif re.search("med\.", degree):
        return True
    
    elif re.search("\(med\)", degree):
        return True
    
    elif re.search("m\.d\. medicine", degree):
        return True
    
    elif re.search("m\.d \- medicine", degree):
        return True
    
    elif re.search("m\.d\. \- medicine", degree):
        return True
    
    elif re.search("m\.d\.medicine", degree):
        return True

    elif re.search("md medicine", degree):
        return True
    
    elif re.search("d\-medicine", degree):
        return True
    
    elif re.search("d \- medicine", degree):
        return True
    
    elif re.search("\(gm", degree):
        return True
    
def find_MD_Anaesthesiology(degree):
    if re.search("anaes", degree):
        return True
    
    elif re.search("aneas", degree):
        return True
    
    elif re.search("anes", degree):
        return True

def find_MD_CommMed(degree):
    if re.search("comm", degree):
        return True   
    
    elif re.search("\(cm\)", degree):
        return True 
    
def find_MD_Immunology(degree):
    if re.search("immu", degree):
        return True

def find_MD_RadioTherapy(degree):
    if re.search("therapy", degree):
        return True
    
    elif re.search("thero", degree):
        return True
    
    elif re.search("theraphy", degree):
        return True
    
    elif re.search("therepy", degree):
        return True
    
    elif re.search("thrapy", degree):
        return True
    
    elif re.search("radiation oncology", degree):
        return True
    
def find_MD_Radiology(degree):
    if re.search("radiology", degree):
        return True

def find_MD_Pharmacology(degree):
    if re.search("pharm", degree):
        return True
    
def find_MD_Dermatology(degree):
    if re.search("derm", degree):
        return True
    
    elif re.search("der\.", degree):
        return True
    
    elif re.search("lepxsy", degree):
        return True
    
    elif re.search("skin", degree):
        return True
    
    elif re.search("derr\.ven", degree):
        return True
    
    elif re.search("vene", degree):
        return True
    
    elif re.search("darma", degree):
        return True
    
    elif re.search("demr", degree):
        return True
    
    elif re.search("d\.v\.", degree):
        return True
    
    elif re.search("dvl", degree):
        return True
    
    elif re.search("d\. v\. ", degree):
        return True
    
    elif re.search("d v l", degree):
        return True
    
def find_MD_Pediatrics(degree):
    if re.search("paed", degree):
        return True
    
    elif re.search("pae\)", degree):
        return True
    
    elif re.search("pedia", degree):
        return True
    
    elif re.search("pead", degree):
        return True
    
    elif re.search("piad", degree):
        return True
    
def find_MD_Anatomy(degree):
    if re.search("anat", degree):
        return True

def find_MD_SocAndPrevMed(degree):
    if re.search("preventive", degree):
        return True
    
    elif re.search("s\.p\.m", degree):
        return True
    
    elif re.search("spm", degree):
        return True

def find_MD_GenSurgery(degree):
    if re.search("gen\. su", degree):
        return True
    
    elif re.search("gen\.su", degree):
        return True
    
    if re.search("surgery", degree):
        return True
    
def find_MD_Opthalmology(degree):
    if re.search("opth", degree):
        return True
    
    if re.search("ophth", degree):
        return True
    
def find_MD_BioPhysics(degree):
    if re.search("bio\-phy", degree):
        return True

def find_MD_ForensicMedicine(degree):
    if re.search("fore", degree):
        return True
    
    elif re.search("fmt", degree):
        return True
    
    elif re.search("f\.m\.t", degree):
        return True
    
    elif re.search("for\.med", degree):
        return True
    
def find_MD_Biochemistry(degree):
    if re.search("biochem", degree):
        return True

    elif re.search("bio\-chem", degree):
        return True
    
    elif re.search("bio chem", degree):
        return True
    
    elif re.search("bio\- dhem", degree):
        return True

def find_MD_PulmonaryMed(degree):
    if re.search("pulmo", degree):
        return True
    
def find_MD_Psychiatry(degree):
    if re.search("psych", degree):
        return True
    
    elif re.search("physch", degree):
        return True
    
    elif re.search("phych", degree):
        return True
        
def find_MD_TransfusionMed(degree):
    if re.search("trans", degree):
        return True

def find_MD_AerospaceMed(degree):
    if re.search("aerospace", degree):
        return True
    
def find_MD_RespiratoryMed(degree):
    if re.search("resp", degree):
        return True
    
    elif re.search("r\.d", degree):
        return True
    
def find_MD_MicroBiology(degree):
    if re.search("micro", degree):
        return True
    
def find_MD_Pathology(degree):
    if re.search("path", degree):
        return True
    
    elif re.search("pata", degree):
        return True
    
    elif re.search("paat", degree):
        return True
    
def find_MD_NuclearMed(degree):
    if re.search("nucl", degree):
        return True 

    
def find_MD_EmergencyMed(degree):
    if re.search("emergen", degree):
        return True
    
def find_MD_Geriatrics(degree):
    if re.search("geri", degree):
        return True

def find_MD_InternalMed(degree):
    if re.search("internal", degree):
        return True
    
def find_MD_Orthopaedics(degree):
    if re.search("ortho", degree):
        return True
    
def find_MD_CCM(degree):
    if re.search("ccm", degree):
        return True
    
def find_MD_SportMed(degree):
    if re.search("sport", degree):
        return True
   
def find_MD_TBandChest(degree):
    if re.search("chest", degree):
        return True
    
    elif re.search("tb ", degree):
        return True
    
    elif re.search("t\.b", degree):
        return True
   
def find_MD_HospAdmin(degree):
    if re.search("hosp", degree):
        return True
        
def find_MD_PalliativeMed(degree):
    if re.search("pallia", degree):
        return True
   
def find_MD_LabMed(degree):
    if re.search("labmed", degree):
        return True

    elif re.search("labora", degree):
        return True
   
def find_MD_AviationMed(degree):
    if re.search("aviation", degree):
        return True
    
def find_MD_PhyMedandRehab(degree):
    if re.search("rehab", degree):
        return True
    
def find_MD_Physician(degree):
    if re.search("physician", degree):
        return True
    
def find_MD_CommHealthAdmin(degree):
    if re.search("community health", degree):
        return True
    
    elif re.search("comm\.hlth", degree):
        return True

def find_MD_MatChildHealth(degree):
    if re.search("mat\.\& ch", degree):
        return True   

count = 0
count_genmed = 0
degree_unaccounted_list = list()
for degree in checking_list:
    
    if str(degree) == "nan":
        continue
    
    degree = degree.lower()
    
    if find_MD_ObsGyne(degree) == True:
        count += 1
        continue
        
    elif find_MD_Radio_Diagnosis(degree) == True:
        count += 1
        continue
    
    elif find_MD_PhyMedandRehab(degree) == True:
        count += 1
        continue
    
    elif find_MD_Physician(degree) == True:
        count += 1
        continue
        
    elif find_MD_Physiology(degree) == True:
        count += 1   
        continue
        
    elif find_MD_Anaesthesiology(degree) == True:
        count += 1
        continue
    
    elif find_MD_Psychiatry(degree) == True:
        count += 1    
        continue 
    
    elif find_MD_CommHealthAdmin(degree) == True:
        count += 1        
        continue 
        
    elif find_MD_CommMed(degree) == True:
        count += 1        
        continue
        
    elif find_MD_Immunology(degree) == True:
        count += 1  
        continue
    
    elif find_MD_RadioTherapy(degree) == True:
        count += 1    
        continue
    
    elif find_MD_Pharmacology(degree) == True:
        count += 1    
        continue
    
    elif find_MD_Orthopaedics(degree) == True:
        count += 1    
        continue 

    elif find_MD_Pediatrics(degree) == True:
        count += 1   
        continue
    
    elif find_MD_Anatomy(degree) == True:
        count += 1    
        continue
    
    elif find_MD_SocAndPrevMed(degree) == True:
        count += 1    
        continue
    
    elif find_MD_GenSurgery(degree) == True:
        count += 1    
        continue
    
    elif find_MD_Opthalmology(degree) == True:
        count += 1    
        continue
    
    elif find_MD_MicroBiology(degree) == True:
        count += 1    
        continue
    
    elif find_MD_Biochemistry(degree) == True:
        count += 1    
        continue
    
    elif find_MD_BioPhysics(degree) == True:
        count += 1   
        continue
    
    elif find_MD_ForensicMedicine(degree) == True:
        count += 1    
        continue
    
    elif find_MD_PulmonaryMed(degree) == True:
        count += 1    
        continue 

    elif find_MD_Dermatology(degree) == True:
        count += 1  
        continue  
    
    elif find_MD_Radiology(degree) == True:
        count += 1    
        continue 
    
    elif find_MD_TransfusionMed(degree) == True:
        count += 1    
        continue 
    
    elif find_MD_AerospaceMed(degree) == True:
        count += 1    
        continue 
    
    elif find_MD_RespiratoryMed(degree) == True:
        count += 1    
        continue  
    
    elif find_MD_Pathology(degree) == True:
        count += 1    
        continue 
    
    elif find_MD_NuclearMed(degree) == True:
        count += 1    
        continue 
    
    
    elif find_MD_EmergencyMed(degree) == True:
        count += 1    
        continue 
    
    elif find_MD_Geriatrics(degree) == True:
        count += 1    
        continue 
    
    elif find_MD_InternalMed(degree) == True:
        count += 1    
        continue 
    
    elif find_MD_CCM(degree) == True:
        count += 1    
        continue 
    
    elif find_MD_SportMed(degree) == True:
        count += 1    
        continue 
    
    elif find_MD_TBandChest(degree) == True:
        count += 1    
        continue
    
    elif find_MD_HospAdmin(degree) == True:
        count += 1    
        continue
    
    elif find_MD_PalliativeMed(degree) == True:
        count += 1    
        continue
    
    elif find_MD_LabMed(degree) == True:
        count += 1    
        continue
    
    elif find_MD_AviationMed(degree) == True:
        count += 1    
        continue
    
    elif find_MD_GenMed(degree) == True:
        count += 1
        count_genmed += 1
        continue
    
    elif find_MD_MatChildHealth(degree) == True:
        count += 1
        continue
    
    else:
        degree_unaccounted_list.append(degree)
        
print(count)
print(count_genmed)

dataEasyView = pd.DataFrame(dict(Counter(degree_unaccounted_list)).items())
dataEasyView.columns = ['degree', 'count']
np.sum(dataEasyView['count'])

#%%%
# For MS
checking_list = data[data.addnQual1_main == "MS"]['qualification_addtional_1']
cleanedSet = set(checking_list)

count = 0

def find_MS_GenMed(degree):
    if re.search("general medicine", degree):
        return True
    
    elif re.search("gen\. med\.", degree):
        return True
    
    elif re.search("gen\.med\.", degree):
        return True
    
    elif re.search("ms \(faculty of med\)", degree):
        return True
    
def find_MS_GenSurgery(degree):
    if re.search("general su", degree):
        return True
    
    elif re.search("gen\. su", degree):
        return True

    elif re.search("genl\. su", degree):
        return True
    
    elif re.search("genl su", degree):
        return True
    
    elif re.search("gen su", degree):
        return True
    
    elif re.search("gen\.su", degree):
        return True
    
    elif re.search("\(surgery\)", degree):
        return True
    
    elif re.search("gen", degree):
        return True

    elif re.search("\(sur", degree):
        return True  
    
    elif re.search("\[sur", degree):
        return True 
    
    elif re.search("ms sur", degree):
        return True 
    
    elif re.search("ms \- sur", degree):
        return True 
    
    elif re.search("ms-sur", degree):
        return True 
    
    elif re.search("ms- sur", degree):
        return True 
    
    elif re.search("master of surgery", degree):
        return True 
    
    elif re.search("\( sur", degree):
        return True
    
    elif re.search("m\.s\. sur", degree):
        return True
    
    elif re.search("m\.s - sur", degree):
        return True
    
    elif re.search("^surgery$", degree):
        return True
    
    elif re.search("m\.s$", degree):
        return True
       
def find_MS_Orthopaedics(degree):
    if re.search("ortho", degree):
        return True
    
    elif re.search("paed", degree):
        return True
    
    elif re.search("otho", degree):
        return True
    

def find_MS_Opthalmology(degree):
    if re.search("ophthal", degree):
        return True
    
    elif re.search("opth", degree):
        return True
    
    elif re.search("opht", degree):
        return True
    
def find_MS_Anatomy(degree):
    if re.search("anat", degree):
        return True

def find_MS_ObstGyne(degree):
    if re.search("gyna", degree):
        return True
    
    elif re.search("gyne", degree):
        return True
    
    elif re.search("gyan", degree):
        return True
    
    elif re.search("o \& g", degree):
        return True
    
    elif re.search("obg", degree):
        return True
    
    elif re.search("obst", degree):
        return True
    
    elif re.search("o\.b\.g", degree):
        return True

def find_MS_ENT(degree):
    if re.search("ent", degree):
        return True
    
    elif re.search("e\.n", degree):
        return True
    
    elif re.search("nose", degree):
        return True
    
    elif re.search("otor", degree):
        return True
    
    elif re.search("oto-rh", degree):
        return True
    
    elif re.search("rhino", degree):
        return True
    
    
def find_MS_Pathology(degree):
    if re.search("patho", degree):
        return True
    
def find_MS_Anaesthesiology(degree):
    if re.search("anae", degree):
        return True
    
    if re.search("anea", degree):
        return True

###
for degree in cleanedSet:
    degree = degree.lower()
    
    if find_MS_GenMed(degree) == True:
        count += 1
        continue
    
    elif find_MS_Orthopaedics(degree) == True:
        count += 1
        continue
    
    elif find_MS_Opthalmology(degree) == True:
        count += 1
        continue
    
    elif find_MS_Anatomy(degree) == True:
        count += 1
        continue
    
    elif find_MS_ObstGyne(degree) == True:
        count += 1
        continue
    
    elif find_MS_ENT(degree) == True:
        count += 1       
        continue
    
    elif find_MS_Pathology(degree) == True:
        count += 1
        continue
    
    elif find_MS_Anaesthesiology(degree) == True:
        count += 1
        continue
    
    if find_MS_GenSurgery(degree) == True:
        count += 1
        continue
    
    
    else:
        print(degree)

print(count)

#%%%

#For Diploma (not DNB)
checking_list = data[data.addnQual1_main == "Diploma"]['qualification_addtional_1']
cleanedSet = set(checking_list)

count = 0

def find_Dip_Opthalmology(degree):
    if re.search("optha", degree):
        return True

    elif re.search("opht", degree):
        return True
    
    elif re.search("doms", degree):
        return True
    
    elif re.search("d\.o\.m\.s", degree):
        return True
    
def find_Dip_ChildHealth(degree):
    if re.search("child", degree):
        return True
    
    elif re.search("d\.c\.h", degree):
        return True

    elif re.search("dch", degree):
        return True  
   
def find_Dip_Paediatrics(degree):
    if re.search("paed", degree):
        return True
    
    elif re.search("pead", degree):
        return True
    
def find_Dip_ObstGyne(degree):
    if re.search("obst", degree):
        return True
    
    elif re.search("obts", degree):
        return True
    
    elif re.search("obg", degree):
        return True

    elif re.search("obost", degree):
        return True
    
    elif re.search("d\.g\.o", degree):
        return True
    
    elif re.search("d\.g\. o", degree):
        return True
    
    elif re.search("d\.go", degree):
        return True
    
    elif re.search("dgo", degree):
        return True

def find_Dip_Anaesthesiology(degree):
    if re.search("anaes", degree):
        return True
    
    elif re.search("anath", degree):
        return True
    
    elif re.search("annest", degree):
        return True

    elif re.search("anes", degree):
        return True
    
    elif re.search("aneas", degree):
        return True
    
    elif re.search("anase", degree):
        return True
    
    elif re.search("anet", degree):
        return True
    
    elif re.search("ana\.", degree):
        return True
    
    elif re.search("dip\.ana", degree):
        return True
    
    elif re.search("d\.a", degree):
        return True
    
    elif re.search("^da$", degree):
        return True
   
def find_Dip_RadioDiagn_Radiology(degree):
    if re.search("diag", degree):
        return True
    
    elif re.search("radiogiagnosis", degree):
        return True
    
    elif re.search("d\.r\.m", degree):
        return True
    
    elif re.search("drd", degree):
        return True
    
    elif re.search("drm", degree):
        return True
    
    elif re.search("dmr", degree):
        return True
    
    elif re.search("d\.m\.r\.", degree):
        return True
    
    elif re.search("dmrd", degree):
        return True
    
    elif re.search("radiation med", degree):
        return True
    
    elif re.search("d\.m\.r\.d", degree):
        return True
    
    elif re.search("diaag", degree):
        return True
    
    elif re.search("r \& d", degree):
        return True
    
    elif re.search("d\.r\.d", degree):
        return True
    
    elif re.search("rad\. dign\.", degree):
        return True
    
    elif re.search("electro", degree):
        return True
    
    elif re.search("radio\.elec", degree):
        return True
    
    elif re.search("radiology", degree):
        return True   
    
    elif re.search("radi\.med\.", degree):
        return True 

def find_Dip_Dermatogoly(degree): 
    if re.search("derm", degree):
            return True
        
    elif re.search("lepro", degree):
            return True
        
    elif re.search("der\.ven", degree):
            return True
        
    elif re.search("d\.v\.d", degree):
            return True
        
    elif re.search("d\.v\.l", degree):
            return True  
     
def find_Dip_Psychiatry(degree): 
    if re.search("psychia", degree):
            return True
        
    elif re.search("psycho", degree):
            return True
        
    elif re.search("phycho", degree):
            return True
        
    elif re.search("psy\.med", degree):
            return True
        
    elif re.search("dip\.psy", degree):
            return True
        
    elif re.search("d\.p\.m", degree):
            return True
        
    elif re.search("dpm", degree):
            return True
        
def find_Dip_TBandChest(degree): 
    if re.search("chest", degree):
            return True
        
    elif re.search("d\.t\.c\.d", degree):
            return True
        
    elif re.search("tuber", degree):
            return True
        
def find_Dip_Orthopedics(degree): 
    if re.search("ortho", degree):
            return True
        
def find_Dip_Pathology(degree): 
    if re.search("path", degree):
            return True 
        
    elif re.search("cl\.path", degree):
            return True 
        
    elif re.search("dcp", degree):
            return True 
        
    elif re.search("d\.c\.p", degree):
            return True 
        
    elif re.search("dc p", degree):
        return True 
        
    elif re.search("d\.p\.b", degree):
        return True 
    
    elif re.search("d\.c\.b", degree):
        return True     
    
def find_Dip_RadioTherapy(degree):
    if re.search("therapy", degree):
        return True
    
    elif re.search("thero", degree):
        return True
    
    elif re.search("rad\.ther", degree):
        return True
    
    elif re.search("theraphy", degree):
        return True
    
    elif re.search("therepy", degree):
        return True
    
    elif re.search("thrapy", degree):
        return True
    
    elif re.search("radiation oncology", degree):
        return True
    
    elif re.search("dmrt", degree):
        return True

def find_Dip_SportMed(degree): 
    if re.search("sport", degree):
            return True
        
def find_Dip_InternalMed(degree): 
    if re.search("internal", degree):
            return True       

def find_Dip_Diabetology(degree): 
    if re.search("diabet", degree):
            return True  


def find_Dip_PublicHealth(degree): 
    if re.search("pub", degree):
            return True  

def find_Dip_TropicalMed(degree): 
    if re.search("tropi", degree):
            return True   
        
    elif re.search("tro\.med\.", degree):
        return True
    
    elif re.search("hygiene", degree):
        return True

def find_Dip_Cardiology(degree): 
    if re.search("cardio", degree):
            return True   

def find_Dip_ENT(degree):
    if re.search("ent", degree):
        return True
    
    elif re.search("e\.n", degree):
        return True
    
    elif re.search("nose", degree):
        return True  
    
    elif re.search("otor", degree):
            return True
    
    elif re.search("oto-rh", degree):
        return True
    
    elif re.search("rhino", degree):
        return True
    
    elif re.search("laryn", degree):
        return True
    
    elif re.search("laryan", degree):
        return True
    
    elif re.search("d\.l\.o", degree):
        return True
    
    elif re.search("dlo", degree):
        return True     
    
def find_Dip_ForensicMed(degree): 
    if re.search("fore\.med", degree):
            return True    

    elif re.search("d\. f\. m", degree):
            return True 

def find_Dip_MaternityChildWelfare(degree): 
    if re.search("m\.c\.w", degree):
            return True  
        
    elif re.search("mcw", degree):
        return True 

def find_Dip_MedicalOncology(degree): 
    if re.search("onco", degree):
            return True  
        
def find_Dip_PhyMedandRehab(degree): 
    if re.search("rehab", degree):
            return True  
        
def find_Dip_Neurology(degree):
    if re.search("neurology", degree):
        return True

def find_Dip_Immuno_BloodTransf(degree):
    if re.search("blood", degree):
        return True

for degree in cleanedSet:
    
    degree = degree.lower()
    
    if find_Dip_Opthalmology(degree) == True:
        count += 1
        continue

    elif find_Dip_ChildHealth(degree) == True:
        count += 1       
        continue
    
    elif find_Dip_Paediatrics(degree) == True:
        count += 1
        continue
    
    elif find_Dip_ObstGyne(degree) == True:
        count += 1
        continue
    
    elif find_Dip_Dermatogoly(degree) == True:
        count += 1
        continue
    
    elif find_Dip_Anaesthesiology(degree) == True:
        count += 1
        continue
    
    elif find_Dip_RadioDiagn_Radiology(degree) == True:
        count += 1
        continue
    
    elif find_Dip_Psychiatry(degree) == True:
        count += 1
        continue
    
    elif find_Dip_TBandChest(degree) == True:
        count += 1
        continue
    
    elif find_Dip_Orthopedics(degree) == True:
        count += 1
        continue
    
    elif find_Dip_Pathology(degree) == True:
        count += 1
        continue
    
    elif find_Dip_RadioTherapy(degree) == True:
        count += 1
        continue
    
    elif find_Dip_SportMed(degree) == True:
        count += 1
        continue
    
    elif find_Dip_InternalMed(degree) == True:
        count += 1
        continue
    
    elif find_Dip_Diabetology(degree) == True:
        count += 1
        continue
    
    
    elif find_Dip_PublicHealth(degree) == True:
        count += 1
        continue

    elif find_Dip_TropicalMed(degree) == True:
        count += 1
        continue
    
    elif find_Dip_Cardiology(degree) == True:
        count += 1
        continue
    
    elif find_Dip_ENT(degree) == True:
        count += 1
        continue
    
    elif find_Dip_ForensicMed(degree) == True:
        count += 1
        continue
    
    elif find_Dip_MaternityChildWelfare(degree) == True:
        count += 1
        continue
    
    elif find_Dip_MedicalOncology(degree) == True:
        count += 1
        continue
    
    elif find_Dip_PhyMedandRehab(degree) == True:
        count += 1
        continue
    
    elif find_Dip_Neurology(degree) == True:
        count += 1
        continue
    
    elif find_Dip_Immuno_BloodTransf(degree) == True:
        count += 1
        continue    
    
    else:
        print(degree)

print(count)





#%%%
#=============================================================================

#Find DNB:
checking_list = data[data.addnQual1_main == "DNB"]['qualification_addtional_1']
cleanedSet = set(checking_list)

count = 0


def find_DNB_ObsGyne(degree):
    if re.search("obst", degree):
        return True
    
    elif re.search("gynae", degree):
        return True
    
    elif re.search("gyana", degree):
        return True
    
    elif re.search("obg", degree):
        return True

    elif re.search("o\.b\.g", degree):
        return True
    
    elif re.search("o\&g", degree):
        return True
    
    elif re.search("obs\.", degree):
        return True
 
def find_DNB_Radio_Diagnosis(degree):
    if re.search("diag", degree):
        return True
    
    elif re.search("radiogiagnosis", degree):
        return True
    
    elif re.search("diaag", degree):
        return True
    
    elif re.search("r \& d", degree):
        return True
    
    elif re.search("rad\. dign\.", degree):
        return True
    
    elif re.search("radio daig", degree):
        return True
    
    elif re.search("\(radio$ ", degree):
        return True

def find_DNB_Physiology(degree):
    if re.search("physi", degree):
        return True

    elif re.search("pshy", degree):
        return True
    
    elif re.search("psysio", degree):
        return True
    
def find_DNB_GenMed(degree):
    if re.search("general", degree):
        return True
    
    elif re.search("gen\. m", degree):
        return True
    
    elif re.search("gen\.m", degree):
        return True

    elif re.search("genl", degree):
        return True
    
    elif re.search("gen ", degree):
        return True
    
    elif re.search("gener", degree):
        return True
    
    elif re.search("gen\-m", degree):
        return True

    elif re.search("\(medicine\)", degree):
        return True
    
    elif re.search("\( medicine\)", degree):
        return True
    
    elif re.search("med\.", degree):
        return True
    
    elif re.search("\(med\)", degree):
        return True
    
    elif re.search("m\.d\. medicine", degree):
        return True
    
    elif re.search("m\.d \- medicine", degree):
        return True
    
    elif re.search("m\.d\. \- medicine", degree):
        return True
    
    elif re.search("m\.d\.medicine", degree):
        return True

    elif re.search("md medicine", degree):
        return True
    
    elif re.search("d\-medicine", degree):
        return True
    
    elif re.search("d \- medicine", degree):
        return True
    
    elif re.search("\(gm", degree):
        return True
    
def find_DNB_Anaesthesiology(degree):
    if re.search("anaes", degree):
        return True
    
    elif re.search("aneas", degree):
        return True
    
    elif re.search("anes", degree):
        return True
    
    elif re.search("aneth", degree):
        return True

   
def find_DNB_Immunology(degree):
    if re.search("immu", degree):
        return True

def find_DNB_RadioTherapy(degree):
    if re.search("therapy", degree):
        return True
    
    elif re.search("thero", degree):
        return True
    
    elif re.search("theraphy", degree):
        return True
    
    elif re.search("therepy", degree):
        return True
    
    elif re.search("thrapy", degree):
        return True
    
    elif re.search("radiation oncology", degree):
        return True
    
def find_DNB_Radiology(degree):
    if re.search("radiology", degree):
        return True
    
    elif re.search("\( radio\)", degree):
        return True
    
    elif re.search("\(radio$", degree):
        return True
    

def find_DNB_Pharmacology(degree):
    if re.search("pharm", degree):
        return True
    
def find_DNB_Dermatology(degree):
    if re.search("derm", degree):
        return True
    
    elif re.search("der\.", degree):
        return True
    
    elif re.search("lepxsy", degree):
        return True
    
    elif re.search("skin", degree):
        return True
    
    elif re.search("derr\.ven", degree):
        return True
    
    elif re.search("vene", degree):
        return True
    
    elif re.search("darma", degree):
        return True
    
    elif re.search("demr", degree):
        return True
    
    elif re.search("d\.v\.", degree):
        return True
    
    elif re.search("dvl", degree):
        return True
    
    elif re.search("d\. v\. ", degree):
        return True
    
    elif re.search("d v l", degree):
        return True
    
    
def find_DNB_Pediatrics(degree):
    if re.search("paed", degree):
        return True
    
    elif re.search("pae\)", degree):
        return True
    
    elif re.search("pedia", degree):
        return True
    
    elif re.search("pead", degree):
        return True
    
    elif re.search("piad", degree):
        return True
    
def find_DNB_Anatomy(degree):
    if re.search("anat", degree):
        return True

def find_DNB_SocAndPrevMed(degree):
    if re.search("preventive", degree):
        return True
    
    elif re.search("s\.p\.m", degree):
        return True
    
    elif re.search("spm", degree):
        return True
    
    elif re.search("social ", degree):
        return True

def find_DNB_GenSurgery(degree):
    if re.search("gen\. su", degree):
        return True
    
    elif re.search("gen\.su", degree):
        return True
    
    elif re.search("genl\. su", degree):
        return True
    
    elif re.search("genl su", degree):
        return True
    
    elif re.search("genl\.su", degree):
        return True

    elif re.search("\(surg\.\)", degree):
        return True
    
    elif re.search("\(surgery\)", degree):
        return True
    
    elif re.search("general surg", degree):
        return True
    
    elif re.search("generalsurg", degree):
        return True
    
    elif re.search("gen sur", degree):
        return True
    
def find_DNB_Opthalmology(degree):
    if re.search("opth", degree):
        return True
    
    if re.search("ophth", degree):
        return True
    
def find_DNB_Biology(degree):
    if re.search("bio", degree):
        return True

def find_DNB_ForensicMedicine(degree):
    if re.search("fore", degree):
        return True
    
    elif re.search("fmt", degree):
        return True
    
    elif re.search("f\.m\.t", degree):
        return True
    
def find_DNB_Biochemistry(degree):
    if re.search("biochem", degree):
        return True

def find_DNB_PulmonaryMed(degree):
    if re.search("pulmo", degree):
        return True
    
def find_DNB_Psychiatry(degree):
    if re.search("psych", degree):
        return True
    
    elif re.search("physch", degree):
        return True
    
    elif re.search("phych", degree):
        return True
        
def find_DNB_TransfusionMed(degree):
    if re.search("trans", degree):
        return True

def find_DNB_AerospaceMed(degree):
    if re.search("aerospace", degree):
        return True
    
def find_DNB_RespiratoryMed(degree):
    if re.search("resp", degree):
        return True
    
    elif re.search("r\.d", degree):
        return True
    
def find_DNB_MicroBiology(degree):
    if re.search("micro", degree):
        return True
    
def find_DNB_Pathology(degree):
    if re.search("path", degree):
        return True
    
    elif re.search("pata", degree):
        return True
    
    elif re.search("paat", degree):
        return True
    
def find_DNB_NuclearMed(degree):
    if re.search("nuclear", degree):
        return True
    

def find_DNB_EmergencyMed(degree):
    if re.search("emergen", degree):
        return True
    

def find_DNB_InternalMed(degree):
    if re.search("internal", degree):
        return True
    
def find_DNB_Orthopaedics(degree):
    if re.search("ortho", degree):
        return True
    
def find_DNB_CCM(degree):
    if re.search("ccm", degree):
        return True
    
def find_DNB_SportMed(degree):
    if re.search("sport", degree):
        return True
   
def find_DNB_TBandChest(degree):
    if re.search("chest", degree):
        return True
    
    elif re.search("tb ", degree):
        return True
    
    elif re.search("t\.b", degree):
        return True
   
def find_DNB_HospAdmin(degree):
    if re.search("hosp", degree):
        return True
        
def find_DNB_PalliativeMed(degree):
    if re.search("pallia", degree):
        return True
   
def find_DNB_LabMed(degree):
    if re.search("labmed", degree):
        return True

    elif re.search("labora", degree):
        return True
   
def find_DNB_AviationMed(degree):
    if re.search("aviation", degree):
        return True
 
def find_DNB_FamilyMed(degree):
    if re.search("family", degree):
        return True

def find_DNB_Cardiology(degree):
    if re.search("card", degree):
        return True
    
def find_DNB_Endocrinology(degree):
    if re.search("endo", degree):
        return True
    
def find_DNB_NeuroSurgery(degree):
    if re.search("neuro", degree):
        return True

def find_DNB_InfectiousDiseases(degree):
    if re.search("infect", degree):
        return True
    
def find_DNB_Genito_Urinary_Surgery(degree):
    if re.search("genito", degree):
        return True
    
    elif re.search("gent", degree):
        return True
    
def find_DNB_Nephrology(degree):
    if re.search("nephro", degree):
        return True
    
    elif re.search("neph\.", degree):
        return True
    
def find_DNB_Neonatology(degree):
    if re.search("neonat", degree):
        return True
    
def find_DNB_ENT(degree):
    if re.search("\(ent", degree):
        return True
    
    elif re.search("otor", degree):
        return True
    
    elif re.search("oto-rh", degree):
        return True
    
    elif re.search("rhino", degree):
        return True
    
    elif re.search("laryn", degree):
        return True
    
    elif re.search("laryan", degree):
        return True
    
    elif re.search("d\.l\.o", degree):
        return True
    
    elif re.search("dlo", degree):
        return True
    
def find_DNB_Rheumatology(degree):
    if re.search("rheuma", degree):
        return True
    
def find_DNB_PlasticSurgery(degree):
    if re.search("plas\.", degree):
        return True
    
    elif re.search("plastic", degree):
        return True

def find_DNB_GastroEnterology(degree):
    if re.search("gastro", degree):
        return True

def find_DNB_PeripheralVascSurg(degree):
    if re.search("vascu", degree):
        return True
    
def find_DNB_RuralSurgery(degree):
    if re.search("rural", degree):
        return True

def find_DNB_PhyMedndRehab(degree):
    if re.search("rehab", degree):
        return True

    

for degree in cleanedSet:
    degree = degree.lower()
    
    if find_DNB_ObsGyne(degree) == True:
        count += 1
        continue
        
    elif find_DNB_Radio_Diagnosis(degree) == True:
        count += 1
        continue
        
    elif find_DNB_Physiology(degree) == True:
        count += 1     
        continue
        
        
    elif find_DNB_Anaesthesiology(degree) == True:
        count += 1
        continue
        
    elif find_DNB_RadioTherapy(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_Opthalmology(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_PulmonaryMed(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_Psychiatry(degree) == True:
        count += 1    
        continue  

    elif find_DNB_Dermatology(degree) == True:
        count += 1    
        continue  
    
    elif find_DNB_Radiology(degree) == True:
        count += 1    
        continue 
    
    elif find_DNB_RespiratoryMed(degree) == True:
        count += 1    
        continue 
    
    elif find_DNB_MicroBiology(degree) == True:
        count += 1    
        continue 
    
    elif find_DNB_Pathology(degree) == True:
        count += 1    
        continue 
    
    elif find_DNB_NuclearMed(degree) == True:
        count += 1    
        continue 
    
    elif find_DNB_EmergencyMed(degree) == True:
        count += 1    
        continue 
    
    elif find_DNB_InternalMed(degree) == True:
        count += 1    
        continue 
    
    elif find_DNB_Orthopaedics(degree) == True:
        count += 1    
        continue 
    
    elif find_DNB_Pediatrics(degree) == True:
        count += 1  
        continue
    
    elif find_DNB_HospAdmin(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_FamilyMed(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_Cardiology(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_Endocrinology(degree) == True:
        count += 1    
        continue

    elif find_DNB_NeuroSurgery(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_InfectiousDiseases(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_Genito_Urinary_Surgery(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_Nephrology(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_Neonatology(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_ENT(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_Rheumatology(degree) == True:
        count += 1   
        
        continue
    
    elif find_DNB_PlasticSurgery(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_GastroEnterology(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_PeripheralVascSurg(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_RuralSurgery(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_PhyMedndRehab(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_SocAndPrevMed(degree) == True:
        count += 1    
        continue

    elif find_DNB_GenSurgery(degree) == True:
        count += 1    
        continue
    
    elif find_DNB_GenMed(degree) == True:
        count += 1
        continue
    
    else:
        print(degree)
        
print(count)


#=============================================================================
#%%%

#Find DM:
checking_list = data[data.addnQual1_main == "DM"]['qualification_addtional_1']
cleanedSet = set(checking_list)

count = 0

def find_DM_Endocrinology(degree):
    if re.search("endo", degree):
        return True

def find_DM_Gastrology(degree):
    if re.search("gastro", degree):
        return True

def find_DM_RadioDiagnosis(degree):
    if re.search("radio ", degree):
        return True
    
def find_DM_Haematology(degree):
    if re.search("haem", degree):
        return True
    
def find_DM_Cardiology(degree):
    if re.search("cardio", degree):
        return True
    
def find_DM_Neurology(degree):
    if re.search("neuro", degree):
        return True
    
def find_DM_Nephrology(degree):
    if re.search("nephro", degree):
        return True
    
def find_DM_Neonatology(degree):
    if re.search("neona", degree):
        return True
    
def find_DM_ChildAdolscentPsychiatry(degree):
    if re.search("child", degree):
        return True

def find_DM_PulmonaryCriticalCare(degree):
    if re.search("pulmo", degree):
        return True

def find_DM_Immunology(degree):
    if re.search("immun", degree):
        return True    
    
def find_DM_PulmonaryMed(degree):
    if re.search("pul\.", degree):
        return True    

def find_DM_GeneralMed(degree):
    if re.search("general medicine", degree):
        return True    

def find_DM_Anaestheshiology(degree):
    if re.search("anaes", degree):
        return True   
    
def find_DM_ENT(degree):
    if re.search("rhino", degree):
        return True   
    
def find_DM_Pharmocology(degree):
    if re.search("pharmaco", degree):
        return True   



for degree in cleanedSet:
    degree = degree.lower()
    
    if find_DM_Endocrinology(degree) == True:
            count += 1    
            continue
        
    elif find_DM_Gastrology(degree) == True:
            count += 1    
            continue
        
    elif find_DM_RadioDiagnosis(degree) == True:
            count += 1    
            continue
        
    elif find_DM_Haematology(degree) == True:
            count += 1    
            continue
        
    elif find_DM_Cardiology(degree) == True:
            count += 1    
            continue
        
    elif find_DM_Neurology(degree) == True:
            count += 1    
            continue
        
    elif find_DM_Nephrology(degree) == True:
            count += 1    
            continue
        
    elif find_DM_Neonatology(degree) == True:
            count += 1    
            continue
        
    elif find_DM_ChildAdolscentPsychiatry(degree) == True:
            count += 1    
            continue   
        
    elif find_DM_PulmonaryCriticalCare(degree) == True:
            count += 1    
            continue    
    
    elif find_DM_Immunology(degree) == True:
            count += 1    
            continue    
    
    elif find_DM_PulmonaryMed(degree) == True:
            count += 1    
            continue    
    
    elif find_DM_GeneralMed(degree) == True:
            count += 1    
            continue 
        
    elif find_DM_Anaestheshiology(degree) == True:
            count += 1    
            continue  
        
    elif find_DM_ENT(degree) == True:
            count += 1    
            continue  
        
    elif find_DM_Pharmocology(degree) == True:
            count += 1    
            continue  
        
    else:
        print(degree)
    
print(count)