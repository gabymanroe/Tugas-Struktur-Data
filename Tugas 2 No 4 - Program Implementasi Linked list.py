#KELOMPOK 1:
#Risa Aulia Nisa (1305621009)                   
#Amelia Fatmasari (1305621010)             
#Allyza Yusykarina Safitri (1305621011)       
#Gabriel Olivia Yvonne Manurung (1305621023)  
#Allan Dinen Irlando (1305621032)

print(50*'=')
print('''Dipresentasikan oleh:
- Allyza Yusykarina Safitri (1305621011)
- Gabriel Olivia Yvonne Manurung (1305621023)

Tugas 2 - Nomor 4
Implementasi Linked list (Senarai Berantai)''')
print(50*'=')

print(50*'=')
print('Program Implementasi Linked list')
print(50*'=')

#Input Data   
def list(data):
    while True:
        try:
            n = int(input('Berapa banyak data yang ingin dimasukkan? '))
        except ValueError:
            print('Mohon masukkan banyak data dalam bentuk angka yang valid')
            print()
            continue
        break
    print()
    
    singkatan_nama = []
    nama_lengkap = []
    for i in range(0,n):
        j =input('Singkatan Nama[' + str(i+1) + '] = ')
        singkatan_nama.append(j)
        k = input('Nama Lengkap[' + str(i+1) + '] = ')
        nama_lengkap.append(k)
        print()

    #Print Data Awal
    print('-------[ DATA AWAL ]-------')
    singkatan_nama.reverse()
    nama_lengkap.reverse()
    for i in range (0,n):
        print(singkatan_nama[i],'\t : \t', nama_lengkap[i])
    print('---------------------------')
    print()

    def menu(tampil):
        #Memilih menu yang akan dijalankan
        print('----------------------------')
        print('==========[ MENU ]==========')
        print('----------------------------')
        print('1. Tambah Data')
        print('2. Cari Data')
        print('3. Hapus Data')
        print('4. Tampilkan Data')
        print('5. Exit')
        print('----------------------------')
        print()
        pilih = input('Pilih menu yang akan dijalankan (1/2/3/4/5): ')
        print()

        #Menambah data
        if pilih == '1':
            print('==========[ TAMBAH DATA ]==========')
            print()
            j =input('Singkatan Nama = ')
            singkatan_nama.append(j)
            k = input('Nama Lengkap = ')
            nama_lengkap.append(k)
            print()
            return menu(tampil)

        #Mencari data
        elif pilih == '2':
            print('==========[ CARI DATA ]==========')
            print()
            cari =input('Singkatan nama yang ingin dicari: ')
            print()
            for i in range (0,len(singkatan_nama)):
                if singkatan_nama[i]==cari:
                    print('Pencarian = Singkatan nama', cari, 'ditemukan.')
                    print('Hasil Pencarian = ')
                    print(singkatan_nama[i],':',nama_lengkap[i])
            if cari not in singkatan_nama:
                print('Singkatan nama', cari, 'tidak ditemukan.')       
            print()
            return menu(tampil)

        #Menghapus data
        elif pilih == '3':
            print('==========[ HAPUS DATA ]==========')
            print()
            if n <= 0 :
                print('Data kosong')
            else :
                x = input('Singkatan nama yang ingin dihapus = ')
                print()
                singkatan_nama.reverse()
                nama_lengkap.reverse()  
                if x not in singkatan_nama:
                    print('Singkatan nama yang ingin dihapus tidak ditemukan.')
                elif len(singkatan_nama)==1:
                    singkatan_nama.pop()
                    nama_lengkap.pop()
                    print('Setelah', x, 'dihapus:')
                    print('Data sudah kosong.')
                else:
                    for i in range(0,len(singkatan_nama)):
                        if singkatan_nama[i]==x:
                            singkatan_nama.pop(i)
                            nama_lengkap.pop(i)
                        
                    print('Setelah', x, 'dihapus:')
                    singkatan_nama.reverse()
                    nama_lengkap.reverse() 
                    for i in range(len(singkatan_nama)) :
                        print(singkatan_nama[i],'\t : \t', nama_lengkap[i])   
            print()
            return menu(tampil)
        
        #Menampilkan data
        elif pilih == '4':
            print('==========[ TAMPILKAN DATA ]==========')
            print()
            singkatan_nama.reverse()
            nama_lengkap.reverse()
            print('-----------[ DATA SEKARANG ]----------')
            for i in range (0,len(singkatan_nama)):
                print(singkatan_nama[i],'\t : \t', nama_lengkap[i])
            print('--------------------------------------')
            print()
            return menu(tampil)
        
        #Exit   
        elif pilih == '5':
            print('Terima kasih telah menggunakan program ini.')
            return ''
        
        #Selain pilhan 1,2,3,4,5
        else:
            print('MAAF, DATA YANG ANDA INPUT SALAH, MOHON MASUKKAN DENGAN BENAR')
            return menu(tampil)
    
    #Memanggil def menu(tampil)
    tampil = 'start'

    if tampil == 'start' :
        print(menu(tampil))    
    return ''

#Memanggil def list(data)     
data = 'start'

if data == 'start' :
    print(list(data))
else:
    print('ERROR')

#Menggunakan kembali program implementasi linked list
while True:
    print(50*'=')
    coba_lagi= input('Apakah Anda ingin mencoba lagi? (1=ya | 0=exit): ')
    print(50*'=')
    if coba_lagi == '1':
        print(list(data))
        continue
    elif coba_lagi=='0':
        print('Terima kasih telah menggunakan program ini.')
        break
    else:
        print('MAAF, DATA YANG ANDA INPUT SALAH, MOHON MASUKKAN DENGAN BENAR')
        print()
        continue
