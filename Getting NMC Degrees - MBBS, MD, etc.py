# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:03:22 2022

@author: savas
"""

import re


#First, we try getting if the doctor did an MD or a MS or something else. 

def find_MBBS(degree):
    if re.search("^m b b s", degree):
        return True
    
    elif re.search("^m\.b\.b\.s", degree):
        return True
    
    elif re.search("mbbs", degree):
        return True
    
    elif re.search("^\*\*\*m\.b\.b\.s\.", degree):
        return True
    
    elif re.search("^bachelor of medicine and bachelor of surgery", degree):
        return True
    
    elif re.search("^mbbs", degree):
        return True
        
    elif re.search("^med\.\& surgery", degree):
        return True
    
    elif re.search("^medical doctor equel to mbbs", degree):
        return True    
    
    elif re.search("^medical doctor", degree):
        return True
    
    elif re.search("^\.mbbs", degree):
        return True
    
    elif re.search("^mbbch$", degree):
        return True
    
    elif re.search("^mbchb$", degree):
        return True
    
    elif re.search("^mbs$", degree):
        return True
    
    
    else:
        return False
    

def find_MD(degree):
    if re.search("^m\.d", degree):
        return True
        
    elif re.search("^md", degree):
        return True
       
    elif re.search("^doctor of medicine", degree):
        return True
    
    elif re.search("^m. d\.", degree):
        return True
    
    elif re.search("^doctor medicine", degree):
        return True   
    
    elif re.search("^\*\*\*docto of medicine", degree):
        return True  
    
    elif re.search("^docto of medicine", degree):
        return True 
    
    elif re.search("^\*\*\*doctor of medicine", degree):
        return True 

    elif re.search("^m d", degree):
        return True  
    
    elif re.search("^\*\*\*m.d.", degree):
        return True

    elif re.search("^m\.\.", degree):
        return True    
    
    elif re.search("^doctor of medicin", degree):
        return True 
    
    else: 
        return False

def find_MS(degree):
   if re.search("^m\.s\.", degree):
       return True
       # print(re.search("^m\.s\.", degree))
   elif re.search("^ms", degree):
       return True
       # print(re.search("^ms", degree))
   elif re.search("^m\.s", degree):
       return True
       # print(re.search("^m\.s\.", degree))
   elif re.search("^master of surgery", degree):
       return True
   
   elif re.search("^m\. s\.", degree):
       return True
   
   elif re.search("\,m\.s\.", degree):
       return True
   
   elif re.search("^m s", degree):
       return True
   
   elif re.search("^\.s\.", degree):
       return True
   
   elif re.search("thoracic and cardiac surger", degree):
       return True

   elif re.search("^general surgery", degree):
       return True  
   
   elif re.search("^surgery", degree):
       return True
    
   else:
       return False
   

def find_DM(degree):
    if re.search("^dm", degree):
        return True   
    
    elif re.search("^d\.m", degree):
        return True
    
    elif re.search("^doctorate of medicine", degree):
        return True
    
    else: 
        return False

def find_diplomate_ntnl_board(degree):
    if re.search("^dnb", degree):
        return True
    
    elif re.search("^dip n\.b\.", degree):
        return True
    
    elif re.search("^dip \. nb", degree):
        return True
    
    elif re.search("^dip nb", degree):
        return True
    
    elif re.search("diplomate n\.b\.", degree):
        return True
    
    elif re.search("diplomate ", degree):
        return True
    
    elif re.search("d\.n\.b\.", degree):
        return True
    
    elif re.search("d n b", degree):
        return True
    
    elif re.search("^diplomate of national board", degree):
        return True
    
    elif re.search("dip\. n\.b\.", degree):
        return True
    
    elif re.search("dip\. nb", degree):
        return True
    
    elif re.search("^diplomate n\. b\.", degree):
        return True         
    
    elif re.search("d\.\.n\.b\.", degree):
        return True
    
    elif re.search("d\.n\.b", degree):
        return True
    
    elif re.search("^diplomateofnational", degree): #board ommited because spelling wrong in a few
        return True
    
    elif re.search("^diplomaten\.b\.", degree):
        return True
    
    elif re.search("^dipnb ", degree):
        return True
    
    elif re.search("^diplomatein", degree):
        return True
    
    elif re.search("^diploma of the national board", degree):
        return True

    else:
        return False

def find_diploma_all(degree):
   
    if re.search("dip\.", degree):
        return True
    
    elif re.search("diploma ", degree):
        return True
      
    elif re.search("dip ", degree):
        return True
    
    elif re.search("^d\. ", degree):
        return True
    
    elif re.search("^d\.g\.o\.", degree):
        return True
    
    elif re.search("^d\.go\.", degree):
        return True
    
    elif re.search("^d\.m\.r\.e\.", degree):
        return True
    
    elif re.search("^d\.c\.h\.", degree):
        return True
    
    elif re.search("^d\.v\.d", degree):
        return True
    
    elif re.search("^d\.g\.o", degree):
        return True
    
    elif re.search("d\.m\.r\.d", degree): #No ^ needed. There is a "radio-diagnosis (d.m.r.d)" too
        return True
    
    elif re.search("^d\.o\.m\.s", degree):
        return True
    
    elif re.search("^dgo", degree):
        return True
    
    elif re.search("^drd", degree):
        return True
    
    elif re.search("^d\.r\.d\.", degree):
        return True
    
    elif re.search("^d\.o\.m\.s.", degree):
        return True
    
    elif re.search("^dcp", degree):
        return True
    
    elif re.search("^d\.c\.p", degree):
        return True
    
    elif re.search("^d\.g\.o\.", degree):
        return True

    elif re.search("d\.g\.o", degree): #Does not need ^
        return True
    
    elif re.search("^d.g. o", degree):
        return True
    
    elif re.search("^d\.o\.", degree):
        return True
    
    elif re.search("^dch", degree):
        return True
    
    elif re.search("^dch", degree):
        return True
    
    elif re.search("^d\.c\.h", degree):
        return True
    
    elif re.search("^dlo", degree):
        return True

    elif re.search("^d\.a", degree):
        return True
    
    elif re.search("^da", degree):
        return True
    
    elif re.search("^doms", degree):
        return True

    elif re.search("^d.obg", degree):
        return True
    
    elif re.search("^d\.t\.c\.d\.", degree):
        return True
    
    elif re.search("^d\.ortho", degree):
        return True
    
    elif re.search("^d (ortho)", degree):
        return True

    elif re.search("^d ortho", degree):
        return True
    
    elif re.search("^d\(ortho\)", degree):
        return True
    
    elif re.search("^d\- ortho", degree):
        return True
    
    elif re.search("^diplomainorthopaedics", degree):
        return True

    elif re.search("^d\.l\.o\.", degree):
        return True
    
    elif re.search("^diplomainobstetrics&gynaecology", degree):
        return True
    
    elif re.search("^diploma(obst. & gynae)", degree):
        return True
    
    elif re.search("^diplomainchildhealth", degree):
        return True
    
    elif re.search("^d\.child health", degree):  
        return True
    
    elif re.search("^dipin ", degree):
        return True
    
    elif re.search("^d\.p\.b\.", degree):
        return True

    elif re.search("^dpm", degree):
        return True
    
    elif re.search("^d\.p\.m\.", degree):
        return True
    
    elif re.search("^d\.p\.m", degree):
        return True
    
    elif re.search("^p\.g\.d", degree):
        return True
    
    elif re.search("^radiodiagnosis", degree):
        return True    
    
    elif re.search("^diplomainradio", degree):
        return True  
    
    elif re.search("^d\.r\.m", degree):
        return True 
    
    elif re.search("^pg dlo", degree):
        return True

    elif re.search("^pgddrm", degree):
        return True
    
    elif re.search("^d\.p\.b\.", degree):
        return True
    
    elif re.search("^d\.d\.v\.l", degree):
        return True
    
    elif re.search("^dc p", degree):
        return True
    
    elif re.search("^d\.l\.o", degree):
        return True
    
    elif re.search("^diplomainanesthesia", degree):
        return True
    
    elif re.search("^diploma-medical", degree):
        return True
    
    elif re.search("^diplomatubercolosis", degree):
        return True
    
    elif re.search("^d\(ophthalmology\)", degree):
        return True
    
    elif re.search("^d \(ophthal\)", degree):
        return True
    
    elif re.search("^rasiodiagnosis", degree):
        return True
    
    elif re.search("^d ophthal\.", degree):
        return True
    
    elif re.search("^din annesthesiology", degree):
        return True
    
    elif re.search("^dipl. in medical radio diagnosis", degree):
        return True
    
    elif re.search("^diplomainpsychologicalmedicine", degree):
        return True
    
    elif re.search("^d \(anaesthesiology\)", degree):
        return True

    elif re.search("^dmcw", degree):
        return True    
    
    elif re.search("^d\.m\.c\.w", degree):
        return True
    
    elif re.search("^dmrd", degree):
        return True
    
    elif re.search("^d\.m\.r", degree):
        return True
    
    elif re.search("^dmrt", degree):
        return True
    
    else:
        return False
 
def find_mch(degree):
   if re.search("^m\.ch", degree):
        return True

   elif re.search("^m\.ch\.", degree):
        return True  
    
   elif re.search("^mch\.", degree):
        return True  
    
   elif re.search("^mch", degree):
        return True 
    
   else:
       return False
   
def find_mrcp_mrc(degree):
    if re.search("^m\.r\.c\.p\.ch.", degree):
        return True 
      
    elif re.search("^m\.r\.c\.p\.", degree):
        return True 
    
    elif re.search("^mrc", degree):
        return True 
    
    elif re.search("^m\.r\.c\.p", degree):
        return True 
    
    elif re.search("^m\.r\.c\.", degree):
        return True
    
    elif re.search("^m r c ", degree):
        return True
    
    else: 
        return False
    
def find_fellow(degree):
    if re.search("^f\.r\.c\.r\.", degree):
        return True 
    
    elif re.search("^f\.r\.c\.s\.", degree):
        return True  
    
    elif re.search("^f\.r\.c\.", degree):
        return True  
    
    elif re.search("^f\.c\.p\.s\.", degree):
        return True  
    
    elif re.search("^f\.c\.p\.s", degree):
        return True 
    
    elif re.search("^frcs", degree):
        return True 
    
    elif re.search("^fcps", degree):
        return True
    
    elif re.search("^fellowshipinadvancedhead", degree):
        return True 
    
    elif re.search("^fellow", degree):
        return True 
    
    else:
        return False
    
def find_public_health(degree):
    if re.search("^dph", degree):
        return True
    
    elif re.search("^master of public health", degree):
        return True
    
    elif re.search("^master pub.hth", degree):
        return True
    
    else:
        return False
    
def find_mha(degree):
    if re.search("adm", degree):
        return True
        
    else: 
        return False
    
def find_lmp(degree):
    if re.search("^lmp", degree):
        return True
        
    else: 
        return False
    
def find_lmf(degree):
    if re.search("^lmf", degree):
        return True
        
    else: 
        return False
    
def find_lcps(degree):
    if re.search("^lcps", degree):
        return True
        
    else: 
        return False
    
def find_lms(degree):
    if re.search("^lms", degree):
        return True
        
    else: 
        return False
    
def find_lsmf(degree):
    if re.search("^lsm", degree):
        return True
        
    else: 
        return False
    
def find_cert_wbmf(degree):
    if re.search("^cert\.", degree):
        return True
        
    else: 
        return False
    
def find_mb(degree):
    if re.search("^mb$", degree):
        return True
        
    else: 
        return False
    
def find_lrcp(degree):
    if re.search("^lrcp$", degree):
        return True
    
    elif re.search("^lrcps$", degree):
        return True
        
    else: 
        return False
    
def find_mcps(degree):
    if re.search("^mcps$", degree):
        return True
    
    
def find_mmf(degree):
    if re.search("^mmf$", degree):
        return True
        
    
        
    else: 
        return False
    
    
