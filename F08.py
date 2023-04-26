from function import RandomNumber

def batchkumpul():
    # Inisialisasi Bahan Bangunan
    pasir_total = 0
    batu_total = 0
    air_total = 0

    pengumpul_count = 0

    i = 0    
    while i < array_length(user):
        if user[i][2] == 'pengumpul':
            founded_pasir = RandomNumber(0,5,345647); founded_batu = RandomNumber(0,5,295847); founded_air = RandomNumber(0,5,375643)
            pasir_total += founded_pasir; batu_total += founded_batu; air_total += founded_air
            pengumpul_count += 1                
        i += 1

    if i == (array_length(user) - 3): # dikurang header, bandung_bondowoso, dan roro_jonggrang
        print('Alemong Kumpul gagal. Summon dulu anjir')
    else:
        print("Mengerahkan", counter ,"jin untuk mengumpulkan bahan.")
        print("Selamat, Jin menemukan total", pasir, "pasir,", batu, "batu, dan", air, "air.")
    return main_bondowoso()    

def batchbangun():
    # Inisialisasi Bahan Bangunan
    pasir_total = 0
    batu_total = 0
    air_total = 0

    pengumpul_count = 0

    i = 0
    while i < array_length(user):
        if user[i][2] == 'pembangun':
            needed_pasir = RandomNumber(0,5,345647); needed_batu = RandomNumber(0,5,295847); needed_air = RandomNumber(0,5,375643)
            pasir_total += needed_pasir ; batu_total += needed_batu ; air_total += needed_air
            pengumpul_count += 1
    if i == (array_length(user) - 3):
        print("Bangun gagal. Anda tidak punya jin pembangun. Silakan summon terlebih dahulu.")
    else:
        print()
        print()
    return main_bondowoso()        

    



