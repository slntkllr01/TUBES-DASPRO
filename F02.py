# F02 - Logout
def logout(loginstatus):
  if loginstatus == True:
    loginstatus = False
    username = ""
    password = ""
  return loginstatus, username, password
    # print("Logout gagal!")
    # print("Anda belum login, silakan login terlebih dahulu sebelum melakukan logout") 
    
  
    
  


