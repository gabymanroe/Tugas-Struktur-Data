#KELOMPOK 1:
#Risa Aulia Nisa (1305621009)                   
#Amelia Fatmasari (1305621010)             
#Allyza Yusykarina Safitri(1305621011)       
#Gabriel Olivia Yvonne Manurung (1305621023)         
#Allan Dinen Irlando (1305621032)

print(50*'=')
print('''Dipresentasikan oleh:


Gabriel Olivia Yvonne Manurung (1305621023)

Tugas 4 - Nomor 3
Selection Sort''')

print(50*'=')
print()

data = []

def menu(tampil):
    #Memilih menu yang akan dijalankan
    print('----------------------------------')
    print('=============[ MENU ]=============')
    print('----------------------------------')
    print('1. Tambah Data')
    print('2. Mengurutkan secara Ascending')
    print('3. Mengurutkan secara Descending')
    print('4. Mengurutkan secara Ascending dan Descending')
    print('5. Restart (Data Baru)')
    print('6. Exit')
    print('----------------------------------')
    print()
    pilih = input('Pilih menu yang akan dijalankan (1/2/3/4/5/6): ')
    print()

    #Memasukkan Data
    if pilih == '1':
        print('==========[ TAMBAH DATA ]==========')
        print()
        while True:
            try:
                n = int(input('Berapa banyak data yang ingin diurutkan? '))
                if n>=0:
                    for i in range(n):
                        isi = float(input('Bilangan ke-'+ str(i+1) + ': '))
                        data.append(isi)
                    print()
                    print('Data sekarang:')
                    print(data)
                    break
                else:
                    print('Mohon masukkan banyak data dalam bilangan bulat positif.')
                    print()
            except ValueError:
                print('Mohon masukkan banyak data dalam bentuk angka yang valid.')
                print()
                continue
                break
        print()
        return menu(tampil)
    
    #Ascending (Mengurutkan dari Terkecil ke Terbesar)
    elif pilih == '2':
        print('==========[ ASCENDING ]==========')
        print()
        if len(data) == 0:
            print('Data masih kosong.')
            print()
        else:
            len(data)>0
            data1 = []
            data1.extend(data)
            print('Data sebelum diurutkan:')
            print(data1)
            print()
            tahap = 0
            for i in range (0,len(data1)-1):
                nilai_min = i
                for j in range (i + 1, len(data1)):
                    if data1[j] < data1[nilai_min]:
                        nilai_min = j                   
                data1[i], data1[nilai_min] = data1[nilai_min], data1[i] #swap
                tahap = tahap + 1
                print('Tahap',tahap,':',data1)
            print()
            print('Setelah diurutkan secara Ascending:')
            print(data1)
            print()
        return menu(tampil)

    #Descending (Mengurutkan dari Terbesar ke Terkecil)
    elif pilih == '3':
        print('==========[ DESCENDING ]==========')
        print()
        if len(data) == 0:
            print('Data masih kosong.')
            print()
        else:
            len(data)>0
            data2 = []
            data2.extend(data)
            print('Data sebelum diurutkan:')
            print(data2)
            print()
            tahap = 0
            for i in range (0,len(data2)-1):
                nilai_min = i
                for j in range (i + 1, len(data2)):
                    if data2[j] > data2[nilai_min]:
                        nilai_min = j                   
                data2[i], data2[nilai_min] = data2[nilai_min], data2[i] #swap
                tahap = tahap + 1
                print('Tahap',tahap,':',data2)
            print()
            print('Setelah diurutkan secara Descending:')
            print(data2)
            print()
        return menu(tampil)

    #Mengurutkan secara Ascending dan Descending
    elif pilih == '4':
        print('==========[ ASCENDING ]==========')
        print()
        if len(data) == 0:
            print('Data masih kosong.')
            print()
        else:
            len(data)>0
            data1 = []
            data1.extend(data)
            print('Data sebelum diurutkan:')
            print(data1)
            print()
            tahap = 0
            for i in range (0,len(data1)-1):
                nilai_min = i
                for j in range (i + 1, len(data1)):
                    if data1[j] < data1[nilai_min]:
                        nilai_min = j                   
                data1[i], data1[nilai_min] = data1[nilai_min], data1[i] #swap
                tahap = tahap + 1
                print('Tahap',tahap,':',data1)
            print()
            print('Setelah diurutkan secara Ascending:')
            print(data1)
            print()
            
        print('==========[ DESCENDING ]==========')
        print()
        if len(data) == 0:
            print('Data masih kosong.')
            print()
        else:
            len(data)>0
            data2 = []
            data2.extend(data)
            print('Data sebelum diurutkan:')
            print(data2)
            print()
            tahap = 0
            for i in range (0,len(data2)-1):
                nilai_min = i
                for j in range (i + 1, len(data2)):
                    if data2[j] > data2[nilai_min]:
                        nilai_min = j                   
                data2[i], data2[nilai_min] = data2[nilai_min], data2[i] #swap
                tahap = tahap + 1
                print('Tahap',tahap,':',data2)
            print()
            print('Setelah diurutkan secara Descending:')
            print(data2)
            print()
        return menu(tampil)

    #Restart
    elif pilih == '5':
        if len(data) == 0:
            print('Data masih kosong.')
            print()
        else:
            len(data)>0
            print('==========[ RESTART ]==========')
            print()
            data.clear()
            print('Program berhasil direstart & semua data telah dihapus.')
            print('Silakan masukkan kembali data terbaru.')
            print()
        return menu(tampil)
       
    #Exit
    elif pilih == '6':
        while True:
            print(50*'=')
            coba_lagi= input('Apakah Anda ingin mencoba lagi? (1=ya | 0=exit): ')
            print(50*'=')
            if coba_lagi == '1':
                data.clear()
                print (menu(tampil))
            elif coba_lagi == '0':
                print('Terima kasih telah menggunakan program ini.')
                exit()
            else:
                print('MAAF, DATA YANG ANDA INPUT SALAH, MOHON MASUKKAN ANGKA 1/0 SAJA.')
                continue

    #Selain pilih 1,2,3,4,5,6
    else:
        print('MAAF, DATA YANG ANDA INPUT SALAH, MOHON MASUKKAN ANGKA 1/2/3/4/5/6/7 SAJA.')
        return menu(tampil)


#Memanggil def menu(tampil)
tampil = 'start'

if tampil == 'start' :
    print(menu(tampil))    
