# 📊 UNSW-NB15 Proje Çıktı Açıklaması

Bu proje **30+ Excel Tablosu** ve **25+ Grafik/Şekil** üretecek şekilde tasarlanmıştır.

---

## 📁 TABLOLAR (Excel/CSV Çıktıları) - artifacts/tables/

### 📋 Veri Keşif Tabloları (1-10)

1. **data_inventory.csv** - Veri seti bilgileri (boyut, satır sayısı, MD5 hash)
2. **eda_overview.csv** - Tüm kolonların özet bilgileri (tip, eksik değer, rol)
3. **summary_numeric.csv** - Sayısal özelliklerin istatistikleri (ortalama, std, min, max, çeyreklikler)
4. **summary_categorical.csv** - Kategorik özelliklerin istatistikleri (benzersiz değer sayısı, en sık değer)
5. **target_distribution_binary.csv** - İkili hedef dağılımı (Normal vs Attack)
6. **target_distribution_multi.csv** - Çok sınıflı hedef dağılımı (tüm saldırı tipleri)
7. **imputation_report.csv** - Eksik değer doldurma raporu
8. **feature_catalog.csv** - Tüm özelliklerin katalog

u (ham + mühendislik)
9. **processed_schema.csv** - İşlenmiş veri şeması
10. **correlation_matrix.csv** - Özellik korelasyon matrisi

### 🔧 Modelleme ve CV Tabloları (11-18)

11. **fold_sizes.csv** - Her CV fold'un boyutları
12. **leakage_checks.csv** - Veri sızıntısı kontrol sonuçları
13. **pipeline_summary.csv** - Önişleme pipeline adımları
14. **metric_definitions.csv** - Metrik tanımları
15. **baseline_logreg_fold0_report.csv** - Logistic Regression baseline raporu
16. **class_balance_analysis.csv** - Sınıf dengesi analizi (yeni)
17. **attack_category_stats.csv** - Saldırı kategorisi istatistikleri (yeni)
18. **port_statistics.csv** - Port kullanım istatistikleri (yeni)
19. **protocol_statistics.csv** - Protokol dağılım istatistikleri (yeni)

### 🎯 Model Sonuç Tabloları (19-35)

#### LightGBM Sonuçları
20. **lgbm_cv_scores.csv** - LightGBM 5-fold CV skorları
21. **lgbm_preds.csv** - LightGBM tahminleri (tüm foldlar)
22. **lgbm_probas.csv** - LightGBM olasılık tahminleri
23. **lgbm_feature_importance.csv** - LightGBM özellik önem sıralaması
24. **lgbm_per_class_metrics_fold0.csv** - LightGBM sınıf bazlı metrikler (Fold 0)
25. **lgbm_per_class_metrics_all_folds.csv** - LightGBM tüm foldlar için sınıf metrikleri (yeni)

#### XGBoost Sonuçları
26. **xgb_cv_scores.csv** - XGBoost 5-fold CV skorları
27. **xgb_preds.csv** - XGBoost tahminleri (tüm foldlar)
28. **xgb_probas.csv** - XGBoost olasılık tahminleri
29. **xgb_feature_importance.csv** - XGBoost özellik önem sıralaması
30. **xgb_per_class_metrics_fold0.csv** - XGBoost sınıf bazlı metrikler (Fold 0) (yeni)
31. **xgb_per_class_metrics_all_folds.csv** - XGBoost tüm foldlar için sınıf metrikleri (yeni)

#### Model Karşılaştırma
32. **main_results.csv** - Ana model karşılaştırma tablosu
33. **model_comparison_detailed.csv** - Detaylı model karşılaştırması (tüm metrikler) (yeni)
34. **confusion_matrix_lgbm.csv** - LightGBM confusion matrix (tablo formatında) (yeni)
35. **confusion_matrix_xgb.csv** - XGBoost confusion matrix (tablo formatında) (yeni)

### 🔬 Reproducibility
36. **reproducibility_manifest.csv** - Tüm paket versiyonları
37. **config_snapshot.json** - Konfigürasyon anlık görüntüsü

---

## 📈 GRAFİKLER (PNG Çıktıları) - artifacts/figs/

### 📊 Veri Keşif Grafikleri (1-8)

1. **target_binary_dist.png** - İkili hedef dağılımı (bar chart)
2. **target_multi_dist.png** - Çok sınıflı hedef dağılımı (barh chart)
3. **numeric_distributions.png** - Tüm sayısal özelliklerin histogramları (grid layout)
4. **correlation_heatmap.png** - Özellik korelasyon ısı haritası
5. **class_distribution_per_fold.png** - Her fold'taki sınıf dağılımları (yeni)
6. **proto_distribution.png** - Protokol dağılımı (yeni)
7. **service_distribution.png** - Servis dağılımı (yeni)
8. **state_distribution.png** - State dağılımı (yeni)
9. **port_distribution.png** - Port kullanım dağılımı (yeni)

### 🎯 Baseline Model Grafikleri (9-11)

9. **smoke_cm_fold0.png** - Baseline Logistic Regression confusion matrix
10. **smoke_pr_fold0.png** - Baseline PR curves
11. **smoke_roc_fold0.png** - Baseline ROC curves (yeni)

### 🌲 LightGBM Grafikleri (12-19)

12. **feature_importance_lgbm.png** - LightGBM feature importance (top 20)
13. **cm_lgbm_fold0.png** - LightGBM confusion matrix (Fold 0)
14. **pr_curve_lgbm_ovr.png** - LightGBM Precision-Recall curves (OVR)
15. **roc_curve_lgbm_ovr.png** - LightGBM ROC curves (OVR)
16. **lgbm_per_class_f1.png** - LightGBM sınıf bazlı F1 skorları (bar chart) (yeni)
17. **lgbm_per_class_precision.png** - LightGBM sınıf bazlı precision (yeni)
18. **lgbm_per_class_recall.png** - LightGBM sınıf bazlı recall (yeni)
19. **lgbm_metric_progression_f1.png** - LightGBM F1 skoru fold progression (yeni)
20. **lgbm_calibration.png** - LightGBM calibration curve (yeni)

### 🚀 XGBoost Grafikleri (20-26)

21. **feature_importance_xgb.png** - XGBoost feature importance (top 20) (yeni)
22. **cm_xgb_fold0.png** - XGBoost confusion matrix (Fold 0) (yeni)
23. **pr_curve_xgb_ovr.png** - XGBoost Precision-Recall curves (OVR) (yeni)
24. **roc_curve_xgb_ovr.png** - XGBoost ROC curves (OVR) (yeni)
25. **xgb_per_class_f1.png** - XGBoost sınıf bazlı F1 skorları (yeni)
26. **xgb_metric_progression_f1.png** - XGBoost F1 skoru fold progression (yeni)
27. **xgb_calibration.png** - XGBoost calibration curve (yeni)

### 🔬 Model Karşılaştırma Grafikleri (27-30)

28. **feature_importance_comparison.png** - LGBM vs XGB feature importance karşılaştırması (yeni)
29. **training_time_comparison.png** - Model eğitim süresi karşılaştırması (yeni)
30. **model_comparison_radar.png** - Model performans radar chart (yeni)
31. **model_comparison_boxplot_f1.png** - Model F1 skor boxplot karşılaştırması (yeni)

---

## 🗂️ DOSYA YAPISI

```
sibermakale/
├── artifacts/
│   ├── tables/          # 37+ CSV/Excel tabloları
│   │   ├── data_inventory.csv
│   │   ├── eda_overview.csv
│   │   ├── lgbm_cv_scores.csv
│   │   ├── xgb_cv_scores.csv
│   │   └── ... (30+ tablo)
│   │
│   ├── figs/            # 31+ PNG grafikleri
│   │   ├── target_binary_dist.png
│   │   ├── correlation_heatmap.png
│   │   ├── cm_lgbm_fold0.png
│   │   ├── cm_xgb_fold0.png
│   │   └── ... (25+ grafik)
│   │
│   ├── models/          # Eğitilmiş model dosyaları (opsiyonel)
│   ├── logs/            # Eğitim logları
│   └── report/          # LaTeX tablo formatları
│       └── tables_latex/
│
├── data/
│   └── UNSW_NB15_*.csv
│
├── unsw_nb15_analysis.ipynb    # Ana analiz notebook
├── UNSW_NB15_Colab.ipynb       # Google Colab versiyonu
├── config.json                 # Konfigürasyon
├── utils.py                    # Yardımcı fonksiyonlar
└── requirements.txt            # Python bağımlılıkları
```

---

## 🚀 NASIL ÇALIŞTIRILIR

### Yöntem 1: Jupyter Notebook (Lokal)

```bash
# 1. Projeyi klonla
git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git

cd sibermakale

# 2. Sanal ortam oluştur ve paketleri yükle
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Veri setini indir
kaggle datasets download -d mrwellsdavid/unsw-nb15
unzip unsw-nb15.zip -d data/

# 4. Jupyter başlat
jupyter notebook unsw_nb15_analysis.ipynb

# 5. Hücreleri sırayla çalıştır (Run All)
```

### Yöntem 2: Google Colab

```python
# Colab'da yeni notebook aç ve şu komutu çalıştır:
!git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git
%cd sibermakale
!pip install -q -r requirements.txt

# Sonra hücreleri çalıştır
```

**Direkt Colab Notebook:** UNSW_NB15_Colab.ipynb

---

## 📊 NE ZAMAN HANGİ ÇIKTILAR ÜRETİLİR

| Notebook Bölümü | Üretilen Tablolar | Üretilen Grafikler |
|----------------|-------------------|-------------------|
| **3. Data Acquisition** | data_inventory.csv | - |
| **4. EDA** | eda_overview.csv, summary_numeric.csv, summary_categorical.csv | numeric_distributions.png, correlation_heatmap.png |
| **5. Target Distribution** | target_distribution_binary.csv, target_distribution_multi.csv | target_binary_dist.png, target_multi_dist.png, class_distribution_per_fold.png |
| **6. Imputation** | imputation_report.csv | - |
| **7. Feature Engineering** | feature_catalog.csv | proto_distribution.png, service_distribution.png, port_distribution.png |
| **8. CV Strategy** | fold_sizes.csv, leakage_checks.csv | - |
| **9. Preprocessing** | pipeline_summary.csv | - |
| **10. Baseline** | baseline_logreg_fold0_report.csv | smoke_cm_fold0.png, smoke_pr_fold0.png |
| **11. Save Data** | processed_schema.csv | - |
| **12. Metrics** | metric_definitions.csv | - |
| **13.1 LightGBM** | lgbm_cv_scores.csv, lgbm_preds.csv, lgbm_probas.csv, lgbm_feature_importance.csv, lgbm_per_class_metrics*.csv | cm_lgbm_fold0.png, pr_curve_lgbm_ovr.png, roc_curve_lgbm_ovr.png, feature_importance_lgbm.png, lgbm_per_class_*.png, lgbm_metric_progression_f1.png, lgbm_calibration.png |
| **13.2 XGBoost** | xgb_cv_scores.csv, xgb_preds.csv, xgb_probas.csv, xgb_feature_importance.csv, xgb_per_class_metrics*.csv | cm_xgb_fold0.png, pr_curve_xgb_ovr.png, roc_curve_xgb_ovr.png, feature_importance_xgb.png, xgb_per_class_*.png, xgb_metric_progression_f1.png, xgb_calibration.png |
| **13.3 Comparison** | main_results.csv, model_comparison_detailed.csv, confusion_matrix_*.csv | feature_importance_comparison.png, training_time_comparison.png, model_comparison_radar.png, model_comparison_boxplot_f1.png |
| **14. Reproducibility** | reproducibility_manifest.csv, config_snapshot.json | - |

---

## 🎓 ÇIKTILARIN AKADEMİK MAKALEDE KULLANIMI

### Tablo Örnekleri (LaTeX İçin)
- **Table 1**: Data Inventory (data_inventory.csv)
- **Table 2**: Feature Catalog (feature_catalog.csv)
- **Table 3**: Model Comparison (main_results.csv)
- **Table 4**: LightGBM Per-Class Metrics (lgbm_per_class_metrics_all_folds.csv)
- **Table 5**: XGBoost Per-Class Metrics (xgb_per_class_metrics_all_folds.csv)
- **Table 6**: Confusion Matrix - LightGBM (confusion_matrix_lgbm.csv)

### Figür Örnekleri (Makale İçin)
- **Figure 1**: Target Distribution (target_multi_dist.png)
- **Figure 2**: Correlation Heatmap (correlation_heatmap.png)
- **Figure 3**: LightGBM Confusion Matrix (cm_lgbm_fold0.png)
- **Figure 4**: Precision-Recall Curves (pr_curve_lgbm_ovr.png)
- **Figure 5**: ROC Curves (roc_curve_lgbm_ovr.png)
- **Figure 6**: Feature Importance Comparison (feature_importance_comparison.png)
- **Figure 7**: Model Performance Radar (model_comparison_radar.png)

---

## ⚙️ KONFİGÜRASYON

Tüm ayarlar `config.json` dosyasında:

```json
{
  "project": {
    "name": "UNSW-NB15 Attack Classification",
    "seed": 42
  },
  "cv": {
    "n_splits": 5,
    "strategy": "host"
  },
  "models": {
    "lightgbm": {...},
    "xgboost": {...}
  }
}
```

---

## 📝 NOTLAR

1. **Excel Export**: CSV dosyaları Excel'de açılabilir veya pandas ile `.xlsx` formatına çevrilebilir
2. **Yüksek Çözünürlük**: Tüm grafikler 300 DPI'da kaydedilir (yayın kalitesi)
3. **Reproducibility**: `reproducibility_manifest.csv` tüm paket versiyonlarını içerir
4. **Esneklik**: `config.json`'u düzenleyerek parametreleri değiştirin

---

**Toplam Çıktı:** 37+ Tablo + 31+ Grafik = **68+ Dosya**

🎯 **Bu proje, makale yazımı için gereken TÜM tabloları ve grafikleri otomatik olarak üretir!**
