import os
from prettytable import PrettyTable


#User
user = {'username':'Nabila', 'pw':'123'}

# List coffee
ListCoffe = ['Americano', 'Cappuccino', 'Mochaccino', 'Espresso', 'Hazelnut Latte']
Price = ['15000', '20000', '20000', '25000', '30000']

# Hapus Terminal
def cls():
    os.system('cls')

# Nomor menu dan jumlah pesanan
no_list = [1,2,3,4,5]
psn = [0,0,0,0,0]

# Table
def tbl1():
    x = PrettyTable()
    x.add_column("No",no_list)
    x.add_column("Pilihan Menu",ListCoffe)
    x.add_column("Harga",Price)
    print(x)


def tbl2():
    x = PrettyTable()
    x.add_column("No",no_list)
    x.add_column("Pilihan Menu",ListCoffe)
    x.add_column("Harga",Price)
    x.add_column("Pesanan",psn)
    print(x)

#  Login User    
def login():
 while True:
    print("="*15)
    print("Silahkan Login")
    print("="*15)

    id = input("Silahkan masukkan username anda : ")
    password = input("Silahkan masukkan password anda : ")
    
    if id == user['username'] and password == user['pw']:
        print("="*15)
        print("Anda berhasil login")
        print("="*15)

    else:
        cls()
        print("="*50)
        print(" Username Atau Password Salah! ")
        print("="*50)
        continue

# Menu 
    restart = "y"
    while restart == "y":
        cls()
        print("="*50)
        print(" Coffee Shop ")
        print("="*50)
        print("1. List Coffee")
        print("2. Pemesanan")
        print("3. Cek pemesanan")
        print("4. Delete")
        print("5. Exit")
        print("="*50)
        plhh = input("Pilihan Anda : ")

        if plhh == '1':
            cls()
            tbl1()
            restart = input("Apakah Anda Ingin Kembali Ke Menu Awal ? y/n : ")
            if restart == "n":
                quit()
            print()
        
        elif plhh == '2':
            cls()
            print("1. Americano")
            print("2. Cappuccino")
            print("3. Mochaccino")
            print("4. Espresso")
            print("5. Hazelnut Latte")
            pilih = input("Pilih pesanan: ")
            if pilih == '1':
                pilih = int(psn[0]+ 1)
                psn[0] = pilih
            elif pilih == '2':
                pilih = int(psn[1]+ 1)
                psn[1] = pilih
            elif pilih == '3':
                pilih = int(psn[2]+ 1)
                psn[2] = pilih
            elif pilih == '4':
                pilih = int(psn[3]+ 1)
                psn[3] = pilih
            elif pilih == '5':
                pilih = int(psn[4]+ 1)
                psn[4] = pilih
            restart = input("Apakah Anda Ingin Kembali Ke Menu Awal ? y/n : ")
            if restart == "n":
                quit()
            print()
        
        elif plhh == '3':
            cls()
            tbl2()
            restart = input("Apakah Anda Ingin Kembali Ke Menu Awal ? y/n : ")
            if restart == "n":
                quit()
            print()
        
        elif plhh == '4':
            cls()
            print("1. Americano")
            print("2. Cappuccino")
            print("3. Mochaccino")
            print("4. Espresso")
            print("5. Hazelnut Latte")
            pilih = input("Pilih pesanan yang dihapus: ")
            if pilih == '1':
                pilih = int(psn[0]- 1)
                psn[0] = pilih
            elif pilih == '2':
                pilih = int(psn[1]- 1)
                psn[1] = pilih
            elif pilih == '3':
                pilih = int(psn[2]- 1)
                psn[2] = pilih
            elif pilih == '4':
                pilih = int(psn[3]- 1)
                psn[3] = pilih
            elif pilih == '5':
                pilih = int(psn[4]- 1)
                psn[4] = pilih
            restart = input("Apakah Anda Ingin Kembali Ke Menu Awal ? y/n : ")
            if restart == "n":
                quit()
            print()
            
        elif plhh == '5':
            cls()
            quit()

login()