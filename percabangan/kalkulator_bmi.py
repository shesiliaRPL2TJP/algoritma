berat = int(input('Masukan berat badan : '))
tinggi = float(input('Masukan tinggi badan : '))
bmi = berat / tinggi;

# Kalkulator BMI

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

# Menghitung BMI
bmi = berat / (tinggi ** 2)

print("BMI kamu:", round(bmi, 2))

# Menentukan kategori
if bmi < 18.5:
    print("Kategori: Kurus (Underweight)")
    print("Keterangan: Perlu tambah berat badan")
elif bmi < 25:
    print("Kategori: Normal (Ideal)")
    print("Keterangan: Pertahankan gaya hidup sehat")
elif bmi < 30:
    print("Kategori: Gemuk (Overweight)")
    print("Keterangan: Perlu olahraga lebih")
else:
    print("Kategori: Obesitas")
    print("Keterangan: Konsultasi dokter")