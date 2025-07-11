#!/bin/bash

# 1. Create virtual environment
echo "🛠️ Creating virtual environment..."
python3 -m venv venv || { echo "Virtual environment could not be created"; exit 1; }

# 2. ACTIVATE the virtual environment (critical step!)
echo "🔌 Activating virtual environment..."
source venv/bin/activate || { echo "Virtual environment could not be activated"; exit 1; }

# 3. Install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt || { echo "Dependencies could not be installed"; exit 1; }

# 4. Run the main program
echo "🚀 Starting the program..."
python yz.py

# 5. Deactivate the virtual environment
deactivate