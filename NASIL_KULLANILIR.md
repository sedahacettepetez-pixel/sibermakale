# 📖 UNSW-NB15 Projesi - Nasıl Kullanılır?

Bu kılavuz projeyi 3 farklı yöntemle nasıl çalıştıracağınızı gösterir:
1. 💻 Bilgisayarınızda (Windows/Mac/Linux)
2. ☁️ Google Colab'da (Ücretsiz GPU)
3. 📦 ZIP İndirme

---

## 🎯 Yöntem 1: Bilgisayarınızda Çalıştırma

### A) Projeyi İndirme

#### Git ile (Önerilen):
```bash
# Projeyi klonla
git clone https://github.com/sedahacettepetez-pixel/sibermakale.git

# Dizine gir
cd sibermakale

# Doğru branch'e geç
git checkout claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a
```

#### ZIP ile:
1. GitHub sayfasına gidin: https://github.com/sedahacettepetez-pixel/sibermakale
2. **"Code"** butonuna tıklayın (yeşil buton)
3. **"Download ZIP"** seçin
4. ZIP dosyasını çıkartın
5. Terminal/CMD ile klasöre girin

---

### B) Kurulum

#### Otomatik Kurulum (Linux/Mac):
```bash
chmod +x setup.sh
./setup.sh
```

#### Manuel Kurulum (Windows/Tüm Platformlar):

**1. Python Kontrolü** (3.9+ gerekli)
```bash
python --version
# veya
python3 --version
```

**2. Sanal Ortam Oluştur**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

**3. Paketleri Yükle**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
⏳ Bu işlem 5-10 dakika sürebilir (PyTorch büyük bir paket).

---

### C) UNSW-NB15 Veri Setini İndirme

#### Yöntem 1: Kaggle API (Önerilen)

**1. Kaggle Hesabı:**
- https://www.kaggle.com adresine gidin
- Hesap oluşturun veya giriş yapın

**2. API Token:**
- Sağ üst → Your Profile → Account
- "Create New API Token" tıklayın
- `kaggle.json` dosyası indirilecek

**3. Token'ı Yerleştirin:**
```bash
# Linux/Mac
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# Windows
mkdir %USERPROFILE%\.kaggle
move %USERPROFILE%\Downloads\kaggle.json %USERPROFILE%\.kaggle\
```

**4. Veri Setini İndirin:**
```bash
kaggle datasets download -d mrwellsdavid/unsw-nb15
unzip unsw-nb15.zip -d data/
```

#### Yöntem 2: Manuel İndirme

1. https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15 adresine gidin
2. "Download" butonuna tıklayın
3. ZIP'i çıkartın
4. CSV dosyalarını `data/` klasörüne taşıyın:
   - `UNSW_NB15_training-set.csv`
   - `UNSW_NB15_testing-set.csv`

**Kontrol:**
```bash
ls data/
# İki CSV dosyası görmelisiniz
```

---

### D) Jupyter Notebook'u Başlatma

```bash
# Sanal ortamı aktifleştirin (henüz aktif değilse)
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Jupyter başlat
jupyter notebook unsw_nb15_analysis.ipynb
```

Tarayıcınızda otomatik açılacak. Açılmazsa:
- Terminalde görünen URL'yi kopyalayın (örn: `http://localhost:8888/...`)
- Tarayıcınıza yapıştırın

---

### E) Pipeline'ı Çalıştırma

Jupyter Notebook'ta:

**1. Hücre Hücre:**
- Her hücreyi `Shift + Enter` ile çalıştırın
- Çıktıları kontrol edin
- İstediğiniz yerde durun

**2. Tümünü Çalıştır:**
- `Cell` → `Run All` menüsünden
- ⏳ İlk çalışma 20-40 dakika sürebilir (CPU'da)

**3. Sonuçları Görün:**
- `artifacts/tables/` - CSV tablolar
- `artifacts/figs/` - Görselleştirmeler
- `artifacts/models/` - Eğitilmiş modeller

---

## ☁️ Yöntem 2: Google Colab ile Çalıştırma

### Avantajlar:
- ✅ **Ücretsiz GPU** (NVIDIA Tesla T4)
- ✅ Kurulum gerektirmez
- ✅ Her yerde erişim
- ✅ 12GB RAM + 100GB disk

### Adımlar:

#### 1. Colab Notebook'u Açın

**Seçenek A: GitHub'dan Direkt Açma**
1. https://colab.research.google.com/ adresine gidin
2. "GitHub" sekmesini seçin
3. Repository: `sedahacettepetez-pixel/sibermakale`
4. Branch: `claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a`
5. `UNSW_NB15_Colab.ipynb` dosyasını açın

**Seçenek B: Manuel Yükleme**
1. Projeyi ZIP olarak indirin
2. `UNSW_NB15_Colab.ipynb` dosyasını Colab'a upload edin

#### 2. GPU'yu Aktifleştirin

- `Runtime` → `Change runtime type`
- **Hardware accelerator**: GPU (T4)
- `Save` tıklayın

#### 3. Hücreleri Sırayla Çalıştırın

```python
# 1. Drive bağla (opsiyonel)
from google.colab import drive
drive.mount('/content/drive')

# 2. Projeyi klonla
!git clone https://github.com/sedahacettepetez-pixel/sibermakale.git
%cd sibermakale

# 3. Bağımlılıkları yükle
!pip install -q -r requirements.txt

# 4. Veri setini yükle (Kaggle veya manuel)

# 5. Analizi çalıştır
```

#### 4. Kaggle API (Colab'da)

```python
# kaggle.json yükle
from google.colab import files
uploaded = files.upload()  # Dosyayı seç

# Konfigure et
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# İndir
!kaggle datasets download -d mrwellsdavid/unsw-nb15
!unzip -q unsw-nb15.zip -d data/
```

#### 5. Sonuçları Kaydet

```python
# Drive'a kaydet
!cp -r artifacts/ /content/drive/MyDrive/UNSW_Results/

# veya ZIP olarak indir
!zip -r results.zip artifacts/
from google.colab import files
files.download('results.zip')
```

### ⚠️ Colab Notları:
- **Runtime süresi**: 12 saat (ücretsiz)
- **RAM**: 12GB (yetmezse restart gerekir)
- **Disk**: 100GB+ (veri seti + modeller için yeterli)
- **GPU**: T4 (ücretsiz), V100/A100 (ücretli)

---

## 📦 Yöntem 3: ZIP Olarak İndirme

### GitHub'dan ZIP İndirme:

#### Adım 1: GitHub Sayfasına Gidin
```
https://github.com/sedahacettepetez-pixel/sibermakale
```

#### Adım 2: Branch Seçin
- Branch seçiciden (genellikle "main" yazan yer)
- `claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a` branch'ini seçin

#### Adım 3: ZIP İndirin
1. Yeşil **"Code"** butonuna tıklayın
2. **"Download ZIP"** seçin
3. İndirilen ZIP'i çıkartın

#### Adım 4: Kuruluma Devam
- Yukarıdaki "Yöntem 1" kısmını takip edin
- Manuel kurulum bölümünden başlayın

---

## 🎬 Hızlı Başlangıç (TL;DR)

### En Hızlı Yol - Colab:
1. https://colab.research.google.com/ → "GitHub" sekmesi
2. `sedahacettepetez-pixel/sibermakale` repo
3. `UNSW_NB15_Colab.ipynb` aç
4. Runtime → GPU aktif et
5. Hücreleri çalıştır

### Bilgisayarda (Linux/Mac):
```bash
git clone https://github.com/sedahacettepetez-pixel/sibermakale.git
cd sibermakale
./setup.sh
kaggle datasets download -d mrwellsdavid/unsw-nb15
unzip unsw-nb15.zip -d data/
jupyter notebook unsw_nb15_analysis.ipynb
```

### Windows:
```cmd
git clone https://github.com/sedahacettepetez-pixel/sibermakale.git
cd sibermakale
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook unsw_nb15_analysis.ipynb
```

---

## 📊 Ne Beklemeli?

### İlk Çalıştırma Süreleri:
- **Kurulum**: 5-10 dakika
- **Veri indirme**: 2-5 dakika
- **Model eğitimi**:
  - CPU: 30-60 dakika
  - GPU (Colab): 10-20 dakika

### Disk Kullanımı:
- Proje dosyaları: ~50MB
- Python paketleri: ~2GB
- Veri seti: ~100MB
- Sonuçlar: ~50MB
- **Toplam**: ~2.5GB

### RAM Kullanımı:
- Minimum: 8GB
- Önerilen: 16GB
- Colab: 12GB (yeterli)

---

## ❗ Sorun Giderme

### Python bulunamadı:
```bash
# Python yükle
# Windows: https://www.python.org/downloads/
# Mac: brew install python3
# Linux: sudo apt install python3
```

### pip hatası:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Jupyter açılmıyor:
```bash
pip install jupyter jupyterlab
jupyter notebook
# veya
jupyter lab
```

### CUDA/GPU hatası:
```bash
# CPU versiyonu yükle
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### Colab'da "Runtime disconnected":
- Runtime → Restart runtime
- Veya daha az veri kullanın (sampling)

---

## 🔗 Faydalı Linkler

- **Proje GitHub**: https://github.com/sedahacettepetez-pixel/sibermakale
- **UNSW-NB15 Kaggle**: https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15
- **Google Colab**: https://colab.research.google.com/
- **Jupyter Docs**: https://jupyter.org/documentation
- **Kaggle API**: https://github.com/Kaggle/kaggle-api

---

## 💡 İpuçları

### Performans:
- **Colab GPU** kullanın (en hızlı, ücretsiz)
- Veri örnekleme yapın (testing için)
- Model parametrelerini azaltın

### Veri:
- İlk çalıştırmada tüm veriyi kullanın
- Test için %10 sample: `df.sample(frac=0.1)`

### Sonuçları Saklama:
- Colab → Google Drive
- Lokal → Git ignore (artifacts/)
- Önemli tabloları commit edin

---

## 🎓 Öğrenme Yolu

1. **İlk Çalıştırma**: Colab'da hızlı test
2. **Detaylı Analiz**: Lokal'de tam pipeline
3. **Parametre Tuning**: HPO ile optimize et
4. **Makale**: Sonuçları `artifacts/` klasöründen al

---

**Başarılar! 🚀**

Herhangi bir sorun için:
- GitHub Issues açın
- KURULUM.md dosyasına bakın
- README.md'yi okuyun
