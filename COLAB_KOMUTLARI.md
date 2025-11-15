# 🚀 Google Colab Komutları - UNSW-NB15 Projesi

## ⚡ TEK KOMUT İLE TAM KURULUM

Google Colab'da yeni bir hücreye yapıştırın ve çalıştırın:

```python
# 1. Projeyi klonla ve doğru branch'e geç
!git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a https://github.com/sedahacettepetez-pixel/sibermakale.git
%cd sibermakale

# 2. Dosyaları kontrol et
!ls -la

# 3. Paketleri yükle (5-10 dakika sürer)
!pip install -q -r requirements.txt

print("✅ Kurulum tamamlandı!")
```

---

## 📋 ADIM ADIM KOMUTLAR

### Adım 1: Projeyi Klonla (Doğru Branch ile)
```python
# Git clone ile doğru branch'i direkt indir
!git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git

# Proje klasörüne gir
%cd sibermakale

# Branch kontrolü
!git branch --show-current

# Dosyaları listele
!ls -lh
```

### Adım 2: GPU Kontrolü (Opsiyonel)
```python
# GPU var mı kontrol et
!nvidia-smi

# Runtime > Change runtime type > GPU (T4) seçin
```

### Adım 3: Bağımlılıkları Yükle
```python
# Pip güncelle
!pip install --upgrade pip

# Tüm paketleri yükle
!pip install -q -r requirements.txt

print("✅ Paketler yüklendi!")
```

### Adım 4: Kaggle API Kurulumu (Veri için)
```python
# Kaggle token dosyasını yükle
from google.colab import files
print("Lütfen kaggle.json dosyanızı yükleyin:")
uploaded = files.upload()

# Kaggle dizini oluştur
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

print("✅ Kaggle API hazır!")
```

### Adım 5: UNSW-NB15 Veri Setini İndir
```python
# Veri setini Kaggle'dan indir
!kaggle datasets download -d mrwellsdavid/unsw-nb15

# ZIP'i aç
!unzip -q unsw-nb15.zip -d data/

# Dosyaları kontrol et
!ls -lh data/

print("✅ Veri seti hazır!")
```

### Adım 6: Analizi Başlat
```python
# Config yükle
import json
with open('config.json', 'r') as f:
    config = json.load(f)

print(f"✅ Proje: {config['project']['name']}")
print("Şimdi hücreleri çalıştırabilirsiniz!")
```

---

## 🎯 HAZIR NOTEBOOK KULLANIMI

**En Kolay Yol:**

1. Google Colab'ı açın: https://colab.research.google.com
2. Yeni notebook oluşturun
3. Aşağıdaki komutu çalıştırın:

```python
# Tek komutla tüm proje hazır!
!git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git && \
  cd sibermakale && \
  pip install -q -r requirements.txt

print("✅ Proje hazır! Şimdi veri setini indirin.")
```

---

## 📱 ALTERNATIF: GitHub'dan Direkt Aç

1. Google Colab'a gidin: https://colab.research.google.com
2. **GitHub sekmesine** tıklayın
3. Şu URL'i girin:
   ```
   https://github.com/sedahacettepetez-pixel/sibermakale/blob/claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a/UNSW_NB15_Colab.ipynb
   ```
4. **Open in Colab** butonuna tıklayın
5. Hücreleri sırayla çalıştırın

---

## 🔧 İPUCU: Branch Kontrolü

Doğru branch'te olduğunuzu kontrol edin:

```python
!git branch --show-current
# Çıktı: claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a
```

Eğer farklı branch'teyseniz:

```python
!git checkout claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a
```

---

## ✅ KONTROL LİSTESİ

- [ ] Projeyi doğru branch ile klonladım
- [ ] GPU aktif (Runtime > Change runtime type > GPU)
- [ ] Paketleri yükledim (`requirements.txt`)
- [ ] Kaggle API token yükledim
- [ ] UNSW-NB15 veri setini indirdim
- [ ] Config.json dosyası mevcut
- [ ] Analizi başlattım

---

**Hazırlayan:** UNSW-NB15 Research Team
**Branch:** `claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a`
**Tarih:** 2025-11-15
