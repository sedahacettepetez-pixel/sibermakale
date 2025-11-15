# UNSW-NB15 Network Intrusion Detection - Comprehensive ML Pipeline

**Siber Güvenlik ve Ağ Trafiği Saldırı Sınıflandırması**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Proje Hakkında

Bu proje, UNSW-NB15 veri seti kullanılarak ağ trafiğindeki saldırıları tespit etmek ve sınıflandırmak için kapsamlı bir makine öğrenimi pipeline'ı sunar. Proje, akademik araştırma ve makale yazımı için optimize edilmiş, detaylı tablolar ve görselleştirmeler içerir.

### 🎯 Hedefler

- **İkili Sınıflandırma**: Normal vs. Saldırı (`label`)
- **Çoklu Sınıflandırma**: Saldırı kategorileri (`attack_cat`)
  - Normal
  - DoS (Denial of Service)
  - Exploits
  - Fuzzers
  - Generic
  - Reconnaissance
  - Shellcode
  - Worms
  - Backdoor
  - Analysis

### 🔬 Özellikler

- ✅ UNSW-NB15'e özel feature engineering
- ✅ Host-based Cross-Validation (sızıntısız)
- ✅ SMOTE-NC ile dengesiz veri işleme
- ✅ Çoklu model: LightGBM, XGBoost, CatBoost, TabTransformer
- ✅ Ensemble öğrenme ve kalibrasyon
- ✅ Kapsamlı metrikler ve görselleştirmeler
- ✅ Reprodüksiyon manifestosu
- ✅ Makale-hazır tablolar ve şekiller

---

## 📁 Proje Yapısı

```
sibermakale/
├── data/                           # Veri dosyaları
│   ├── UNSW_NB15_training-set.csv
│   └── UNSW_NB15_testing-set.csv
├── artifacts/                      # Çıktılar
│   ├── tables/                     # CSV tablolar (makale için)
│   ├── figs/                       # Görselleştirmeler (PNG)
│   ├── logs/                       # Eğitim logları
│   ├── models/                     # Kaydedilmiş modeller
│   ├── processed/                  # İşlenmiş veri (Parquet)
│   └── report/                     # Rapor ve LaTeX tabloları
├── config.json                     # Ana konfigürasyon
├── requirements.txt                # Python bağımlılıkları
├── utils.py                        # Yardımcı fonksiyonlar
├── unsw_nb15_analysis.ipynb       # Ana Jupyter notebook
└── README.md                       # Bu dosya
```

---

## 🚀 Hızlı Başlangıç

### 1. Ortam Kurulumu

```bash
# Sanal ortam oluştur (önerilen)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows

# Bağımlılıkları yükle
pip install -r requirements.txt
```

### 2. Veri Hazırlama

#### Seçenek A: Kaggle'dan İndirme

```bash
# Kaggle API kurulumu (kaggle.json gerekli)
kaggle datasets download -d mrwellsdavid/unsw-nb15
unzip unsw-nb15.zip -d data/
```

#### Seçenek B: Yerel Dosyalar

UNSW-NB15 veri setini indirip `data/` klasörüne yerleştirin:
- `UNSW_NB15_training-set.csv`
- `UNSW_NB15_testing-set.csv`

### 3. Jupyter Notebook'u Çalıştırma

```bash
jupyter notebook unsw_nb15_analysis.ipynb
```

veya JupyterLab:

```bash
jupyter lab
```

### 4. Pipeline'ı Çalıştırma

Notebook'u hücre hücre çalıştırın veya "Run All" ile tüm pipeline'ı çalıştırın.

---

## 📊 Pipeline Adımları

### 1. Kurulum ve Ortam
- Paket yükleme ve import işlemleri
- Konfigürasyon yükleme
- Dizin yapısı oluşturma

### 2. Veri Alma ve Keşif
- UNSW-NB15 train/test setlerini yükleme
- Data inventory oluşturma (MD5, boyut, vb.)
- EDA: Sayısal/kategorik özet tablolar
- Hedef dağılımı analizi

### 3. Veri Temizleme
- Tip dönüşümü (kategorik → string, sayısal → float)
- Eksik değer doldurma (median/mode)
- `service == "-"` → `_missing_` dönüşümü
- Sonsuz değer temizleme

### 4. Feature Engineering (UNSW-NB15 Özel)
- **Bytes oranları**: `bytes_total`, `bytes_ratio_sd`, `bytes_per_sec`
- **Paket oranları**: `pkts_total`, `pkts_per_sec`
- **Port gruplama**: `sport_bucket`, `dsport_bucket` (well_known/registered/dynamic)
- **İnteraksiyon**: `proto_service`
- **Zaman özellikleri**: `hour`, `hour_sin`, `hour_cos` (opsiyonel)

### 5. Cross-Validation Stratejisi
- **Host-based CV**: `(srcip, dstip)` çiftlerine göre GroupKFold
- **Time-based CV**: `stime` ile sıralama ve blok bölme (alternatif)
- **Leakage kontrolü**: Train-valid arasında host çiftleri kontrolü

### 6. Preprocessing Pipeline
- **Kategorik**: OneHotEncoder (handle_unknown='ignore')
- **Sayısal**: RobustScaler
- **SMOTE-NC**: İsteğe bağlı (train fold'da)

### 7. Baseline Model (Logistic Regression)
- Fold 0 ile smoke test
- Confusion matrix ve PR curve
- Sanity check

### 8. Model Eğitimi (5-Fold CV)

#### 8.1 LightGBM
- Gradient boosting
- Feature importance (gain/split)
- Otomatik early stopping

#### 8.2 XGBoost
- Gradient boosting
- Tree method: hist
- Feature importance

#### 8.3 CatBoost (Opsiyonel)
- Kategorik özellikler için optimize
- Hızlı eğitim

#### 8.4 TabTransformer (Opsiyonel)
- PyTorch tabanlı deep learning
- Transformer architecture
- Focal loss

### 9. Ensemble ve Kalibrasyon
- Soft voting / Stacking
- Isotonic/Platt calibration
- Optimal eşik belirleme

### 10. Değerlendirme ve Görselleştirme
- Metrikler: Macro F1, PR-AUC, Accuracy
- Confusion matrix
- PR/ROC curves (OVR)
- Calibration plots
- Feature importance

### 11. Reprodüksiyon
- Paket versiyonları
- Random seed
- Konfigürasyon snapshot

---

## 📈 Çıktılar

### Tablolar (`artifacts/tables/`)

| Dosya | İçerik |
|-------|--------|
| `config_snapshot.json` | Tüm ayarlar |
| `data_inventory.csv` | Veri seti bilgisi (boyut, MD5, vb.) |
| `eda_overview.csv` | Tüm sütunlar için özet |
| `summary_numeric.csv` | Sayısal değişken istatistikleri |
| `summary_categorical.csv` | Kategorik değişken istatistikleri |
| `target_distribution_binary.csv` | İkili hedef dağılımı |
| `target_distribution_multi.csv` | Çoklu hedef dağılımı |
| `imputation_report.csv` | Eksik değer doldurma raporu |
| `feature_catalog.csv` | Tüm özellikler katalogu |
| `fold_sizes.csv` | CV fold boyutları |
| `leakage_checks.csv` | Veri sızıntısı kontrolleri |
| `pipeline_summary.csv` | Preprocessing adımları |
| `baseline_logreg_fold0_report.csv` | Baseline model raporu |
| `lgbm_cv_scores.csv` | LightGBM CV skorları |
| `lgbm_preds.csv` | LightGBM tahminler |
| `lgbm_probas.csv` | LightGBM olasılıklar |
| `lgbm_feature_importance.csv` | LightGBM özellik önemleri |
| `xgb_cv_scores.csv` | XGBoost CV skorları |
| `xgb_preds.csv` | XGBoost tahminler |
| `xgb_probas.csv` | XGBoost olasılıklar |
| `xgb_feature_importance.csv` | XGBoost özellik önemleri |
| `main_results.csv` | Model karşılaştırma özeti |
| `metric_definitions.csv` | Metrik tanımları |
| `reproducibility_manifest.csv` | Reprodüksiyon bilgisi |

### Görselleştirmeler (`artifacts/figs/`)

| Dosya | İçerik |
|-------|--------|
| `target_binary_dist.png` | İkili hedef dağılımı |
| `target_multi_dist.png` | Çoklu hedef dağılımı |
| `smoke_cm_fold0.png` | Baseline confusion matrix |
| `smoke_pr_fold0.png` | Baseline PR curve |
| `pr_curve_lgbm_ovr.png` | LightGBM PR curves |
| `roc_curve_lgbm_ovr.png` | LightGBM ROC curves |
| `cm_lgbm_fold0.png` | LightGBM confusion matrix |
| `feature_importance_lgbm.png` | LightGBM top features |

---

## ⚙️ Konfigürasyon

`config.json` dosyasında tüm ayarları düzenleyebilirsiniz:

```json
{
  "project": {
    "seed": 42  // Rastgelelik seed'i
  },
  "data": {
    "train_path": "data/UNSW_NB15_training-set.csv",
    "test_path": "data/UNSW_NB15_testing-set.csv"
  },
  "cv": {
    "n_splits": 5,
    "strategy": "host"  // veya "time" veya "stratified"
  },
  "imbalance": {
    "use_smote_nc": true,
    "class_weight": "balanced"
  },
  "models": {
    "lightgbm": { ... },
    "xgboost": { ... }
  }
}
```

---

## 📊 Metrikler

### Ana Metrikler

- **Macro F1**: Sınıflar arası dengeli F1 skoru
- **PR-AUC (OVR)**: Precision-Recall eğrisi altındaki alan (One-vs-Rest)
- **Accuracy**: Genel doğruluk
- **Precision/Recall**: Sınıf bazlı kesinlik ve duyarlılık

### Ablation Metrikleri

- SMOTE var/yok etkisi
- Focal loss etkisi
- Kalibrasyon etkisi
- Model hiperparametreleri

---

## 🔬 Genişletmeler (Opsiyonel)

### TabTransformer Eğitimi

```python
# TabTransformer için ayrı notebook veya section
# - PyTorch implementation
# - Focal loss for imbalanced data
# - AdamW optimizer
# - Early stopping
```

### Hyperparameter Optimization (Optuna)

```python
# Optuna ile HPO
# - TPE sampler
# - Median pruner
# - 50-100 trials
```

### Ensemble Learning

```python
# Soft voting
# Stacking with meta-learner
# Weighted combination
```

### SHAP Explainability

```python
# SHAP summary plots
# Beeswarm plots
# Dependency plots
```

### Cross-Dataset Validation

```python
# Train: UNSW-NB15
# Test: CIC-IDS2017
# Transfer learning evaluation
```

---

## 🧪 Testler ve Doğrulama

### Veri Sızıntısı Kontrolleri

```python
# Host-based CV için
# - Train-valid arasında host çakışması yok
# - Time-based CV için monoton zaman sırası
```

### Smoke Test

```python
# Logistic Regression ile hızlı test
# - Fold 0 ile sanity check
# - Pipeline doğrulama
```

---

## 📝 Makale Kullanımı

### Tablo Referansları

```latex
% LaTeX'te kullanım örneği
\begin{table}[h]
\centering
\caption{Model Comparison Results}
\label{tab:main_results}
\input{artifacts/report/tables_latex/main_results.tex}
\end{table}
```

### Şekil Referansları

```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.8\textwidth]{artifacts/figs/pr_curve_lgbm_ovr.png}
\caption{Precision-Recall Curves for LightGBM (OVR)}
\label{fig:pr_curves}
\end{figure}
```

---

## 🐛 Sorun Giderme

### Veri Bulunamadı Hatası

```bash
# data/ klasörünü kontrol edin
ls data/

# CSV dosyalarını indirin veya kopyalayın
```

### Paket Eksik Hatası

```bash
# Tüm bağımlılıkları yeniden yükleyin
pip install -r requirements.txt --upgrade
```

### Memory (Bellek) Hatası

```python
# Batch size'ı küçültün (TabTransformer)
config['models']['tabtransformer']['batch_size'] = 128

# Veya veri alt-örnekleme
df_sample = df.sample(frac=0.5, random_state=42)
```

### CUDA Hatası (PyTorch)

```python
# CPU kullanımına geç
device = 'cpu'

# veya config.json'da
"task_type": "CPU"
```

---

## 📚 Referanslar

### UNSW-NB15 Dataset

- **Paper**: Moustafa, N., & Slay, J. (2015). UNSW-NB15: a comprehensive data set for network intrusion detection systems (UNSW-NB15 network data set). *2015 military communications and information systems conference (MilCIS)*, 1-6.
- **Website**: https://research.unsw.edu.au/projects/unsw-nb15-dataset
- **Kaggle**: https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15

### Algoritmalar

- **LightGBM**: Ke, G., et al. (2017). LightGBM: A highly efficient gradient boosting decision tree. *NIPS*.
- **XGBoost**: Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. *KDD*.
- **SMOTE**: Chawla, N. V., et al. (2002). SMOTE: synthetic minority over-sampling technique. *JAIR*.
- **TabTransformer**: Huang, X., et al. (2020). TabTransformer: Tabular data modeling using contextual embeddings. *arXiv*.

---

## 👥 Katkıda Bulunma

Katkılar memnuniyetle karşılanır! Lütfen:

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Commit atın (`git commit -am 'Yeni özellik ekle'`)
4. Push yapın (`git push origin feature/yeni-ozellik`)
5. Pull Request açın

---

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

---

## 📧 İletişim

Sorularınız için:

- **Issues**: GitHub Issues kullanın
- **Email**: [your-email@example.com]
- **Twitter**: [@your_handle]

---

## 🙏 Teşekkürler

- UNSW Sydney - Veri seti için
- Scikit-learn, LightGBM, XGBoost topluluklarına
- Açık kaynak ML topluluğuna

---

**Son Güncelleme**: 2025-11-15
**Versiyon**: 1.0.0
**Python**: 3.9+

---

**Happy Modeling! 🚀**
