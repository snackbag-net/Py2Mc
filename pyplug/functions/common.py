import pyplug.creator.storage as storage


def color(text):
	if text == "black":
		return f"\" + ChatColor.BLACK + \""
	elif text == "dark_blue":
		return f"\" + ChatColor.DARK_BLUE + \""
	elif text == "dark_green":
		return f"\" + ChatColor.DARK_GREEN + \""
	elif text == "dark_aqua":
		return f"\" + ChatColor.DARK_AQUA + \""
	elif text == "dark_red":
		return f"\" + ChatColor.DARK_RED + \""
	elif text == "dark_purple":
		return f"\" + ChatColor.DARK_PURPLE + \""
	elif text == "gold":
		return f"\" + ChatColor.GOLD + \""
	elif text == "gray":
		return f"\" + ChatColor.GRAY + \""
	elif text == "dark_gray":
		return f"\" + ChatColor.DARK_GRAY + \""
	elif text == "blue":
		return f"\" + ChatColor.BLUE + \""
	elif text == "green":
		return f"\" + ChatColor.GREEN + \""
	elif text == "aqua":
		return f"\" + ChatColor.AQUA + \""
	elif text == "red":
		return f"\" + ChatColor.RED + \""
	elif text == "light_purple":
		return f"\" + ChatColor.LIGHT_PURPLE + \""
	elif text == "yellow":
		return f"\" + ChatColor.YELLOW + \""
	elif text == "white":
		return f"\" + ChatColor.WHITE + \""
	elif text == "obfuscated":
		return f"\" + ChatColor.MAGIC + \""
	elif text == "bold":
		return f"\" + ChatColor.BOLD + \""
	elif text == "strikethrough":
		return f"\" + ChatColor.STRIKETHROUGH + \""
	elif text == "underline":
		return f"\" + ChatColor.UNDERLINE + \""
	elif text == "italic":
		return f"\" + ChatColor.ITALIC + \""
	elif text == "reset":
		return f"\" + ChatColor.RESET + \""
	else:
		return f"\" + ChatColor.RESET + \""


class Var:
	@staticmethod
	def set(savepoint, name, value):
		storage.variables[savepoint] = {}
		storage.variables[savepoint][name] = value
		return ""

	@staticmethod
	def get(savepoint, name):
		try:
			return storage.variables[savepoint][name]
		except KeyError:
			print(f"Error while getting variable 'storage.variables[{savepoint}][{name}]' - KeyError!")

	@staticmethod
	def clear(savepoint, name):
		try:
			del (storage.variables[savepoint][name])
			return ""
		except KeyError:
			print(f"Error while del() variable 'storage.variables[{savepoint}][{name}]' - KeyError!")
			return ""


class Get:
	@staticmethod
	def name(player):
		return f"\" + {player}.getName() + \""
