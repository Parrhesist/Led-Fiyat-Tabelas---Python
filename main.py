#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Altın Fiyat Tabelası - LED Tabela Uygulaması

Bu uygulama, web sitelerinden altın fiyat verilerini çekerek LED tabela formatında görüntüler.
Kuyumcu işletmeleri için tasarlanmıştır.

Geliştirici: Mehmet Açıkgöz (Parrhesist)
E-posta: mehmetacikgoz8585@gmail.com
GitHub: https://github.com/Parrhesist
Lisans: MIT

Kullanım:
    python main.py

Gereksinimler:
    pip install -r requirements.txt
"""

import tkinter as tk
from tkinter import messagebox
import requests  # pyright: ignore[reportMissingModuleSource]
from bs4 import BeautifulSoup  # pyright: ignore[reportMissingModuleSource]
import random

class GoldApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Altın Fiyatları")
        self.root.configure(bg="black")

        # Pencere çerçevelerini kaldır
        self.root.overrideredirect(True)

        # Program penceresinin boyutunu ve konumunu ayarla
        window_width = 555
        window_height = 880
        x_coordinate = -5
        y_coordinate = 0
        self.root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        # Başlık
        self.label_baslik = tk.Label(self.root, text="Fiyat Tabelası", fg="yellow", bg="black", height=1, font=("Elephant", 34, "bold"), borderwidth=0)
        self.label_baslik.grid(row=0, column=0, columnspan=1, padx=120, pady=0, sticky="w")

        # Başlığa tıklayınca çıkış yapma
        self.label_baslik.bind("<Button-1>", self.cikis)

        # Logonun yanıp sönme efekti
        self.flash_state = False
        self.flash_logo()

        # Altınlar tablosu için çerçeve oluştur
        self.frame_altinlar = tk.Frame(self.root, bg="black", bd=0)
        self.frame_altinlar.grid(row=1, column=0, columnspan=3, padx=0, pady=2, sticky="w")

        self.onceki_fiyatlar = {}
        self.label_etiketler = {}  # Fiyat etiketlerini saklamak için bir sözlük
        self.renkler = {}  # Eski renkleri saklamak için bir sözlük

        # Otomatik güncelleme başlat
        self.otomatik_guncelle()
        # Rastgele fiyat güncelleme başlat
        self.rastgele_fiyat_degistir()

    def flash_logo(self):
        new_fg = "red" if self.flash_state else "white"
        self.label_baslik.config(foreground=new_fg)
        self.flash_state = not self.flash_state
        self.root.after(600, self.flash_logo)

    def verileri_getir(self):
        try:
            # TODO: Kendi veri kaynağınızın URL'sini buraya ekleyin
            # Örnek: url = "https://www.doviz.com/altin-fiyatlari"
            url = "https://yourwebsite.com/"
            
            # User-Agent ekleyerek web scraping'i daha güvenilir hale getirin
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, "html.parser")

            # Tabloyu id ile bulun
            tablo = soup.find("table", id="price-table")
            veriler = tablo.find("tbody").find_all("tr")

            # Altın ONS fiyatını çek
            ons_fiyati = soup.find(id="gold-ons-price").text.strip().replace(".", "").replace(",", ".").replace("₺", "")
            ons_fiyati = float(ons_fiyati)

            # Altın KG/USD değerini hesapla
            ons_fiyati_alis = ons_fiyati - 2 
    
            # Eski widget'ları temizle
            for widget in self.frame_altinlar.winfo_children():
                widget.destroy()

            altin_data = []

            for veri in veriler:
                altin_cinsi = veri.find("td", class_="product-name").text.strip()
                alis_fiyati = float(veri.find("td", class_="buy-price").text.strip().replace(".", "").replace(",", ".").replace("₺", ""))
                satis_fiyati = float(veri.find("td", class_="sell-price").text.strip().replace(".", "").replace(",", ".").replace("₺", ""))

                altin_data.append((altin_cinsi, alis_fiyati, satis_fiyati))

            # AltınKG/USD satırını ekleyin
            altin_data.append(("Altın/ONS", ons_fiyati_alis, ons_fiyati))

            row_index = 0
            for altin_cinsi, alis_fiyati, satis_fiyati in altin_data:
                label_altin_cinsi = tk.Label(self.frame_altinlar, text=altin_cinsi, fg="yellow", bg="black", font=("Helvetica", 30, "bold"), borderwidth=0.00, highlightthickness=3, width=22, height=1)
                label_altin_cinsi.grid(row=row_index, column=0, padx=0, pady=0, sticky="w")

                # Alış fiyatı etiketi oluştur
                label_alis_fiyati = tk.Label(self.frame_altinlar, text="{:,.2f}".format(alis_fiyati), fg="red", bg="black", font=("Helvetica", 33, "bold"), borderwidth=0.00, highlightthickness=3, width=10, height=1)
                label_alis_fiyati.grid(row=row_index + 1, column=0, padx=0, pady=0, sticky="w")
                
                # Satış fiyatı etiketi oluştur
                label_satis_fiyati = tk.Label(self.frame_altinlar, text="{:,.2f}".format(satis_fiyati), fg="green", bg="black", font=("Helvetica", 33, "bold"), borderwidth=0.00, highlightthickness=3, width=10, height=1)
                label_satis_fiyati.grid(row=row_index + 1, column=0, padx=0, pady=0, sticky="e")

                # Etiketleri sakla
                self.label_etiketler[(altin_cinsi, "alis")] = label_alis_fiyati
                self.label_etiketler[(altin_cinsi, "satis")] = label_satis_fiyati

                # Eski renkleri sakla
                self.renkler[(altin_cinsi, "alis")] = (label_alis_fiyati.cget("bg"), label_alis_fiyati.cget("fg"))
                self.renkler[(altin_cinsi, "satis")] = (label_satis_fiyati.cget("bg"), label_satis_fiyati.cget("fg"))

                row_index += 2
                self.onceki_fiyatlar[altin_cinsi] = {'alis': alis_fiyati, 'satis': satis_fiyati}

            # Tabloyu yatayda 344 piksel genişliğinde ayarla
            self.frame_altinlar.config(width=555)

        except Exception as e:
            messagebox.showerror("Hata", f"Veri alırken bir hata oluştu: {e}")

    def cikis(self, event=None):
        self.root.quit()

    def otomatik_guncelle(self):
        self.verileri_getir()
        self.root.after(20000, self.otomatik_guncelle)

    def rastgele_fiyat_degistir(self):
        if not self.label_etiketler:
            return

        secilen_etiketler = random.sample(list(self.label_etiketler.keys()), random.randint(1, len(self.label_etiketler)))

        for (altin_cinsi, fiyat_tipi) in secilen_etiketler:
            mevcut_fiyat = self.onceki_fiyatlar[altin_cinsi][fiyat_tipi]
            degisim = random.choice([-0.02, 0.01])
            yeni_fiyat = mevcut_fiyat + degisim

            etiket = self.label_etiketler[(altin_cinsi, fiyat_tipi)]

            # Fiyat değişimine göre ok ekleme
            if degisim > 0:
                ok_isareti = "▲"
                etiket.config(bg="green", fg="white")
            else:
                ok_isareti = "▼"
                etiket.config(bg="red", fg="white")

            # Alış fiyatı güncelleme
            if fiyat_tipi == "alis":
                etiket.config(text="{:,.2f} {}".format(yeni_fiyat, ok_isareti))
            else:
                etiket.config(text="{} {:,.2f}".format(ok_isareti, yeni_fiyat))

        # Belirli bir süre sonra rengi tekrar eski haline döndür
        self.root.after(1500, self.rengi_siyah_yap, secilen_etiketler)

        # 3 saniyede bir güncelleme yap
        self.root.after(3000, self.rastgele_fiyat_degistir)

    def rengi_siyah_yap(self, etiketler):
        for (altin_cinsi, fiyat_tipi) in etiketler:
            etiket = self.label_etiketler[(altin_cinsi, fiyat_tipi)]
            eski_bg, eski_fg = self.renkler[(altin_cinsi, fiyat_tipi)]
            etiket.config(bg=eski_bg, fg=eski_fg)

if __name__ == "__main__":
    root = tk.Tk()
    app = GoldApp(root)
    root.mainloop()
