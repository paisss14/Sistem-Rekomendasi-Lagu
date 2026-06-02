class lagu:
    def __init__(self, judul, artis, genre, rating):
        self.judul = judul
        self.artis = artis 
        self.genre = genre
        self.rating = int(rating)
        
def __str__(self):
    return f"(self.judul) | {self.artis} | {self.genre} | Rating: {self.rating}"

class Node:
    def __init__(self, lagu):
        self.lagu = lagu
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def tambah(self, lagu):
        if self.head is None:
            self.head = node_baru
            return
        sekarang = self.head
        while sekarang.next:
            sekarang = sekarang.next
        sekarang.next = node.baru

def ambil_semua(self):
    hasil =[]
    sekarang = self.head
    while sekarang:
        hasil.append(sekarang.lagu)
        sekarang = sekarang.next
    return hasil
def quick_sort(arr):
    if len(arr) <= 1 :
        return arr
    pivot = arr[0]
    kiri  = [x for x in arr[1:] if x.rating >= pivot.rating]
    kanan = [x for x in arr[1:]if x.rating  <  pivot.rating]
    return quick_sort(kiri) + [pivot] + quick_sort(kanan)

class SistemMusik:
    
  def_init_(self):
    self.daftar_lagu = []
    self.tumpukan = []
    self.antrian = []
    self.playlist = LinkedList() 

  def tambah_lagu(self, lagu):
    self.daftar_lagu.append(lagu) 
    self.playlist.tambah(lagu) 

  def ambil_lagu(self):
    return self.daftar_lagu

  def ubah_lagu(self,judul,artis_baru,genre_baru,rating_baru):
    for lagu in self.daftar_lagu:
      if lagu.judul.lower() == judul.lower():
         lagu.artis = artis_baru
         lagu.genre = genre_baru
         lagu.rating = int(rating_baru) 
         return True
    return False

  def hapus_lagu(self,judul):
    for lagu in self.daftar_lagu:
      if lagu.judul.lower() == judul.lower():
         self.daftar_lagu.remove(lagu) 
         return True
    return False

  def cari_lagu(self,judul):
    terurut=sorted(self.daftar_lagu
            key=lambda x: x.judul.lower()) 
    return binary_search(terurut,judul) 

  def rekomendasi(self):
    return quick_sort(self.daftar_lagu) 

  def putar_lagu(self,judul):
    for lagu in self.daftar_lagu:
      if lagu.judul.lower() == judul.lower():
         self.tumpukan.append(lagu) 
         return lagu
    return None

  def masuk_antrian(self.judul):
    for lagu in self.daftar_lagu:
      if lagu.judul.lower() == judul.lower():
         self.antrian.append(lagu) 
         return True
    return False

  def lagu_berikutnya(self):
    if not self.antrian:
       return None

    lagu = self.antrian.pop(0) 
    self.tumpukan.append(lagu) 
    return lagu

class AplikasiMusik:
    def __init__(self, root):
        self.sistem = SistemMusik()
        self.root = root
        self.root.title("Sistem Rekomendasi Lagu")
        self.root.geometry("860x580")
        self.root.resizable(False, False)

        self._buat_form()
        self._buat_tombol()
        self._buat_listbox()

    def _buat_form(self):
        label = ["Judul", "Artis", "Genre", "Rating (1-10)"]
        self.entri = {}
        for i, teks in enumerate(label):
            tk.Label(self.root, text=teks, anchor="w", widht=12).grid(
                row=i, column=0, padx=8, pady=4, sticky="w")
            e = tk.Entry(self.root, widht=30)
            e.grid(row=i, column=1, padx=4, pady=4)
            self.entri[teks] = e

    def _buat_tombol(self):
        tombol - [
            ("Tambah Lagu",    self.tambah_lagu),
            ("Update Lagu",    self.ubah_lagu),
            ("Hapus Lagu",     self.hapus_lagu),
            ("Cari Lagu",      self.putar_lagu),
            ("Rekomendasi",    self.rekomendasi),
            ("Putar Lagu",     self.putar_lagu),
            ("Masuk Antrian",  self.masuk_antrian),
            ("Lagu Berikutnya",self.lagu_berikutnya),
            ("Riwayat",        self.tampilkan_riwayat),
            ("Tampilkan Semua",self.tampilkan_semua),
        ]
        for i, (teks, perintah) i enumerate(tombol):
            tk.Button(self.root, text=teks, widht=18, command=perintah).grid(
                row=i, column=2, padx=8, pady=3)
        
    def _buat_listbox(self):
        self.kotak_daftar = tk.Listbox(self.root, widht=95, height=18,
                                       font=(Courier", 9))
        self.kotak_daftar.grid(row=10, column=0, columnspan=3,
                               padx=8, pady=8)

    def _nilai(self, kunci):
        return self.entri[kunci].get().strip()

    def _refresh(self, daftar, judul_header="=== DAFTAR LAGU ==="):
        self.kotak_daftar.delete(0, tk.END)
        self.kotak_daftar.insert(tk.END, judul_header)
        for lagu in daftar:
            self.kotak_daftar.insert(tk.END, str(lagu))



