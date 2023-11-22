def say(nama,alamat,gender,umur,hoby):
    print("saya adalah",nama)
    print("tempat tinggal di",alamat)
    print("kelamin saya adalah",gender)
    print("saya berumur",umur)
    print("hoby saya adalah",hoby)

say("nabil","depok","laki laki","19","mengedit video")

def cek_kelulusan(nilai):
    if nilai < 60:
        print("Gagal")
    elif 61 <= nilai <= 70:
        print("Baik")
    elif 71 <= nilai <= 80:
        print("Sangat Baik")
    elif 81 <= nilai <= 100:
        print("Istimewa")
    
    else:
        print("Tidak Lulus")
cek_kelulusan(60)

def ganjil(angka):
    for i in range(1, angka + 1, 2):
        print(i)
ganjil(100)