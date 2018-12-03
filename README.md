# Türkiye İller ve İlçeler Listesi

Türkiye'deki il ve ilçelerin listesini [İçişleri Bakanlığının](https://www.e-icisleri.gov.tr/Anasayfa/MulkiIdariBolumleri.aspx) sayfasından toplayan betik.

## Bağımlılıklar

- [selenium](https://pypi.org/project/selenium/)

Bu proje bir Python projesidir.
> Python 3.7 ile test edilmiştir

## Kullanım

* Bu kod deposunu indiriniz:
```
git clone https://github.com/molcay/TR-il-ilce-listesi.git
```

* İndirdiğiniz dizine geçip, sanal ortam(`virtual environemnt`) oluşturunuz ve sanal ortamı aktif hale:
```
cd TR-il-ilce-listesi
python3 -m venv myvenv
source myvenv/bin/activate
```

* Proje bağımlılıklarını yükleyiniz:
```
pip install -r requirements.txt
```

* Betiği çalıştırınız:
```
python script.py
```

### Yapılacaklar
- [ ] `get_cities` fonksiyonu içinde `while` döngüsünden kurtul.
- [ ] `script.py`'ı komut satırından parametre alabilen hale getir.
