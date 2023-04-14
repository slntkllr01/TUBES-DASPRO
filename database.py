# Inisialisasi panjang (length) array
nuser = 0 # length user
ncandi = 0 # length candi
nbangunan = 0 # length bangunan

# Inisialisasi Array
user = [[] for i in range (103)] # asumsi maksimal terdapat 103 baris (1 baris sisanya adalah header)
candi = [[] for i in range (101)] # asumsi maksimal terdapat 101 baris (1 baris sisanya adalah header)
bangunan = [[] for i in range (4)] # asumsi maksimal terdapat 4 baris (1 baris sisanya adalah header)

# Database pengguna
username = ''
password = ''
role = ''