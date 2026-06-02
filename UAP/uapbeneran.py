import tkinter as tk
from tkinter import messagebox

class Lagu:
    def __init__(self, judul, artis, genre, rating):
        self.judul = judul
        self.artis = artis 
        self.genre = genre
        self.rating = int(rating)
        
    def __str__(self):
        return f"{self.judul} | {self.artis} | {self.genre} | Rating: {self.rating}"

class Node:
    def __init__(self, lagu):
        self.lagu = lagu
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, lagu):
        node_baru = Node(lagu)
        if self.head is None:
            self.head = node_baru
            return
        sekarang = self.head
        while sekarang.next:
            sekarang = sekarang.next
        sekarang.next = node_baru

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

def binary_search(arr, judul):
    kiri, kanan = 0, len(arr) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if arr[tengah].judul.lower() == judul.lower():
            return arr[tengah]
        elif arr[tengah].judul.lower() < judul.lower():
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return None

class SistemMusik:
  def __init__(self): 
      self.daftar_lagu  = []
      self.tumpukan     = []
      self.antrian      = []
      self.playlist     = LinkedList() 

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
      terurut = sorted(self.daftar_lagu, key=lambda x: x.judul.lower()) 
      return binary_search(terurut,judul) 

  def rekomendasi(self):
      return quick_sort(self.daftar_lagu) 

  def putar_lagu(self,judul):
      for lagu in self.daftar_lagu:
          if lagu.judul.lower() == judul.lower():
            self.tumpukan.append(lagu) 
            return lagu
      return None

  def masuk_antrian(self, judul):
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
            tk.Label(self.root, text=teks, anchor="w", width=12).grid(row=i, column=0, padx=8, pady=4, sticky="w")
            e = tk.Entry(self.root, width=30)
            e.grid(row=i, column=1, padx=4, pady=4)
            self.entri[teks] = e

    def _buat_tombol(self):
        tombol = [
            ("Tambah Lagu",    self.tambah_lagu),
            ("Update Lagu",    self.ubah_lagu),
            ("Hapus Lagu",     self.hapus_lagu),
            ("Cari Lagu",      self.cari_lagu),
            ("Rekomendasi",    self.rekomendasi),
            ("Putar Lagu",     self.putar_lagu),
            ("Masuk Antrian",  self.masuk_antrian),
            ("Lagu Berikutnya",self.lagu_berikutnya),
            ("Riwayat",        self.tampilkan_riwayat),
            ("Tampilkan Semua",self.tampilkan_semua),
        ]
        for i, (teks, perintah) in enumerate(tombol):
            tk.Button(self.root, text=teks, width=18, command=perintah).grid(row=i, column=2, padx=8, pady=3)
        
    def _buat_listbox(self):
        self.kotak_daftar = tk.Listbox(self.root, width=95, height=18, font=("Courier", 9))
        self.kotak_daftar.grid(row=10, column=0, columnspan=3, padx=8, pady=8)

    def _nilai(self, kunci):
        return self.entri[kunci].get().strip()

    def _refresh(self, daftar, judul_header="=== DAFTAR LAGU ==="):
        self.kotak_daftar.delete(0, tk.END)
        self.kotak_daftar.insert(tk.END, judul_header)
        for lagu in daftar:
            self.kotak_daftar.insert(tk.END, str(lagu))

    
    def tambah_lagu(self):
        judul = self._nilai("Judul")
        artis = self._nilai("Artis")
        genre = self._nilai("Genre")
        rating = self._nilai("Rating (1-10)")
        if not judul or not artis or not genre or not rating:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")
            return
        try:
            lagu = Lagu(judul, artis, genre, int(rating))
            self.sistem.tambah_lagu(lagu)
            self._refresh(self.sistem.ambil_lagu())
            messagebox.showinfo("Berhasil", f'"{judul}" berhasil ditambahkan.')
        except ValueError:
            messagebox.showerror("Error", "Rating harus berupa angka!")

    def ubah_lagu(self):
        ok = self.sistem.ubah_lagu(
            self._nilai("Judul"),
            self._nilai("Artis"),
            self._nilai("Genre"),
            self._nilai("Rating (1-10)")
        )
        if ok:
            self._refresh(self.sistem.ambil_lagu())
            messagebox.showinfo("Berhasil", "Data lagu diperbarui.")
        else:
            messagebox.showerror("Error", "Lagu tidak ditemukan.")

    def hapus_lagu(self):
        ok = self.sistem.hapus_lagu(self._nilai("Judul"))
        if ok:
            self._refresh(self.sistem.ambil_lagu())
            messagebox.showinfo("Berhasil", "Lagu dihapus.")
        else:
            messagebox.showerror("Error", "Lagu tidak ditemukan.")

    def cari_lagu(self):
        lagu = self.sistem.cari_lagu(self._nilai('Judul'))    
        if lagu:
            messagebox.showinfo('Ditemukan: ', str(lagu))
        else:
            messagebox.showerror('tidak di temukan', 'Lagu tidak ada')

    def rekomendasi(self):
        hasil = self.sistem.rekomendasi()
        self._refresh(hasil, '=== Rekomendasi Lagu ===')

    def putar_lagu(self):
        lagu = self.sistem.putar_lagu(self._nilai("Judul"))
        if lagu:
            messagebox.showinfo('Sedang Memutar Lagu: ', str(lagu))
        else:
            messagebox.showerror('Eror', 'Lagu tidak ditemukan.')

    def masuk_antrian(self):
        ok = self.sistem.masuk_antrian(self._nilai('Judul'))
        if ok:
             messagebox.showinfo('Antrian', 'Lagu masuk antrian.')
        else:
            messagebox.showerror('Eror', 'Lagu tidak ditemukan.')

    def lagu_berikutnya(self):
        lagu = self.sistem.lagu_berikutnya()
        if lagu:
            messagebox.showinfo('Lagu berikutnya: ', str(lagu))
        else:
            messagebox.showwarning('Antrian kosong', 'Tidak ada lagu di antrian.')

    def tampilkan_riwayat(self):
        self._refresh(reversed(self.sistem.tumpukan), '=== RIWAYAT LAGU DIPUTAR ===')

    def tampilkan_semua(self):
        self._refresh(self.sistem.ambil_lagu())

root = tk.Tk()
app = AplikasiMusik(root)
root.mainloop()