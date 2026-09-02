# Contoh: Kategori nilai
nilai = int(input("masukan nilai (0-100): "))

if nilai >= 90:
    kategori = "A (Sangan Baik)"
elif nilai >= 80:
    kategori = "B (Baik)"
elif nilai >= 70:
    kategori = "c (cukup)"
elif nilai = 60:
    kategori = "D (kurang)"
else:
    kategori = "E (sangat kurang)"

print("Nilai :", nilai)
print("Kategori :", kategori)