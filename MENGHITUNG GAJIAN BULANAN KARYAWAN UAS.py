def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    """Fungsi untuk menghitung gaji bulanan karyawan."""
    total_gaji = 0

    for hari in range(1, hari_kerja + 1):
        if jam_kerja_per_hari[hari - 1] > 8:
            jam_lembur = jam_kerja_per_hari[hari - 1] - 8
            gaji_harian = (8 * tarif_per_jam) + (jam_lembur * tarif_per_jam * 1.5)
        else:
            gaji_harian = jam_kerja_per_hari[hari - 1] * tarif_per_jam

        total_gaji += gaji_harian

    return total_gaji

def main():
    print("=== Program Hitung Gaji Karyawan ===")

    try:
        tarif_per_jam = float(input("Masukkan tarif gaji per jam: "))
        hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))

        print("Masukkan jam kerja untuk setiap hari:")
        jam_kerja_per_hari = []
        for hari in range(1, hari_kerja + 1):
            jam_kerja = float(input(f"Hari ke-{hari}: "))
            jam_kerja_per_hari.append(jam_kerja)

        total_gaji = hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja)
        print(f"\nTotal gaji bulanan Anda adalah: Rp{total_gaji:.2f}")

    except ValueError:
        print("Harap masukkan angka yang valid.")

if __name__ == "__main__":
    main()
