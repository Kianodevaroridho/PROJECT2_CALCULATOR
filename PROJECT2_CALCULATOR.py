print("====================")
print("CALCULATOR BY PYTHON")
print("====================")

print("1. PENJUMLAHAN")
print("2. PENGURANGAN")
print("3. PERKALIAN")
print("4. PEMBAGIAN")
print("--------------------")

#Logika
def penjumlahan(x,y):
    return x+y

def pengurangan(x,y):
    return x-y

def perkalian(x,y):
    return x*y

def pembagian(x,y):
    return x/y

tipe = input("Silakan masukan nomor yang anda pilih :")

if tipe in ('1', '2', '3', '4'):
    angka1= float(input("Angka Pertama :"))
    angka2= float(input("Angka kedua :"))
    print("--------------------")
    if tipe == '1':
        print("Jawabanya adalah :", penjumlahan(angka1, angka2))
    if tipe == '2':
        print("Jawabanya adalah :", pengurangan(angka1, angka2))
    if tipe == '3':
        print("Jawabanya adalah :", perkalian(angka1, angka2))
    if tipe == '4':
        print("Jawabanya adalah :", pembagian(angka1, angka2))
else:
    print("SILAKAN COBA KEMBALI!!!")
    print("--------------------")