import time

from pyplug.helper import Color

class Statement:
	@staticmethod
	def if_(value_a, statement, value_b, do: list):
		return_value = ""

		return_value = return_value + "}" + f" else if ({value_a}{statement}{value_b}) " + "{\n"

		for x in range(len(do)):
			return_value = return_value + do[x]['return_value'] + ";\n"

		imports = []  # define imports
		for i in range(len(do)):  # check for imports
			try:
				if do[i]['imports'] is not None:  # if there's imports
					imports.append(do[i]['imports'])
			except TypeError as err:  # if there's old Py2Mc legacy code
				print(
					Color.RED + Color.BOLD + 'ERROR (CANT get IMPORT with TypeError): ' + Color.RESET + 'Somewhere in Py2Mc, there\'s still legacy code. Please report this issue in our discord server. INFOS: ' + "if_(arg: do)",
					err)
				time.sleep(1)

		if imports == []:
			imports = None

		return {"imports": imports, "return_value": return_value + "//"}

	@staticmethod
	def elif_(value_a, statement, value_b, do: list):
		return_value = ""

		return_value = return_value + "}" + f" else if ({value_a}{statement}{value_b}) " + "{\n"

		for x in range(len(do)):
			try:
				return_value = return_value + do[x]['return_value'] + ";\n"
			except TypeError as err:  # if there's old Py2Mc legacy code
				print(Color.RED + Color.BOLD + 'ERROR (CANT get GENERATE with TypeError): ' + Color.RESET + 'Somewhere in Py2Mc, there\'s still legacy code. Please report this issue in our discord server. INFOS: ' + "elif_(arg: do)", err)
				time.sleep(1)

		imports = [] # define imports
		for i in range(len(do)): # check for imports
			try:
				if do[i]['imports'] is not None:  # if there's imports
					imports.append(do[i]['imports'])
			except TypeError as err:  # if there's old Py2Mc legacy code
				print(Color.RED + Color.BOLD + 'ERROR (CANT get IMPORT with TypeError): ' + Color.RESET + 'Somewhere in Py2Mc, there\'s still legacy code. Please report this issue in our discord server. INFOS: ' + "elif_(arg: do)", err)
				time.sleep(1)

		if imports == []:
			imports = None

		return {"imports": imports, "return_value": return_value + "//"}

	@staticmethod
	def else_(do: list):
		return_value = ""

		return_value = return_value + "}" + f" else " + "{\n"

		for x in range(len(do)):
			return_value = return_value + do[x]['return_value'] + ";\n"

		imports = []  # define imports
		for i in range(len(do)):  # check for imports
			try:
				if do[i]['imports'] is not None:  # if there's imports
					try:
						imports.append(do[i]['imports'])
					except TypeError as err:  # if there's old Py2Mc legacy code
						print(
							Color.RED + Color.BOLD + 'ERROR (CANT get GENERATE with TypeError): ' + Color.RESET + 'Somewhere in Py2Mc, there\'s still legacy code. Please report this issue in our discord server. INFOS: ' + "else_(arg: do)",
							err)
						time.sleep(1)
			except TypeError as err:  # if there's old Py2Mc legacy code
				print(
					Color.RED + Color.BOLD + 'ERROR (CANT get IMPORT with TypeError): ' + Color.RESET + 'Somewhere in Py2Mc, there\'s still legacy code. Please report this issue in our discord server. INFOS: ' + "else_(arg: do)",
					err)
				time.sleep(1)

		if imports == []:
			imports = None

		return {"imports": imports, "return_value": return_value + "//"}

class Needed:
	@staticmethod
	def end(amount: int = 1):
		return_value = "}" * amount + "//"
		return {"imports": None, "return_value": return_value}
