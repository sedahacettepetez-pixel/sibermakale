# 🚀 Google Colab Kurulum Kılavuzu - UNSW-NB15 Projesi

## ⚡ HIZLI BAŞLANGIÇ (3 Adım)

### Adım 1: Projeyi Klonla

Google Colab'da yeni bir hücre açın ve çalıştırın:

```python
# Projeyi klonla
!git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git
%cd sibermakale

# Paketleri yükle (5-10 dakika)
!pip install -q -r requirements.txt

print("✅ Kurulum tamamlandı!")
```

### Adım 2: Veri Setini Yükle

**Seçenek A: Manuel Upload (Önerilen)**

```python
from google.colab import files
import os

# data/ klasörü oluştur
!mkdir -p data

print("📁 Lütfen UNSW-NB15 CSV dosyalarını yükleyin:")
print("  - UNSW_NB15_training-set.csv")
print("  - UNSW_NB15_testing-set.csv")

uploaded = files.upload()

# Dosyaları data/ klasörüne taşı
!mv *.csv data/

# Kontrol et
!ls -lh data/

print("✅ Veri seti yüklendi!")
```

**Seçenek B: Google Drive'dan Yükle**

```python
from google.colab import drive
drive.mount('/content/drive')

# Drive'daki dosyaları kopyala
!mkdir -p data
!cp "/content/drive/MyDrive/UNSW-NB15/*.csv" data/

# Kontrol et
!ls -lh data/

print("✅ Drive'dan veri yüklendi!")
```

**Seçenek C: Wget ile İndir (Eğer direkt link varsa)**

```python
!mkdir -p data
!wget -P data/ "VERİ_SETİ_URL"

# Kontrol et
!ls -lh data/

print("✅ Veri seti indirildi!")
```

### Adım 3: Analizi Başlat

```python
# Notebook'u açın ve çalıştırın
# File > Open notebook > GitHub
# URL: https://github.com/sedahacettepetez-pixel/sibermakale
# Branch: claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a
# File: unsw_nb15_analysis.ipynb

# Veya tüm hücreleri çalıştır:
# Runtime > Run all
```

---

## 📥 UNSW-NB15 VERİ SETİNİ NEREDEN İNDİRİRİM?

### Resmi Kaynak (UNSW)
https://research.unsw.edu.au/projects/unsw-nb15-dataset

**İndirmeniz Gereken Dosyalar:**
- `UNSW_NB15_training-set.csv` (veya `UNSW-NB15_1.csv`)
- `UNSW_NB15_testing-set.csv` (veya `UNSW-NB15_2.csv`)

### Alternatif: Kaggle (Manuel İndirme)
1. https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15 adresine git
2. "Download" butonuna tıkla (Kaggle hesabı gerekir)
3. ZIP'i aç
4. CSV dosyalarını Google Colab'a yükle

---

## 🎯 TAM KOD BLOKLARı

### Tek Komutla Kurulum + Veri Upload

```python
# 1. Projeyi kur
!git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git
%cd sibermakale
!pip install -q -r requirements.txt

# 2. Veri klasörü oluştur
!mkdir -p data

# 3. Veri yükle
from google.colab import files
print("📁 CSV dosyalarını yükleyin (training ve testing):")
uploaded = files.upload()
!mv *.csv data/

# 4. Kontrol
!ls -lh data/

print("✅ Hazır! Şimdi Cell > Run All ile analizi başlatın.")
```

---

## 🔧 GOOGLE DRIVE İLE ENTEGRASYON

### Drive'ı Mount Edip Veri Yükleme

```python
# Drive'ı bağla
from google.colab import drive
drive.mount('/content/drive')

# Proje klasörüne git
%cd /content/sibermakale

# Drive'dan veri kopyala
!mkdir -p data
!cp /content/drive/MyDrive/Datasets/UNSW-NB15/*.csv data/

# Alternatif: Belirli dosyaları kopyala
!cp "/content/drive/MyDrive/UNSW_NB15_training-set.csv" data/
!cp "/content/drive/MyDrive/UNSW_NB15_testing-set.csv" data/

print("✅ Veriler Drive'dan yüklendi!")
```

---

## 📊 ÇIKTILARI İNDİRME

### Analiz Tamamlandıktan Sonra

```python
# Tüm çıktıları ZIP'le
!zip -r unsw_nb15_outputs.zip artifacts/

# İndir
from google.colab import files
files.download('unsw_nb15_outputs.zip')

print("✅ Çıktılar indirildi!")
```

### Sadece IEEE Makalesini İndir

```python
from google.colab import files
files.download('artifacts/IEEE_Research_Paper_UNSW_NB15.docx')

print("✅ Makale indirildi!")
```

### Belirli Klasörleri İndir

```python
# Sadece tabloları indir
!zip -r tables.zip artifacts/tables/
files.download('tables.zip')

# Sadece görselleri indir
!zip -r figures.zip artifacts/figs/
files.download('figures.zip')
```

---

## ⚙️ GPU AKTĐF ETME (Önerilen)

```python
# Runtime > Change runtime type > Hardware accelerator > GPU (T4)

# GPU kontrolü
!nvidia-smi

# GPU varsa:
import torch
print(f"CUDA Available: {torch.cuda.is_available()}")
print(f"GPU Device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")
```

---

## 🐛 SORUN GİDERME

### Problem 1: "No such file or directory: data/"

```python
# Çözüm: data/ klasörü oluştur
!mkdir -p data
!ls -la  # Klasörü kontrol et
```

### Problem 2: "FileNotFoundError: UNSW-NB15 dataset"

```python
# Çözüm: Dosyaları kontrol et
!ls -lh data/

# Dosya adları farklıysa, config.json'ı güncelle veya dosya adlarını değiştir
!mv data/UNSW-NB15_1.csv data/UNSW_NB15_training-set.csv
!mv data/UNSW-NB15_2.csv data/UNSW_NB15_testing-set.csv
```

### Problem 3: "Memory Error" veya "Out of Memory"

```python
# Çözüm 1: High-RAM Runtime seç
# Runtime > Change runtime type > Runtime shape > High-RAM

# Çözüm 2: config.json'da sample_size'ı azalt
import json
with open('config.json', 'r') as f:
    config = json.load(f)

config['shap']['sample_size'] = 500  # Default: 1000
config['n_splits'] = 3  # Default: 5

with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)

print("✓ Config güncellendi - daha az bellek kullanacak")
```

### Problem 4: Paket kurulum hatası

```python
# requirements.txt'i manuel yükle
!pip install pandas numpy scipy scikit-learn
!pip install lightgbm xgboost catboost
!pip install shap lime matplotlib seaborn
!pip install python-docx jupyter
```

---

## 📝 KONTROL LİSTESİ

- [ ] Projeyi klonladım
- [ ] Paketleri yükledim (`pip install -r requirements.txt`)
- [ ] GPU aktif (Runtime > GPU)
- [ ] `data/` klasörü oluşturdum
- [ ] CSV dosyalarını `data/` klasörüne yükledim
- [ ] Dosya adlarını kontrol ettim
- [ ] Notebook'u açtım (`unsw_nb15_analysis.ipynb`)
- [ ] Cell > Run All ile başlattım
- [ ] Analiz tamamlandı (~45-60 dakika GPU ile)
- [ ] Çıktıları indirdim

---

## 🎉 BAŞARILI!

Artık projeniz Google Colab'da çalışıyor!

**Beklenen Süre:**
- GPU (T4): ~45-60 dakika
- CPU: ~2-3 saat (önerilmez)

**Çıktılar:**
- 60+ tablo (CSV/XLSX)
- 50+ görsel (PNG)
- 1 IEEE makalesi (DOCX)

---

**Proje:** UNSW-NB15 Network Intrusion Detection System
**Branch:** `claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a`
**Son Güncelleme:** 2025-11-15
