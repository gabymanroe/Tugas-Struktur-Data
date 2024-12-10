#KELOMPOK 1:
#Risa Aulia Nisa (1305621009)                   
#Amelia Fatmasari (1305621010)             
#Allyza Yusykarina Safitri (1305621011)       
#Gabriel Olivia Yvonne Manurung (1305621023)         
#Allan Dinen Irlando (1305621032)

print(50*'=')
print('''Dipresentasikan oleh:
Gabriel Olivia Yvonne Manurung (1305621023)

Tugas 1 - Nomor 1
Kalkulator Konversi Desimal ke Biner, Oktal, Heksadesimal''')


#Konversi desimal ke biner

def biner(desimal):
    if desimal==0:
        print('Hasil konversi desimal ke biner:',end='')
        print(desimal)
        return ''
    else:
        hasil=[]
        print()
        print('Proses pengubahan desimal ke biner')
        while desimal>0:
            sisa = int(desimal%2)
            desimal = int(desimal//2)
            print(desimal, 'sisa', sisa)
            hasil.append(sisa)
        hasil.reverse()
        print('Hasil konversi desimal ke biner: ',end='')
        for a in hasil:
            print(a, end='')
        return ''

#Konversi desimal ke oktal
def oktal(desimal):
    if desimal==0:
        print('Hasil konversi desimal ke oktal: ',end='')
        print(desimal)
        return ''
    else:
        hasil=[]
        print()
        print('Proses pengubahan desimal ke oktal:')
        while desimal>0:
            sisa = int(desimal%8)
            desimal = int(desimal//8)
            print(desimal, 'sisa', sisa)
            hasil.append(sisa)
        hasil.reverse()
        print('Hasil konversi desimal ke oktal: ',end='')
        for a in hasil:
            print(a, end='')
        return ''
        print(50*'=')
        
#Konversi desimal ke heksadesimal
def heksadesimal(desimal):
    if desimal==0:
        print('Hasil konversi desimal ke heksadesimal: ',end='')
        print(desimal)
        return ''
    else:
        hasil=[]
        print()        
        print('Proses pengubahan desimal ke heksadesimal: ')
        while desimal>0:
            sisa = int(desimal%16)
            desimal = int(desimal//16)
            print(desimal, 'sisa', sisa)
            hasil.append(sisa)
            if sisa == 10:
                hasil[hasil.index(10)]='A'
            if sisa == 11:
                hasil[hasil.index(11)]='B'
            if sisa == 12:
                hasil[hasil.index(12)]='C'
            if sisa == 13:
                hasil[hasil.index(13)]='D'
            if sisa == 14:
                hasil[hasil.index(14)]='E'
            if sisa == 15:
                hasil[hasil.index(15)]='F'
        hasil.reverse()
        print('Hasil konversi desimal ke heksadesimal: ',end='')
        for a in hasil:
            print(a, end='')
        return ''
    
#Memulai program
def perulangan():
    print(50*'=')
    desimal=int(input('Masukkan angka desimal: '))
    print(50*'=')
    
    biner(desimal)
    print()
    oktal(desimal)
    print()
    heksadesimal(desimal)
    print()
    print()
    
perulangan()

#Menggunakan kembali kalkulator konversi
while True:
    print(50*'=')
    coba_lagi= input('Apakah Anda ingin mencoba lagi? (1=ya | 0=exit): ')
    print(50*'=')
    if coba_lagi == "1":
        perulangan()
        continue
    elif coba_lagi=='0':
        print('Terima kasih telah menggunakan program ini')
        break
    else:
        print('MAAF, DATA YANG ANDA INPUT SALAH, MOHON MASUKKAN DENGAN BENAR')
        print()
        continue
