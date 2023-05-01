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
    global loginstatus, role, username, password
    command = input(">>> ")
    if command == "login":
        loginstatus, username, password, role = login()
        if loginstatus:
            main()
        else:
            main_program()
    elif command == "help":
        role_help(loginstatus, role)
        main_program()
    elif command == "exit":
        exit()
    else:
        print("Maaf, Command tidak terdaftar!")
        main_program()

# Menu yang bisa dipanggil bondowoso (rekursif)
def main():
    command = input(">>> ")
    if command == "help":
        role_help(loginstatus, role)
        main()
    elif command == "exit":
        exit()
    elif command == "summonjin":
        summonjin(role, user, candi)
        main()
    elif command == "hapusjin":
        hapusjin(role, user, candi)
        main()
    elif command == "ubahjin":
        ubahjin(role, user)
        main()
    elif command == "kumpul":
        kumpul(role, bb)
        main()
    elif command == "bangun":
        bangun(role, username, user, bb, candi)
        main()
    elif command == "batchkumpul":
        batchkumpul(user, bb, role)
        main()
    elif command == "batchbangun":
        batchbangun(user, candi, bb, role)
        main()
    elif command == "laporanjin":
        laporanjin(role, bb, user, candi)
        main()
    elif command == "laporancandi":
        laporancandi(candi, role)
        main()
    elif command == "hancurkancandi":
        hancurkancandi(role, candi)
        main()
    elif command == "ayamberkokok":
        ayamberkokok(role, candi)
    elif command == "save":
        save()
        main()
    elif command == "logout":
        logout(loginstatus, username, password, role)
        main_program()
    else:
        print("Maaf, Command tidak terdaftar!")
        main()

main_program()