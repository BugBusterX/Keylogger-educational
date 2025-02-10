# Keylogger-educational
"This is a simple keylogger for educational purposes, created using python and the pynput library . Not for illegal use."
# Keylogger Educational 📝  

This is an educational keylogger for ethical hacking and cybersecurity learning.  

**⚠️ Disclaimer:** This project is for educational purposes only. Do not use it for malicious activities.  

## 🔥 Installation (For Kali Linux)

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/BugBusterX/Keylogger-educational.git
   ```
2. **Navigate to the project directory:**  
   ```bash
   cd Keylogger-educational
   ```
3. **Install required dependencies:**  
   ```bash
   pip install pynput
   ```
4. **Run the keylogger:**  
   ```bash
   python3 keylogger.py
   ```

## 🚀 Windows Version 
# Keylogger-Educational (Windows Installation Guide)

## 📌 Introduction
This repository contains an *educational keylogger* for learning purposes only. It is designed to demonstrate keylogging techniques in ethical hacking and cybersecurity training.

*⚠ Disclaimer:* This project is for educational purposes only. Unauthorized usage is illegal and punishable by law.

---

## 🔧 Prerequisites
Before running the keylogger, ensure you have the required dependencies installed.

### 1️⃣ Install Python (if not installed)
Download and install Python (latest version):
- [Download Python](https://www.python.org/downloads/)
- During installation, *check the box*: Add Python to PATH

To verify Python installation, open *Command Prompt (cmd)* and run:
sh
python --version


### 2️⃣ Install Required Python Modules
Run the following command to install dependencies:
sh
pip install pynput


---

## 🏗 Running the Script
After installation, navigate to the script's directory and run:
sh
python keylogger.py


If you encounter the error ModuleNotFoundError: No module named 'pynput', ensure you have installed the dependencies correctly.

---

## 🚀 Creating an Executable File
To run the keylogger as a *standalone .exe file*, use PyInstaller:

### 1️⃣ Install PyInstaller
sh
pip install pyinstaller


### 2️⃣ Convert Python Script to EXE
sh
pyinstaller --onefile --hidden-import=pynput keylogger.py


### 3️⃣ Locate Your EXE File
After running the above command, your *executable file* will be located in the dist/ folder:
sh
cd dist
keylogger.exe


---

## 🛠 Troubleshooting
### 🔴 'pynput' Module Not Found
Reinstall pynput by running:
sh
pip install --force-reinstall pynput


### 🔴 'pyinstaller' is Not Recognized
Ensure pip and Python are added to your system *PATH*. Run:
sh
python -m pip install --upgrade pip


### 🔴 'Script file does not exist' Error
Make sure you are in the correct directory where keylogger.py is located.
Use:
sh
dir

Then, navigate to the correct folder using:
sh
cd path\to\your\script


---

## 🚧 Windows Support


## 📩 Contact & Contributions
For contributions, issues, or queries, feel free to open an *Issue* or a *Pull Request*.

📧 Email: busterbug53@gmail.com  
🔗 GitHub: [BugBusterX](https://github.com/BugBusterX)

---

*🚀 Happy Ethical Hacking!*
## 📢 Note  
This tool is intended for ethical hacking and cybersecurity research only. Unauthorized use is strictly prohibited.
