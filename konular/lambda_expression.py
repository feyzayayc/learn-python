# isimsiz fenkşınlar

denklem = lambda x: x*2

sonuc = denklem(4)

print(sonuc)


isim_soyisim = ['feyza yayci','akis yayci','raziş yayci','fürkan doğan']

print(isim_soyisim)
isim_soyisim.sort()
print(isim_soyisim)
isim_soyisim.sort(key=lambda x:x.split(' ')[-1].lower()) #soyisme göre sıralama
print(isim_soyisim)