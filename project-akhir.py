from prettytable import PrettyTable
import csv

tabel = PrettyTable()


#-----------------------------------------------------------------------------------------------------#
"""
Data Admin
"""
dataAdmin = {
    "ID" : [1, 2, 3, 4],
    "username" : ["fazry", "ariantika","efrida", "admin"],
    "password" : ["123", "123", "123", "admin"]
}
#-----------------------------------------------------------------------------------------------------#
"""
Data Pengguna
"""
dataPengguna = {
    "ID" : [1, 2, 3],
    "username" : ["fazry", "ariantika","efrida"],
    "password" : ["123", "123", "123"]
}


dataBuku = {
    "nama" : ["Pemograman Web", "Pemograman Java" , "Pemograman Python"],
    "penulis" : ["Sandhika Galih" , "Eko Kurniawan Khannedy", "Afrizal"],
    "tahunterbit" : [2015 , 2017, 2019],
    "penerbit" : ["WPU", "PZN" , "KT"],
    "status" : ["ada", "ada" , "ada"]
}

#-----------------------------------------------------------------------------------------------------#
"""
Menu Awal
"""
def menu_awal() :
    print("""
======== PERPUSTAKAAN PROGAMMER ==========
        1. Login Admin/User
        2. Register Admin/User
==========================================
        """)
    opt = input("Masukkan Pilihan : ")
    if opt == "1":
        print("> Login sebagai User/Admin? ")
        pil = int(input("Jika Admin Ketik 1, Jika User Ketik 2 : "))#.upper().lower()
        if pil == 1:
            adbuk = input("Masukkan Username Admin : ")
            pasbuk = input("Masukkan Password : ")
            search2 = dataAdmin.get("username").index(adbuk)
            if adbuk == dataAdmin.get("username")[search2] and pasbuk == dataAdmin.get("password")[search2]:
                menu_admin()
            else:
                menu_awal()

        elif pil == 2:
            usBuk = input("Masukkan Username : ")
            pasBuk = input("Masukkan Password : ")
            search = dataPengguna.get("username").index(usBuk)
            if usBuk == dataPengguna.get("username")[search] and pasBuk == dataPengguna.get("password")[search]:
                    print("Login Berhasil")
                    print("Anda Login Sebagai User, Anda Hanya Dapat Melihat Isi Data!")
                    menu_pengguna()
            else:
                    print("Username atau Password Anda Salah!, Coba Lagi!")

    elif opt == "2":
            print("> Register untuk User/Admin? ")
            pil = int(input("Jika Admin Ketik 1, Jika User Ketik 2 : "))
            if pil == 1:
                registerAkunAdmin()
            elif pil == 2:
                registerAkunUser()
    elif opt == "3":
        exit()
#-----------------------------------------------------------------------------------------------------#
"""
Register Akun Admin
"""
def registerAkunAdmin():
    register_berhasil2 = False
    while register_berhasil2 == False :
        print("=============== REGISTER PENGGUNA ============")
        username = input('Username : ')
        password = input('Password : ')
        print("==============================================")

        if username not in dataPengguna.get('username') :
            dataPengguna['username'].append(username)
            dataPengguna['password'].append(password)
            dataPengguna['ID'].append(dataPengguna['ID'][-1] + 1)

            print('Register berhasil')
            menu_awal()

            register_berhasil2 = True
        else :
            print('Username sudah terpakai')
            menu_awal()
        break
#-----------------------------------------------------------------------------------------------------#
"""
Register Akun User
"""
def registerAkunUser():
    register_berhasil2 = False
    while register_berhasil2 == False :
        print("=============== REGISTER PENGGUNA ============")
        username = input('Username : ')
        password = input('Password : ')
        print("==============================================")

        if username not in dataPengguna.get('username') :
            dataPengguna['username'].append(username)
            dataPengguna['password'].append(password)
            dataPengguna['ID'].append(dataPengguna['ID'][-1] + 1)

            print('Register berhasil')
            menu_awal()

            register_berhasil2 = True
        else :
            print('Username sudah terpakai')
            menu_awal()
        break

#-----------------------------------------------------------------------------------------------------#
"""
Menu Admin
"""
def menu_admin ():
    print("""
======== PERPUSTAKAAN PROGAMMER (ADMIN) ========
    1. TAMBAH BUKU
    2. CEK DAN LAPORAN BUKU
    3. UBAH BUKU
    4. HAPUS BUKU
    5. CEK DAN LAPORAN PENGGUNA
    6. HAPUS PENGGUNA
    7. KELUAR

================================================    """)
    ulang = "ya"
    while ulang == "ya":

        pilih=int(input("pilih: "))
        if pilih == 1:
            print("================== Tambah Data Buku ==================")
            nama=input("Silahkan Masukkan Buku yang digunakan : ")
            penulis=input("Silahkan Masukkan Penulis yang digunakan : ")
            tahunterbit=input("Silahkan Masukkan Tahun Terbit yang digunakan : ")
            penerbit=input("Silahkan Masukkan Penerbit yang digunakan : ")
            status=input("Silahkan Masukkan Status yang digunakan : ")
            tbuku(nama,penulis,tahunterbit,penerbit,status)
            cbuku()
            print(tabel)
            ulang = input("Apakah ingin mencoba lagi (ya/tidak)?  ")
            menu_admin()
        elif pilih == 2:
            print("================== Cek dan Laporan Data Buku ==================")
            cbuku()
            print(tabel)
            ulang = input("Apakah ingin mencoba lagi (ya/tidak)?  ")
            menu_admin()
            # laporan()
        elif pilih == 3:
            print("================== Ubah Data Buku ===================")
            ubuku()
            cbuku()
            print(tabel)
            ulang = input("Apakah ingin mencoba lagi (ya/tidak)?  ")
            menu_admin()
        elif pilih == 4:
            print("================== Hapus Data Buku ==================")
            hapus = int(input("Masukkan Data Buku yang mau dihapus: "))
            hbuku(hapus - 1)
            cbuku()
            print(tabel)
            ulang = input("Apakah ingin mencoba lagi (ya/tidak)?  ")
            menu_admin()
        elif pilih == 5 :
            print("================== Tampil Data Pengguna ==================")
            cpguna()
            print(tabel)
            ulang = input("Apakah ingin mencoba lagi (ya/tidak)?  ")
            menu_admin()
        elif pilih == 6 :
            print("================== Hapus Data Pengguna ==================")
            hapus = int(input("Masukkan Data Pengguna yang mau dihapus: "))
            hpguna(hapus - 1)
            cpguna()
            print(tabel)
            ulang = input("Apakah ingin mencoba lagi (ya/tidak)?  ")
            menu_admin()
        elif pilih == 7 :
            exit()
        else:
            print("Maaf Pilihan Tidak Tersedia")
#-----------------------------------------------------------------------------------------------------#
"""
Menu Pengguna
"""
def menu_pengguna ():
    print("""
======== PERPUSTAKAAN PROGAMMER ========
    1. PINJAM BUKU
    2. CEK BUKU
    3. KELUAR

========================================    """)

#-----------------------------------------------------------------------------------------------------#
"""
Fungsi Admin
"""
# menambah data buku
def tbuku(nama, penulis, tahunterbit, penerbit, status) :
    dataBuku.get("nama").append(nama)
    dataBuku.get("penulis").append(penulis)
    dataBuku.get("tahunterbit").append(tahunterbit)
    dataBuku.get("penerbit").append(penerbit)
    dataBuku.get("status").append(status)

#  Ubah data buku
def ubuku():
    namaBuku = input('Masukkan Data Buku yang mau diedit : ')
    indexBuku = dataBuku['nama'].index(namaBuku)
    buku = input('Masukkan Data Buku yg baru : ')
    dataBuku['nama'][indexBuku] = buku

    namaPenulis = input('Masukkan Data Penulis yang mau diedit : ')
    indexPenulis = dataBuku['penulis'].index(namaPenulis)
    dataPenulis = input('Masukkan Data Penulis yg baru : ')
    dataBuku['nama'][indexPenulis] = dataPenulis

    namaTahunterbit = input('Masukkan Data Tahun terbit yang mau diedit : ')
    indexTahunTerbit = dataBuku['tahunterbit'].index(namaTahunterbit)
    dataTahunterbit = input('Masukkan Data Tahun terbit yg baru : ')
    dataBuku['nama'][indexTahunTerbit] = dataTahunterbit

    namaPenerbit = input('Masukkan Data Penerbit yang mau diedit : ')
    indexPenerbit = dataBuku['penerbit'].index(namaPenerbit)
    dataPenerbit = input('Masukkan Data Penerbit yg baru : ')
    dataBuku['nama'][indexPenerbit] = dataPenerbit

    namaStatus = input('Masukkan Data Status yang mau diedit : ')
    indexStatus = dataBuku['status'].index(namaStatus)
    dataStatus = input('Masukkan Data Status yg baru : ')
    dataBuku['nama'][indexStatus] = dataStatus

# Hapus data buku
def hbuku(hapus):
    dataBuku.get("nama").pop(hapus)

# cek dan tampilkan data buku
def cbuku() :
    tabel.field_names = ["No" , "Nama", "Penulis", "Tahun Terbit", "Penerbit" , "Status"]
    tabel.clear_rows()
    for i in range (len(dataBuku.get("nama"))) :
        tabel.add_row([i + 1, dataBuku.get("nama")[i],dataBuku.get("penulis")[i],dataBuku.get("tahunterbit")[i],dataBuku.get("penerbit")[i],dataBuku.get("status")[i]])

# cek dan tampilkan data pengguna
def cpguna() :
    tabel.field_names = ["Id" , "Username" , "Password"]
    tabel.clear_rows()
    for i in range (len(dataPengguna.get("username"))) :
        tabel.add_row([i + 1, dataPengguna.get("username")[i], dataPengguna.get("password")[i]])

# Hapus data pengguna
def hpguna(hapus):
    dataPengguna.get("username").pop(hapus)


#-----------------------------------------------------------------------------------------------------#
# Ouput awal
menu_awal()