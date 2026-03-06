# Keylogger (Educational)

##  Legal Disclaimer
This software is developed for **academic and research purposes only**. It is intended to study input device handling and SMTP communication in Python. Unauthorized monitoring of computer systems is a criminal offense. The author is not liable for any damages or legal issues resulting from the use of this code.

##  Research Focus
- Analyzing low-level keyboard hook mechanisms via `pynput`.
- Testing secure data transmission over TLS (Transport Layer Security) using `smtplib`.
- Implementing non-blocking background threads in Python.

##  Environment Setup (Local Debugging)
To test this tool in a controlled environment:
1. Ensure Python 3.x is installed.
2. Install necessary research libraries: `pip install pynput python-dotenv`.
3. Create a `.env` file with your **test credentials** (never use your primary account).
4. Run the analysis script: `python main.py`.

##  Repository Structure
- `keylogger.py`: The core logic for event logging.
- `.env`: (Ignored by Git) Local configuration for testing.
- `LICENSE`: MIT License information.

