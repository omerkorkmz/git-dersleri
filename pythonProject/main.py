a = int(input("sayi1: "))
b = int(input("sayi2: "))

 secenek = int(input("1-topla\n2-cikar\n3-carp\n4-bol"))

    if   secenek == 1:
        print(a+b)
    elif secenek == 2:
        print(a-b)
    elif secenek == 3:
        print(a*b)
    else secenek == 4:
        print(a/b)