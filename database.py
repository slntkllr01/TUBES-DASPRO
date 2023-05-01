from csvfunction import *
from function import *

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