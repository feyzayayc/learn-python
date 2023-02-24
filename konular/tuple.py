import sys
sayilar = (1, 2, 3, 4, 5, 6, 7)

# for sayi in sayilar:
# print(sayi)

isim, soyisim, yas = ('feyza', 'yayci', 23)
# print(isim)
# print(soyisim)
# print(yas)

sayilar_listesi = [1, 2, 3, 4, 5, 6, 7]
# tuple'lar listelere göre daha az yer kaplar

print(sys.getsizeof(sayilar))
print(sys.getsizeof(sayilar_listesi))
print(len(sayilar_listesi))
