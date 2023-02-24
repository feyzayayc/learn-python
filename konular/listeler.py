meyveler = ['elma', 'portakal', 'kivi', 'domates', 'ananas', 'erik']

print(meyveler)
print(meyveler[0])
print(meyveler[2])

print('------------------------>')

meyveler.append('muz')
print(meyveler)


yeni_list = meyveler[1:4]
print("=>", yeni_list)

yepyeni_list = meyveler[1:]
print(yepyeni_list)

yepyeni_list2 = meyveler[:4]
print(yepyeni_list2)

sebzeler = ['havuç', 'patlıcan']

print(meyveler+sebzeler)


print(meyveler.count('kivi'))
meyveler.pop()
print(meyveler)
