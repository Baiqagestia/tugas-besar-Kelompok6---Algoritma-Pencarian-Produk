# Struktur data berbentuk tree (nested dictionary)
produk_tree = {
    "Elektronik": {
        "Laptop": {
            "Gaming": ["Asus ROG", "MSI GF63", "Lenovo Legion"],
            "Office": ["Asus Vivobook", "HP Pavilion"]
        },
        "Smartphone": ["iPhone 13", "Samsung Galaxy"]
    },
    "Fashion": {
        "Pria": ["Kemeja", "Sepatu Sneakers"],
        "Wanita": ["Dress", "Heels"]
    }
}

# Fungsi Binary Search
def binary_search_produk(data, target):
    kiri, kanan = 0, len(data) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah] == target:
            return True
        elif data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return False

# Fungsi pencarian berdasarkan path kategori
def cari_produk(tree, kategori_path, nama_produk):
    pointer = tree
    try:
        for k in kategori_path:
            pointer = pointer[k]
        if isinstance(pointer, list):
            pointer.sort()
            return binary_search_produk(pointer, nama_produk)
        else:
            return False
    except KeyError:
        return False

# Fungsi menu interaktif
def tampilkan_menu(tree):
    kategori_path = []

    print("=== MENU KATEGORI UTAMA ===")
    level1 = list(tree.keys())
    for i, kat in enumerate(level1):
        print(f"{i + 1}. {kat}")
    pilihan1 = int(input("Pilih kategori utama: ")) - 1
    kategori_path.append(level1[pilihan1])

    pointer = tree[kategori_path[0]]
    if isinstance(pointer, dict):
        print("\n=== SUBKATEGORI ===")
        level2 = list(pointer.keys())
        for i, sub in enumerate(level2):
            print(f"{i + 1}. {sub}")
        pilihan2 = int(input("Pilih subkategori: ")) - 1
        kategori_path.append(level2[pilihan2])

        pointer = pointer[kategori_path[1]]
        if isinstance(pointer, dict):
            print("\n=== SUB-SUBKATEGORI ===")
            level3 = list(pointer.keys())
            for i, subsub in enumerate(level3):
                print(f"{i + 1}. {subsub}")
            pilihan3 = int(input("Pilih sub-subkategori: ")) - 1
            kategori_path.append(level3[pilihan3])

    print("\nMasukkan nama produk yang ingin dicari:")
    produk_dicari = input("Nama produk: ")

    ditemukan = cari_produk(tree, kategori_path, produk_dicari)
    kategori_str = " > ".join(kategori_path)
    if ditemukan:
        print(f"\n✅ Produk '{produk_dicari}' ditemukan dalam kategori {kategori_str}.")
    else:
        print(f"\n❌ Produk '{produk_dicari}' TIDAK ditemukan dalam kategori {kategori_str}.")

# Jalankan program
tampilkan_menu(produk_tree)
