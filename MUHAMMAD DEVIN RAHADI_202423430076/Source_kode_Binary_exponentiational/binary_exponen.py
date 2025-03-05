print("NAMA : MUHAMMAD DEVIN RAHADI")
print("NIM : 23343076\n")

def pangkat_biner(basis, eksponen):
    """
    Fungsi untuk menghitung perpangkatan menggunakan metode Binary Exponentiation.
    
    Parameter:
    basis (int) : Bilangan dasar yang akan dipangkatkan.
    eksponen (int) : Bilangan pangkat (harus bilangan bulat non-negatif).

    Mengembalikan:
    int : Hasil dari basis^eksponen.
    """
    hasil = 1  # Inisialisasi hasil awal sebagai 1
    while eksponen > 0:
        if eksponen % 2 == 1:  # Jika eksponen ganjil
            hasil *= basis
        basis *= basis  # Basis dikalikan dengan dirinya sendiri
        eksponen //= 2  # Eksponen dibagi dua (geser bit ke kanan)
    return hasil

# Contoh Penggunaan
a = int(input("Masukkan bilangan basis: "))
n = int(input("Masukkan bilangan eksponen: "))

print(f"Hasil dari {a}^{n} adalah: {pangkat_biner(a, n)}")
