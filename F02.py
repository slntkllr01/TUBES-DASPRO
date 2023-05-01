def logout(loginstatus: bool, username: str, password: str, role: str):
  # Jika status login adalah True, akan logout dengan mengosongkan username, password, dan role
  if loginstatus == True:
    loginstatus = False
    username = ""
    password = ""
    role = ""
    print()
  else:
    # Jika status login adalah False, akan ditampilkan pesan error
    print("\nLogout gagal!\nAnda belum login, silakan login terlebih dahulu sebelum melakukan logout\n") 