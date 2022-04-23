import os

def cls():
    os.system('cls')
    
def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp. ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p

def hasilpersen(jumlah, persen) :
  return (jumlah / 100) * persen

cls()
print("Silahkan Masukkan Gaji dan Total Jam Lembur Anda!!!")
gp = int(input('> Gaji pokok       : '))
total_jam = int(input('> Total jam lembur : ') or 0)


tj = hasilpersen(gp, 15)
lembur = total_jam * hasilpersen(gp, 5)
total_gaji = gp + tj+ lembur


print('=' * 37)
print("="*5, "Gaji Karyawan".center(25), "="*5)
print("=" * 37)
print(f'> Gaji pokok   : {formatrupiah(gp)}')
print(f'> Tunjangan    : {formatrupiah(int(tj))}')
print(f'> Upah lembur  : {formatrupiah(int(lembur))}')
print(f'> Total Gaji Anda adalah {formatrupiah(int(total_gaji))}')
print("=" * 37)