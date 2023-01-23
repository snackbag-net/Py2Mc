import os


def ifFileExistsM(path: str) -> bool:
	try:
		os.mkdir(path)
	except FileExistsError:
		return True
