def mergesort(lst):  # fungsi untuk mengurutkan list
    if len(lst) <= 1:  # panjang list kurang dari atau sama dengan 1
        return lst  # jika list kurang dari atau sama dengan 1, maka return list

# membelah list menjadi 2 bagian, bagian kiri dan kanan
    middle = len(lst) // 2

    left = mergesort(lst[0:middle])  # membelah bagian kiri
    right = mergesort(lst[middle:len(lst)])  # membelah bagian kanan

    return merge(left, right)


def merge(left, right):  # fungsi untuk menggabungkan 2 list
    result = []  # membuat list kosong
    a, b = 0, 0  # membuat index kosong

    while a < len(left) and b < len(right):  # mengecek apakah index kiri dan kanan masih ada

    # mengecek apakah salah satu left atau right ada yang isalpha atau alphabet
        if str(left[a]).isalpha() or str(right[b]).isalpha():
            compare = str(left[a]) < str(right[b])
        else:
            compare = int(left[a]) < int(right[b])

        if compare:  # jika index kiri lebih kecil dari index kanan
            result.append(left[a])  # maka append index kiri ke list kosong
            a += 1  # index kiri bertambah 1
        else:  # jika index kanan lebih kecil dari index kiri
            result.append(right[b])  # maka append index kanan ke list kosong
            b += 1  # index kanan bertambah 1

    result += left[a:]  # mengecek apakah index kiri masih ada atau tidak
    result += right[b:]  # mengecek apakah index kanan masih ada atau tidak

    return result


soal2 = [31, 49, 16, 27, 36, 15, 8, 17, 2, 50]
jawab2 = mergesort(soal2)

print(jawab2)