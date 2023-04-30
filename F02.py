from database import *

def logout():
  if loginstatus == True:
    loginstatus = False
    username = ""
    password = ""
  else:
    print("Logout gagal!\nAnda belum login, silakan login terlebih dahulu sebelum melakukan logout") 
    
  
    
  


