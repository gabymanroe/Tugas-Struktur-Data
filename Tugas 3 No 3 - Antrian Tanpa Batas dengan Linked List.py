#KELOMPOK 1:
#Risa Aulia Nisa (1305621009)                   
#Amelia Fatmasari (1305621010)             
#Allyza Yusykarina Safitri (1305621011)       
#Gabriel Olivia Yvonne Manurung (1305621023)         
#Allan Dinen Irlando (1305621032)

print(50*'=')
print('''Dipresentasikan oleh:
Gabriel Olivia Yvonne Manurung (1305621023)

Tugas 3 - Nomor 3
Antrian Tanpa Batas dengan Linked List''')

print(50*'=')

class Antrian:
    def __init__(self):
        self.list=[]
    def insert(self, item):
        self.list.append(item)
    def __str__(self):
        if len(self.list) == 0:
            print('Antrian kosong')
        else:
            for i in range (len(self.list)):
                print (self.list[i])
    def remove(self):
        if len(self.list) <= 0:
            print('Tidak ada data yang dimasukkan')
        else:
            delete=input('Masukkan data yang ingin dihapus: ')
            if delete in self.list:
                self.list.remove(delete)
                print('Data',delete, 'berhasil dihapus.')
                print()
                print('Isi antrian setelah diambil satu data:')
                antrian.__str__()
            else:
                print('Data tidak ada di dalam antrian.')    
    def getSize(self):
        return len(self.list)

antrian = Antrian()
def menu(tampil):
    #Memilih menu yang akan dijalankan
    print('----------------------------')
    print('==========[ MENU ]==========')
    print('----------------------------')
    print('1. Masukkan data ke antrian')
    print('2. Hapus data pada antrian')
    print('3. Tampilkan antrian')
    print('4. Tampilkan banyak antrian')
    print('5. Selesai')
    print('----------------------------')
    print()
    pilih = input('Pilih menu yang akan dijalankan (1/2/3/4/5): ')
    print()

    #Memasukkan data ke antrian
    if pilih == '1':
        print('==========[ MEMASUKKAN DATA ]==========')
        while True:
            try:
                n = int(input('Berapa banyak data yang ingin dimasukkan? '))
                if n>=0:
                    break
                else:
                    print('Mohon masukkan banyak data dalam bilangan bulat positif.')
            except ValueError:
                print('Mohon masukkan banyak data dalam bentuk angka yang valid.')
                print()
                continue
            break

        for i in range (n):
            j = antrian.insert(input('Masukkan data yang ingin dimasukkan ke antrian: '))
            print('Data berhasil dimasukkan ke antrian.')
        print()
        print('Isi antrian setelah data dimasukkan:')
        antrian.__str__()
        print()
        return menu(tampil)

    #Hapus data pada antrian
    elif pilih == '2':
        print('==========[ HAPUS DATA ]==========')
        antrian.remove()
        print()
        return menu(tampil)

    #Menampilkan antrian   
    elif pilih == '3':
        print('==========[ MENAMPILAN ANTRIAN ]==========')
        antrian.__str__()
        print()
        return menu(tampil)
    
    #Menampilkan banyak antrian    
    elif pilih == '4':
        print('==========[ MENAMPILAN BANYAK ANTRIAN ]==========')
        x = antrian.getSize()
        print('Banyak antrian: ', x)
        print()
        return menu(tampil)

    #Exit   
    elif pilih =='5':
        while True:      
            coba_lagi= input('Apakah Anda ingin mencoba lagi? (1=ya | 0=exit): ')
            if coba_lagi == '1':
                print (menu(tampil))
            elif coba_lagi == '0':
                print('Terima kasih telah menggunakan program ini.')
                exit()
            else:
                print('MAAF, DATA YANG ANDA INPUT SALAH, MOHON MASUKKAN ANGKA 1/0 SAJA.')
                continue

    #Selain pilih 1,2,3,4,5
    else:
        print('MAAF, DATA YANG ANDA INPUT SALAH, MOHON MASUKKAN ANGKA 1/2/3/4/5 SAJA.')
        return menu(tampil)

#Memanggil def menu(tampil)
tampil = 'start'

if tampil == 'start' :
    print(menu(tampil))    
