#!/bin/bash

# 1. Sanal ortam oluştur
echo "🛠️ Sanal ortam oluşturuluyor..."
python3 -m venv venv || { echo "Sanal ortam oluşturulamadı"; exit 1; }

# 2. Sanal ortamı AKTİF ET (kritik adım!)
echo "🔌 Sanal ortam etkinleştiriliyor..."
source venv/bin/activate || { echo "Sanal ortam etkinleştirilemedi"; exit 1; }

# 3. Bağımlılıkları yükle
echo "📦 Bağımlılıklar yükleniyor..."
pip install --upgrade pip
pip install -r requirements.txt || { echo "Bağımlılıklar yüklenemedi"; exit 1; }

# 4. Ana programı çalıştır
echo "🚀 Program başlatılıyor..."
python yz.py

# 5. Sanal ortamdan çık
deactivate