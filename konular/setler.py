# Kümeler : sıraya bakmaz, aynı veriyi 2 kere eklenemez
alacaklar = set()
# print(dir(alacaklar)) # kullanabileceğimiz method'ları bu şekilde görebiliriz.
alacaklar.add('araba')
alacaklar.add('ev')
alacaklar.add('kitap')
alacaklar.add('koltuk')
print(alacaklar)
alacaklar.remove('ev')
print(alacaklar)
alacaklar.discard('koltuk')  # varsa sil, yoksa hata verme
print(alacaklar)
alacaklar.clear()
print(alacaklar)


print('<-------------------------->')

tek_sayilar = set([1, 3, 5, 7, 9])
cift_sayilar = set([0, 2, 4, 6, 8])
print(tek_sayilar.union(cift_sayilar))  # kümeleri birleştiri

asal_sayilar = set([2, 3, 5, 7, 11])

print(tek_sayilar.intersection(asal_sayilar))  # 2 kümenin kesişimini verdi
