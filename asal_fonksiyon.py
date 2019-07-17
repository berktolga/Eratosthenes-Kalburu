# Bu dosya import edilen modül dosyasıdır.
#Bu fonksiyon ile sayının asal olup olmadığını kontrol ediyoruz.
def asal_mi(x):
    sayac = 0
    for i in range(2, x,1):
        if (x % i == 0):
            sayac += 1
            break
    if (sayac == 0):
        return x