# Katkıda Bulunma Rehberi

Bu projeye katkıda bulunmak istediğiniz için teşekkür ederiz! Bu rehber, projeye nasıl katkıda bulunabileceğinizi açıklar.

## Nasıl Katkıda Bulunabilirsiniz

### 1. Bug Bildirimi
- GitHub Issues sayfasında yeni bir issue oluşturun
- Sorunu detaylı bir şekilde açıklayın
- Hata mesajlarını ve ekran görüntülerini ekleyin
- Hangi işletim sisteminde test ettiğinizi belirtin

### 2. Özellik Önerisi
- Yeni özellikler için GitHub Issues'da feature request oluşturun
- Özelliğin neden gerekli olduğunu açıklayın
- Varsa örnek kullanım senaryolarını ekleyin

### 3. Kod Katkısı
- Bu repository'yi fork edin
- Feature branch oluşturun (`git checkout -b feature/YeniOzellik`)
- Değişikliklerinizi commit edin
- Pull Request oluşturun

## Geliştirme Ortamı Kurulumu

### Gereksinimler
- Python 3.7+
- Git
- pip

### Kurulum Adımları
```bash
# Repository'yi klonlayın
git clone https://github.com/Parrhesist/Led-Fiyat-Tabelas---Python.git
cd Led-Fiyat-Tabelas---Python

# Sanal ortam oluşturun (önerilen)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows

# Gerekli paketleri yükleyin
pip install -r requirements.txt

# Geliştirme paketlerini yükleyin
pip install -r requirements-dev.txt
```

## Kod Standartları

### Python Kod Stili
- PEP 8 standartlarına uyun
- Maksimum satır uzunluğu: 120 karakter
- Docstring'leri Türkçe yazın
- Değişken ve fonksiyon isimlerini açıklayıcı yapın

### Commit Mesajları
- Türkçe yazın
- Açık ve anlaşılır olun
- Örnek: "Fiyat güncelleme fonksiyonu eklendi"

### Pull Request Açıklamaları
- Ne yapıldığını açıklayın
- Test edildi mi belirtin
- Ekran görüntüleri ekleyin (gerekirse)

## Test Etme

### Manuel Test
- Uygulamayı farklı Windows sürümlerinde test edin
- Farklı ekran çözünürlüklerinde test edin
- Hata durumlarını test edin

### Otomatik Test (Gelecekte)
- Unit testler ekleyin
- Integration testler ekleyin
- CI/CD pipeline kurun

## İletişim

- **GitHub Issues**: [Proje Issues Sayfası](https://github.com/Parrhesist/Led-Fiyat-Tabelas---Python/issues)
- **E-posta**: mehmetacikgoz8585@gmail.com
- **GitHub**: [@Parrhesist](https://github.com/Parrhesist)

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Katkıda bulunduğunuz kodlar da aynı lisans altında olacaktır.

---

Katkıda bulunduğunuz için tekrar teşekkür ederiz! 🎉
