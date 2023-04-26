def load():
    def cekJawaban(jawab) : 
        if jawab == "y" or jawab == "n" :
            return True
        else :
            return False
            
    jawab = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    while cekJawaban(jawab) == False :
        jawab = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if cekJawaban(jawab) == True :
            break
  
    
  
    

    
