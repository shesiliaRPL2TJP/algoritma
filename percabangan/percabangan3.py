# Contoh Syarat Kelulusan dengan 2 kondisi
nilai = int(input("nilai ujian : "))
absen = int(input("jumlah absen : "))

if nilai >= 75:
    if absen <= 5:
        print("LULUS - selamat")
    else:
        print("TIDAK LULUS - absen terlalu banyak")
else:
    print("TIDAK LULUS -Nilai dibawah KKM")