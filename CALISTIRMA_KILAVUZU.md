# 🚀 UNSW-NB15 Proje Çalıştırma Kılavuzu

## 📋 İçindekiler
1. [Google Colab ile Çalıştırma](#-google-colab-ile-çalıştırma)
2. [Masaüstü Kurulum (Windows)](#-masaüstü-kurulum-windows)
3. [Masaüstü Kurulum (macOS/Linux)](#-masaüstü-kurulum-macoslinux)
4. [Veri Setini İndirme](#-veri-setini-indirme)
5. [Çıktıları Görüntüleme](#-çıktıları-görüntüleme)

---

## 🌐 Google Colab ile Çalıştırma

### ⚡ 3 ADIMDA BAŞLANGIÇ

**ADIM 1: Projeyi Kur**

Google Colab'a gidin: **https://colab.research.google.com**

Yeni bir hücre açıp şu kodu çalıştırın:

```python
# Projeyi klonla ve kur
!git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git
%cd sibermakale
!pip install -q -r requirements.txt

print("✅ Kurulum tamamlandı!")
```

**ADIM 2: Veri Setini Yükle**

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

**ADIM 3: Analizi Başlat**

```python
# Notebook'u GitHub'dan aç:
# File > Open notebook > GitHub
# URL: https://github.com/sedahacettepetez-pixel/sibermakale
# Branch: claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a
# Dosya: unsw_nb15_analysis.ipynb

# Veya tüm hücreleri çalıştır:
# Runtime > Run all
```

### 📥 Google Drive ile Veri Yükleme

```python
from google.colab import drive
drive.mount('/content/drive')

# Drive'dan veri kopyala
%cd /content/sibermakale
!mkdir -p data
!cp "/content/drive/MyDrive/UNSW-NB15/*.csv" data/

print("✅ Drive'dan veri yüklendi!")
```

---

## 💻 Masaüstü Kurulum (Windows)

### ADIM 1: Gereksinimleri Yükle

1. **Python 3.8+ Kurulumu**
   - İndir: https://www.python.org/downloads/
   - ⚠️ "Add Python to PATH" seçeneğini işaretle!

2. **Git Kurulumu**
   - İndir: https://git-scm.com/download/win
   - Varsayılan ayarlarla kur

### ADIM 2: Projeyi İndir

**PowerShell veya CMD açın:**

```cmd
cd %USERPROFILE%\Desktop
git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a https://github.com/sedahacettepetez-pixel/sibermakale.git
cd sibermakale
```

### ADIM 3: Sanal Ortam ve Paketler

```cmd
python -m venv venv
venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt
```

### ADIM 4: Veri Setini Ekle

1. UNSW-NB15 veri setini indirin (bkz. [Veri Setini İndirme](#-veri-setini-indirme))
2. CSV dosyalarını `sibermakale\data\` klasörüne kopyalayın

```cmd
# Klasörü kontrol et
dir data\
```

### ADIM 5: Notebook'u Başlat

```cmd
jupyter notebook unsw_nb15_analysis.ipynb
```

Tarayıcıda açılacaktır. **Cell → Run All** ile analizi başlatın.

---

## 🍎 Masaüstü Kurulum (macOS/Linux)

### ADIM 1: Terminal'i Aç

**macOS:** `Command + Space` → "Terminal" → Enter
**Linux:** `Ctrl + Alt + T`

### ADIM 2: Projeyi İndir

```bash
cd ~/Desktop
git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git
cd sibermakale
```

### ADIM 3: Sanal Ortam ve Paketler

```bash
# Sanal ortam oluştur
python3 -m venv venv

# Aktif et
source venv/bin/activate

# Paketleri yükle
pip install --upgrade pip
pip install -r requirements.txt
```

### ADIM 4: Veri Setini Ekle

1. UNSW-NB15 veri setini indirin (bkz. [Veri Setini İndirme](#-veri-setini-indirme))
2. CSV dosyalarını `sibermakale/data/` klasörüne kopyalayın

```bash
# Klasörü kontrol et
ls -lh data/
```

### ADIM 5: Notebook'u Başlat

```bash
jupyter notebook unsw_nb15_analysis.ipynb
```

---

## 📥 Veri Setini İndirme

### UNSW-NB15 Veri Setini Nereden İndiririm?

**Seçenek 1: UNSW Resmi Web Sitesi (Önerilen)**

https://research.unsw.edu.au/projects/unsw-nb15-dataset

İndirmeniz gereken dosyalar:
- `UNSW_NB15_training-set.csv`
- `UNSW_NB15_testing-set.csv`

**Seçenek 2: Kaggle (Manuel İndirme)**

https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15

1. Kaggle hesabınızla giriş yapın
2. "Download" butonuna tıklayın
3. ZIP dosyasını açın
4. CSV dosyalarını `data/` klasörüne kopyalayın

**Seçenek 3: Alternatif Kaynak (IEEE Dataport)**

https://ieee-dataport.org/open-access/unsw-nb15-network-data-set

### Dosya Yapısı

İndirdikten sonra `data/` klasörünüz şöyle görünmeli:

```
data/
├── UNSW_NB15_training-set.csv  (veya UNSW-NB15_1.csv)
└── UNSW_NB15_testing-set.csv   (veya UNSW-NB15_2.csv)
```

**Not:** Dosya adları farklı olabilir. Kod otomatik olarak şu isimleri arar:
- Training: `UNSW_NB15_training-set.csv`, `UNSW-NB15_1.csv`, `training-set.csv`
- Testing: `UNSW_NB15_testing-set.csv`, `UNSW-NB15_2.csv`, `testing-set.csv`

---

## 📂 Proje Yapısı

```
sibermakale/
├── unsw_nb15_analysis.ipynb    # Ana analiz notebook'u ⭐
├── UNSW_NB15_Colab.ipynb       # Colab versiyonu
├── config.json                  # Yapılandırma
├── utils.py                     # Yardımcı fonksiyonlar
├── requirements.txt             # Python bağımlılıkları
├── data/                        # Veri seti buraya 📥
│   ├── UNSW_NB15_training-set.csv
│   └── UNSW_NB15_testing-set.csv
├── artifacts/                   # Çıktılar buraya 📊
│   ├── figs/                    # 50+ görsel
│   ├── tables/                  # 60+ tablo
│   └── IEEE_Research_Paper_UNSW_NB15.docx
├── README.md
├── COLAB_KOMUTLARI.md
└── SISTEM_DOKUMANTASYONU.md
```

---

## 📊 Çıktıları Görüntüleme

### Analiz Tamamlandıktan Sonra

Tüm çıktılar `artifacts/` klasöründe olacak:

**Google Colab'da İndirme:**

```python
# Tüm çıktıları ZIP'le ve indir
!zip -r unsw_nb15_outputs.zip artifacts/

from google.colab import files
files.download('unsw_nb15_outputs.zip')

print("✅ Çıktılar indirildi!")
```

**Masaüstünde Görüntüleme:**

Windows:
```cmd
cd artifacts
explorer .
```

macOS:
```bash
cd artifacts
open .
```

Linux:
```bash
cd artifacts
xdg-open .
```

### Ana Çıktılar

1. **IEEE Araştırma Makalesi**
   - `artifacts/IEEE_Research_Paper_UNSW_NB15.docx`
   - 15-20 sayfa, yayın-hazır makale

2. **Tablolar (60+)**
   - `artifacts/tables/*.csv`
   - Excel veya LibreOffice ile açın

3. **Görseller (50+)**
   - `artifacts/figs/*.png`
   - Yüksek çözünürlük PNG formatında

---

## 🎯 Hızlı Başlangıç Özeti

### Google Colab (5 dakika)
```python
!git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git
%cd sibermakale
!pip install -q -r requirements.txt
!mkdir -p data
# Sonra veri setini yükle ve Run All
```

### Windows (10 dakika)
```cmd
git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a https://github.com/sedahacettepetez-pixel/sibermakale.git
cd sibermakale
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
REM Veri setini data\ klasörüne kopyala
jupyter notebook unsw_nb15_analysis.ipynb
```

### macOS/Linux (10 dakika)
```bash
git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a https://github.com/sedahacettepetez-pixel/sibermakale.git
cd sibermakale
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Veri setini data/ klasörüne kopyala
jupyter notebook unsw_nb15_analysis.ipynb
```

---

## ⏱️ Beklenen Süre

- **Google Colab (GPU T4):** ~45-60 dakika
- **Masaüstü (CPU):** ~2-3 saat
- **Masaüstü (GPU):** ~1-1.5 saat

---

## ❓ Sık Karşılaşılan Sorunlar

### 1. "FileNotFoundError: UNSW-NB15 dataset"
**Çözüm:** Veri setini `data/` klasörüne ekleyin
```bash
ls -lh data/  # Dosyaların olduğunu kontrol et
```

### 2. "ModuleNotFoundError"
**Çözüm:** Paketleri yükleyin
```bash
pip install -r requirements.txt
```

### 3. "Out of Memory" Hatası
**Çözüm (Colab):** Runtime > Change runtime type > High-RAM
**Çözüm (Masaüstü):** config.json'da sample_size'ı azaltın

### 4. "git: command not found"
**Çözüm:** Git'i yükleyin: https://git-scm.com/downloads

### 5. Branch bulunamadı
**Çözüm:**
```bash
git fetch --all
git checkout claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a
```

---

## ✅ Başarı Kontrol Listesi

- [ ] Git ve Python yüklü
- [ ] Projeyi klonladım
- [ ] Sanal ortam oluşturdum ve aktif ettim
- [ ] requirements.txt paketlerini yükledim
- [ ] UNSW-NB15 veri setini indirdim
- [ ] CSV dosyalarını `data/` klasörüne koydum
- [ ] Jupyter Notebook başlattım
- [ ] Tüm hücreleri çalıştırdım (Run All)
- [ ] Analiz tamamlandı
- [ ] `artifacts/` klasöründe çıktıları gördüm
- [ ] IEEE makalesini açtım

---

## 📄 Proje Bilgileri

**Proje:** UNSW-NB15 Network Intrusion Detection System
**Branch:** `claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a`
**Repository:** https://github.com/sedahacettepetez-pixel/sibermakale
**Son Güncelleme:** 2025-11-15

**Veri Seti Referansı:**
```
Moustafa, N., & Slay, J. (2015). UNSW-NB15: a comprehensive data set for
network intrusion detection systems (UNSW-NB15 network data set).
Military Communications and Information Systems Conference (MilCIS), 2015.
```

---

**🎉 Başarılar! Projeniz hazır!**
