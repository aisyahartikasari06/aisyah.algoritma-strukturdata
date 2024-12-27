def cetak_pola(baris):
    """Fungsi untuk mencetak pola bintang segitiga"""
    for i in range(1, baris + 1):
        print("*" * i)

def main():
    print("=== Program Pola Bintang ===")
    try:
        jumlah_baris = int(input("Masukkan jumlah baris untuk pola segitiga: "))
        print("\n=== Pola Segitiga ===")
        cetak_pola(jumlah_baris)
    except ValueError:
        print("Harap masukkan angka yang valid.")

if __name__ == "__main__":
    main()
