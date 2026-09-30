# Membuat list kosong
belanja = []

# Memasukkan 5 nama barang
for i in range(5):
    barang = input(f"Masukkan nama barang ke-{i+1}: ")
    belanja.append(barang)

# Menampilkan daftar belanja bernomor
print("\nDaftar Belanja:")
for i, barang in enumerate(belanja):
    print(f"{i+1}. {barang}")