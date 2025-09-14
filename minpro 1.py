print("Nama: Annisa Nayzhua Febriyani")
print("Kelas: Sistem informasi 2025'A")
print("Nim: 2509116013")
print("-"*20)

penyewa = [] #list kosong yang akan menampung data penyewa kost.

def Inputan_data_Penyewa(): #Fungsi untuk menambahkan data Penyewa
    nama = input("Masukkan Nama Penyewa: ")
    kamar = input("Masukkan Nomor Kamar Kost: ")
    if any(kamar == k for _, k in penyewa):
        print("sudah terpakai")
        return False
    data =(nama,kamar)
    penyewa.append(data)  # menambahkan tuple ke list
    print("<3 Penyewa berhasil ditambahkan <3")

def melihat_info_penyewa(): #Fungsi untuk menampilkan data Penyewa
    if len(penyewa) == 0:
        print("Data Masih Kosong")
    else:
        print("=== Daftar Penyewa Kost ===")
        for nomor_urut, (nama, kamar) in enumerate(penyewa, start=1): # memberi nomor urut mulai dari 1
            print("====================================")
            print(f"No      : {nomor_urut}")
            print(f"Nama    : {nama}")
            print(f"Kamar   : {kamar}")
            print("====================================")
        print()

while True: # Perulangan terus-menerus
    print("=== SISTEM PENGELOLAAN SEWA KOST ===")
    print("1. Tambah Penyewa")
    print("2. Lihat Data Penyewa")
    print("3. Keluar")
    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        Inputan_data_Penyewa() # memanggil fungsi untuk menambahkan data penyewa
    elif pilihan == "2":
        melihat_info_penyewa() # memanggil fungsi untuk menampilkan data penyewa
    elif pilihan == "3":
        print("<3 Terima kasih telah menggunakan sistem <3")
        break # Menghentikan Perulangan
    else:
        print("Pilihan tidak valid, silahkan dicoba lagi.")