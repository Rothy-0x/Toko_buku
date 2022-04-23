import os 

os.system("cls")

dataPelanggan = {
                "nama"   : "",
                "usia"   : [],
                "gender" : [],
                "ePay"   : 0,
                "koin"   : 0,
                "vip"    : 1
                }

dataBarang = {  "nomor"  : ["1", "2", "3"],
                "barang" : ["Semen", "Pasir", "Keramik"],
                "harga"  : [7_000, 2_000, 8_000]  }


index = None

def register(nm, us, gd, ep, ko):
    global index
    dataPelanggan.get("nama").append(nm)
    dataPelanggan.get("usia").append(us)
    dataPelanggan.get("gender").append(gd)
    dataPelanggan.get("ePay").append(ep)
    dataPelanggan.get("koin").append(ko)
    index = dataPelanggan.get("nama").index(nm)

def lobby():
    print("="*5, "LOBBY".center(40), "="*5)
    print(">> 1. Masuk Untuk Beli ")
    print(">> 2. Keluar ")
    lobi = input("$ Masukkan Pilihan : ")
    if lobi == "1":
        menu()
    elif lobi == "2":
        raise SystemExit
    else:
        print(">> Input Tidak Sesuai!")
        return lobby()

def beliKoin():
    print()
    print("="*5, "MENU TAMBAH KOIN".center(40), "="*5)
    print(">> 1. Rp 7.000 mendapatkan koin sebanyak  : 5000 Koin")
    print(">> 2. Rp 10.000 mendapatkan koin sebanyak : 7000 Koin")
    print(">> 3. Rp 13.000 mendapatkan koin sebanyak : 10000 Koin")
    koinB = input("Paket = ")
    if koinB == "1" :
        print(">> KOIN Berhasil Terisi")
        hargaKoin = 7000
        kurangEpay = dataPelanggan.get("ePay")[index] - hargaKoin
        koinB = 5000
        tambah = dataPelanggan["koin"][index] + koinB
        dataPelanggan.get("koin").pop (index)
        dataPelanggan.get("koin").append (tambah)
        print(f"Saldo KOIN Anda Adalah {tambah}")
        print(f"Saldo E-Pay Anda Sekarang Adalah {kurangEpay}")
        return menuToko()
    elif koinB == "2" :
        print(">> KOIN Berhasil Terisi")
        hargaKoin = 10000
        kurangEpay = dataPelanggan.get("ePay")[index] - hargaKoin
        koinB = 7000
        tambah = dataPelanggan.get("koin")[index] + koinB
        print(f"Saldo KOIN anda adalah {tambah}")
        print(f"Saldo E-Pay Anda Sekarang Adalah {kurangEpay}")
        return menuToko()
    elif koinB == "3":
        print(">> KOIN Berhasil Terisi")
        hargaKoin = 13000
        kurangEpay = dataPelanggan["ePay"] - hargaKoin
        koinB = 10000
        tambah = dataPelanggan["koin"] + koinB
        dataPelanggan["koin"] = tambah
        print(f"Saldo KOIN anda adalah {tambah}")
        print(f"Saldo E-Pay Anda Sekarang Adalah {kurangEpay}")
        return menuToko()
    else: 
        print(">> Maaf Inputan Anda Tidak Sesuai !")
        return beliKoin()

def beliBarang():
    print()
    print("="*5, "MENU ITEMS".center(35), "="*5)
    print(">> 1. Semen   : 7000 Koin/KG") 
    print(">> 2. Pasir   : 2000 Koin/SAK")
    print(">> 3. Keramik : 8000 Koin/Buah")
    print()
    pilih = input("Masukan Pilihan Anda: ")
    cariin = dataBarang.get("nomor").index(pilih)
    if pilih in dataBarang["nomor"]:
        jumlah = int(input("$ Beli Berapa? : "))
        harga  = dataBarang["harga"][cariin]
        total  = harga * jumlah
        print(f">> Anda akan membelinya sebanyak  {jumlah} dengan Harga {total} KOIN")    
        return menuToko()
    else:
        print (">> Barang TIDAK ADA")
        return beliBarang()

def memVIP():
    try:
        print("*** PEMBELIAN VIP ***")
        print("Harga VIP adalah Rp.75000 dengan ePay dan 3500 dengan KOIN ")
        konfir = input("Apakah Anda yakin ingin membeli VIP? (ya/tidak) : ")
        if konfir == "ya":
            konfir2 = input("Apakah Anda Ingin Menggunakan (1). E-Pay / (2) KOIN Untuk Melakukan Transaksi ? : ")
            if konfir2 == "1":
                if dataPelanggan["ePay"] < 75000:
                    print(">> Maaf E-Pay Anda Tidak Mencukupi Silahkan Top Up Kembali!")
                    return menuToko()
                else:
                    vip = dataPelanggan["vip"] - 1
                    dataPelanggan["vip"] = vip
                    harga_vip = 7500
                    saldo_sekarang = dataPelanggan["ePay"] - harga_vip
                    print(">>",dataPelanggan["nama"],"Sekarang Menjadi User VIP")
                    print("Saldo Anda sekarang adalah", saldo_sekarang)
                    dataPelanggan["ePay"] = saldo_sekarang
                    bl = input("$ Ingin Membeli Barang Dengan Diskon (y/n) : ")
                    if bl == "y":
                        beli_VIP()
                    else:
                        menuToko()
            elif konfir2 == "2" :
                if dataPelanggan["koin"] < 3500:
                    print(">> Maaf KOIN Anda Tidak Mencukupi Silahkan Top Up Terlebih Dahulu!")
                    beliKoin()
                else:
                    vip = dataPelanggan["vip"] - 1
                    dataPelanggan["vip"] = vip
                    harga_vip = 3500
                    saldo_sekarang = dataPelanggan["koin"] - harga_vip
                    dataPelanggan["koin"] = saldo_sekarang
                    print("VIP telah Dibeli")
                    print("Sekarang ", dataPelanggan["nama"], "Telah Berlangganan VIP")
                    print("Saldo Anda sekarang adalah", dataPelanggan["koin"])
                    bl = input("ingin beli barang dengan VIP? (y/n) : ")
                    if bl == "y":
                        beli_VIP()
                    else:
                        menuToko()
            else:
                print("Maaf Inputan anda salah !!!!")
                return memVIP()
        else :
            print("Maaf Inputan anda salah !!!!")
            return memVIP()
    except ValueError:
        print("Pastikan INPUT yang BENAR")

def beli_VIP():
    if dataPelanggan["vip"] < 1 :
        while True:
            try:
                bangunan = input(">> Beli Barang Apa ? : ")
                if bangunan in dataBarang.get("barang"):
                    dataBarangbeli = dataBarang.get("barang").index(bangunan)
                    harga = dataBarang["harga"][dataBarangbeli] * 20/100
                    hrg = dataBarang["harga"][dataBarangbeli]-harga
                    while True:
                        jumlah = int(input("$ Jumlah Barang Yang Ingin Di Beli : "))
                        if jumlah <=0:
                            print(">> Jumlah Tidak Boleh Minus")
                        else:
                            total = jumlah * hrg
                            while True:
                                print(f"Total yang harus dibayar = {total}")
                                bayar = int(input(">> Uang Anda : "))
                                sisa = dataPelanggan["koin"] - bayar
                                dataPelanggan["koin"] = sisa
                                if bayar < 0 :
                                    print("Uang Kurang!")
                                else:
                                    kembalian = bayar - total
                                    if kembalian < 0:
                                        print(">> Uang Anda Kurang")
                                        return menu()
                                    else:
                                        print(f"Kembalian Anda = {kembalian}")
                                        print("Terimakasih")
                                        vip = dataPelanggan["vip"] + 1
                                        dataPelanggan["vip"] = vip
                                        menu()
                else:
                    print(f"Maaf {bangunan} tidak ada")
            except ValueError:
                print("Terjadi Eror")

def menu():
    print("="*5, "SILAHKAN ISI DATA DIRI".center(40), "="*5)
    global namaPelanggan
    namaPelanggan = input("$ Siapa Nama Anda : ")
    namaPelanggan = namaPelanggan.capitalize()
    dataPelanggan["nama"] = namaPelanggan
    usiaPelanggan = int(input("$ Berapa Usia Anda : "))
    dataPelanggan["usia"] = usiaPelanggan
    if usiaPelanggan < 17:
        print(">> Anda Harus Memiliki KTP Untuk Belanja Disini !")
        print(">> Biarkan Orang Tua Anda Yang Membeli")
        menu()
    else:
        genderPelanggan = input("$ [L/P] (?) : ")
        genderPelanggan = genderPelanggan.upper()
        dataPelanggan["gender"] = genderPelanggan
        uangPelanggan = int(input("$ Berapa Saldo E-Pay Anda : "))
        dataPelanggan["ePay"] = uangPelanggan
        uang = 0

        
        if usiaPelanggan <= 30 and genderPelanggan == "L" or genderPelanggan == "l":
            print(f">> Selamat Datang Bang {namaPelanggan}")
            print(f"Saldo E-Pay Anda {uangPelanggan}")
            print(f"Saldo Koin Anda {uang}")
            print("Anda Harus Menggunakan Koin Untuk Membeli Barang, Gunakan E-Pay Anda Untuk Membeli Koin!")
            return menuToko()
        if usiaPelanggan <= 40 and genderPelanggan == "L" or genderPelanggan == "l":
            print(f">> Selamat Datang Pak {namaPelanggan}")
            print(f"Saldo E-Pay Anda {uangPelanggan}")
            print(f"Saldo Koin Anda {uang}")
            print("Anda Harus Menggunakan Koin Untuk Membeli Barang, Gunakan E-Pay Anda Untuk Membeli Koin!")
            return menuToko()
        if usiaPelanggan <= 65 and genderPelanggan == "L" or genderPelanggan == "l":
            print(f">> Selamat Datang Kakek {namaPelanggan}")
            print(f"Saldo E-Pay Anda {uangPelanggan}")
            print(f"Saldo Koin Anda {uang}")
            print("Anda Harus Menggunakan Koin Untuk Membeli Barang, Gunakan E-Pay Anda Untuk Membeli Koin!")
            return menuToko()
        if usiaPelanggan <= 25 and genderPelanggan == "P" or genderPelanggan == "p":
            print(f">> Selamat Datang Mba {namaPelanggan}")
            print(f"Saldo E-Pay Anda {uangPelanggan}")
            print(f"Saldo Koin Anda {uang}")
            print("Anda Harus Menggunakan Koin Untuk Membeli Barang, Gunakan E-Pay Anda Untuk Membeli Koin!")
            return menuToko()
        if usiaPelanggan <= 40 and genderPelanggan == "P" or genderPelanggan == "p":
            print(f">> Selamat Datang Bu {namaPelanggan}")
            print(f"Saldo E-Pay Anda {uangPelanggan}")
            print(f"Saldo Koin Anda {uang}")
            print("Anda Harus Menggunakan Koin Untuk Membeli Barang, Gunakan E-Pay Anda Untuk Membeli Koin!")
            return menuToko()
        if usiaPelanggan <= 65 and genderPelanggan == "P" or genderPelanggan == "p":
            print(f">> Selamat Datang Nenek {namaPelanggan}")
            print(f"Saldo E-Pay Anda {uangPelanggan}")
            print(f"Saldo Koin Anda {uang}")
            print("Anda Harus Menggunakan Koin Untuk Membeli Barang, Gunakan E-Pay Anda Untuk Membeli Koin!")
            return menuToko()
            
        

def menuToko():
    print("="*5, "LIST MENU TOKO".center(40), "="*5)
    print(">> 1. Beli Koin")
    print(">> 2. Beli Barang")
    print(">> 3. Join VIP dan Dapatkan DISKONNYA!")
    print(">> 4. Kembali Ke Lobby")
    print(">> 5. Exit")
    option = input("$ Tentukan Pilihan Anda : ")
    # try:
    if option == "1":
        return beliKoin()
    elif option == "2":
        return beliBarang()
    elif option == "3":
        memVIP()
    elif option == "4":
        print()
    elif option == "5":
        print()
    else:
        print(">> Terjadi Error !")
        return menuToko()

lobby()


