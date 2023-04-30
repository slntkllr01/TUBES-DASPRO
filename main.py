from F01 import *
from F02 import *
from F03 import *
from F04 import *
from F05 import *
from F06 import *
from F07 import *
from F08 import *
from F09 import *
from F10 import *
from F11 import *
from F12 import *
from F13 import *
from F14 import *
from F15 import *
from F16 import *
from database import *

# Fungsi untuk memanggil main sebelum login (rekursif)
def main_program():
    command = input(">>> ")
    if command == "login":
        loginstatus, username, password, role = login()
        if loginstatus:
            main(role)
        else:
            main_program()
    elif command == "help":
        help()
        main_program()
    elif command == "exit":
        exit()
    else:
        print("Maaf, Command tidak terdaftar!")
        main_program()

# Menu yang bisa dipanggil bondowoso (rekursif)
def main_bondowoso():
    command = input(">>> ")
    if command == "help":
        help()
        main_bondowoso()
    elif command == "exit":
        exit()
    elif command == "summonjin":
        summonjin()
        main_bondowoso()
    elif command == "hapusjin":
        hapusjin()
        main_bondowoso()
    elif command == "ubahjin":
        ubahjin()
        main_bondowoso()
    elif command == "batchkumpul":
        kumpul()
        main_bondowoso()
    elif command == "batchbangun":
        bangun()
        main_bondowoso()
    elif command == "laporanjin":
        laporanjin()
        main_bondowoso()
    elif command == "laporancandi":
        laporancandi()
        main_bondowoso()
    elif command == "save":
        save()
        main_bondowoso()
    elif command == "logout":
        logout()
        main_program()
    else:
        print("Maaf, Command tidak terdaftar!")
        main_bondowoso()

# Menu yang bisa dipanggil roro (rekursif)
def main_roro():
    command = input(">>> ")
    if command == "help":
        help()  
        main_roro()
    elif command == "exit":
        exit()
    elif command == "hancurkancandi":
        hancurkancandi()
        main_roro()
    elif command == "ayamberkokok":
        ayamberkokok()
        main_roro()
    elif command == "save":
        save()
        main_roro()
    elif command == "logout":
        logout()
        main_program()
    else:
        print("Maaf, Command tidak terdaftar!")
        main_bondowoso()


# Menu yang bisa dipanggil pembangun (rekursif)
def main_pembangun():
    command = input(">>> ")
    if command == "help":
        help()
        main_pembangun()
    elif command == "exit":
        exit()
    elif command == "bangun":
        bangun()
        main_pembangun()
    elif command == "save":
        save()
        main_pembangun()
    elif command == "logout":
        logout()
        main_program()
    else:
        print("Maaf, Command tidak terdaftar!")
        main_pembangun()

# Menu yang bisa dipanggil pengumpul (rekursif)
def main_pengumpul():
    command = input(">>> ")
    if command == "help":
        help()
        main_pengumpul()
    elif command == "exit":
        exit()
    elif command == "kumpul":
        kumpul()
        main_pengumpul()
    elif command == "save":
        save()
        main_pengumpul()
    elif command == "logout":
        logout()
        main_program()
    else:
        print("Maaf, Command tidak terdaftar!")
        main_pengumpul()

# Fungsi untuk main (menu utama)
def main(role):
    if role == "pembangun":
        main_pembangun()
    elif role == "pengumpul":
        main_pengumpul()
    elif role == "roro":
        main_roro()
    elif role == "bondowoso":
        main_bondowoso()

main_program()



