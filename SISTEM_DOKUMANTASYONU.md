# 🚀 UNSW-NB15 Ağ Tabanlı Saldırı Tespit Sistemi (IDS)
## Tam Kapsamlı End-to-End Machine Learning Pipeline

---

## 📋 Sistem Mimarisi

```
┌─────────────────────────────────────────────────────────────────┐
│                    UNSW-NB15 IDS PIPELINE                         │
└─────────────────────────────────────────────────────────────────┘

1. VERİ YÜKLEME & TEMİZLEME
   ├─ UNSW_NB15_training-set.csv (175,341 satır)
   ├─ UNSW_NB15_testing-set.csv (82,332 satır)
   ├─ Eksik değer analizi ve imputation
   └─ Data type conversion ve validation

2. ÖZELLİK MÜHENDİSLİĞİ (60+ Özellik)
   ├─ Bytes Features (7)
   │   ├─ bytes_total, bytes_ratio_sd/ds
   │   ├─ bytes_per_sec, bytes_per_pkt
   │   └─ bytes_mean_size, bytes_size_diff
   ├─ Packet Features (6)
   │   ├─ pkts_total, pkts_ratio_sd
   │   ├─ pkts_per_sec, pkts_density
   │   └─ spkts_rate, dpkts_rate
   ├─ Network Load & Jitter (6)
   │   ├─ load_total, load_ratio
   │   ├─ jitter_total, jitter_ratio
   │   └─ loss_total, loss_ratio
   ├─ State-TTL İlişkileri (3)
   │   ├─ state_ttl_intensity
   │   ├─ state_ttl_deviation
   │   └─ ct_ratio_srv_dst
   ├─ Port Analizi (5)
   │   ├─ sport/dsport_bucket (well-known/registered/dynamic)
   │   ├─ sport/dsport_service_type (web/email/dns/ftp/etc)
   │   └─ same_port_bucket
   ├─ İnteraksiyon Features (2)
   │   ├─ proto_service (Protocol × Service)
   │   └─ proto_state (Protocol × State)
   └─ Temporal Features (5)
       ├─ hour, hour_sin, hour_cos
       ├─ is_business_hour
       └─ is_night

3. CROSS-VALIDATION STRATEJISI
   ├─ Host-Based GroupKFold (5-fold)
   ├─ Veri Sızıntısı Engelleme: srcip + dstip gruplama
   ├─ Stratified sampling per attack category
   └─ Leakage detection ve validation

4. ÖN İŞLEME PIPELINE
   ├─ Categorical Encoding: OneHotEncoder
   ├─ Numeric Scaling: RobustScaler
   ├─ İmbalanced Data Handling: SMOTENC (k=5)
   ├─ Feature Selection: Variance Threshold
   └─ Outlier Detection: IsolationForest (opsiyonel)

5. MODEL EĞİTİMİ (5-Fold CV)
   ├─ LightGBM
   │   ├─ learning_rate: 0.05
   │   ├─ n_estimators: 500 (early_stopping)
   │   ├─ max_depth: 10
   │   ├─ num_leaves: 64
   │   └─ class_weight: balanced
   ├─ XGBoost
   │   ├─ learning_rate: 0.05
   │   ├─ n_estimators: 500
   │   ├─ max_depth: 8
   │   ├─ subsample: 0.8
   │   └─ scale_pos_weight: auto
   ├─ CatBoost
   │   ├─ learning_rate: 0.05
   │   ├─ iterations: 500
   │   ├─ depth: 8
   │   ├─ auto_class_weights: Balanced
   │   └─ task_type: GPU (Colab'da)
   └─ TabTransformer (PyTorch)
       ├─ Embedding dim: 32
       ├─ Transformer layers: 6
       ├─ Attention heads: 8
       ├─ FFN dim: 128
       └─ Dropout: 0.1

6. ENSEMBLE METHODS
   ├─ Soft Voting Classifier
   │   └─ Weights: [0.3, 0.3, 0.2, 0.2] (LGBM, XGB, Cat, TabTr)
   ├─ Stacking Classifier
   │   ├─ Level-0: LightGBM, XGBoost, CatBoost, TabTransformer
   │   ├─ Level-1: Logistic Regression (calibrated)
   │   └─ cv: 3-fold stratified
   └─ Weighted Average (Optimized)
       └─ Optuna HPO for optimal weights

7. MODEL KALİBRASYONU
   ├─ Platt Scaling (sigmoid-based)
   ├─ Isotonic Regression (non-parametric)
   ├─ Calibration Curves (reliability diagrams)
   └─ Brier Score evaluation

8. THRESHOLD OPTİMİZASYONU
   ├─ F1-Maximization threshold search
   ├─ Precision-Recall trade-off analysis
   ├─ Class-specific thresholds (multi-class)
   └─ Cost-sensitive threshold selection

9. MODEL DEĞERLENDİRME
   ├─ Metrikler
   │   ├─ Macro/Weighted F1-Score
   │   ├─ Precision, Recall, Accuracy
   │   ├─ OVR PR-AUC (One-vs-Rest)
   │   ├─ ROC-AUC (multi-class)
   │   ├─ Confusion Matrix (9×9 sınıf)
   │   └─ Per-class metrics (support, F1, precision, recall)
   ├─ Görselleştirmeler (35+ grafik)
   │   ├─ Confusion Matrices
   │   ├─ PR/ROC Curves (per-class)
   │   ├─ Feature Importance (GAIN, SPLIT, SHAP)
   │   ├─ Calibration Curves
   │   ├─ Learning Curves
   │   └─ Model Comparison (Radar, Boxplot, Bar)
   └─ İstatistiksel Testler
       ├─ McNemar's test (model pairs)
       ├─ Friedman test (multiple models)
       └─ Wilcoxon signed-rank test

10. AÇIKLANABİLİRLİK (EXPLAINABILITY)
    ├─ SHAP Analysis
    │   ├─ TreeExplainer (for GBDT models)
    │   ├─ Summary plots (global importance)
    │   ├─ Dependence plots (feature interactions)
    │   ├─ Waterfall plots (instance-level)
    │   └─ Force plots (per-prediction)
    ├─ Feature Importance Comparison
    │   ├─ GAIN-based importance
    │   ├─ SPLIT-based importance
    │   ├─ Permutation importance
    │   └─ SHAP importance
    ├─ LIME (Local Interpretable Model-agnostic)
    └─ Partial Dependence Plots (PDP)

11. PERFORMANS PROFİLİNG
    ├─ Training Time (per model, per fold)
    ├─ Inference Time (ms per sample)
    ├─ Memory Consumption (peak RAM, GPU)
    ├─ Model Size (disk space)
    └─ Throughput (samples/second)

12. FEDERATED LEARNING (Experimental)
    ├─ FedAvg Algorithm
    ├─ Local model training (per client)
    ├─ Gradient aggregation
    ├─ Privacy preservation (Differential Privacy)
    └─ Communication efficiency

13. CROSS-DATASET EVALUATIONş
    ├─ Test on CIC-IDS2017
    ├─ Test on NSL-KDD
    ├─ Domain adaptation metrics
    └─ Transfer learning analysis

14. OTOMATIK RAPOR OLUŞTURMA
    ├─ Markdown Report
    │   ├─ Executive Summary
    │   ├─ Methodology
    │   ├─ Results & Tables
    │   ├─ Visualizations
    │   └─ Conclusions
    ├─ PDF Export (via pandoc)
    ├─ DOCX Export (for Word)
    ├─ LaTeX Tables (for publications)
    └─ HTML Dashboard (interactive)

15. REPRODUCIBILITY
    ├─ Fixed random seeds (42)
    ├─ Environment snapshot (requirements.txt)
    ├─ Configuration versioning (config.json)
    ├─ Model checkpoints (.pkl, .pt)
    ├─ Data versioning (MD5 hashes)
    └─ Experiment tracking (MLflow compatible)
```

---

## 📊 ÇIKTI DOSYALARI

### Tablolar (50+ CSV)
```
artifacts/tables/
├── eda/
│   ├── data_inventory.csv
│   ├── eda_overview.csv
│   ├── summary_numeric.csv
│   ├── summary_categorical.csv
│   ├── correlation_matrix.csv
│   └── feature_catalog_comprehensive.csv
├── preprocessing/
│   ├── imputation_report.csv
│   ├── processed_schema.csv
│   ├── smotenc_results.csv
│   └── class_balance_before_after.csv
├── cv/
│   ├── fold_sizes.csv
│   ├── leakage_checks.csv
│   └── fold_distribution.csv
├── models/
│   ├── lgbm_cv_scores.csv
│   ├── lgbm_preds.csv
│   ├── lgbm_probas.csv
│   ├── lgbm_feature_importance.csv
│   ├── xgb_cv_scores.csv
│   ├── xgb_preds.csv
│   ├── xgb_probas.csv
│   ├── xgb_feature_importance.csv
│   ├── catboost_cv_scores.csv
│   ├── catboost_preds.csv
│   ├── catboost_feature_importance.csv
│   ├── tabtransformer_cv_scores.csv
│   └── tabtransformer_preds.csv
├── ensemble/
│   ├── soft_voting_results.csv
│   ├── stacking_results.csv
│   └── ensemble_comparison.csv
├── calibration/
│   ├── platt_calibration_results.csv
│   ├── isotonic_calibration_results.csv
│   └── brier_scores.csv
├── metrics/
│   ├── main_results.csv
│   ├── model_comparison_detailed.csv
│   ├── per_class_metrics_all.csv
│   ├── confusion_matrices/
│   │   ├── lgbm_cm.csv
│   │   ├── xgb_cm.csv
│   │   ├── catboost_cm.csv
│   │   └── ensemble_cm.csv
│   └── statistical_tests.csv
├── shap/
│   ├── shap_values.csv
│   ├── shap_importance.csv
│   └── shap_interaction_values.csv
├── profiling/
│   ├── training_times.csv
│   ├── inference_times.csv
│   ├── memory_usage.csv
│   └── model_sizes.csv
└── reproducibility/
    ├── reproducibility_manifest.csv
    ├── config_snapshot.json
    └── data_md5_hashes.csv
```

### Grafikler (50+ PNG @ 300 DPI)
```
artifacts/figs/
├── eda/
│   ├── target_binary_dist.png
│   ├── target_multi_dist.png
│   ├── numeric_distributions.png
│   ├── correlation_heatmap.png
│   ├── class_distribution_per_fold.png
│   ├── proto_distribution.png
│   ├── service_distribution.png
│   └── port_analysis.png
├── models/
│   ├── lgbm/
│   │   ├── cm_lgbm.png
│   │   ├── pr_curve_lgbm.png
│   │   ├── roc_curve_lgbm.png
│   │   ├── feature_importance_lgbm.png
│   │   ├── learning_curve_lgbm.png
│   │   └── calibration_lgbm.png
│   ├── xgb/
│   │   ├── cm_xgb.png
│   │   ├── pr_curve_xgb.png
│   │   ├── roc_curve_xgb.png
│   │   └── feature_importance_xgb.png
│   ├── catboost/
│   │   ├── cm_catboost.png
│   │   ├── pr_curve_catboost.png
│   │   └── feature_importance_catboost.png
│   └── tabtransformer/
│       ├── training_loss.png
│       ├── validation_metrics.png
│       └── attention_weights.png
├── ensemble/
│   ├── ensemble_cm.png
│   ├── ensemble_pr_roc.png
│   └── ensemble_comparison_radar.png
├── calibration/
│   ├── calibration_curves_all_models.png
│   ├── reliability_diagrams.png
│   └── threshold_optimization.png
├── comparison/
│   ├── model_comparison_radar.png
│   ├── model_comparison_boxplot.png
│   ├── feature_importance_comparison.png
│   ├── training_time_comparison.png
│   └── f1_score_progression.png
├── shap/
│   ├── shap_summary.png
│   ├── shap_dependence_plots/ (10+ plots)
│   ├── shap_waterfall.png
│   └── shap_force_plots.png
└── profiling/
    ├── memory_timeline.png
    ├── inference_time_boxplot.png
    └── throughput_comparison.png
```

---

## 🚀 KULLANIM

### Google Colab'da:

```python
# 1. Projeyi Klonla
!git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git

%cd sibermakale

# 2. GPU Aktif Et
# Runtime → Change runtime type → GPU (T4)

# 3. Paketleri Yükle
!pip install -q -r requirements.txt

# 4. Veriyi İndir
from google.colab import files
uploaded = files.upload()  # kaggle.json yükle

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download -d mrwellsdavid/unsw-nb15
!unzip -q unsw-nb15.zip -d data/

# 5. TÜM HÜCRELERİ ÇALIŞTIR
# Run All Cells

# 6. Sonuçları İndir
!zip -r results.zip artifacts/
files.download('results.zip')
```

### Lokal'de:

```bash
git clone -b claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a \
  https://github.com/sedahacettepetez-pixel/sibermakale.git
cd sibermakale
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook unsw_nb15_analysis.ipynb
```

---

## 📈 BEKLENEN PERFORMANS

| Model | Macro F1 | PR-AUC | Accuracy | Training Time |
|-------|----------|--------|----------|---------------|
| LightGBM | ~0.85 | ~0.87 | ~0.92 | ~120s |
| XGBoost | ~0.84 | ~0.86 | ~0.91 | ~180s |
| CatBoost | ~0.85 | ~0.87 | ~0.92 | ~150s |
| TabTransformer | ~0.82 | ~0.84 | ~0.90 | ~600s |
| **Ensemble (Stacking)** | **~0.87** | **~0.89** | **~0.93** | N/A |

---

## 🔬 AKADEMİK KULLANIM

### Makale İçin Tablolar:

- **Table 1**: Dataset Statistics → `data_inventory.csv`
- **Table 2**: Feature Engineering → `feature_catalog_comprehensive.csv`
- **Table 3**: Model Comparison → `model_comparison_detailed.csv`
- **Table 4**: Per-Class Metrics → `per_class_metrics_all.csv`
- **Table 5**: Confusion Matrix → `confusion_matrices/*.csv`

### Makale İçin Figürler:

- **Figure 1**: System Architecture → (manuel çizim)
- **Figure 2**: Feature Correlation → `correlation_heatmap.png`
- **Figure 3**: Confusion Matrices → `models/*/cm_*.png`
- **Figure 4**: PR/ROC Curves → `models/*/pr_roc_*.png`
- **Figure 5**: Model Comparison → `comparison/model_comparison_radar.png`
- **Figure 6**: SHAP Summary → `shap/shap_summary.png`
- **Figure 7**: Calibration → `calibration/calibration_curves_all_models.png`

---

## 📌 ÖNEMLİ NOTLAR

1. **GPU Kullanımı**: CatBoost ve TabTransformer için GPU şiddetle tavsiye edilir
2. **Bellek**: En az 16GB RAM gerekli (tam veri seti için)
3. **Süre**: Tüm pipeline ~2-3 saat (GPU ile), ~6-8 saat (CPU ile)
4. **Disk**: ~5GB boş alan (artifacts için)
5. **Reproducibility**: Her çalıştırmada aynı sonuçlar için seed=42 sabit

---

## 🛠️ TEKNİK DETAYLAR

### Veri Sızıntısı Engelleme:
- Host-based GroupKFold ile aynı IP çiftleri farklı foldlara düşmez
- Temporal leakage yoktur (time-based features kullanılsa da)
- Test set strict isolation

### İmbalanced Data Stratejisi:
- SMOTENC (k=5) ile oversampling
- Class weights kullanımı
- Focal loss (CatBoost için)
- Stratified sampling

### Hyperparameter Optimization:
- Optuna ile Bayesian optimization
- Cross-validation içinde
- Pruning stratejisi (MedianPruner)
- Multi-objective optimization (F1 + PR-AUC)

---

**Hazırlayan:** UNSW-NB15 Research Team
**Versiyon:** 2.0 - Comprehensive Edition
**Tarih:** 2025-11-15
**Branch:** `claude/unsw-nb15-setup-config-01DEmKoC2eHKvoYkAuYHsr8a`
