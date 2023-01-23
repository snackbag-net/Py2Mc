class Log:
	@staticmethod
	def info(text: str):
		return "Bukkit.getLogger().info(\"" + text + "\")"

	@staticmethod
	def warn(text: str):
		return "Bukkit.getLogger().warning(\"" + text + "\""
