# 🚀 UNSW-NB15 Proje Çalıştırma Kılavuzu

## 📋 İçindekiler
1. [Google Colab ile Çalıştırma](#-google-colab-ile-çalıştırma)
2. [Masaüstü Kurulum (Windows)](#-masaüstü-kurulum-windows)
3. [Masaüstü Kurulum (macOS/Linux)](#-masaüstü-kurulum-macoslinux)
4. [Projeyi İndirme ve Çalıştırma](#-projeyi-indirme-ve-çalıştırma)
5. [Çıktıları Görüntüleme](#-çıktıları-görüntüleme)

---

## 🌐 Google Colab ile Çalıştırma

### ⚡ TEK KOMUTLA KURULUM (EN KOLAY)

Google Colab'a gidin: **https://colab.research.google.com**

Yeni bir hücre açıp şu kodu çalıştırın:

```python
# ADIM 1: Projeyi klonla ve kur
!git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git
%cd sibermakale
!pip install -q -r requirements.txt

print("✅ Kurulum tamamlandı!")
```

### 📊 ADIM 2: Veri Setini İndir

```python
# Kaggle token yükle (ilk kez)
from google.colab import files
print("📁 Lütfen kaggle.json dosyanızı yükleyin:")
uploaded = files.upload()

# Kaggle yapılandır
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# UNSW-NB15 veri setini indir
!kaggle datasets download -d mrwellsdavid/unsw-nb15
!unzip -q unsw-nb15.zip -d data/

print("✅ Veri seti hazır!")
```

### 🎯 ADIM 3: Notebook'u Çalıştır

```python
# Jupyter notebook'u aç
from google.colab import drive
drive.mount('/content/drive')

# unsw_nb15_analysis.ipynb dosyasını Colab'da açın
# File > Open notebook > GitHub sekmesi
# URL: https://github.com/sedahacettepetez-pixel/sibermakale
# Branch: claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a
# Dosya: unsw_nb15_analysis.ipynb
```

### 📥 ADIM 4: Çıktıları İndir

```python
# Tüm çıktıları ZIP olarak indir
!zip -r unsw_nb15_outputs.zip artifacts/ -x "*.git*"

from google.colab import files
files.download('unsw_nb15_outputs.zip')

print("✅ Çıktılar indirildi!")
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

3. **Jupyter Notebook Kurulumu**
   ```cmd
   pip install jupyter notebook
   ```

### ADIM 2: Projeyi İndir

**PowerShell veya CMD açın** (Windows Tuşu + R → `cmd` → Enter)

```cmd
cd %USERPROFILE%\Desktop
git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a https://github.com/sedahacettepetez-pixel/sibermakale.git
cd sibermakale
```

### ADIM 3: Sanal Ortam Oluştur ve Paketleri Yükle

```cmd
python -m venv venv
venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt
```

### ADIM 4: Veri Setini İndir

**Seçenek A: Kaggle ile (Otomatik)**
```cmd
pip install kaggle

REM Kaggle token dosyanızı C:\Users\<KullanıcıAdı>\.kaggle\ klasörüne kopyalayın
mkdir %USERPROFILE%\.kaggle
REM kaggle.json dosyanızı bu klasöre kopyalayın

kaggle datasets download -d mrwellsdavid/unsw-nb15
tar -xf unsw-nb15.zip -C data\
```

**Seçenek B: Manuel İndirme**
1. https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15 adresine git
2. "Download" butonuna tıkla
3. ZIP'i aç ve `data/` klasörüne kopyala

### ADIM 5: Notebook'u Başlat

```cmd
jupyter notebook unsw_nb15_analysis.ipynb
```

Tarayıcıda otomatik açılacaktır. **Cell → Run All** ile tüm analizi başlatın.

---

## 🍎 Masaüstü Kurulum (macOS/Linux)

### ADIM 1: Terminal'i Aç

**macOS:** `Command + Space` → "Terminal" yaz → Enter
**Linux:** `Ctrl + Alt + T`

### ADIM 2: Gereksinimleri Kontrol Et

```bash
# Python kontrolü
python3 --version  # 3.8+ olmalı

# Git kontrolü
git --version

# Python yoksa:
# macOS: brew install python3
# Ubuntu/Debian: sudo apt install python3 python3-pip python3-venv
# Fedora: sudo dnf install python3 python3-pip
```

### ADIM 3: Projeyi İndir

```bash
cd ~/Desktop
git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git
cd sibermakale
```

### ADIM 4: Sanal Ortam ve Paketler

```bash
# Sanal ortam oluştur
python3 -m venv venv

# Aktif et
source venv/bin/activate

# Paketleri yükle
pip install --upgrade pip
pip install -r requirements.txt
```

### ADIM 5: Veri Setini İndir

```bash
# Kaggle kurulumu
pip install kaggle

# Kaggle token yapılandır
mkdir -p ~/.kaggle
# kaggle.json dosyanızı ~/.kaggle/ klasörüne kopyalayın
chmod 600 ~/.kaggle/kaggle.json

# Veri setini indir
kaggle datasets download -d mrwellsdavid/unsw-nb15
unzip -q unsw-nb15.zip -d data/

echo "✅ Veri seti hazır!"
```

### ADIM 6: Notebook'u Başlat

```bash
jupyter notebook unsw_nb15_analysis.ipynb
```

---

## 📂 Projeyi İndirme ve Çalıştırma

### Klasör Yapısı

İndirdikten sonra projeniz şöyle görünecek:

```
sibermakale/
├── unsw_nb15_analysis.ipynb    # Ana analiz notebook'u
├── UNSW_NB15_Colab.ipynb       # Colab versiyonu
├── config.json                  # Yapılandırma dosyası
├── utils.py                     # Yardımcı fonksiyonlar
├── requirements.txt             # Python bağımlılıkları
├── data/                        # Veri seti buraya gelecek
│   ├── UNSW-NB15_1.csv
│   ├── UNSW-NB15_2.csv
│   ├── UNSW-NB15_3.csv
│   └── UNSW-NB15_4.csv
├── artifacts/                   # Çıktılar buraya kaydedilecek
│   ├── figs/                    # 40+ görselleştirme
│   ├── tables/                  # 50+ tablo (CSV/XLSX)
│   └── IEEE_Research_Paper_UNSW_NB15.docx  # Araştırma makalesi
├── README.md
├── KURULUM.md
├── COLAB_KOMUTLARI.md
└── SISTEM_DOKUMANTASYONU.md
```

### Tüm Hücreleri Çalıştırma

**Jupyter Notebook'ta:**
1. Menüden **Cell → Run All** seçin
2. Ya da her hücreyi tek tek çalıştırın: `Shift + Enter`

**Tahmini Süre:**
- Google Colab (T4 GPU): ~45-60 dakika
- Masaüstü (CPU): ~2-3 saat
- Masaüstü (GPU): ~1-1.5 saat

---

## 📊 Çıktıları Görüntüleme

### Analiz Tamamlandıktan Sonra

Tüm çıktılar `artifacts/` klasöründe olacak:

```bash
# Klasör yapısını görüntüle
ls -R artifacts/

# Windows:
dir /s artifacts\
```

### Ana Çıktılar

1. **IEEE Araştırma Makalesi**
   - Dosya: `artifacts/IEEE_Research_Paper_UNSW_NB15.docx`
   - Microsoft Word ile açın
   - 15-20 sayfa, tam hazır makale!

2. **Tablolar (50+)**
   - Konum: `artifacts/tables/`
   - Format: CSV ve XLSX
   - Excel veya LibreOffice ile açın

3. **Görseller (40+)**
   - Konum: `artifacts/figs/`
   - Format: PNG (yüksek çözünürlük)
   - Herhangi bir görüntü görüntüleyici ile açın

### Çıktıları Masaüstünüzde Görüntüleme

**Windows:**
```cmd
cd artifacts
explorer .
```

**macOS:**
```bash
cd artifacts
open .
```

**Linux:**
```bash
cd artifacts
xdg-open .  # veya nautilus . / dolphin . / thunar .
```

### Çıktıları ZIP Yapma

**Windows (PowerShell):**
```powershell
Compress-Archive -Path artifacts -DestinationPath unsw_nb15_outputs.zip
```

**macOS/Linux:**
```bash
zip -r unsw_nb15_outputs.zip artifacts/
```

---

## 🎯 Hızlı Başlangıç Özeti

### Google Colab (5 dakika)
```python
!git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git
%cd sibermakale
!pip install -q -r requirements.txt
# Sonra veri setini yükle ve Run All
```

### Masaüstü Windows (10 dakika)
```cmd
git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a https://github.com/sedahacettepetez-pixel/sibermakale.git
cd sibermakale
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook unsw_nb15_analysis.ipynb
```

### Masaüstü macOS/Linux (10 dakika)
```bash
git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a https://github.com/sedahacettepetez-pixel/sibermakale.git
cd sibermakale
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook unsw_nb15_analysis.ipynb
```

---

## ❓ Sık Karşılaşılan Sorunlar

### 1. "git: command not found"
**Çözüm:** Git'i yükleyin: https://git-scm.com/downloads

### 2. "pip: command not found"
**Çözüm:** Python'u PATH'e ekleyin veya `python -m pip` kullanın

### 3. "ModuleNotFoundError"
**Çözüm:**
```bash
pip install -r requirements.txt
```

### 4. "Kaggle API token not found"
**Çözüm:**
1. Kaggle.com → Account → Create API Token
2. `kaggle.json` dosyasını `~/.kaggle/` klasörüne kopyala

### 5. "Out of Memory" Hatası
**Çözüm:**
- Google Colab: Runtime → Change runtime type → High-RAM
- Masaüstü: `config.json`'da `sample_size` değerini azalt

### 6. Branch bulunamadı hatası
**Çözüm:**
```bash
git fetch --all
git checkout claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a
```

---

## 📞 Destek

Sorun yaşıyorsanız:
1. `SISTEM_DOKUMANTASYONU.md` dosyasını okuyun
2. `requirements.txt` dosyasındaki paketlerin kurulu olduğundan emin olun
3. Python versiyonunu kontrol edin: `python --version` (3.8+ olmalı)

---

## 📄 Lisans ve Referans

**Proje:** UNSW-NB15 Network Intrusion Detection System
**Branch:** `claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a`
**Repository:** https://github.com/sedahacettepetez-pixel/sibermakale
**Son Güncelleme:** 2025-11-15

**Veri Seti Referansı:**
```
Moustafa, N., & Slay, J. (2015). UNSW-NB15: a comprehensive data set for
network intrusion detection systems (UNSW-NB15 network data set).
In 2015 military communications and information systems conference (MilCIS)
(pp. 1-6). IEEE.
```

---

## ✅ Başarı Kontrol Listesi

- [ ] Git yüklü ve çalışıyor
- [ ] Python 3.8+ yüklü
- [ ] Projeyi doğru branch ile klonladım
- [ ] Sanal ortam oluşturdum ve aktif ettim
- [ ] requirements.txt paketlerini yükledim
- [ ] UNSW-NB15 veri setini indirdim
- [ ] Jupyter Notebook başlattım
- [ ] Tüm hücreleri çalıştırdım
- [ ] artifacts/ klasöründe çıktıları gördüm
- [ ] IEEE_Research_Paper_UNSW_NB15.docx dosyasını açtım

---

**🎉 Başarılar! Projeniz hazır ve çalışıyor!**
