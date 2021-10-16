
aylik_net_Asgari_u = 2340.70

top_satilan_emlak_parasi = top_kiralanan_emlak_parasi = 0
top_satilan_konut_parasi = top_satilan_arsa_parasi = top_satilan_isyeri_parasi = 0
top_konut_kira_parasi = top_arsa_kira_parasi = top_isyeri_kira_parasi = 0

toplam_satilan_konut_sayisi = toplam_satilan_isyeri_sayisi = toplam_satilan_arsa_sayisi = 0
top_kiralik_konut_sayisi = top_kiralik_arsa_sayisi = top_kiralik_isyeri_sayisi = 0

en_yuksek_satan_danisman = en_yuksek_satilan_emlak_tipi = ''
en_yuksek_satilan_bedeli = 0
en_yuksek_kira_veren_danisman = en_yuksek_kira_verilen_tipi = ''
en_yuksek_kira_bedeli = 0
asgari_ucretten_yuksek_kira_sayisi = 0
kota_dolduran_sayisi = 0
satamayanlar = 0

en_cok_satan_danisman = en_cok_satis_parasi_getiren_danisman = ""
en_cok_satan_adedi = en_cok_satan_adedi_bedeli = en_cok_satis_parasi_getiren_bedeli = en_cok_satis_parasi_getiren_adedi =0
primi_yuksek_olan_sayisi = 0
_25K_10_adet_fazla_kiralayan_sayisi = 0

en_yuksek_prim_danisman = en_dusuk_prim_danisman = ""
en_yuksek_prim_miktar = en_yuksek_prim_maas = en_yuksek_prim_top_ucret = 0
en_dusuk_prim_miktar = en_dusuk_prim_maas = en_dusuk_prim_top_ucret = 0
tum_danismanlara_odenecek_tutar = 0

acentenin_toplam_emlak_komisyonu = acentenin_danisman_ucreti_verdikten_sonra_emlak_komisyonu = 0

# Burdan Baslar   ######## >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Go

danisman_sayisi = int(input("Danışmanı sayısı giriniz: "))
while danisman_sayisi < 1:
    danisman_sayisi = int(input("Yanlis deger girdiniz. danışmanı sayısı giriniz: "))

for danisman in range(danisman_sayisi):

    emlak_sayac = kiralanan_sayac = satilan_sayac = 0
    bir_kisinin_top_satilan_konut_parasi = bir_kisinin_top_satilan_isyeri_parasi = bir_kisinin_top_satilan_arsa_parasi = 0
    bir_kisinin_top_konut_kirasi = birkisinin_top_arsa_kirasi = birkisinin_top_isyeri_kirasi = 0
    para_bedeli = 0
    ayin_en_yuksek_kirasi = ayin_en_yuksek_satisi = 0
    ayin_en_yuksek_satis_tipi = ayin_en_yuksek_kira_tipi = ''
    bir_kisinin_top_kiralanan_konut_sayac = 0
    danismanin_en_yuksek_kiralik_konutu_bedel = 0

    ad_soyad = input("\nAdiniz ve Soyadiniz: ")
    maas = float(input("Aylık net maaşınız ne kadar: "))
    while maas < aylik_net_Asgari_u:
        maas = float(input("Yanlis deger girdiniz! tekrar maasinizi giriniz: "))
    kota = float(input("Kota tutari giriniz:"))
    while kota < maas * 10:
        kota = float(input("Yanlis deger girdiniz! tekrar giriniz: "))

    baska_emlak_var_mi = 'e'
    while baska_emlak_var_mi in "eE":
        emlak_sayac += 1

        # Emlak Tipi
        emlak_tipi = input("Emlak tipini giriniz (konut:K/k) (isyeri:I/i) (Arsa:A/a): ")
        while emlak_tipi not in "KkIiAa":
            emlak_tipi = input('Hatali giris, lutfen bastan giriniz: ')

        # Islem Turu, Satilik / Kiralik
        islem_turu = input("İslem turunu belirleyiniz: (satis:S/s) (kiralama:K/k): ")
        while islem_turu not in 'SsKk':
            islem_turu = input('Hatali giris, lutfen bastan giriniz: ')

        # Satis / Kira para bedeli
        para_bedeli = float(input("Para bedelini giriniz: "))
        while para_bedeli <= 0:
            para_bedeli = float(input('hatali giris, lutfen bastan giriniz: '))

        if islem_turu in "Ss":
            satilan_sayac += 1

            if ayin_en_yuksek_satisi < para_bedeli:
                ayin_en_yuksek_satisi = para_bedeli
                ayin_en_yuksek_satis_tipi = emlak_tipi

            # top_satilan_komnut/arsa/isyeri_sayisi  global degiskendir: tum danismanlar tarafindan satilanlarin (konut/arsa/isyeri) saysini tutar.
            if emlak_tipi in "Kk":
                toplam_satilan_konut_sayisi += 1
                bir_kisinin_top_satilan_konut_parasi += para_bedeli

            elif emlak_tipi in "Ii":
                toplam_satilan_isyeri_sayisi += 1
                bir_kisinin_top_satilan_isyeri_parasi += para_bedeli

            elif emlak_tipi in "Aa":
                toplam_satilan_arsa_sayisi += 1
                bir_kisinin_top_satilan_arsa_parasi += para_bedeli

        elif islem_turu in "Kk":
            kiralanan_sayac += 1

            if ayin_en_yuksek_kirasi < para_bedeli:
                ayin_en_yuksek_kirasi = para_bedeli
                ayin_en_yuksek_kira_tipi = emlak_tipi

            # top_kiralik_komnut/arsa/isyeri_sayisi  global degiskendir: tum danismanlar tarafindan kiralanan (konut/arsa/isyeri) saysini tutar.
            if emlak_tipi in "Kk":
                if danismanin_en_yuksek_kiralik_konutu_bedel < para_bedeli:
                    danismanin_en_yuksek_kiralik_konutu_bedel = para_bedeli
                top_kiralik_konut_sayisi += 1
                bir_kisinin_top_konut_kirasi += para_bedeli
                bir_kisinin_top_kiralanan_konut_sayac += 1
                if para_bedeli > aylik_net_Asgari_u:
                    asgari_ucretten_yuksek_kira_sayisi += 1
# correct this later
            elif emlak_tipi in "Ii":
                top_kiralik_isyeri_sayisi += 1
                birkisinin_top_isyeri_kirasi += para_bedeli

            elif emlak_tipi in "Aa":
                top_kiralik_arsa_sayisi += 1
                birkisinin_top_arsa_kirasi += para_bedeli



        # Danisman isleminin devami edip etmemesini kontrol eder.
        baska_emlak_var_mi = input("Bu ay sattığıniz veya kiraladığıniz başka emlak var mi: (E/e/H/h) :")
        while baska_emlak_var_mi not in "EeHh":
            baska_emlak_var_mi = input("Hatali giris, lutfen tekrar giriniz: ")

    # Her danismanin isi bittikten sonra buraya gelir.
    top_satilan_konut_parasi += bir_kisinin_top_satilan_konut_parasi
    top_satilan_arsa_parasi += bir_kisinin_top_satilan_arsa_parasi
    top_satilan_isyeri_parasi += bir_kisinin_top_satilan_isyeri_parasi

    top_konut_kira_parasi += bir_kisinin_top_konut_kirasi
    top_arsa_kira_parasi += birkisinin_top_arsa_kirasi
    top_isyeri_kira_parasi += birkisinin_top_isyeri_kirasi

    satilan_emlak_oran = satilan_sayac * 100 / emlak_sayac
    kiralik_emlak_oran = kiralanan_sayac * 100 / emlak_sayac
    birkisinin_top_emlak_Kirasi = birkisinin_top_arsa_kirasi + birkisinin_top_isyeri_kirasi + bir_kisinin_top_konut_kirasi
    birkisinin_top_emlak_Satisi = bir_kisinin_top_satilan_konut_parasi + bir_kisinin_top_satilan_isyeri_parasi + bir_kisinin_top_satilan_arsa_parasi

    #   Acentenin Emlak Komisyonu:  acentenin_toplam_emlak_komisyonu --> Global degiskendir, tum danismanlardan gelen komisyonu saklar.
    #                               acentenin_emlak_komisyonu  --> Local Degisken, Suanki --islem yapan-- danismandan gelen komisyonu tutar.
    acentenin_emlak_komisyonu = birkisinin_top_emlak_Satisi * 0.04 + birkisinin_top_emlak_Kirasi
    acentenin_toplam_emlak_komisyonu += acentenin_emlak_komisyonu

    prim = acentenin_emlak_komisyonu * 0.10

    #  !!!!!!  ###   Dusuk Prim Suan Belli Degil   ###    !!!!!!
    dusuk_prim = prim

    if prim > maas:
        primi_yuksek_olan_sayisi += 1

    if kiralanan_sayac >= 10 or birkisinin_top_emlak_Kirasi >= 25000:
        _25K_10_adet_fazla_kiralayan_sayisi += 1

    print("\n\nSayin ", ad_soyad)
    print("Bu ay sattiginiz emlak sayisi: ", satilan_sayac, " ve orani: %" + "%.2f" % satilan_emlak_oran, " Kiraladiginiz emlak adedi: ",
          kiralanan_sayac, " ve orani: %" + "%.2f" % kiralik_emlak_oran)
    print("\nBu ay sattigi emlak tiplerine gore toplam bedelleri: ")
    print("Satilan Konut icin toplam bedel: %.2f" % bir_kisinin_top_satilan_konut_parasi, " TL")
    print("Satilan arsa icin toplam bedel: %.2f" % bir_kisinin_top_satilan_arsa_parasi, " TL")
    print("Satilan isyeri icin toplam bedel: %.2f" % bir_kisinin_top_satilan_isyeri_parasi, " TL")
    print("\nBu ay kiraladiginiz konutlarin ortalama kira bedeli: %.2f" % (
                bir_kisinin_top_konut_kirasi / bir_kisinin_top_kiralanan_konut_sayac), " TL")
    print("Bu ay en yüksek bedelle kiraladığı konutun kira bedeli: %.2f" % danismanin_en_yuksek_kiralik_konutu_bedel,
          " TL")


    print("\nBu ayki maasiniz: %.2f" % maas, " TL")
    print("Bu ayki priminiz: %.2f" % prim, " TL")
    print("Bu ayki kotaniz: %.2f" % kota, " TL")
    print("Bu ay acenteye kazandırdığıniz toplam komisyon tutarı: %.2f" % acentenin_emlak_komisyonu, " TL")

    if kota <= acentenin_emlak_komisyonu:
        kota_dolduran_sayisi += 1
        ikramiye = aylik_net_Asgari_u / 2
        print("Bu ay kotasını doldurdunuz.")
        print("Bu ayki ikramiyaniz: ", ikramiye)
    else:
        print("Bu ay kotasini dolduramadiniz")
        ikramiye = 0

    #   TOPLAM UCRET:   #
    bir_kisinin_toplam_ucret = maas + prim + ikramiye
    acentenin_danisman_ucreti_verdikten_sonra_emlak_komisyonu += (acentenin_emlak_komisyonu - bir_kisinin_toplam_ucret)
    tum_danismanlara_odenecek_tutar += bir_kisinin_toplam_ucret

    print("Bu ay toplam ucretiniz: %.2f" % bir_kisinin_toplam_ucret, " TL")

    if en_yuksek_prim_miktar < prim:
        en_yuksek_prim_miktar = prim
        en_yuksek_prim_danisman = ad_soyad
        en_yuksek_prim_maas = maas
        en_yuksek_prim_top_ucret = bir_kisinin_toplam_ucret

    if en_dusuk_prim_miktar > prim or en_dusuk_prim_miktar==0:
        en_dusuk_prim_miktar = prim
        en_dusuk_prim_danisman = ad_soyad
        en_dusuk_prim_maas = maas
        en_dusuk_prim_top_ucret = bir_kisinin_toplam_ucret

    if en_yuksek_satilan_bedeli < ayin_en_yuksek_satisi:
        en_yuksek_satilan_bedeli = ayin_en_yuksek_satisi
        en_yuksek_satan_danisman = ad_soyad
        en_yuksek_satilan_emlak_tipi = ayin_en_yuksek_satis_tipi

    if en_yuksek_kira_bedeli < ayin_en_yuksek_kirasi:
        en_yuksek_kira_bedeli = ayin_en_yuksek_kirasi
        en_yuksek_kira_veren_danisman = ad_soyad
        en_yuksek_kira_verilen_tipi = ayin_en_yuksek_kira_tipi

    if satilan_sayac == 0:
        satamayanlar += 1

    if en_cok_satan_adedi < satilan_sayac:
        en_cok_satan_adedi = satilan_sayac
        en_cok_satan_danisman = ad_soyad
        en_cok_satan_adedi_bedeli = birkisinin_top_emlak_Satisi

    if en_cok_satis_parasi_getiren_bedeli < birkisinin_top_emlak_Satisi:
        en_cok_satis_parasi_getiren_bedeli = birkisinin_top_emlak_Satisi
        en_cok_satis_parasi_getiren_danisman = ad_soyad
        en_cok_satis_parasi_getiren_adedi = satilan_sayac

# ---------------------------------------------------------------------------------------
#   Tum danismanlardan elde edilen sonuclar.

toplam_satilanlar_sayisi = toplam_satilan_konut_sayisi + toplam_satilan_isyeri_sayisi + toplam_satilan_arsa_sayisi
toplam_kiraliklar_sayisi = top_kiralik_konut_sayisi + top_kiralik_arsa_sayisi + top_kiralik_isyeri_sayisi
print("\nTum Verilerden Elde Edilen Sonuclar.\n")
print("Her emlak tipi için o ay satılan ve kiralanan emlak sayıları ile satılma oranları (%)")
print("Satilanlarin Sayisi: ", toplam_satilanlar_sayisi, " Orani: %",
      "%.2f" % (toplam_satilanlar_sayisi * 100 / (toplam_satilanlar_sayisi + toplam_kiraliklar_sayisi)))
print("Satilan Konut Sayisi: ", toplam_satilan_konut_sayisi,
      " ve Orani: %" + "%.2f" % (toplam_satilan_konut_sayisi * 100 / toplam_satilanlar_sayisi))
print("Satilan Arsa Sayisi: ", toplam_satilan_arsa_sayisi,
      " ve Orani: %" + "%.2f" % (toplam_satilan_arsa_sayisi * 100 / toplam_satilanlar_sayisi))
print("Satilan Iyeri Sayisi: ", toplam_satilan_isyeri_sayisi,
      " ve Orani: %" + "%.2f" % (toplam_satilan_isyeri_sayisi * 100 / toplam_satilanlar_sayisi))
print("\nKiraliklarin Sayisi: ", toplam_kiraliklar_sayisi, " ve Orani: %",
      "%.2f" % (toplam_kiraliklar_sayisi * 100 / (toplam_satilanlar_sayisi + toplam_kiraliklar_sayisi)))
print("Kiralik Konut Sayisi: ", top_kiralik_konut_sayisi,
      " ve Orani: %" + "%.2f" % (top_kiralik_konut_sayisi * 100 / toplam_kiraliklar_sayisi))
print("Kiralik Arsa Sayisi: ", top_kiralik_arsa_sayisi,
      " ve Orani: %" + "%.2f" % (top_kiralik_arsa_sayisi * 100 / toplam_kiraliklar_sayisi))
print("Kiralik Isyeri Sayisi: ", top_kiralik_isyeri_sayisi,
      " ve Orani: %" + "%.2f" % (top_kiralik_isyeri_sayisi * 100 / toplam_kiraliklar_sayisi))

top_satilan_emlak_parasi = top_satilan_konut_parasi + top_satilan_arsa_parasi + top_satilan_isyeri_parasi
top_kiralanan_emlak_parasi = top_konut_kira_parasi + top_arsa_kira_parasi + top_isyeri_kira_parasi

print("\nHer emlak tipi için o ay satılan emlaklarin satis bedellerinin toplami (TL) ve ortalamasi (TL): ")
print("Satilan emlaklarin toplam bedeli: %.2f" % top_satilan_emlak_parasi, " TL")

print("Satilan konutlarin toplam bedeli: %.2f" % top_satilan_konut_parasi,
      " TL  ve Ortalamasi: %.2f" % (top_satilan_konut_parasi / toplam_satilanlar_sayisi), " TL")
print("Satilan Arsalarin toplam bedeli: %.2f" % top_satilan_arsa_parasi,
      " TL  ve Ortalamasi: %.2f" % (top_satilan_arsa_parasi / toplam_satilanlar_sayisi), " TL")
print("Satilan Isyerileri toplam bedeli: %.2f" % top_satilan_isyeri_parasi,
      " TL  ve Ortalamasi: %.2f" % (top_satilan_isyeri_parasi / toplam_satilanlar_sayisi), " TL")

print("\nBu ay en yuksek bedelle satilan emlagin tipi: ", en_yuksek_satilan_emlak_tipi)
print("Emlagin satis bedeli: %.2f" % en_yuksek_satilan_bedeli, " TL")
print("Emalgi satan danisman: ", en_yuksek_satan_danisman)

print("\nBu ay en yuksek bedelle kiralanan emlagin tipi: ", en_yuksek_kira_verilen_tipi)
print("Emlagin kira bedeli: %.2f" % en_yuksek_kira_bedeli, " TL")
print("Emlagi kira veren danisman: ", en_yuksek_kira_veren_danisman)

print("\nKiralanan konutlarin kira bedeli: %.2f" % top_konut_kira_parasi, " TL")

print("Aylik asgari net ucretten yuksek kiralanan konutlarin sayisi: ", asgari_ucretten_yuksek_kira_sayisi,
      " ve Kiralanan konutlar icindeki Orani: %",
      "%.2f" % (asgari_ucretten_yuksek_kira_sayisi * 100 / top_kiralik_konut_sayisi))

print("\nSatamayanlarin sayisi: ", satamayanlar, " ve orani: %", "%.2f" % (satamayanlar * 100 / danisman_sayisi))

print("\nSatis adedi olarak en cok satan danisman: ", en_cok_satan_danisman, "   Satis sayisi: ", en_cok_satan_adedi,
      "  ve Getirdigi para bedeli: %.2f" % en_cok_satan_adedi_bedeli, " TL")
print("Satis bedeli olarak en cok satan danisman: ", en_cok_satis_parasi_getiren_danisman,
      " ve Satis bedeli: %.2f" % en_cok_satis_parasi_getiren_bedeli,
      " TL  ve Satis sayisi: ", en_cok_satis_parasi_getiren_adedi)
print("\nKotasini dolduranlarin sayisi: ", kota_dolduran_sayisi, " ve danismanlar arasindaki Orani: %",
      "%.2f" % (kota_dolduran_sayisi * 100 / danisman_sayisi))
print("\nPrimi maasindan yuksek olanlarin sayisi: ", primi_yuksek_olan_sayisi, " ve danismanlar arasindaki Orani: %",
      "%.2f" % (primi_yuksek_olan_sayisi * 100 / danisman_sayisi))
print("\nEn az 10 adet veya en az 25000TL emlak kiralayan danismanlarin sayisi: ", _25K_10_adet_fazla_kiralayan_sayisi)
print("\nBu ay en yuksek prim alan danisman: ", en_yuksek_prim_danisman, " Maasi: %.2f" % en_yuksek_prim_maas,
      " TL , Primi: %.2f" % en_yuksek_prim_miktar,
      " TL ,  ve Aylik Toplam Ucreti: %.2f" % en_yuksek_prim_top_ucret, " TL")
print("\nBu ay en dusuk prim alan danisman: ", en_dusuk_prim_danisman, " Maasi: %.2f" % en_dusuk_prim_maas,
      " TL , Primi: %.2f" % en_dusuk_prim_miktar,
      " TL ,  ve Aylik Toplam Ucreti: %.2f" % en_dusuk_prim_top_ucret, " TL")

print("\nBu ay tum danismanlara odenecek ucretlerin toplami: %.2f" % tum_danismanlara_odenecek_tutar,
      " TL ve Ortalamasi: ",
      "%.2f" % (tum_danismanlara_odenecek_tutar / danisman_sayisi), " TL")

print(
    "\nBu ay acentenin toplam kazandigi komisyon (--danismanlarin ucretlerini vermeden once--): %.2f" % acentenin_toplam_emlak_komisyonu,
    " TL")
print(
    "Bu ay acentenin toplam kazandigi komisyon (--danismanlarin ucretlerini verdikten sonra--): %.2f" % acentenin_danisman_ucreti_verdikten_sonra_emlak_komisyonu,
    " TL")


