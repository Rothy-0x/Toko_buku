users = {
    "Nama":  ["Alby", "Natalin"],
    "Pin": ["1802", "2912"],
    "No_rek": ["00612", "00628"],
    "Saldo": [750000, 500000],
}


def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p


def ceksaldo(data):
    saldo = users.get("Saldo")[data]
    print(f'\nSaldo Anda {formatrupiah(saldo)}')
    return


def transfer(data):
    no_rek = input('Masukan No Rekening : ')

    index = users.get("No_rek").index(no_rek)
    nama = users.get('Nama')[index]

    if no_rek in users.get("No_rek")[index]:
        print(f'\nNama Pemilik Akun Adalah {nama}')
        tf = int(input('Masukan Nominal Yang ingin di Transfer : '))
        konfirmasi = input(
            'Apakah Anda Yaking Ingin Mentransfer ? (y/n) : ')
        if konfirmasi == 'y':
            saldo = users.get("Saldo")[data] - tf

            users.get("Saldo")[data] = saldo
            print(f'Berhasil, Jumlah Transaksi Sebesar {formatrupiah(tf)}')
            print(f'Saldo Anda Sisa {formatrupiah(saldo)}')
        elif konfirmasi == 'n':
            return
    else:
        print('Nomor Rekening Tidak  Di Temukan ')
        return


def main(data):
    a = False
    while a == False:
        pilihan = menu()
        if pilihan == '1':
            ceksaldo(data)
        elif pilihan == '2':
            transfer(data)
        elif pilihan == '3':
            exit()
        else:
            print("MASUKAN PILIHAN YANG SESUAI")


def menu():
    print("=" * 42)
    print("="*5, "ATM BERJAYA".center(30), "="*5)
    print("=" * 42)
    print('1. Cek Saldo')
    print('2. Tranfers Uang')
    print('3. Exit')
    print("=" * 42)

    pilihan = input("Masukan Pilihan : ")

    return pilihan


def login():
    nama = input("\nMasukan Nama Anda : ")
    pin = input("Masukan Pin Anda : ")
    try:
        search_user = users.get("Nama").index(nama)
        if nama in users.get("Nama")[search_user] and pin == users.get("Pin")[search_user]:
            print("Berhasil Login")
            main(search_user)
        else:
            print("Gagal Login Password Anda Salah!")
            konfirmasi = input('ingin login lagi ? (y/n) : ')
            if konfirmasi == 'y':
                login()
            else:
                print("Sampai Jumpa!")
                exit()
    except ValueError:
        print("Maaf Data Tidak Di Temukan !")


login()
