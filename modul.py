stok = []

def tambah_data():
    input_nama = str(input("masukan nama barang : "))
    input_stok = int(input("masukan stok barang : "))
    stok_sementara = {"nama_barang" : input_nama , "stok_barang" : input_stok}
    stok.append(stok_sementara)
    print("--- Data berhasil ditambahkan ---")
    return ('\n')

def edit_data():
    index = int(input("Hapus data index ke : "))
    nama = input("Masukkan nama barang : ")
    jumlah = int(input("Masukkan stok barang : "))
    stok_baru = {"nama_barang" : nama , "stok_barang" : jumlah}
    stok[index] = stok_baru
    print("--- Data telah diubah ---")
    return ('\n')

def hapus_data():
    index = int(input("hapus data index ke : "))
    stok.pop(index)
    print("--- Data berhasil dihapus ---")    
    return ('\n')

def cari_data():
    cari = str(input("Cari nama barang : "))
    items = []
    for i in stok:
        if cari in i["nama_barang"]:
            items.append(i)
    if items:
        for item in items:
            return f"{item['nama_barang']} : {item['stok_barang']}"
    else:
        return "Data barang kosong"
    print()
    return ('\n')
    
def tampil_data():
    if stok:
        for i in stok:
            print(f"{i['nama_barang']} : {i['stok_barang']}")
    else:
        print("Data barang kosong")
    return ('\n')

def jumlah_data():
    print(f"Jumlah data terimpan {len(stok)}")
    return ('\n')