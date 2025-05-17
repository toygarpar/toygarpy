#methods - urunEkle(), urunGuncelle(), urunleriGetir()


"""
urunEkle("iphone 16 pro", 90000)

urunGuncelle("iphone 16 pro", 99000)


urunleriGetir()



"""
import module1


def urunEkle(urunAdi, fiyat):
    module1.urunler.append({
        "id" : len(module1.urunler) + 1,
        "urunAdi": urunAdi,
        "fiyat" : fiyat

    })


def urunGuncelle(id, urunAdi, fiyat):
    for urun in module1.urunler:
        if urun["id"] == id:
            urun["urunAdi"]  = urunAdi
            urun["fiyat"]   =  fiyat
            break



def urunleriGetir():
    return module1.urunler
