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



