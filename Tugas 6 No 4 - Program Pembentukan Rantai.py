#KELOMPOK 1:
#Risa Aulia Nisa (1305621009)                   
#Amelia Fatmasari (1305621010)             
#Allyza Yusykarina Safitri(1305621011)       
#Gabriel Olivia Yvonne Manurung (1305621023)         
#Allan Dinen Irlando (1305621032)

print(50*'=')
print('''Dipresentasikan oleh:


Gabriel Olivia Yvonne Manurung (1305621023)

Tugas 6 - Nomor 4
Pembentukan Rantai''')

print(50*'=')
print()

class simpul:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

# collision handling = seperate chaining
class tabelhash:
    def __init__(self,max):
        self.size = max
        self.arr = [None for i in range(self.size)]
    
    def fungsi_hash(self, key):
        index = key % self.size
        return index

    def tambah(self, keyval, value):
        index = self.fungsi_hash(keyval)
        if self.arr[index] == None:
            self.arr[index] = simpul(keyval,value)
            return True
        else:
            flag = 0
            temp = self.arr[index]
            if temp.key == keyval:
                    flag = 1
                    return False
            while temp.next != None:
                if temp.key == keyval:
                    flag = 1
                    return False
                    break
                temp = temp.next
            if flag == 0:
                temp.next = simpul(keyval,value)
                return True
            
    def cari(self, keyval):
        index = self.fungsi_hash(keyval)
        temp = self.arr[index]
        while temp!=None:
            if temp.key == keyval:
                return temp.value
            temp = temp.next
        
    
    def hapus(self, key):
        if self.cari(key) is not None:
            index = self.fungsi_hash(key)
            if self.arr[index].key == key:
                self.arr[index]=self.arr[index].next
                return True
            else:
                temp = self.arr[index]
                while temp.next.key != key:
                    temp = temp.next
                temp.next = temp.next.next
                return True
        else:
            return False

            
    def printhash(self):
        for i in range(self.size):
            print(f'Indeks ke-{i}:',end = ' ->')
            temp = self.arr[i]
            while temp!=None:
                print(f'[ {temp.key} : {temp.value} ]', end = '->')
                temp=temp.next
            print(' Null')
            
#Banyak alamat Hash
def size():
    print('=============[PROGRAM PEMBENTUKAN RANTAI]=============')
    print()
    banyak_alamat = input('Masukkan banyak alamat hash untuk menyimpan data: ')
    print()
    if banyak_alamat.isnumeric() == True:
        banyak_alamat = int(banyak_alamat)
    else:
        print('Mohon masukkan dalam bentuk angka yang valid.')
        return size()
    return banyak_alamat

banyak_alamat = size()
    
hash = tabelhash(banyak_alamat)

def menu(tampil):
    #Memilih menu yang akan dijalankan
    print('------------------------------------------')
    print('=================[ MENU ]=================')
    print('------------------------------------------')
    print('1. Memasukkan data')
    print('2. Menampilkan data dengan kunci tertentu')
    print('3. Hapus data dengan kunci tertentu')
    print('4. Menampilkan tabel hash')
    print('5. Exit')
    print('------------------------------------------')
    pilih = input('Pilih menu yang akan dijalankan (1/2/3/4/5): ')
    print()

    #Memasukkan Data
    if pilih == '1':
        print('==========[ MEMASUKKAN DATA ]==========')
        print()
        while True:
            try:
                n = int(input('Banyak data yang ingin dimasukkan: '))
                print()
                if n>= 0:   
                    break
                else:
                    print('Mohon masukkan banyak data dalam bilangan bulat positif.')
                    print()
            except ValueError:
                print('Mohon masukkan banyak data dalam bentuk angka yang valid.')
                print()

        print('Mohon masukkan kunci berupa kombinasi 3 angka.')           
        for i in range (0,n):
            print()
            key = input('Masukkan kunci: ')
            if key.isnumeric() == True and len(key)==3:
                key = int(key)
                value = input(str('Masukkan nama data: '))
                if hash.tambah(key,value) == True:
                    print('Data berhasil ditambahkan ke tabel hash.')
                else:
                    print('Kunci sudah pernah ditambahkan, gagal dimasukkan ke tabel hash.')
            else:
                print('Kunci yang dimasukkan tidak valid.')
                print()
        print()
        print('Tabel Hash dengan Pembentukan Rantai: ')
        hash.printhash()
        print()
        return menu(tampil)
        
    #Menampilkan data dengan kunci tertentu
    elif pilih == '2':
        print('==========[ MENAMPILKAN DATA DENGAN KUNCI TERTENTU ]==========')
        print()
        key = input('Masukkan kunci dari data yang ingin dicari: ')
        if key.isnumeric() == True and len(key)==3:
            key = int(key)
            if hash.cari(key) is not None:
                value = hash.cari(key)
                print()
                print('Data dengan kunci',key, 'ditemukan')
                print('Hasil pencarian:',value)
            else:
                print('Data dengan kunci', key, 'tidak ditemukan.')
        else:
            print('Kunci yang dimasukkan tidak valid.')
        print()
        return menu(tampil)

    #Hapus data dengan kunci tertentu
    elif pilih == '3':
        print('==========[ HAPUS DATA DENGAN KUNCI TERTENTU ]==========')
        print()
        key = input('Masukkan kunci dari data yang ingin dihapus: ')
        if key.isnumeric() == True and len(key)==3:
            key = int(key)
            value = hash.cari(key)
            if hash.hapus(key) == True:
                hash.hapus(key)
                print('Data', value, 'dengan kunci',key, 'berhasil dihapus.')
                print()
                print('Setelah kunci', key, 'dihapus:')
                hash.printhash()
            else:
                print('Data yang ingin dihapus tidak ditemukan, sehingga tidak dapat dihapus.')
        else:
            print('Kunci yang dimasukkan tidak valid')
        print()
        return menu(tampil)

    #Menampilkan tabel hash
    elif pilih == '4':
        print('==========[ MENAMPILKAN TABEL HASH ]==========')
        print()
        print('Tabel Hash dengan Pembentukan Rantai: ')
        hash.printhash()
        print()
        return menu(tampil)

    #Exit
    elif pilih == '5':
        print('Terima kasih telah menggunakan program ini.')
        exit()

    #Selain pilih 1,2,3,4,5
    else:
        print('MAAF, DATA YANG ANDA INPUT SALAH, MOHON MASUKKAN ANGKA 1/2/3/4/5 SAJA.')
        return menu(tampil)


#Memanggil def menu(tampil)
tampil = 'start'
if tampil == 'start' :
    print(menu(tampil))    
