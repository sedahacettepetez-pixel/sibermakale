# 🚀 Hızlı Kurulum Kılavuzu

Bu kılavuz, UNSW-NB15 projesini adım adım kurmanız için hazırlanmıştır.

---

## 📥 Projeyi İndirme

### Yöntem 1: Git Clone (Önerilen)

```bash
# Projeyi klonlayın
git clone https://github.com/sedahacettepetez-pixel/sibermakale.git

# Proje dizinine girin
cd sibermakale
```

### Yöntem 2: ZIP İndirme

1. GitHub sayfasından "Code" → "Download ZIP" seçin
2. ZIP dosyasını çıkartın
3. Terminal ile dizine girin

---

## ⚙️ Otomatik Kurulum (Linux/Mac)

En basit yöntem! Tek komutla her şey hazır:

```bash
./setup.sh
```

Bu script otomatik olarak:
- ✅ Python versiyonunu kontrol eder
- ✅ Sanal ortam (venv) oluşturur
- ✅ Tüm bağımlılıkları yükler
- ✅ Dizin yapısını oluşturur

---

## 🔧 Manuel Kurulum

Otomatik kurulum çalışmazsa manuel olarak:

### 1. Python Kontrolü

```bash
python3 --version
# Python 3.9 veya üzeri gerekli
```

### 2. Sanal Ortam Oluşturma

```bash
# Sanal ortam oluştur
python3 -m venv venv

# Aktifleştir (Linux/Mac)
source venv/bin/activate

# Aktifleştir (Windows)
venv\Scripts\activate
```

### 3. Bağımlılıkları Yükleme

```bash
# pip güncelle
pip install --upgrade pip

# Bağımlılıkları yükle
pip install -r requirements.txt
```

**Not:** Bu işlem 5-10 dakika sürebilir (PyTorch büyük bir paket).

---

## 📊 Veri Setini İndirme

### Yöntem 1: Kaggle API (Önerilen)

```bash
# Kaggle API kurulumu (ilk kez)
# 1. Kaggle hesabınızdan API token indirin (kaggle.json)
# 2. Token'ı yerleştirin
mkdir -p ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# Veri setini indirin
kaggle datasets download -d mrwellsdavid/unsw-nb15

# Çıkartın
unzip unsw-nb15.zip -d data/
```

### Yöntem 2: Manuel İndirme

1. Kaggle'dan indirin: https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15
2. ZIP'i çıkartın
3. CSV dosyalarını `data/` klasörüne taşıyın:
   - `UNSW_NB15_training-set.csv`
   - `UNSW_NB15_testing-set.csv`

### Veri Kontrolü

```bash
ls -lh data/
# İki CSV dosyası görmelisiniz
```

---

## 🎯 Jupyter Notebook'u Başlatma

### Jupyter Notebook

```bash
# Sanal ortamı aktifleştir (henüz aktif değilse)
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows

# Notebook'u başlat
jupyter notebook unsw_nb15_analysis.ipynb
```

### JupyterLab (Gelişmiş)

```bash
jupyter lab
```

---

## 🎓 Kullanım

### İlk Çalıştırma

1. Jupyter notebook'ta hücreleri sırayla çalıştırın (Shift+Enter)
2. Veya "Run All" ile tüm pipeline'ı çalıştırın
3. Sonuçlar `artifacts/` klasörüne kaydedilecek

### Dizin Yapısı Kontrol

```bash
tree -L 2 -I 'venv|__pycache__'
```

Şu yapıyı görmelisiniz:

```
sibermakale/
├── data/
│   ├── UNSW_NB15_training-set.csv
│   └── UNSW_NB15_testing-set.csv
├── artifacts/
│   ├── tables/
│   ├── figs/
│   ├── logs/
│   ├── models/
│   └── processed/
├── config.json
├── requirements.txt
├── utils.py
├── unsw_nb15_analysis.ipynb
└── README.md
```

---

## 🧪 Hızlı Test

Kurulumun doğru çalıştığını test edin:

```python
# Python interpreter'da
python3 -c "import pandas, numpy, sklearn, lightgbm, xgboost; print('✓ Tüm paketler yüklü!')"
```

---

## ❗ Sorun Giderme

### Hata: Python versiyonu eski

```bash
# Python 3.9+ yükleyin
sudo apt install python3.9  # Ubuntu/Debian
brew install python@3.9      # Mac
```

### Hata: pip install başarısız

```bash
# pip güncelleme
python3 -m pip install --upgrade pip

# Tekrar dene
pip install -r requirements.txt
```

### Hata: Jupyter bulunamadı

```bash
# Jupyter yükle
pip install jupyter jupyterlab

# Veya requirements.txt'den tekrar yükle
pip install -r requirements.txt
```

### Hata: CUDA/GPU hatası (PyTorch)

```bash
# CPU versiyonu yükle
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### Hata: Bellek yetersiz

```python
# config.json'da batch size küçült
"tabtransformer": {
  "batch_size": 128  # 256'dan küçült
}
```

---

## 📝 Notlar

- **İlk kurulum:** 2-3 GB disk alanı gerektirir
- **PyTorch:** CUDA olmadan CPU modunda çalışır (yavaş ama çalışır)
- **Veri seti:** ~100MB (CSV dosyaları)
- **İşlenmiş veri:** ~50MB (Parquet)
- **Model eğitimi:** İlk çalışma 10-30 dakika sürebilir (CPU'da)

---

## 🔗 Yararlı Linkler

- **Proje GitHub:** https://github.com/sedahacettepetez-pixel/sibermakale
- **UNSW-NB15 Dataset:** https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15
- **Jupyter Docs:** https://jupyter.org/documentation
- **Pandas Docs:** https://pandas.pydata.org/docs/
- **Scikit-learn:** https://scikit-learn.org/

---

## 💡 İpuçları

1. **Sanal ortamı her zaman aktif tutun:**
   ```bash
   source venv/bin/activate
   ```

2. **Notebook'u kapatırken:**
   - Çalışan kernel'i kapatın (Kernel → Shut Down)
   - Jupyter server'ı durdurun (Terminal'de Ctrl+C)

3. **Git commit öncesi:**
   ```bash
   # Büyük dosyaları ignore et
   git status
   # .gitignore kontrol et
   ```

4. **Dependency güncelleme:**
   ```bash
   pip list --outdated
   pip install --upgrade <package_name>
   ```

---

## 🆘 Yardım

Sorun yaşarsanız:

1. **README.md** dosyasını okuyun
2. **GitHub Issues** açın
3. **Error mesajını** tam olarak kopyalayın

---

**Başarılar! 🎉**

Bu proje ile UNSW-NB15 veri seti üzerinde gelişmiş makine öğrenimi analizi yapabilirsiniz.
