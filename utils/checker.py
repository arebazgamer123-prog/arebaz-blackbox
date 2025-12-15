import shutil
import sys

def check_nmap():
    if shutil.which("nmap") is None:
        print("❌ Nmap is not installed")
        print("Install it first and try again")
        sys.exit(1)
