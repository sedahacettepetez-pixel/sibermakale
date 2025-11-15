#!/bin/bash

##############################################################################
# UNSW-NB15 Project Setup Script
# Bu script projeyi kurmak için gerekli tüm adımları otomatik olarak çalıştırır
##############################################################################

set -e  # Hata durumunda dur

echo "================================================================="
echo "  UNSW-NB15 Projesi - Otomatik Kurulum"
echo "================================================================="
echo ""

# Renk kodları
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Python versiyonunu kontrol et
echo -e "${YELLOW}[1/6] Python versiyonu kontrol ediliyor...${NC}"
python_version=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1-2)
required_version="3.9"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" = "$required_version" ]; then
    echo -e "${GREEN}✓ Python $python_version yüklü${NC}"
else
    echo -e "${RED}✗ Python $required_version veya üzeri gerekli. Mevcut: $python_version${NC}"
    exit 1
fi

# Sanal ortam oluştur
echo ""
echo -e "${YELLOW}[2/6] Sanal ortam oluşturuluyor...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓ Sanal ortam oluşturuldu${NC}"
else
    echo -e "${GREEN}✓ Sanal ortam zaten mevcut${NC}"
fi

# Sanal ortamı aktifleştir
echo ""
echo -e "${YELLOW}[3/6] Sanal ortam aktifleştiriliyor...${NC}"
source venv/bin/activate
echo -e "${GREEN}✓ Sanal ortam aktif${NC}"

# pip güncellemesi
echo ""
echo -e "${YELLOW}[4/6] pip güncelleniyor...${NC}"
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
echo -e "${GREEN}✓ pip güncellendi${NC}"

# Bağımlılıkları yükle
echo ""
echo -e "${YELLOW}[5/6] Bağımlılıklar yükleniyor (bu işlem birkaç dakika sürebilir)...${NC}"
pip install -r requirements.txt
echo -e "${GREEN}✓ Tüm bağımlılıklar yüklendi${NC}"

# Dizin yapısını kontrol et
echo ""
echo -e "${YELLOW}[6/6] Dizin yapısı kontrol ediliyor...${NC}"
directories=(
    "data"
    "artifacts/tables"
    "artifacts/figs"
    "artifacts/logs"
    "artifacts/models"
    "artifacts/processed"
    "artifacts/report/tables_latex"
)

for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo -e "${GREEN}  ✓ $dir oluşturuldu${NC}"
    else
        echo -e "${GREEN}  ✓ $dir mevcut${NC}"
    fi
done

echo ""
echo "================================================================="
echo -e "${GREEN}  Kurulum Tamamlandı! 🎉${NC}"
echo "================================================================="
echo ""
echo "Sonraki adımlar:"
echo ""
echo "1. Sanal ortamı aktifleştir (henüz aktif değilse):"
echo "   source venv/bin/activate"
echo ""
echo "2. UNSW-NB15 veri setini indirin:"
echo "   a) Kaggle API ile:"
echo "      kaggle datasets download -d mrwellsdavid/unsw-nb15"
echo "      unzip unsw-nb15.zip -d data/"
echo ""
echo "   b) Veya manuel olarak data/ klasörüne yerleştirin:"
echo "      - UNSW_NB15_training-set.csv"
echo "      - UNSW_NB15_testing-set.csv"
echo ""
echo "3. Jupyter notebook'u başlatın:"
echo "   jupyter notebook unsw_nb15_analysis.ipynb"
echo ""
echo "4. Veya JupyterLab kullanın:"
echo "   jupyter lab"
echo ""
echo "Daha fazla bilgi için README.md dosyasına bakın."
echo ""
echo "================================================================="
