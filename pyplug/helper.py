import os
import sys


def ifFileExistsM(path: str) -> bool:
	try:
		os.mkdir(path)
	except FileExistsError:
		return True


def pipInstaller():
	try:
		import requests
	except ImportError:
		print("[AUTOINSTALLER] A few packages aren't installed. Auto installing...")
		os.system("python3 -m pip install --upgrade pip")
		os.system("python3 -m pip install requests")
		print("\n\nPlease start the script again!")
		sys.exit(0)

class Color:
	LIGHTPURPLE = '\033[95m'
	PURPLE = '\033[35m'
	LIGHTCYAN = '\033[96m'
	CYAN = '\033[36m'
	LIGHTBLUE = '\033[94m'
	BLUE = '\033[34m'
	LIGHTGREEN = '\033[92m'
	GREEN = '\033[32m'
	LIGHTYELLOW = '\033[93m'
	YELLOW = '\033[33m'
	LIGHTRED = '\033[91m'
	RED = '\033[31m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	RESET = '\033[0m'
