#!/bin/bash
# setup.sh - Enhanced unified setup script

echo "🔧 Setting up Gesture-Controlled Calculator"
echo "Note: Using project root requirements.txt"

# Verify requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: requirements.txt not found in project root"
    echo "Create it with:"
    echo "   pip freeze > requirements.txt"
    exit 1
fi

# WSL/Linux Setup
echo -e "\n=== WSL Setup ==="
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Windows Setup
echo -e "\n=== Windows Setup ==="
echo "1. Open CMD as Administrator"
echo "2. Run these commands:"
echo "   cd C:\\Users\\juanh\\bci-math-calculator"
echo "   python -m venv venv"
echo "   venv\\Scripts\\activate"
echo "   pip install -r requirements.txt"
echo "3. Press Enter when done to continue..."
read -p ""

echo -e "\n✅ Setup complete!"
echo -e "\nTo run:"
echo "1. WSL: source venv/bin/activate && python calculator/app.py"
echo "2. Windows: venv\\Scripts\\activate && python camera-control/gesture_detection.py"