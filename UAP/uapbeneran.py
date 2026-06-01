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