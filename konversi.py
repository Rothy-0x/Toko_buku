print("===Aplikasi Konversi Jarak, Waktu dan Kecepatan===")
user = {"admin": "admin"}

username = input("Username : ")
password = input("Password : ")

if user.get(username) == password:
    print("Login Berhasil")

ulang = "y"
while ulang == "y":
    print("===Menu===")
    print("1. Jarak")
    print("2. Waktu")
    print("3. Kecepatan")
    print("4. Exit")
    masuk = float(input(" Pilih Menu : "))

    if masuk == 1:
        a = float(input("Masukkan Kecepatan (Km/Jam) = "))
        b = float(input("Masukkan Waktu (Jam) = "))

        jarak = a*b
        print("Jarak : ", jarak, "Km")
        print("Selesai")

    elif masuk == 2:
        a = float(input("Masukkan Jarak (Km) = "))
        b = float(input("Masukkan Kecepatan (Km/Jam) = "))

        waktu = a/b
        print("Waktu : ", waktu, "Jam")
        print("Selesai")

    elif masuk == 3:
        a = float(input("Masukkan Jarak (Km) = "))
        b = float(input("Masukkan Waktu (Km/Jam) = "))

        kecepatan = a/b
        print("Kecepatan : ", kecepatan, "(Km/Jam)")
        print("Selesai")

    elif masuk == 4:
        print("Senang bekerja sama dengan anda!")
        raise SystemExit

        ulang = "y"
