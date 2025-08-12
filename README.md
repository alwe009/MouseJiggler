# 🖱️ MouseJiggler
A simple utility that keeps your computer awake by simulating small, periodic mouse movements. Useful for preventing screen locks, auto logouts, or sleep mode during long work sessions.

## 📜 Project Purpose
MouseJiggler moves your mouse slightly at intervals so your system doesn’t go idle. Unlike shady “keep-awake” tools, **this project is open source** — you can inspect the exact code before deciding to run it.

## 📂 Code & Security
This repository contains:  
- `main.py` → The complete source code for MouseJiggler  
- `requirements.txt` → Python dependencies  
- `.gitignore` → Git ignore rules  
- `build.bat` → Script used to package into an `.exe`  

You are encouraged to **read the code first** to ensure it’s safe. Transparency builds trust. ✅

## 🚀 How to Use
### Option 1 — Run from Python
1. Clone this repository:  
   ```bash
   git clone https://github.com/alwe009/MouseJiggler.git  
   cd MouseJiggler  
   ```
2. Create a virtual environment (optional but recommended):  
   ```bash
   python -m venv venv  
   source venv/bin/activate   # On Linux/Mac  
   venv\Scripts\activate      # On Windows  
   ```
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt  
   ```
4. Run the program:  
   ```bash
   python main.py  
   ```

### Option 2 — Download the EXE (No Python Required)
1. Go to the [Releases page](https://github.com/alwe009/MouseJiggler/releases/tag/v1.0.0).
2. Download the latest `MouseJiggler.exe`.  
3. Run it — no installation needed.  

⚠️ **Note:** Some antivirus software may flag unknown `.exe` files. This is a false positive due to the file being unsigned. If you are unsure, **run the Python source code instead**.

## 🔧 Building the EXE Yourself
If you want to generate your own `.exe`:  
```bash
pip install -r requirements.txt  
pyinstaller --onefile main.py  
```
Your `.exe` will be in the `dist` folder.

## 📜 License
This project is licensed under the [MIT License](LICENSE).
