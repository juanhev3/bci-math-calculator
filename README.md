# 🧠 Gesture-Controlled AI Calculator

[![DEMO](docs/DEMO.gif)](https://yoursite.com/demo)

Control a math calculator with hand gestures using:
- **MediaPipe** for real-time hand tracking
- **Flask** backend with secure expression evaluation
- **WebSocket** updates (optional)

## ✨ Features
- Pinch gesture detection → `1+1=2`
- Voice feedback (optional)
- Cross-platform (Windows/WSL)
- [Add your features...]

## 🛠️ Setup
```bash
# 1. Clone repository
git clone https://github.com/yourusername/bci-math-calculator.git

# 2. Set up environments
cd bci-math-calculator
./setup.sh  # See setup instructions below
```
## 🛠️ Setup

```bash
# 1. Clone repository
git clone https://github.com/yourusername/bci-math-calculator.git
cd bci-math-calculator

# 2. Run setup script (WSL/Linux)
./setup.sh

# 3. For Windows camera control:
#    Manually execute the commands shown after running setup.sh
```


## 🎮 Gesture Mapping
| Gesture | Action | Visual Feedback |
|---------|--------|-----------------|
| 👌 Pinch | Sends calculation | Green "PINCH DETECTED" |
| ✋ Open Hand | Resets to 0 | Blue screen flash |

## 📚 Documentation
- [System Architecture](docs/ARCHITECTURE.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)

[![Deploy](https://img.shields.io/badge/Run_on-Replit-blue)]()