mahasiswa=[]
nim=[]
lanjut=True

while lanjut:
    print(''' 
+---------------------+
| MENU DATA MAHASISWA |
+---------------------+
| 1. Tambah Mahasiswa |
| 2. Edit Mahasiswa   |
| 3. Hapus Mahasiswa  |
| 4. Tampilkan Data   |
| 5. Quit             |
+---------------------+
    ''')

    pilihan=input('Masukkan pilihan : ')

    if pilihan=='1':
        mahasiswa.append(input('Nama Mahasiswa : '))
        nim.append(input('NIM Mahasiswa  : '))

    if pilihan=='2':
        cari=nim.index(input('Cari NIM Mahasiswa : '))
        print('''
+----------------+
| DATA MAHASISWA |
+----------------+''')
        print('+------------------------------------+\n| Nama Mahasiswa : ',mahasiswa[cari],'\n| NIM Mahasiswa  : ',nim[cari],'\n+------------------------------------+')
        mahasiswa.pop(cari)
        nim.pop(cari)
        print('\n== Edit Data Mahasiswa ==\n')
        nim.append(input('Masukkan NIM Mahasiswa  : '))
        mahasiswa.append(input('Masukkan Nama Mahasiswa : '))
        print('!! Data berhasil diedit !!')

    if pilihan=='3':
        cari=nim.index(input('Cari NIM Mahasiswa : '))
        mahasiswa.pop(cari)
        nim.pop(cari)
        print('!! Data berhasil dihapus !!')

    if pilihan=='4':
        print('''
+----------------+
| DATA MAHASISWA |
+----------------+''')
        for i in range(len(mahasiswa)):
            print('+------------------------------------+\n| Nama Mahasiswa : ',mahasiswa[i],'\n| NIM Mahasiswa  : ',nim[i], '\n+------------------------------------+')

    if pilihan=='5':
        lanjut=False
        print('!! Anda keluar dari program !!')
