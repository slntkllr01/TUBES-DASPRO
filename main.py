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
        loginstatus, username, password, role = login(user)
        if loginstatus:
            main_menu()
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

# Menjalankan fungsi Load
candi, bb, user = load(user, bahan_bangunan, candi)

# Menu yang bisa dipanggil bondowoso (rekursif)
def main_menu():
    command = input(">>> ")
    if command == "help":
        role_help(loginstatus, role)
        main_menu()
    elif command == "exit":
        exit(user, bb, candi)
    elif command == "summonjin":
        summonjin(role, user, candi)
        main_menu()
    elif command == "hapusjin":
        hapusjin(role, user, candi)
        main_menu()
    elif command == "ubahjin":
        ubahjin(role, user)
        main_menu()
    elif command == "kumpul":
        kumpul(role, bb)
        main_menu()
    elif command == "bangun":
        bangun(role, username, user, bb, candi)
        main_menu()
    elif command == "batchkumpul":
        batchkumpul(user, bb, role)
        main_menu()
    elif command == "batchbangun":
        batchbangun(user, candi, bb, role)
        main_menu()
    elif command == "laporanjin":
        laporanjin(role, bb, user, candi)
        main_menu()
    elif command == "laporancandi":
        laporancandi(candi, role)
        main_menu()
    elif command == "hancurkancandi":
        hancurkancandi(role, candi)
        main_menu()
    elif command == "ayamberkokok":
        ayamberkokok(role, candi)
        if role == 'roro_jonggrang':
            return
        else:
            main_menu()
    elif command == "save":
        save(user, bb, candi)
        main_menu()
    elif command == "logout":
        logout(loginstatus, username, password, role)
        main_program()
    elif command == "login":
        print("\nLogin gagal!\nAnda telah login dengan username " + str(username) + ", silahkan lakukan “logout” sebelum melakukan login kembali.\n")
        main_menu()
    else:
        print("Maaf, Command tidak terdaftar!")
        main_menu()

# Menjalankan Main Program
main_program()