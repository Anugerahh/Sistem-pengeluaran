# Program Pencatat Pengeluaran Harian Sederhana

def pencatat_pengeluaran():
    print("=== PENCATAT PENGELUARAN HARIAN ===")
    
    daftar_pengeluaran = []
    total = 0

    while True:
        nama = input("\nMasukkan nama barang/kebutuhan (ketik 'selesai' untuk berhenti): ").strip()
        
        if nama.lower() == 'selesai':
            break
            
        try:
            harga = float(input(f"Masukkan harga untuk '{nama}': Rp "))
            daftar_pengeluaran.append((nama, harga))
            total += harga
            print(f"✓ '{nama}' berhasil ditambahkan.")
        except ValueError:
            print("⚠️ Mohon masukkan angka yang valid untuk harga.")

    # Menampilkan ringkasan
    print("\n" + "="*40)
    print("          RINGKASAN PENGELUARAN")
    print("="*40)
    
    if not daftar_pengeluaran:
        print("Belum ada pengeluaran yang dicatat.")
    else:
        for item, harga in daftar_pengeluaran:
            print(f"• {item:<22} : Rp {harga:,.0f}")
        print("-" * 40)
        print(f"TOTAL PENGELUARAN        : Rp {total:,.0f}")
    
    print("="*40)

if __name__ == "__main__":
    pencatat_pengeluaran()