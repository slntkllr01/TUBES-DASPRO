import sys
from F14 import save

def exit():
    validasi  = False
    while not validasi: # Dalam artian, while True
        choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if choice == "y" or choice == 'Y':
            save()
            sys.exit()
        elif choice == "n" or choice == "N":
            sys.exit()
        else:
            valid_input = False



  
    

    
