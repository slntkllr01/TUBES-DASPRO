import argparse
import sys
import os

def load():
    parser = argparse.ArgumentParser(prog="python main.py", usage= '%(prog)s ' "nama_folder")

    parser.add_argument("nama_folder",  type=str ,nargs = '?', default = "Tidak ada nama folder yang diberikan!")

    args = parser.parse_args()

    if os.path.isdir(args.nama_folder):
        print("\nloading...")
        print('\nSelamat datang di program "Manajerial Candi"\nMasukkan command "help" untuk daftar\ncommand yang dapat kamu panggil.')
        folder = args.nama_folder
    else:
        if (args.nama_folder == "Tidak ada nama folder yang diberikan!"):
            print("Tidak ada nama folder yang diberikan!")
            parser.print_usage()
            sys.exit()
        else:
            print("Tidak ada Folder yang bernama", args.nama_folder, "pada sistem")
            parser.print_usage()
            sys.exit()         
