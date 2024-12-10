#Kelompok 1
#Risa Aulia Nisa                (1305621009)
#Amelia Fatmasari               (1305621010)
#Allyza Yusykarina Safitri      (1305621011)
#Gabriel Olivia Yvonne Manurung (1305621023)
#Allan Dinen Irlando            (1305621032)


print()
print('Amelia Fatmasari                (1305621010)')
print('Gabriel Olivia Yvonne Manurung  (1305621023)')
print()
print('Tugas 4')
print('Nomor 1')
print()
print('-----------------------------------------------------------------------')
print('                 Selamat Datang di Program Quick Sort                  ')         
print('-----------------------------------------------------------------------')
print()


data1 = []
data2 = []

urutanitrs = 1

def masukkan():
    while True:
        try:
            a = int(input('Banyak data yang ingin dimasukkan: '))
            print()
            if a >= 0:   
                break
            else:
                print('Ketik banyak data dalam bilangan bulat positif (1/2/3/.../dst)')
                print()
        except ValueError:
            print('Ketik banyak data dalam bilangan bulat positif (Berupa nomor bukan huruf)')
            print()
            
    if a == 0:
        print('Tidak ada data yang dimasukkan (Data kosong). Silakan pilih dan ketik nomor "4".')
    else:
        for i in range (0, a):
            j = float(input('Data ' + str(i+1) + ': '))
            data1.append(j)
            data2.append(j)
        print()
        print('Isi data awal: ')
        for i in range(0, len(data1)-1):
            print(data1[i], end=', ')
        print(data1[len(data1)-1])
    return menu()


def menu():
    print()
    print('========================================================================')
    print('Silakan pilih menu di bawah ini: ')
    print('1. Mengurutkan data secara ascending')
    print('2. Mengurutkan data secara descending')
    print('3. Mengurutkan data secara ascending dan descending')
    print('4. Menambah data')
    print('5. Menghapus data')
    print('6. Restart data')
    print('7. Selesai')
    q = input('Jawab: ')
    print()
    if q == '1':
        if len(data1 and data2) <= 0:
            print('Tidak ada data (Data kosong). Silakan pilih dan ketik nomor "4".')
        else:
            print('---------------------------------------------------------------------')
            print('                     Pengurutan Secara Ascending                     ')
            print('---------------------------------------------------------------------')
            print()
            for d in range(len(data2)):
                data2.clear()
            for f in range(len(data1)):
                data2.append(data1[f])
            print('Data sebelum diurut:', data2)
            hasil = quickSortAscending(data2, 0, len(data2) - 1)
            print('Data setelah diurut:', data2)
            global urutanitrs
            urutanitrs = 1
        return menu()
      
    elif q == '2':
        if len(data1 and data2) <= 0:
            print('Tidak ada data (Data kosong). Silakan pilih dan ketik nomor "4".')
        else:
            print('---------------------------------------------------------------------')
            print('                    Pengurutan Secara Descending                     ')
            print('---------------------------------------------------------------------')
            print()
            for d in range(len(data2)):
                data2.clear()
            for f in range(len(data1)):
                data2.append(data1[f])
            print('Data sebelum diurut:', data2)
            hasil = quickSortDescending(data2, 0, len(data2) - 1)
            print('Data setelah diurut:', data2)      
            urutanitrs = 1
        return menu()

    elif q == '3':
        if len(data1 and data2) <= 0:
            print('Tidak ada data (Data kosong). Silakan pilih dan ketik nomor "4".')
        else:
            print('---------------------------------------------------------------------')
            print('                     Pengurutan Secara Ascending                     ')
            print('---------------------------------------------------------------------')
            print()
            for d in range(len(data2)):
                data2.clear()
            for f in range(len(data1)):
                data2.append(data1[f])
            print('Data sebelum diurut:', data2)
            hasil = quickSortAscending(data2, 0, len(data2) - 1)
            print('Data setelah diurut:', data2)      
            urutanitrs = 1
            print()
            print()
            print('---------------------------------------------------------------------')
            print('                    Pengurutan Secara Descending                     ')
            print('---------------------------------------------------------------------')
            print()
            for d in range(len(data2)):
                data2.clear()
            for f in range(len(data1)):
                data2.append(data1[f])
            print('Data sebelum diurut:', data2)
            hasil = quickSortDescending(data2, 0, len(data2) - 1)
            print('Data setelah diurut:', data2)   
            urutanitrs = 1
        return menu()

    elif q == '4':
        print('---------------------------------------------------------------------')
        print('                           Penambahan data                           ')
        print('---------------------------------------------------------------------')
        print()
        while True:
            try:
                b = int(input('Banyak data yang ingin ditambahkan: '))
                print()
                if b >= 1:
                    break
                else:
                    print('Ketik banyak data dalam bilangan bulat positif (1/2/3/.../dst)')
                    print()
            except ValueError:
                print('Ketik banyak data dalam bilangan bulat positif (Berupa nomor bukan huruf)')
                print()

        for i in range (0, b):
            j = float(input('Data ' + str(i+1) + ': '))
            data1.append(j)
            data2.append(j)
            print('Data', j, 'ditambahkan')
        print()
        print('Isi data sekarang: ')
        for i in range(0, len(data1)-1):
            print(data1[i], end=', ')
        print(data1[len(data1)-1])
        return menu()

    elif q == '5':
        if len(data1 and data2) <= 0:
            print('Tidak ada data yang dapat dihapus (Data kosong). Silakan pilih dan ketik nomor "4".')
            return menu()
        else:
            print('---------------------------------------------------------------------')
            print('                           Penghapusan data                          ')
            print('---------------------------------------------------------------------')
            print()
            print('Isi data: ')
            for i in range(0, len(data1)-1):
                print(data1[i], end=', ')
            print(data1[len(data1)-1])
            print()

            while True:
                try:
                    c = int(input('Banyak data yang ingin dihapus: '))
                    print()
                    if c >= 1:
                        for i in range (0, c):
                            k = float(input('Data ' + str(i+1) + ': '))
                            if k in data1 and data2:
                                data1.remove(k)
                                data2.remove(k)
                                print('Data', k, 'dihapus')
                            else:
                                print('Data tidak ditemukan sehingga tidak dapat dihapus')
                        break
                    else:
                        print('Ketik banyak data dalam bilangan bulat positif (1/2/3/.../dst)')
                        print()
                except ValueError:
                    print('Ketik banyak data dalam bilangan bulat positif (Berupa nomor bukan huruf)')
                    print()

            print()
            print('Isi data sekarang: ')
            if len(data1) == 0:
                print('Tidak ada data (Data kosong)')
            else:
                for i in range(0, len(data1)-1):
                    print(data1[i], end=', ')
                print(data1[len(data1)-1])
            return menu()

    elif q == '6':
        for t in range(len(data1)):
            data1.clear()
        print('Program sudah berhasil direstart, semua data telah dihapus')
        print()
        print('Silakan masukkan kembali data terbaru')
        print()
        print('-----------------------------------------------------------------------')
        print()
        return masukkan()
      
    elif q == '7':
        print('Program diakhiri')
        print()
        print('Terima kasih sudah menggunakan program ini ^-^')
        return ''
  
    else:
        print('Pilih dan ketik nomor sesuai menu yang ingin digunakan (1/2/3/4/5/6/7)')
        return menu()

  
def partitionAscending(array, low, high):
    global urutanitrs
    pivot = array[high]
    print('Pivot', pivot)
    s = low - 1
    for k in range(low, high):
        if array[k] <= pivot:
            s = s + 1
            (array[s], array[k]) = (array[k], array[s])            
            print(array[k], 'tukar dengan', array[s])
            print(array)
            print()
    (array[s + 1], array[high]) = (array[high], array[s + 1])
    print(array[k+1], 'tukar dengan', array[s + 1])
    print(array)
    print('-------------------------------------------------------')
    print()
    print('Iterasi ', urutanitrs, ':',  array)
    urutanitrs = urutanitrs + 1
    return s + 1
    
def quickSortAscending(array, low, high):
    if low < high:
        f = partitionAscending(array, low, high)
        quickSortAscending(array, low, f - 1)
        quickSortAscending(array, f + 1, high)


def partitionDescending(array, low, high):
    global urutanitrs
    pivot = array[high]
    print('Pivot', pivot)
    s = low - 1
    for k in range(low, high):
        if array[k] >= pivot:
            s = s + 1
            (array[s], array[k]) = (array[k], array[s])
            print(array[k], 'tukar dengan', array[s])
            print(array)
            print()
    (array[s + 1], array[high]) = (array[high], array[s + 1])
    print(array[k+1], 'tukar dengan', array[s + 1])
    print(array)
    print('-------------------------------------------------------')
    print()
    print('Iterasi ', urutanitrs, ':', array)
    urutanitrs = urutanitrs + 1
    return s + 1

def quickSortDescending(array, low, high):
    if low < high:
        f = partitionDescending(array, low, high)
        quickSortDescending(array, low, f - 1)
        quickSortDescending(array, f + 1, high)


masukkan()
