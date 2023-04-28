from function import *
from csvfunction import *

# Inisialisasi Array Database
user = [[] for i in range (103)] # 1 untuk header
candi = [[] for i in range (101)] # 1 untuk header
bahan_bangunan = [[] for i in range (4)] # 1 untuk header

# Inisialisasi Database Pengguna
username = ''
password = ''
role = ''

# Inisialisasi Status Login
loginstatus = False

user_csv = csv_to_array('user.csv')
user = add_to_database(user, user_csv)

bb_csv = csv_to_array('bahan_bangunan.csv')
bb = add_to_database(bahan_bangunan, bb_csv)

candi_csv = csv_to_array('candi.csv')
candi = add_to_database(candi, candi_csv)
