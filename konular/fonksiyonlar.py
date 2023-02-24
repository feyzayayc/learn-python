def toplama(x, y=2):
    return x+y

# print(toplama(5, 3))
# print(toplama(5))


def toplama2(*args, **kwargs):  # args ve kwargs ifadeleri değiştirilebilir
    print(args)  # direkt olarak verilenler
    print(kwargs)  # değişkenle gelenler


print(toplama2(1, 2, 3, 4, 5, y=6, z=7))


def fonsk(a, b, *args, **kwargs):
    return a+b


print(fonsk(1, 2, 3, 4, q=0))
