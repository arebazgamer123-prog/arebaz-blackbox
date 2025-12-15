#!/usr/bin/env python3
import os
import sys
import time

def slow_print(text, delay=0.002):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def show_banner():
    os.system("clear" if os.name != "nt" else "cls")
    banner = r"""
█████╗ ██████╗ ███████╗██████╗  █████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══███╔╝
███████║██████╔╝█████╗  ██████╔╝███████║  ███╔╝ 
██╔══██║██╔══██╗██╔══╝  ██╔══██╗██╔══██║ ███╔╝  
██║  ██║██║  ██║███████╗██████╔╝██║  ██║███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝

      ☠️  A R E B A Z   B L A C K B O X  ☠️
   Advanced Network Reconnaissance Framework

   "Not an exploit. Not an attack. A mirror."
"""
    slow_print("\033[91m" + banner + "\033[0m")

def main():
    show_banner()
    target = input("\nEnter Target (IP / Domain): ")
    print("Target selected:", target)
    # ⬇️ এখান থেকে তোমার scan / menu / logic add করবে

if __name__ == "__main__":
    main()
