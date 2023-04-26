from database import *

def help():
  if loginstatus == False:
     print(f"""
=========== HELP ===========
1. login
   Untuk masuk menggunakan akun
2. load
   Untuk memuat file eksternal ke dalam permainan
3. save
   Untuk menyimpan data permainan
4. exit
   Untuk keluar dari permainan""")
  else:
      if role == 'bandung_bondowoso' :
        print(f"""
=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. summonjin
   Untuk memanggil jin
3. hapusjin
   Untuk menghilangkan jin
4. ubahjin
   Untuk mengubah tipe jin
5. batchkumpul
   Untuk memerintahkan seluruh jin pengumpul mengumpulkan bahan
6. batchbangun
   Untuk memerintahkan seluruh jin pembangun membangun candi
7. laporanjin
   Untuk mengambil laporan kinerja seluruh jin
8. laporancandi
   Untuk mengambil laporan progress pembangunan candi
9. save
   Untuk menyimpan data permainan
10. exit
   Untuk keluar dari permainan""")
      elif role == 'roro_jonggrang':
        print(f"""
=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. hancurkancandi
   Untuk menghancurkan candi yang tersedia
3. ayamberkokok
   Untuk menyelesaikan permainan
4. save
   Untuk menyimpan data permainan
5. exit
   Untuk keluar dari permainan""")
      else : #Jin
        if role == 'pengumpul':
          print(f"""
=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. kumpul
   Untuk mengumpulkan resource candi
3. save
   Untuk menyimpan data permainan
4. exit
   Untuk keluar dari permainan""")
        else : # role = Pembangun
          print(f"""
=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. bangun
   Untuk membangun candi
3. save
   Untuk menyimpan data permainan
4. exit
   Untuk keluar dari permainan""")
          
# Note : Pengumpul dan Pembangun tidak bisa exit          