from F01 import *
from F02 import *
from F03 import *
from F04 import *
from F05 import *
from F06 import *
from F07 import *
from F08 import *
# from F09 import *
# from F10 import *
# from F11 import *
# from F12 import *
from F13 import *
from F14 import *
from F15 import *
from F16 import *
from database import *

# Fungsi untuk memanggil main utama
def main_program():
    command = input(">>> ")
    if command == "login":
        login()
    elif command == "help":
        help()
    elif command == "exit":
        exit()
    else:
        print("Maaf, Command tidak terdaftar!")
        return main_program()

# Menu yang bisa dipanggil bondowoso
def main_bondowoso():
    command = input(">>> ")
    if command == "help":
        help()
    elif command == "logout":
        logout()
    elif command == "exit":
        exit()
    elif command == "summonjin":
        summonjin()
    elif command == "hapusjin":
        hapusjin()
    elif command == "ubahjin":
        ubahjin()
    elif command == "batchkumpul":
        kumpul()
    # elif command == "batchbangun":
    #     bangun()
    # elif command == "laporanjin":
    #     laporanjin()
    # elif command == "laporancandi":
    #     laporancandi()
    elif command == "save":
        save()
    else:
        print("Maaf, Command tidak terdaftar!")
        return main_bondowoso()

# Menu yang bisa dipanggil roro
def main_roro():
    command = input(">>> ")
    if command == "help":
        help()
    elif command == "logout":
        logout()
    elif command == "exit":
        exit()
    # elif command == "hancurkancandi":
    #     hancurkancandi()
    # elif command == "ayamberkokok":
    #     ayamberkokok()
    elif command == "save":
        save()
    else:
        print("Maaf, Command tidak terdaftar!")
        return main_roro()

def main_pengumpul():
    command = input(">>> ")

def main_pembangun():
    command = input(">>> ")

if loginstatus == False:
    main_program()
else: # Login Status = True
    if role == "bandung_bondowoso":
        main_bondowoso() 
    elif role == "roro_jonggrang":
        main_roro()
    else: # Jin
        if role == 'pengumpul':
            main_pengumpul()
        else: # Role = Pembangun
            main_pembangun()

            
                    





