# 📥 UNSW-NB15 IDS Project - İndirme Linkleri

Son Güncelleme: 2025-11-15

---

## 🚀 HIZLI BAŞLANGIÇ

### Seçenek 1: Google Colab (En Kolay)

```bash
# 1. GitHub'dan direkt Colab'da aç:
https://colab.research.google.com/github/sedahacettepetez-pixel/sibermakale/blob/claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a/unsw_nb15_analysis.ipynb
```

**Adımlar:**
1. Yukarıdaki linke tıkla
2. Google hesabınla giriş yap
3. Runtime → Change runtime type → GPU seç (opsiyonel)
4. Cell 2'yi çalıştır (dataset upload)
5. Cell → Run All

---

### Seçenek 2: Desktop (Windows/Mac/Linux)

#### A) Git Clone ile

```bash
# Terminal/CMD'de:
git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a https://github.com/sedahacettepetez-pixel/sibermakale.git

cd sibermakale

# Paketleri kur
pip install -r requirements.txt

# Jupyter başlat
jupyter notebook unsw_nb15_analysis.ipynb
```

#### B) ZIP İndirme

1. **Direkt ZIP linki:**
   ```
   https://github.com/sedahacettepetez-pixel/sibermakale/archive/refs/heads/claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a.zip
   ```

2. **Manuel GitHub'dan:**
   - https://github.com/sedahacettepetez-pixel/sibermakale
   - Branch seç: `claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a`
   - Code → Download ZIP

3. **ZIP açtıktan sonra:**
   ```bash
   cd sibermakale-claude-unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a
   pip install -r requirements.txt
   jupyter notebook unsw_nb15_analysis.ipynb
   ```

---

## 📁 DATASET İNDİRME

### UNSW-NB15 Dataset (Zorunlu)

**Seçenek 1: Kaggle (Önerilen - Kolay)**
```
https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15
```
- Kaggle hesabı gerekli (ücretsiz)
- Download butonu → ZIP indir
- ZIP'i aç → CSV dosyalarını `data/` klasörüne koy

**Seçenek 2: UNSW Resmi**
```
https://research.unsw.edu.au/projects/unsw-nb15-dataset
```
- CSV format seç
- 4 dosya indir: UNSW_NB15_training-set.csv, testing-set.csv, vb.
- `data/` klasörüne kopyala

**Seçenek 3: Google Drive (Hazır - Hızlı)**
```
https://drive.google.com/drive/folders/1UNSW-NB15-DATASET-LINK-HERE
```
(Not: Link eklenecek - manuel yükleme gerekirse)

### Opsiyonel Cross-Dataset'ler

**CIC-IDS2017:**
```
https://www.unb.ca/cic/datasets/ids-2017.html
```
→ `data/cic-ids2017/` klasörüne

**CIC-IDS2018:**
```
https://www.unb.ca/cic/datasets/ids-2018.html
```
→ `data/cic-ids2018/` klasörüne

**NSL-KDD:**
```
https://www.unb.ca/cic/datasets/nsl.html
```
→ `data/nsl-kdd/` klasörüne

---

## 🔧 KURULUM DETAYLARI

### Windows

```cmd
# Python 3.9+ kurulu olmalı
python --version

# Sanal ortam oluştur (opsiyonel)
python -m venv venv
venv\Scripts\activate

# Paketleri kur
pip install -r requirements.txt

# Jupyter başlat
jupyter notebook
```

### macOS/Linux

```bash
# Python 3.9+ kurulu olmalı
python3 --version

# Sanal ortam oluştur (önerilen)
python3 -m venv venv
source venv/bin/activate

# Paketleri kur
pip install -r requirements.txt

# Jupyter başlat
jupyter notebook
```

### Google Colab

```python
# Colab'da paket kurulumu (ilk hücre)
!pip install -r requirements.txt

# Dataset upload (Cell 2 otomatik)
# Manuel: Files → Upload → CSV dosyalarını seç
```

---

## 📊 PROJE YAPISI

```
sibermakale/
├── unsw_nb15_analysis.ipynb    ← Ana notebook (94 cells)
├── config.json                 ← Ayarlar (seed, hyperparameters)
├── requirements.txt            ← Python paketleri (25+)
├── utils.py                    ← Yardımcı fonksiyonlar
├── COLAB_KOMUTLARI.md         ← Türkçe Colab kılavuzu
├── CALISTIRMA_KILAVUZU.md     ← Türkçe kurulum kılavuzu
├── README.md                   ← Proje dokümantasyonu
├── DOWNLOAD_LINKS.md          ← Bu dosya
├── data/                       ← Dataset klasörü (manuel)
│   ├── UNSW_NB15_*.csv
│   ├── cic-ids2017/
│   ├── cic-ids2018/
│   └── nsl-kdd/
└── outputs/                    ← Sonuçlar (otomatik)
    ├── tables/                 ← 75+ XLSX dosyası
    ├── figs/                   ← 60+ PNG figür
    ├── models/                 ← Kaydedilen modeller
    └── final_report.docx       ← Kapsamlı rapor
```

---

## 🎯 HIZLI TEST

### 5 Dakikada Test Et

```bash
# 1. Notebook'u aç
jupyter notebook unsw_nb15_analysis.ipynb

# 2. Sadece ilk 10 hücreyi çalıştır:
# - Cell 1-10: Environment setup ve config

# 3. Dummy data ile test:
# config.json'da sample_size değerini küçült:
"sample_size": 1000  # Sadece 1000 satır test için

# 4. Run selected cells
# Cell → Run All Above
```

---

## 📞 DESTEK

### Sorun mu var?

1. **Paket hatası:**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Dataset bulunamadı:**
   - `data/` klasörünü kontrol et
   - CSV dosyaları doğru yerde mi?

3. **Memory hatası:**
   - RAM: Minimum 16GB
   - Sample size küçült: `config.json` → `sample_size: 10000`

4. **GPU hatası (TabNet):**
   - config.json → `task_type: "CPU"`
   - veya TabNet hücrelerini skip et

---

## 📈 BEKLENEN ÇIKTILAR

### Çalıştırma süresi:
- Full dataset: **4-8 saat**
- 10% sample: **30-45 dakika**
- Quick test (1000 rows): **5 dakika**

### Sonuçlar:
```
outputs/
├── tables/                 75+ XLSX files
├── figs/                   60+ PNG files @ 300 DPI
├── final_report.docx       Comprehensive report
├── project_flowchart.png   Pipeline diagram
└── detailed_workflow.png   Workflow diagram
```

---

## 🔗 ÖNEMLİ LİNKLER

| Link | Açıklama |
|------|----------|
| **GitHub Repo** | https://github.com/sedahacettepetez-pixel/sibermakale |
| **Branch** | `claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a` |
| **Colab Direkt** | https://colab.research.google.com/github/sedahacettepetez-pixel/sibermakale/blob/claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a/unsw_nb15_analysis.ipynb |
| **ZIP Download** | https://github.com/sedahacettepetez-pixel/sibermakale/archive/refs/heads/claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a.zip |
| **UNSW-NB15 Dataset** | https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15 |
| **Kaggle (Kolay)** | https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15 |

---

## ✅ HAZIR CHECKLIST

Başlamadan önce:

- [ ] Python 3.9+ yüklü
- [ ] pip çalışıyor
- [ ] Git kurulu (clone için)
- [ ] 16GB+ RAM var
- [ ] 50GB+ disk alanı var
- [ ] İnternet bağlantısı var (paket indirme için)

Notebook için:

- [ ] Proje indirildi (git clone veya ZIP)
- [ ] `requirements.txt` kuruldu
- [ ] Dataset `data/` klasörüne eklendi
- [ ] Jupyter notebook çalışıyor

---

## 🎉 BAŞARILAR!

Her şey hazır! Notebook'u çalıştır ve Q1 makale sonuçlarını al!

**Not:** Herhangi bir sorun için:
- GitHub Issues: https://github.com/sedahacettepetez-pixel/sibermakale/issues
- README.md'yi oku
- CALISTIRMA_KILAVUZU.md'ye bak

---

**Last Updated:** 2025-11-15
**Version:** 1.0 (Final - Production Ready)
**Git Commit:** 3e0cbc3
