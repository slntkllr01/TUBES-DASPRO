import sys
from F14 import save

def exit(user, bb, candi):
    validasi  = False
    while not validasi: # Dalam artian, while True
        choice = input("\nApakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if choice == "y" or choice == 'Y':
            save(user, bb, candi)
            sys.exit()
        elif choice == "n" or choice == "N":
            sys.exit()
        else:
            valid_input = False



  
    

    
