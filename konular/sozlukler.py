person = {
    'isim': 'feyza',
    'soyisim': 'yayci',
    'yas': 23
}

person2 = dict(isim='feyza', soyisim='yayci2', yas=24)

# print(type(person))
# print(person)
# print(type(person2))
# print(person2)

person['renk'] = 'kırmızı'
# print(person)

# print('name => ', person['isim'])

if "okul" in person:
    print(person['okul'])
else:
    print('Bu key yoktur!!')

# print(help(person.get))
# print(person.get('yas','default değer'))
# print(person.items())


for anahtar, deger in person.items():
    print(anahtar, " ==> ", deger)
