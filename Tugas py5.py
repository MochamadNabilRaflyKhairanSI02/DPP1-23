kendaraan = ["Corvette c8","Sport car","6200cc","Merah","4 roda"]
print(kendaraan)

#dari program diatas tambahkan: diakhir tambahkan (hargakendaraan dan jumlah roda) disisipkan setelah nama kendaraan (merk kendaraan dan)

kendaraan.append("Rp843.000.000")
kendaraan.append("manual")
kendaraan.insert(2,"Chevrolet")
print("kendaraan ini saya gunakan untuk keperluan pameran")
print(kendaraan)

#menghitung luas bangun datar

menghitung = input("PILIH OPERASI: \n 1. hitung luas persegi \n 2. hitung luas lingkaran \n 3. hitung luas segitiga \n pilihan:")
match menghitung:
    case "1":
        sisi=int (input("masukan nilai sisi"))
        luas= sisi*sisi
        print(luas)
    case "2":
        jari_jari=int (input("masukan nilai jari-jari: "))
        luas = 3.14* jari_jari*jari_jari
        print(luas)
    case "3":
        alas = int (input("masukan nilai alas: "))
        tinggi = int (input("masukan nilai tinggi" ))
        luas = 0.5*alas*tinggi
        print(luas)
    case _:
        print("salah pilih")
