"""
Utility functions for UNSW-NB15 Attack Classification Project
"""

import os
import json
import time
import hashlib
import warnings
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Union, Any

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    classification_report, confusion_matrix,
    precision_recall_curve, roc_curve, auc,
    average_precision_score, roc_auc_score,
    brier_score_loss
)
from sklearn.preprocessing import label_binarize

warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100


def load_config(config_path: str = "config.json") -> Dict:
    """Load configuration from JSON file."""
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config


def save_config_snapshot(config: Dict, output_path: str):
    """Save configuration snapshot to JSON file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(config, f, indent=2)
    print(f"✓ Configuration snapshot saved to {output_path}")


def ensure_directories(config: Dict):
    """Ensure all required directories exist."""
    dirs = [
        config['output']['artifacts_dir'],
        config['output']['tables_dir'],
        config['output']['figs_dir'],
        config['output']['logs_dir'],
        config['output']['models_dir'],
        config['output']['report_dir'],
        os.path.join(config['output']['report_dir'], 'tables_latex'),
        os.path.dirname(config['data']['processed_path'])
    ]
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
    print(f"✓ All directories verified")


def compute_md5(file_path: str) -> str:
    """Compute MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def create_data_inventory(file_paths: List[str], output_path: str):
    """Create data inventory table."""
    inventory = []
    for file_path in file_paths:
        if os.path.exists(file_path):
            start_time = time.time()
            df = pd.read_csv(file_path)
            load_time = time.time() - start_time

            inventory.append({
                'file_name': os.path.basename(file_path),
                'file_size_bytes': os.path.getsize(file_path),
                'n_rows': len(df),
                'n_cols': len(df.columns),
                'md5': compute_md5(file_path),
                'load_time_sec': round(load_time, 2)
            })

    inventory_df = pd.DataFrame(inventory)
    inventory_df.to_csv(output_path, index=False)
    print(f"✓ Data inventory saved to {output_path}")
    return inventory_df


def create_eda_overview(df: pd.DataFrame, config: Dict, output_path: str):
    """Create EDA overview table."""
    overview = []

    categorical_cols = config['features']['categorical']
    numeric_cols = config['features']['numeric']
    id_time_cols = config['features']['id_time']
    target_cols = [config['targets']['binary'], config['targets']['multi']]

    for col in df.columns:
        if col in target_cols:
            role = 'target'
        elif col in categorical_cols:
            role = 'categorical'
        elif col in numeric_cols:
            role = 'numeric'
        elif col in id_time_cols:
            role = 'id_time'
        else:
            role = 'other'

        n_unique = df[col].nunique()
        n_missing = df[col].isna().sum()
        missing_pct = round(n_missing / len(df) * 100, 2)
        sample_values = df[col].dropna().head(3).tolist()

        overview.append({
            'column': col,
            'dtype': str(df[col].dtype),
            'role': role,
            'n_unique': n_unique,
            'n_missing': n_missing,
            'missing_pct': missing_pct,
            'sample_values': str(sample_values)
        })

    overview_df = pd.DataFrame(overview)
    overview_df.to_csv(output_path, index=False)
    print(f"✓ EDA overview saved to {output_path}")
    return overview_df


def create_numeric_summary(df: pd.DataFrame, numeric_cols: List[str], output_path: str):
    """Create summary statistics for numeric columns."""
    summary = []

    for col in numeric_cols:
        if col in df.columns:
            col_data = df[col]
            summary.append({
                'column': col,
                'count': col_data.count(),
                'mean': col_data.mean(),
                'std': col_data.std(),
                'min': col_data.min(),
                'q1': col_data.quantile(0.25),
                'median': col_data.median(),
                'q3': col_data.quantile(0.75),
                'max': col_data.max(),
                'n_missing': col_data.isna().sum(),
                'missing_pct': round(col_data.isna().sum() / len(df) * 100, 2)
            })

    summary_df = pd.DataFrame(summary)
    summary_df.to_csv(output_path, index=False)
    print(f"✓ Numeric summary saved to {output_path}")
    return summary_df


def create_categorical_summary(df: pd.DataFrame, categorical_cols: List[str], output_path: str):
    """Create summary statistics for categorical columns."""
    summary = []

    for col in categorical_cols:
        if col in df.columns:
            col_data = df[col]
            value_counts = col_data.value_counts()

            if len(value_counts) > 0:
                top_val = value_counts.index[0]
                top_freq = value_counts.iloc[0]
                top_pct = round(top_freq / len(df) * 100, 2)
            else:
                top_val = None
                top_freq = 0
                top_pct = 0.0

            summary.append({
                'column': col,
                'n_unique': col_data.nunique(),
                'top': top_val,
                'top_freq': top_freq,
                'top_pct': top_pct,
                'n_missing': col_data.isna().sum(),
                'missing_pct': round(col_data.isna().sum() / len(df) * 100, 2)
            })

    summary_df = pd.DataFrame(summary)
    summary_df.to_csv(output_path, index=False)
    print(f"✓ Categorical summary saved to {output_path}")
    return summary_df


def create_target_distribution(df: pd.DataFrame, target_col: str, split_col: str,
                                output_path: str, is_binary: bool = False):
    """Create target distribution table."""
    distributions = []

    # Overall distribution
    overall_dist = df[target_col].value_counts()
    for label, count in overall_dist.items():
        distributions.append({
            'split': 'all',
            target_col: label,
            'count': count,
            'pct': round(count / len(df) * 100, 2)
        })

    # Per-split distribution
    if split_col in df.columns:
        for split_val in df[split_col].unique():
            split_df = df[df[split_col] == split_val]
            split_dist = split_df[target_col].value_counts()
            for label, count in split_dist.items():
                distributions.append({
                    'split': split_val,
                    target_col: label,
                    'count': count,
                    'pct': round(count / len(split_df) * 100, 2)
                })

    dist_df = pd.DataFrame(distributions)
    dist_df.to_csv(output_path, index=False)
    print(f"✓ Target distribution saved to {output_path}")
    return dist_df


def compute_metrics(y_true: np.ndarray, y_pred: np.ndarray,
                    y_proba: Optional[np.ndarray] = None,
                    class_names: Optional[List[str]] = None) -> Dict:
    """Compute comprehensive classification metrics."""
    metrics = {}

    # Basic metrics from classification report
    report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)

    metrics['accuracy'] = report['accuracy']
    metrics['macro_f1'] = report['macro avg']['f1-score']
    metrics['weighted_f1'] = report['weighted avg']['f1-score']
    metrics['macro_precision'] = report['macro avg']['precision']
    metrics['macro_recall'] = report['macro avg']['recall']

    # PR-AUC (OVR)
    if y_proba is not None and len(y_proba.shape) > 1:
        n_classes = y_proba.shape[1]
        y_true_bin = label_binarize(y_true, classes=range(n_classes))

        # Compute average precision for each class
        pr_aucs = []
        for i in range(n_classes):
            if len(np.unique(y_true_bin[:, i])) > 1:
                pr_auc = average_precision_score(y_true_bin[:, i], y_proba[:, i])
                pr_aucs.append(pr_auc)

        metrics['ovr_pr_auc'] = np.mean(pr_aucs) if pr_aucs else 0.0

        # Brier score (calibration)
        brier_scores = []
        for i in range(n_classes):
            if len(np.unique(y_true_bin[:, i])) > 1:
                brier = brier_score_loss(y_true_bin[:, i], y_proba[:, i])
                brier_scores.append(brier)
        metrics['brier_score'] = np.mean(brier_scores) if brier_scores else 0.0

    return metrics


def plot_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray,
                          class_names: List[str], output_path: str,
                          title: str = "Confusion Matrix"):
    """Plot and save confusion matrix."""
    cm = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=class_names, yticklabels=class_names)
    plt.title(title)
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Confusion matrix saved to {output_path}")


def plot_pr_curves(y_true: np.ndarray, y_proba: np.ndarray,
                   class_names: List[str], output_path: str,
                   title: str = "Precision-Recall Curves (OVR)"):
    """Plot and save PR curves for multi-class (OVR)."""
    n_classes = len(class_names)
    y_true_bin = label_binarize(y_true, classes=range(n_classes))

    plt.figure(figsize=(12, 8))

    for i in range(n_classes):
        if len(np.unique(y_true_bin[:, i])) > 1:
            precision, recall, _ = precision_recall_curve(y_true_bin[:, i], y_proba[:, i])
            pr_auc = average_precision_score(y_true_bin[:, i], y_proba[:, i])
            plt.plot(recall, precision, label=f'{class_names[i]} (AP={pr_auc:.3f})')

    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title(title)
    plt.legend(loc='best')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ PR curves saved to {output_path}")


def plot_roc_curves(y_true: np.ndarray, y_proba: np.ndarray,
                    class_names: List[str], output_path: str,
                    title: str = "ROC Curves (OVR)"):
    """Plot and save ROC curves for multi-class (OVR)."""
    n_classes = len(class_names)
    y_true_bin = label_binarize(y_true, classes=range(n_classes))

    plt.figure(figsize=(12, 8))

    for i in range(n_classes):
        if len(np.unique(y_true_bin[:, i])) > 1:
            fpr, tpr, _ = roc_curve(y_true_bin[:, i], y_proba[:, i])
            roc_auc = auc(fpr, tpr)
            plt.plot(fpr, tpr, label=f'{class_names[i]} (AUC={roc_auc:.3f})')

    plt.plot([0, 1], [0, 1], 'k--', label='Random')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc='best')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ ROC curves saved to {output_path}")


def plot_calibration_curve(y_true: np.ndarray, y_proba: np.ndarray,
                           class_names: List[str], output_path: str,
                           n_bins: int = 10, title: str = "Calibration Plot"):
    """Plot calibration (reliability) diagram."""
    from sklearn.calibration import calibration_curve

    n_classes = len(class_names)
    y_true_bin = label_binarize(y_true, classes=range(n_classes))

    plt.figure(figsize=(10, 8))

    for i in range(min(n_classes, 5)):  # Plot max 5 classes
        if len(np.unique(y_true_bin[:, i])) > 1:
            prob_true, prob_pred = calibration_curve(
                y_true_bin[:, i], y_proba[:, i], n_bins=n_bins, strategy='uniform'
            )
            plt.plot(prob_pred, prob_true, marker='o', label=class_names[i])

    plt.plot([0, 1], [0, 1], 'k--', label='Perfectly calibrated')
    plt.xlabel('Mean Predicted Probability')
    plt.ylabel('Fraction of Positives')
    plt.title(title)
    plt.legend(loc='best')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Calibration curve saved to {output_path}")


def create_feature_catalog(features: Dict, output_path: str):
    """Create feature catalog table."""
    catalog = []

    # Raw categorical features
    for feat in features.get('categorical', []):
        catalog.append({
            'feature': feat,
            'source': 'raw',
            'dtype': 'categorical',
            'description': f'Raw categorical feature: {feat}',
            'created_by': 'original_data'
        })

    # Raw numeric features
    for feat in features.get('numeric', []):
        catalog.append({
            'feature': feat,
            'source': 'raw',
            'dtype': 'numeric',
            'description': f'Raw numeric feature: {feat}',
            'created_by': 'original_data'
        })

    # Engineered features
    for feat, desc in features.get('engineered', {}).items():
        catalog.append({
            'feature': feat,
            'source': 'engineered',
            'dtype': 'mixed',
            'description': desc,
            'created_by': 'feature_engineering'
        })

    catalog_df = pd.DataFrame(catalog)
    catalog_df.to_csv(output_path, index=False)
    print(f"✓ Feature catalog saved to {output_path}")
    return catalog_df


def find_optimal_threshold(y_true: np.ndarray, y_proba: np.ndarray,
                           metric: str = 'f1') -> float:
    """Find optimal classification threshold based on metric."""
    thresholds = np.linspace(0, 1, 101)
    scores = []

    for thresh in thresholds:
        y_pred = (y_proba >= thresh).astype(int)

        if metric == 'f1':
            from sklearn.metrics import f1_score
            score = f1_score(y_true, y_pred, average='macro', zero_division=0)
        else:
            raise ValueError(f"Unknown metric: {metric}")

        scores.append(score)

    optimal_idx = np.argmax(scores)
    optimal_threshold = thresholds[optimal_idx]

    return optimal_threshold


def create_reproducibility_manifest(output_path: str):
    """Create reproducibility manifest with package versions."""
    import sys
    import sklearn
    import lightgbm
    import xgboost

    manifest = [
        {'component': 'python', 'version_or_value': sys.version.split()[0], 'notes': 'Python version'},
        {'component': 'pandas', 'version_or_value': pd.__version__, 'notes': 'Data manipulation'},
        {'component': 'numpy', 'version_or_value': np.__version__, 'notes': 'Numerical computing'},
        {'component': 'scikit-learn', 'version_or_value': sklearn.__version__, 'notes': 'ML library'},
        {'component': 'lightgbm', 'version_or_value': lightgbm.__version__, 'notes': 'Gradient boosting'},
        {'component': 'xgboost', 'version_or_value': xgboost.__version__, 'notes': 'Gradient boosting'},
        {'component': 'random_seed', 'version_or_value': '42', 'notes': 'Global random seed'},
    ]

    try:
        import torch
        manifest.append({'component': 'pytorch', 'version_or_value': torch.__version__, 'notes': 'Deep learning'})
    except:
        pass

    try:
        import catboost
        manifest.append({'component': 'catboost', 'version_or_value': catboost.__version__, 'notes': 'Gradient boosting'})
    except:
        pass

    manifest_df = pd.DataFrame(manifest)
    manifest_df.to_csv(output_path, index=False)
    print(f"✓ Reproducibility manifest saved to {output_path}")
    return manifest_df


def timer(func):
    """Decorator to time function execution."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱ {func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper


def plot_numeric_distributions(df: pd.DataFrame, numeric_cols: List[str],
                               output_dir: str, n_cols: int = 4):
    """Plot histograms for numeric features."""
    n_features = len(numeric_cols)
    n_rows = (n_features + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(4*n_cols, 3*n_rows))
    axes = axes.flatten() if n_features > 1 else [axes]

    for idx, col in enumerate(numeric_cols[:len(axes)]):
        if col in df.columns:
            df[col].hist(bins=50, ax=axes[idx], edgecolor='black')
            axes[idx].set_title(f'{col}', fontsize=10)
            axes[idx].set_xlabel('Value')
            axes[idx].set_ylabel('Frequency')

    # Hide extra subplots
    for idx in range(n_features, len(axes)):
        axes[idx].axis('off')

    plt.tight_layout()
    output_path = os.path.join(output_dir, 'numeric_distributions.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Numeric distributions saved to {output_path}")


def plot_correlation_heatmap(df: pd.DataFrame, numeric_cols: List[str], output_path: str):
    """Plot correlation heatmap."""
    corr_df = df[numeric_cols].corr()

    plt.figure(figsize=(14, 12))
    sns.heatmap(corr_df, cmap='coolwarm', center=0,
                annot=False, square=True, linewidths=0.5)
    plt.title('Feature Correlation Heatmap', fontsize=14)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Correlation heatmap saved to {output_path}")

    # Save correlation table
    corr_table_path = output_path.replace('.png', '.csv')
    corr_df.to_csv(corr_table_path)
    print(f"✓ Correlation table saved to {corr_table_path}")
    return corr_df


def plot_feature_importance_comparison(fi_dicts: Dict[str, pd.DataFrame],
                                       output_path: str, top_n: int = 20):
    """Compare feature importance across models."""
    fig, axes = plt.subplots(1, len(fi_dicts), figsize=(6*len(fi_dicts), 8))
    if len(fi_dicts) == 1:
        axes = [axes]

    for idx, (model_name, fi_df) in enumerate(fi_dicts.items()):
        top_fi = fi_df.nlargest(top_n, fi_df.columns[1])
        axes[idx].barh(range(len(top_fi)), top_fi.iloc[:, 1])
        axes[idx].set_yticks(range(len(top_fi)))
        axes[idx].set_yticklabels(top_fi['feature'], fontsize=8)
        axes[idx].set_xlabel('Importance')
        axes[idx].set_title(f'{model_name} - Top {top_n} Features')
        axes[idx].invert_yaxis()

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Feature importance comparison saved to {output_path}")


def plot_per_class_metrics(metrics_df: pd.DataFrame, output_path: str,
                            metric_name: str = 'f1-score'):
    """Plot per-class metrics as bar chart."""
    if metric_name not in metrics_df.columns:
        print(f"⚠ {metric_name} not found in metrics")
        return

    # Filter out avg rows
    plot_df = metrics_df[~metrics_df.index.str.contains('avg|accuracy', na=False)].copy()

    plt.figure(figsize=(12, 6))
    plt.bar(range(len(plot_df)), plot_df[metric_name])
    plt.xticks(range(len(plot_df)), plot_df.index, rotation=45, ha='right')
    plt.ylabel(metric_name.title())
    plt.xlabel('Class')
    plt.title(f'Per-Class {metric_name.title()}')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Per-class metrics plot saved to {output_path}")


def plot_training_time_comparison(models_df: pd.DataFrame, output_path: str):
    """Plot training time comparison."""
    plt.figure(figsize=(10, 6))

    models = models_df['model'].values
    times = models_df['train_time_sec_mean'].values

    plt.bar(range(len(models)), times, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'][:len(models)])
    plt.xticks(range(len(models)), models)
    plt.ylabel('Training Time (seconds)')
    plt.xlabel('Model')
    plt.title('Average Training Time Comparison (5-Fold CV)')
    plt.grid(axis='y', alpha=0.3)

    # Add value labels
    for i, v in enumerate(times):
        plt.text(i, v + max(times)*0.02, f'{v:.1f}s', ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Training time comparison saved to {output_path}")


def plot_model_comparison_radar(models_df: pd.DataFrame, output_path: str):
    """Plot radar chart for model comparison."""
    from math import pi

    metrics = ['macro_f1_mean', 'ovr_pr_auc_mean', 'accuracy_mean']
    labels = ['Macro F1', 'PR-AUC', 'Accuracy']

    angles = [n / float(len(metrics)) * 2 * pi for n in range(len(metrics))]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    for idx, row in models_df.iterrows():
        values = [row[m] for m in metrics]
        values += values[:1]
        ax.plot(angles, values, 'o-', linewidth=2, label=row['model'], color=colors[idx % len(colors)])
        ax.fill(angles, values, alpha=0.15, color=colors[idx % len(colors)])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1)
    ax.set_title('Model Performance Comparison', y=1.08, fontsize=14)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    ax.grid(True)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Radar chart saved to {output_path}")


def plot_class_distribution_per_fold(df: pd.DataFrame, target_col: str,
                                      output_path: str, n_splits: int = 5):
    """Plot class distribution across CV folds."""
    fig, axes = plt.subplots(1, n_splits, figsize=(4*n_splits, 4))
    if n_splits == 1:
        axes = [axes]

    for fold in range(n_splits):
        fold_df = df[df['cv_fold'] == fold]
        fold_df[target_col].value_counts().plot(kind='bar', ax=axes[fold])
        axes[fold].set_title(f'Fold {fold}')
        axes[fold].set_xlabel('Class')
        axes[fold].set_ylabel('Count')
        axes[fold].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Class distribution per fold saved to {output_path}")


def plot_categorical_distribution(df: pd.DataFrame, cat_col: str, output_path: str, top_n: int = 15):
    """Plot distribution of categorical feature."""
    value_counts = df[cat_col].value_counts().head(top_n)

    plt.figure(figsize=(10, 6))
    value_counts.plot(kind='barh')
    plt.xlabel('Count')
    plt.ylabel(cat_col)
    plt.title(f'{cat_col} Distribution (Top {top_n})')
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Categorical distribution saved to {output_path}")


def plot_metric_progression(cv_scores_df: pd.DataFrame, metric_col: str,
                             output_path: str, model_name: str = 'Model'):
    """Plot metric progression across folds."""
    plt.figure(figsize=(10, 6))

    folds = cv_scores_df['fold'].values
    scores = cv_scores_df[metric_col].values

    plt.plot(folds, scores, 'o-', linewidth=2, markersize=8)
    plt.axhline(y=scores.mean(), color='r', linestyle='--',
                label=f'Mean: {scores.mean():.4f}')
    plt.fill_between(folds, scores.mean() - scores.std(),
                     scores.mean() + scores.std(), alpha=0.2)

    plt.xlabel('Fold')
    plt.ylabel(metric_col.replace('_', ' ').title())
    plt.title(f'{model_name} - {metric_col.replace("_", " ").title()} Across Folds')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Metric progression saved to {output_path}")


def create_per_class_metrics_table(y_true: np.ndarray, y_pred: np.ndarray,
                                   y_proba: np.ndarray, class_names: List[str],
                                   output_path: str, fold: int = None):
    """Create detailed per-class metrics table."""
    from sklearn.metrics import classification_report, precision_recall_fscore_support

    # Get per-class metrics
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true, y_pred, average=None, zero_division=0
    )

    # Binarize for AUC calculations
    y_true_bin = label_binarize(y_true, classes=range(len(class_names)))

    metrics_data = []
    for i, class_name in enumerate(class_names):
        row = {
            'class': class_name,
            'precision': precision[i],
            'recall': recall[i],
            'f1_score': f1[i],
            'support': support[i]
        }

        # Add PR-AUC if available
        if len(np.unique(y_true_bin[:, i])) > 1:
            row['pr_auc'] = average_precision_score(y_true_bin[:, i], y_proba[:, i])
        else:
            row['pr_auc'] = 0.0

        if fold is not None:
            row['fold'] = fold

        metrics_data.append(row)

    metrics_df = pd.DataFrame(metrics_data)
    metrics_df.to_csv(output_path, index=False)
    print(f"✓ Per-class metrics table saved to {output_path}")
    return metrics_df


def plot_boxplot_comparison(data_dict: Dict[str, List[float]],
                             output_path: str, title: str = 'Metric Comparison',
                             ylabel: str = 'Score'):
    """Plot boxplot comparison across models."""
    plt.figure(figsize=(10, 6))

    positions = range(1, len(data_dict) + 1)
    bp = plt.boxplot(data_dict.values(), positions=positions, patch_artist=True,
                     labels=data_dict.keys())

    # Color the boxes
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    for patch, color in zip(bp['boxes'], colors[:len(bp['boxes'])]):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)

    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Boxplot comparison saved to {output_path}")


if __name__ == "__main__":
    print("Utility functions module loaded successfully")
