def logout(loginstatus, username, password, role):
  if loginstatus == True:
    loginstatus = False
    username = ""
    password = ""
    role = ""
    print()
  else:
    print("Logout gagal!\nAnda belum login, silakan login terlebih dahulu sebelum melakukan logout") 
    
  
    
  


