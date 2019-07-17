import asal_fonksiyon,time
asal_olanlar=[] #"asal_olanlar" isminde boş bir liste oluşturduk.
silinenler=[] #"silinenler" isminde boş bir liste oluşturduk.

x=int(input("Bir sayi giriniz:"))#Kullanıcıdan bir sayı alıyoruz.
liste=list(range(2,x+1)) #Range fonksiyonu 2'den girdiğimiz x'e kadar olan sayıları oluşturacak ve list fonksiyonu da
# onlardan bir liste oluşturacak.Range, girdiğimiz sayının bir eksiğini aldığı için +1 ekledik.

while (len(liste)!=0):#Liste eleman sayısı 0 olana kadar döngü çalışacak.
    y=liste[0]  #Listenin 0.indeksi y'ye atandı.
    #Böylece her j ve katları silindiğinde otomatik olarak y'ye listedeki geriye kalan elemanlardan ilki atanmış olacak.
    while (y <= x): #y girilen x değerinden kuçük veya eşit olduğu sürece döngü devam edecek.
        for j in liste:# j, 2'den x'e kadar olan sayıları teker teker tutacak.
            if(j%y==0): # y, j'yi tam bölüyor ise
                silinenler.append(j)#j'yi silinenler listesine ekleyecek ve
                liste.remove(j) # j'yi listeden silecek.(j ve katları silinecek.)
                print("{} siliniyor...".format(j))
                time.sleep(0.5)
                print("----")
                print("Kalan Sayılar",liste)
                print("***")
                time.sleep(0.5)
                if (asal_fonksiyon.asal_mi(j)):#Silinecek olan j import ettiğimiz fonksiyon ile asal mı değil mi kontrol edilecek.
                    asal_olanlar.append(j) #Asal ise asal olanlar listesine eklenecek.
                    print("{} asal".format(j))
                    print("***")
                    time.sleep(0.5)
        break

print("---------------")

print("Asal olanlar",asal_olanlar)

print("Silinenler",silinenler)




